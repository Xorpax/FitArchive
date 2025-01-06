from csv_handler import Handler
from gui import App

if __name__ == "__main__":
    try:
        file_path = r".\example1.csv"
        empty_csv_path = r".\exercises.csv"
        h = Handler(csv_path=file_path)
        FitArchive = App(csv_path=file_path)
        FitArchive.mainloop()
    except KeyboardInterrupt:
        print("Closing...")
