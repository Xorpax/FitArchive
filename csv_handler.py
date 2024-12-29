import pandas as pd



class Handler:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.workouts = []
    
    def get_dataset(self):
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            return e
    
    def update_workouts(self) -> None:
        current_workouts = self.get_dataset().columns.values
        self.workouts = current_workouts

    def add_workout(self, workout_name: str) -> str:
        self.update_workouts()
        workout_name = workout_name.capitalize()
        dataset = self.get_dataset()
        if workout_name in self.workouts:
            return f"Entry for {workout_name} already exists!"
        dataset[workout_name] = ""
        dataset.to_csv(self.csv_path, index=False)
        return f"Entry for {workout_name} has been successfully created."

# open csv file and read it, displaying contents in a gui
# allow adding scores with dates (writing to the csv)
#
