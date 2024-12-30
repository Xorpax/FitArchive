import pandas as pd
import datetime


class Handler:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.exercises = []
    
    def get_dataset(self) -> pd.DataFrame:
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            return e
    
    def update_exercises(self) -> None:
        current_exercises = self.get_dataset().columns
        self.exercises = current_exercises.values

    def add_exercise(self, exercise_name: str) -> str:
        self.update_exercises()
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        if exercise_name in self.exercises:
            return f"Entry for {exercise_name} already exists!"
        dataset[exercise_name] = ""
        dataset.to_csv(self.csv_path, index=False)
        return f"Entry for {exercise_name} has been successfully created."
    
    def add_exercise_data(self, exercise_name: str, score: float, date: str):
        raise NotImplementedError("This method will add scores (weight or reps) along with dates to the appropriate exercise")

# open csv file and read it, displaying contents in a gui
# allow adding scores with dates (writing to the csv)
