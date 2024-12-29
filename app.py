from csv_handler import Handler

if __name__ == "__main__":
    file_path = r".\example1.csv"
    wrong_path = r"..\example1.csv"
    h = Handler(csv_path=file_path)
    print(h.get_dataset())