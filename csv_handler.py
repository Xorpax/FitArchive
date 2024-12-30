import pandas as pd
import datetime


class Handler:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.workouts = []
    
    def get_dataset(self) -> pd.DataFrame:
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            return e
    
    def update_workouts(self) -> None:
        current_workouts = self.get_dataset().columns
        self.workouts = current_workouts.values

    def add_workout(self, workout_name: str) -> str:
        self.update_workouts()
        workout_name = workout_name.capitalize()
        dataset = self.get_dataset()
        if workout_name in self.workouts:
            return f"Entry for {workout_name} already exists!"
        dataset[workout_name] = ""
        dataset.to_csv(self.csv_path, index=False)
        return f"Entry for {workout_name} has been successfully created."
    
    def add_workout_data(self, workout_name: str, score: float, date: str):
        raise NotImplementedError("This method will add scores (weight or reps) along with dates to the appropriate exercise")

# open csv file and read it, displaying contents in a gui
# allow adding scores with dates (writing to the csv)
