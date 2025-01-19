from gui import App
import os

if __name__ == "__main__":
    current_dir = os.getcwd()
    exercises_file = os.path.join(current_dir, "exercises.csv")
    FitArchive = App(csv_path=exercises_file)
    FitArchive.mainloop()
