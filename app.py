from gui import App

if __name__ == "__main__":
    empty_csv_path = r".\exercises.csv"
    mine = r".\private.csv"
    FitArchive = App(csv_path=mine)
    FitArchive.mainloop()
