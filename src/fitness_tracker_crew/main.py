#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from crew import FitnessTrackerTeam
except ImportError:
    # Alternative import for different project structures
    from .crew import FitnessTrackerTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A comprehensive fitness workout tracking system with the following features:

Exercise Management:
- Pre-loaded exercise database with categories (strength, cardio, flexibility)
- Exercise details: name, category, primary muscles, equipment, instructions
- Custom exercise creation
- Exercise search and filtering

Workout Logging:
- Log workouts with date, duration, and notes
- Log individual exercises with sets, reps, weight, distance, time
- Support for different exercise types (strength, cardio, bodyweight)
- RPE (Rate of Perceived Exertion) tracking
- Workout templates for common routines

Progress Tracking:
- Track personal records (1RM, max reps, best time)
- Calculate training volume (sets × reps × weight)
- Progress charts for strength, endurance, and body metrics
- Workout frequency and consistency tracking
- Strength standards and progress indicators

Analytics & Insights:
- 1RM (One Rep Max) estimation using Epley/Brzycki formulas
- Training volume analytics over time
- Progress rate calculations
- Workout intensity analysis
- Recovery and fatigue indicators
- Goal setting and achievement tracking

Body Metrics:
- Track weight, body fat percentage, measurements
- Progress photos (metadata tracking)
- Body metric trends and correlations with performance

Goals & Planning:
- Set fitness goals (strength, endurance, weight loss/gain)
- Workout plan creation and scheduling
- Goal progress tracking and adjustments
- Milestone celebrations

Safety & Validation:
- Prevent unrealistic weight/reps entries
- Form reminders and safety guidelines
- Progressive overload recommendations
- Deload week suggestions

Reporting:
- Workout history and statistics
- Performance reports
- Export data to CSV/PDF
- Share workout achievements

The system should include a comprehensive exercise database with at least 50 common exercises across different categories.
Include sample workout data for demonstration purposes.
"""

module_name = "workout_tracker"
class_name = "FitnessTracker"

def run():
    """
    Run the fitness tracker crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = FitnessTrackerTeam().crew().kickoff(inputs=inputs)
    print("Fitness Workout Tracker development completed!")

if __name__ == "__main__":
    run()