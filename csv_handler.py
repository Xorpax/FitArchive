import pandas as pd
import numpy as np
import datetime


class Handler:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.exercises = []
        self.update_exercises()
    
    def get_dataset(self) -> pd.DataFrame:
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            return e
    
    def update_exercises(self) -> None:
        current_exercises = self.get_dataset().columns
        self.exercises = current_exercises.values

    def add_exercise(self, exercise_name: str) -> str:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        if exercise_name in self.exercises:
            return f"Entry for {exercise_name} already exists!"
        dataset[exercise_name] = ""
        dataset.to_csv(self.csv_path, index=False)
        self.update_exercises()
        return f"Entry for {exercise_name} has been successfully created."
    
    def add_exercise_data(self, exercise_name: str, score: float, date: str, units:str) -> str:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        correct_datatypes = (isinstance(score, float) or isinstance(score, int)) and isinstance(date, str) and isinstance(units, str)
        if exercise_name not in self.exercises:
            return f"No entry for {exercise_name}. Aborting"
        try:
            assert correct_datatypes
        except AssertionError:
            return f"Invalid data types"
        
        exercise_col = dataset[exercise_name].dropna()
        entry_index = len(exercise_col)
        entry = f"{score}{units}|{date}"
        dataset.loc[entry_index, exercise_name] = entry
        dataset.to_csv(self.csv_path, index=False)
        self.update_exercises()
        return f"Entry: {entry} successfully added for {exercise_name}"
    
    def remove_exercise(self, exercise_name: str) -> str:
        exercise_name = exercise_name.capitalize()
        if exercise_name not in self.exercises:
            return f"No entry for {exercise_name}"
        dataset = self.get_dataset()
        entries_len = len(dataset[exercise_name].dropna())
        choice = input(f"There are {entries_len} entries for {exercise_name}. Would you like to remove them? (Y/N)").upper()
        if choice[0] == "Y":
            dataset.drop(columns=exercise_name, inplace=True)
            dataset.to_csv(self.csv_path, index=False)
            return f"{exercise_name} and its records have successfully been removed."
        return f"Aborting."
    
    def remove_record(self, exercise_name: str, row_index: int) -> str:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        if exercise_name not in self.exercises:
            return f"No entry for {exercise_name}. Aborting."
        if dataset.loc[row_index, exercise_name] == np.nan:
            return f"Cannot remove {exercise_name} at {row_index}. Aborting."
        dataset.loc[row_index, exercise_name] = np.nan
        dataset.dropna(subset=exercise_name, inplace=True)
        dataset.to_csv(self.csv_path, index=False)
        return f"Successfully removed {exercise_name} at {row_index}"
        

# open csv file and read it, displaying contents in a gui
# allow adding scores with dates (writing to the csv)
