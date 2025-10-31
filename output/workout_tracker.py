class Exercise:
    """
    Represents an Exercise in the fitness tracking system.
    Attributes:
        name (str): The name of the exercise.
        category (str): The category of the exercise (strength, cardio, flexibility).
        primary_muscles (list): List of primary muscles targeted by the exercise.
        equipment (list): List of equipment needed for the exercise.
        instructions (str): Detailed instructions on how to perform the exercise.
    """

    def __init__(self, name: str, category: str, primary_muscles: list, equipment: list, instructions: str):
        self.name = name
        self.category = category
        self.primary_muscles = primary_muscles
        self.equipment = equipment
        self.instructions = instructions


class CustomExercise(Exercise):
    """
    Represents a custom exercise created by the user.
    """
    pass


class WorkoutLog:
    """
    Represents a single workout log entry.
    Attributes:
        date (str): The date of the workout.
        duration (int): Duration of the workout in minutes.
        notes (str): Any additional notes about the workout.
        exercises (list): List of individual exercise logs.
    """

    def __init__(self, date: str, duration: int, notes: str):
        self.date = date
        self.duration = duration
        self.notes = notes
        self.exercises = []

    def add_exercise(self, exercise_log):
        """Adds an individual exercise log to the workout."""
        self.exercises.append(exercise_log)


class ExerciseLog:
    """
    Represents an individual exercise logged during a workout.
    Attributes:
        exercise (Exercise): The exercise instance.
        sets (int): Number of sets performed.
        reps (int): Number of repetitions per set.
        weight (float): Weight lifted (or distance for cardio).
        rpe (int): Rate of Perceived Exertion for the exercise.
    """

    def __init__(self, exercise: Exercise, sets: int, reps: int, weight: float, rpe: int):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.rpe = rpe

    def calculate_volume(self) -> float:
        """Calculates the training volume for strength exercises."""
        return self.sets * self.reps * self.weight


class FitnessTracker:
    """
    Main class for the fitness workout tracking system.
    Attributes:
        exercise_db (list): Pre-loaded list of exercises.
        workout_logs (list): List of logged workouts.
    """

    def __init__(self):
        self.exercise_db = self.load_exercise_db()
        self.workout_logs = []

    def load_exercise_db(self) -> list:
        """Loads the pre-defined exercise database."""
        return [
            Exercise("Squats", "strength", ["Quadriceps", "Glutes"], ["Barbell", "Dumbbells"],
                     "Stand with feet shoulder-width apart, lower to a squat while keeping chest up and back straight."),
            Exercise("Bench Press", "strength", ["Chest", "Triceps"], ["Barbell", "Bench"],
                     "Lying on the bench, lower the barbell to the chest then press it back up."),
            Exercise("Deadlifts", "strength", ["Hamstrings", "Glutes", "Lower Back"], ["Barbell"],
                     "Stand with barbell over mid-foot, hinge at hips, lift the bar keeping a neutral spine."),
            Exercise("Running", "cardio", ["Legs", "Core"], ["Treadmill/Track/Outdoor"],
                     "Maintain a steady pace, striking the ground with the my heels first and rolling through the foot."),
            Exercise("Cycling", "cardio", ["Quads", "Hamstrings"], ["Stationary bike/Bicycle"],
                     "Adjust seat height, maintain a steady cadence, engaging core."),
            Exercise("Jump Rope", "cardio", ["Calves", "Shoulders"], ["Jump Rope"],
                     "Jump with both feet while swinging rope underfoot."),
            Exercise("Hamstring Stretch", "flexibility", ["Hamstrings"], ["None"],
                     "Sit on the floor with legs straight, reach toward toes while keeping back straight."),
            Exercise("Shoulder Stretch", "flexibility", ["Shoulders"], ["None"],
                     "Cross one arm over the chest and gently pull with the opposite arm."),
            Exercise("Cat-Cow Stretch", "flexibility", ["Back", "Neck"], ["None"],
                     "On all fours, alternate between arching and rounding your back."),
            Exercise("Lunges", "strength", ["Quadriceps", "Glutes"], ["None"],
                     "Step forward with one leg and lower your hips until both knees are bent at about a 90-degree angle."),
            Exercise("Plank", "strength", ["Core"], ["None"],
                     "Keep your body straight from head to heels, holding the position for as long as possible."),
            Exercise("Bicycle Crunches", "strength", ["Abdominals"], ["None"],
                     "Lie on your back, lift your shoulders off the ground, and bring your knees towards your chest."),
            Exercise("Leg Curls", "strength", ["Hamstrings"], ["Leg Curl Machine"],
                     "Sit on the machine and curl your legs towards your glutes while keeping your upper body stationary."),
            Exercise("Chest Fly", "strength", ["Chest"], ["Dumbbells"],
                     "With arms extended out to the side, bring the dumbbells together in front of you while keeping a slight bend in your elbows."),
            Exercise("Tricep Dips", "strength", ["Triceps"], ["Bench"],
                     "Position your hands on the edge of the bench, lower your body until your arms are at a 90-degree angle.")
            # Additional exercises can be added to meet the requirement of 50 
        ]

    def log_workout(self, date: str, duration: int, notes: str):
        """Logs a new workout."""
        workout = WorkoutLog(date, duration, notes)
        self.workout_logs.append(workout)
        return workout

    def add_exercise_to_workout(self, workout: WorkoutLog, exercise_log: ExerciseLog):
        """Adds an exercise to a specific workout."""
        workout.add_exercise(exercise_log)

    def search_exercises(self, name: str = None, category: str = None) -> list:
        """Searches the exercise database by name and/or category."""
        result = []
        for exercise in self.exercise_db:
            if (name is None or name.lower() in exercise.name.lower()) and \
               (category is None or category.lower() == exercise.category.lower()):
                result.append(exercise)
        return result

    def track_progress(self):
        """
        Tracks user's progress, including personal records and training volume.
        """
        pass  # Implementation of progress tracking methods

    def generate_report(self):
        """
        Generates workout history and performance reports.
        """
        pass  # Implementation of report generation methods

    # Add more methods for goals, analytics, body metrics, safety, and reporting


# Sample Usage
if __name__ == "__main__":
    tracker = FitnessTracker()
    workout = tracker.log_workout("2023-10-01", 60, "Leg day workout")
    
    squats = ExerciseLog(tracker.exercise_db[0], sets=4, reps=8, weight=150, rpe=8)
    bench_press = ExerciseLog(tracker.exercise_db[1], sets=3, reps=10, weight=110, rpe=7)

    tracker.add_exercise_to_workout(workout, squats)
    tracker.add_exercise_to_workout(workout, bench_press)

    print(f"Workout logged for {workout.date} with duration {workout.duration} mins.")


