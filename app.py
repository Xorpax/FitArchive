from csv_handler import Handler
from gui import App

if __name__ == "__main__":
    try:
        file_path = r".\example1.csv"
        empty_csv_path = r".\exercises.csv"
        h = Handler(csv_path=file_path)
        # h.add_exercise("Pull ups")
        # h.add_exercise_data("Pull ups", score=15, date="12.12.2024", units="reps")
        # h.add_exercise_data("Pull ups", score=16, date="13.12.2024", units="reps")
        # h.add_exercise_data("Pull ups", score=18, date="14.12.2024", units="reps")
        # print(h.get_dataset())
        # h.remove_exercise("pull ups")
        # h.add_exercise_data("Goblet squats", score=7, date="14.12.2024", units="kg")
        # h.add_exercise_data("Goblet squats", score=7, date="16.12.2024", units="kg")
        # print(h.get_dataset())
        # h.remove_record(exercise_name="goblet squats", row_index=1)
        FitArchive = App(csv_path=empty_csv_path)
        FitArchive.mainloop()
    except KeyboardInterrupt:
        print("Closing...")
