import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


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
        if not self.is_csv_empty():
            current_exercises = self.get_dataset().columns
            self.exercises = current_exercises.values

    def add_exercise(self, exercise_name: str, category: str, units: str) -> str:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        if exercise_name in self.exercises:
            return f"Entry for {exercise_name} already exists!"
        if self.is_csv_empty():
            dataset = pd.DataFrame({exercise_name: [f"PR:0|{units}", f"Category:{category}", "Note:"]})
        else:
            dataset[exercise_name] = pd.Series([f"PR:0|{units}", f"Category:{category}", "Note:"])
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
        
        pb = float(dataset[exercise_name].tolist()[0].split("|")[0].split(":")[1])
        if score > pb:
            dataset.loc[0, exercise_name] = f"PR:{score}|{units}"
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
        dataset.drop(columns=exercise_name, inplace=True)
        dataset.to_csv(self.csv_path, index=False)
        self.update_exercises()
        return f"{exercise_name} and its records have successfully been removed."
    
    def remove_record(self, exercise_name: str, row_index: int) -> bool:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        if row_index > len(dataset[exercise_name]) - 1:
            print(f"Invalid index")
            return False
        if exercise_name not in self.exercises:
            print(f"No entry for {exercise_name}. Aborting.")
            return False
        if dataset.loc[row_index, exercise_name] == np.nan:
            print(f"Cannot remove {exercise_name} at {row_index}. Aborting.")
            return False
        dataset.loc[row_index, exercise_name] = np.nan
        dataset.dropna(subset=exercise_name, inplace=True)
        dataset.to_csv(self.csv_path, index=False)
        print(f"Successfully removed {exercise_name} at {row_index}")
        return True

    def sort_records(self, exercise_name: str, sort_type: str) -> tuple[pd.DataFrame, list[str]]:
        """Return a list of special rows (PR, Category, Note) and a dataframe of sorted scores"""
        sort_type = sort_type.capitalize()
        sort_types = ["Index ascending", "Index descending", "Score ascending", "Score descending", "Date ascending", "Date descending"]
        if sort_type not in sort_types:
            return f"No type {sort_type}"
        
        dataset = self.get_dataset()[exercise_name].dropna()
        special_fields = dataset[:3].str.split(":")
        dataset = dataset[3:]
        if dataset.empty:
            return dataset, special_fields
        if "descending" in sort_type:
            dataset = dataset[::-1]
        
        dataset = dataset.str.split("|", expand=True)
        unit = special_fields[0][1].split("|")[1]
        dataset[1] = pd.to_datetime(dataset[1], format="%d.%m.%Y")
        dataset[0] = pd.to_numeric(dataset[0].str.replace(unit, ""), downcast="float")

        if sort_type == sort_types[0]:
            dataset = dataset.sort_index(ascending=True,)
        elif sort_type == sort_types[1]:
            dataset = dataset.sort_index(ascending=False)
        elif sort_type == sort_types[2]:
            dataset = dataset.sort_values(by=0)
        elif sort_type == sort_types[3]:
            dataset = dataset.sort_values(by=0, ascending=False)
        elif sort_type == sort_types[4]:
            dataset = dataset.sort_values(by=1)
        elif sort_type == sort_types[5]:
            dataset = dataset.sort_values(by=1, ascending=False)
        return dataset, special_fields

    def is_csv_empty(self) -> bool:
        df = self.get_dataset()
        if isinstance(df, pd.DataFrame):
            return df.empty
        return True

    def is_date_duplicate(self, exercise_name: str, date: str):
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()[exercise_name][3:].str.split("|", expand=True)
        return date in dataset.values

    def save_note(self, exercise_name: str, note: str) -> str:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        if exercise_name not in self.exercises:
            return f"No entry for {exercise_name}"
        dataset.loc[2, exercise_name] = f"Note:{note}"
        dataset.to_csv(self.csv_path, index=False)
        return f"Succesfully saved the note for {exercise_name}"

    def edit_record(self, exercise_name: str, row_index: int, new_score: float) -> bool:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()
        num_rows = len(dataset[exercise_name])
        if row_index > num_rows:
            print("too many")
            return False
        pb_row = dataset[exercise_name][0]
        pb = float(pb_row.split("|")[0].split(":")[1])
        unit = pb_row.split("|")[1]
        if new_score > pb:
            pb = f"PR:{new_score}|{unit}"
            dataset.loc[0, exercise_name] = pb
        date = dataset[exercise_name][row_index].split("|")[1]
        dataset.loc[row_index, exercise_name] = f"{new_score}{unit}|{date}"
        dataset.to_csv(self.csv_path, index=False)
        return True

    def visualise(self, exercise_name: str) -> None:
        exercise_name = exercise_name.capitalize()
        dataset = self.get_dataset()[exercise_name].dropna()
        unit = dataset[0].split("|")[1]
        category = dataset[1].split(":")[1]
        df = dataset[3:].str.split("|", expand=True).reset_index(drop=True)
        scores = df[0].str.replace(unit, "").astype(float)
        df[0] = scores
        df.rename(columns={0: f"score ({unit})", 1: "date (DD-MM-YYYY)"}, inplace=True)

        # figure styling
        rc = {
            "axes.facecolor": "#353130",  # Dark grey background
            "axes.edgecolor": "#45403f",  # Grey axes edges
            "axes.labelcolor": "#ffffff",
            "grid.color": "#444444",      # Gray gridlines
            "text.color": "#ffffff",
            "xtick.color": "#ffffff",
            "ytick.color": "#ffffff",
            "xtick.labelsize": 12,        # Font size for x-tick labels
            "ytick.labelsize": 12,        # Font size for y-tick labels 
            "figure.facecolor": "#353130" # Window background color
        }

        sns.set_theme(context="paper", font_scale=1.75, rc=rc, style="darkgrid")
        plt.figure(figsize=(10, 7.8))
        sns.lineplot(data=df, x="date (DD-MM-YYYY)", y=f"score ({unit})", markers=True, marker="o", color="#f0a310", linewidth=2.25)
        plt.ylim(bottom=df[f"score ({unit})"].min(), top=df[f"score ({unit})"].max())
        plt.xlim(df["date (DD-MM-YYYY)"][0], df["date (DD-MM-YYYY)"].values[-1])
        plt.title(f"{exercise_name} ({category})")

        plt.xticks(rotation=-35)
        plt.yticks(df[f"score ({unit})"])
        plt.tight_layout()
        plt.show()