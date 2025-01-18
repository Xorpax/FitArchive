from gui import App
import os

if __name__ == "__main__":
    current_dir = os.getcwd()
    empty_csv_path = os.path.join(current_dir, "exercises.csv")
    mine = os.path.join(current_dir, "private.csv")
    FitArchive = App(csv_path=empty_csv_path)
    FitArchive.mainloop()
