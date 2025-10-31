from workout_tracker import FitnessTracker, ExerciseLog, CustomExercise
import gradio as gr
import pandas as pd
import datetime

tracker = FitnessTracker()

def log_workout(date: str, duration: int, notes: str, exercises: list):
    workout = tracker.log_workout(date, duration, notes)
    for exercise in exercises:
        exercise_log = ExerciseLog(
            exercise['exercise'],
            sets=exercise['sets'],
            reps=exercise['reps'],
            weight=exercise['weight'],
            rpe=exercise['rpe']
        )
        tracker.add_exercise_to_workout(workout, exercise_log)
    return f"Workout logged for {workout.date} with duration {workout.duration} mins."

def get_exercise_list():
    exercise_details = [{"name": exercise.name, "category": exercise.category} for exercise in tracker.exercise_db]
    return exercise_details

def custom_exercise_creation(name: str, category: str, primary_muscles: str, equipment: str, instructions: str):
    new_exercise = CustomExercise(name, category, primary_muscles.split(','), equipment.split(','), instructions)
    tracker.exercise_db.append(new_exercise)
    return f"Custom exercise '{name}' added!"

def search_exercises(name: str, category: str):
    results = tracker.search_exercises(name, category)
    return [(exercise.name, exercise.category, exercise.primary_muscles, exercise.equipment, exercise.instructions) for exercise in results]

def track_progress():
    # Placeholder for actual tracking and analytics
    return "Progress tracking feature is under development."

def export_workout_log():
    workout_data = []
    for log in tracker.workout_logs:
        for exercise in log.exercises:
            workout_data.append({
                "Date": log.date,
                "Duration": log.duration,
                "Exercise": exercise.exercise.name,
                "Sets": exercise.sets,
                "Reps": exercise.reps,
                "Weight": exercise.weight,
                "RPE": exercise.rpe
            })
    df = pd.DataFrame(workout_data)
    csv_file = "workout_log.csv"
    df.to_csv(csv_file, index=False)
    return csv_file

with gr.Blocks() as app:
    with gr.Tab("Log Workout"):
        with gr.Row():
            date_input = gr.Textbox(label="Date (YYYY-MM-DD)", value=datetime.date.today().strftime("%Y-%m-%d"))
            duration_input = gr.Number(label="Duration (Minutes)", value=60)
            notes_input = gr.Textbox(label="Notes", placeholder="Additional notes about the workout")
            exercise_select = gr.Dataframe(get_exercise_list(), label="Select Exercises", interactive=True)
            sets_input = gr.Number(label="Sets", value=3)
            reps_input = gr.Number(label="Reps", value=10)
            weight_input = gr.Number(label="Weight", value=0)
            rpe_input = gr.Number(label="RPE", value=0)
        
        log_button = gr.Button("Log Workout")
        log_output = gr.Textbox(label="Log Output", interactive=False)
        log_button.click(fn=log_workout, inputs=[date_input, duration_input, notes_input, exercise_select], outputs=log_output)
    
    with gr.Tab("Manage Exercises"):
        with gr.Row():
            name_input = gr.Textbox(label="Exercise Name")
            category_input = gr.Textbox(label="Category")
            primary_muscles_input = gr.Textbox(label="Primary Muscles (comma separated)")
            equipment_input = gr.Textbox(label="Equipment (comma separated)")
            instructions_input = gr.Textbox(label="Instructions")
            create_button = gr.Button("Add Custom Exercise")
            creation_output = gr.Textbox(label="Creation Output", interactive=False)
            create_button.click(fn=custom_exercise_creation, inputs=[name_input, category_input, primary_muscles_input, equipment_input, instructions_input], outputs=creation_output)
    
    with gr.Tab("Search Exercises"):
        search_name_input = gr.Textbox(label="Search Exercise Name")
        search_category_input = gr.Textbox(label="Search Category")
        search_results = gr.Dataframe(label="Search Results", interactive=False)
        search_button = gr.Button("Search")
        search_button.click(fn=search_exercises, inputs=[search_name_input, search_category_input], outputs=search_results)
    
    with gr.Tab("Progress Tracking"):
        progress_output = gr.Textbox(label="Progress Output", interactive=False)
        track_button = gr.Button("Track Progress")
        track_button.click(fn=track_progress, outputs=progress_output)

    with gr.Tab("Export Data"):
        export_output = gr.Textbox(label="Export Output", interactive=False)
        export_button = gr.Button("Export Workout Log")
        export_button.click(fn=export_workout_log, outputs=export_output)
    
app.launch()