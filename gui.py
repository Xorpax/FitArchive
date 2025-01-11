import customtkinter as ctk
from PIL import Image
import configparser
from csv_handler import Handler
import pandas as pd
from datetime import datetime
import os
import string
from tkinter import font

CONFIG = configparser.ConfigParser()
CONFIG.read(r".\config.ini")
THEMES_PATH = r".\themes"
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")
# ctk.set_default_color_theme("green")
THEME = CONFIG["Appearance"]["Theme"]
COLOUR_SCHEME = CONFIG["Appearance"]["ColourScheme"]

ctk.set_appearance_mode(THEME)
ctk.set_default_color_theme(COLOUR_SCHEME)


class SidePanel(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.fitarchive_path = r".\assets\FitArchiveLogo.png"
        self.collapse_path = r".\assets\push_left_icon.png"
        self.collapse_img = ctk.CTkImage(Image.open(self.collapse_path), size=(25, 25))
        self.expand_path = r".\assets\push_right_icon.png"
        self.expand_img = ctk.CTkImage(Image.open(self.expand_path), size=(25, 25))
        self.exercises_path = r".\assets\exercise.png"
        self.bmi_calculator_path = r".\assets\calculator.png"
        self.measurements_path = r".\assets\muscle.png"
        self.notes_path = r".\assets\notes.png"
        self.settings_path = r".\assets\settings.png"
        self.font = CONFIG["SidePanel"]["Font"]
        self.font_size = int(CONFIG["SidePanel"]["FontSize"])
        self.text_color = CONFIG["SidePanel"]["TextColor"]
        self.buttons = []
        self.btn_height = int(CONFIG["SidePanel"]["BtnHeight"])
        
        self.initialise_buttons()
    
    def initialise_buttons(self) -> None:
        fitarchive_img = ctk.CTkImage(Image.open(self.fitarchive_path), size=(25, 25))
        landing_page_btn = ctk.CTkButton(self,
                                       corner_radius=0,
                                       image=fitarchive_img,
                                       compound=ctk.RIGHT,
                                       text_color=self.text_color,
                                       font=(self.font, self.font_size),
                                       height=self.btn_height,
                                       anchor=ctk.W, 
                                       command=self.collapse, 
                                       textvariable=ctk.StringVar(value="FitArchive"))

        self.title_btn = ctk.CTkButton(self,
                                       corner_radius=0,
                                       image=self.collapse_img,
                                       compound=ctk.RIGHT,
                                       text_color=self.text_color,
                                       font=(self.font, self.font_size),
                                       height=self.btn_height,
                                       anchor=ctk.W, 
                                       command=self.collapse, 
                                       textvariable=ctk.StringVar(value="Side Panel"))

        exercises_img = ctk.CTkImage(Image.open(self.exercises_path), size=(25, 25))
        exercises_btn = ctk.CTkButton(self,
                                    corner_radius=0,
                                    image=exercises_img,
                                    compound=ctk.RIGHT,
                                    text_color=self.text_color,
                                    font=(self.font, self.font_size),
                                    height=self.btn_height,
                                    anchor=ctk.W,
                                    textvariable=ctk.StringVar(value="Exercises"))

        bmi_calculator_img = ctk.CTkImage(Image.open(self.bmi_calculator_path), size=(25, 25))
        bmi_calculator_btn = ctk.CTkButton(self,
                                        corner_radius=0,
                                        image=bmi_calculator_img,
                                        compound=ctk.RIGHT,
                                        text_color=self.text_color,
                                        font=(self.font, self.font_size),
                                        height=self.btn_height,
                                        anchor=ctk.W,
                                        textvariable=ctk.StringVar(value="BMI Calculator"))

        notes_img = ctk.CTkImage(Image.open(self.notes_path), size=(25, 25))
        notes_btn = ctk.CTkButton(self,
                                corner_radius=0,
                                image=notes_img,
                                compound=ctk.RIGHT,
                                text_color=self.text_color,
                                font=(self.font, self.font_size),
                                height=self.btn_height,
                                anchor=ctk.W,
                                textvariable=ctk.StringVar(value="Notes"))  

        settings_img = ctk.CTkImage(Image.open(self.settings_path), size=(25, 25))
        settings_btn = ctk.CTkButton(self,
                                    corner_radius=0,
                                    image=settings_img,
                                    compound=ctk.RIGHT,
                                    text_color=self.text_color,
                                    font=(self.font, self.font_size),
                                    height=self.btn_height,
                                    anchor=ctk.W,
                                    textvariable=ctk.StringVar(value="Settings"))

        self.buttons.append(self.title_btn)
        self.buttons.append(landing_page_btn)
        self.buttons.append(exercises_btn)
        self.buttons.append(bmi_calculator_btn)
        self.buttons.append(notes_btn)
        self.buttons.append(settings_btn)

        self.title_btn.pack(anchor=ctk.N, fill=ctk.X)
        landing_page_btn.pack(anchor=ctk.N, fill=ctk.X)
        exercises_btn.pack(anchor=ctk.N, fill=ctk.X)
        bmi_calculator_btn.pack(anchor=ctk.N, fill=ctk.X)
        notes_btn.pack(anchor=ctk.N, fill=ctk.X)
        settings_btn.pack(anchor=ctk.S, fill=ctk.X, side=ctk.BOTTOM)

    def collapse(self) -> None:
        for btn in self.buttons:
            txt_var = btn.cget("textvariable").get()
            if txt_var == "Side Panel":
                btn.configure(image=self.expand_img, command=self.expand)
            btn.configure(text="", width=45)

    def expand(self) -> None:
        for btn in self.buttons:
            txt_var = btn.cget("textvariable").get()
            if txt_var == "Side Panel":
                btn.configure(image=self.collapse_img, command=self.collapse)
            btn.configure(text=btn.cget("textvariable"))

class App(ctk.CTk):
    def __init__(self, csv_path) -> None:
        super().__init__()

        # config info
        self.font_type = CONFIG["MainPanel"]["Font"]
        self.header_size = int(CONFIG["MainPanel"]["HeaderSize"])
        self.font_size = int(CONFIG["MainPanel"]["FontSize"])

        # button functions
        self.btn_functions = {
            "FitArchive": self.show_landing_page,
            "Exercises": self.exercises,
            "BMI Calculator": self.bmi_calculator,
            "Measurements": self.measurements,
            "Notes": self.notes,
            "Settings": self.settings,
        }

        # information about user's display
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # window setup
        self.minsize(width=1405, height=800)
        self.maxsize(width=self.screen_width, height=self.screen_height)
        self.geometry(f"{self.screen_width}x{self.screen_height}")
        self.title("FitArchive")
        self.iconbitmap(r".\assets\FitArchiveLogo1.ico")
        self.after(0, lambda: self.wm_state('zoomed'))

        # side panel
        self.side_panel = SidePanel(self, corner_radius=0, border_color="blue", border_width=0)
        self.side_panel.pack(expand=False, side=ctk.LEFT, fill=ctk.BOTH, anchor=ctk.NW, padx=1)
        for btn in self.side_panel.buttons:
            btn_val = btn.cget("textvariable").get()
            if btn_val != "Side Panel":
                btn.configure(command=self.btn_functions.get(btn_val))

        # main panel
        self.main_panel = ctk.CTkFrame(self, corner_radius=0, border_color="red", border_width=0)
        self.main_panel.pack(expand=True, fill=ctk.BOTH, side=ctk.RIGHT)
        self.show_landing_page()

        # file operations
        self.csv_path = csv_path
        self.handler = Handler(self.csv_path)
              

    def show_landing_page(self) -> None:
        # welcome section
        self.clear_main_panel()
        header = ctk.CTkLabel(self.main_panel, text="Welcome to FitArchive!", font=(self.font_type, self.header_size, "bold"), anchor=ctk.NW)
        header.pack(pady=40)
        motto = ctk.CTkLabel(self.main_panel, text="Track your workouts, achieve your goals.", font=(self.font_type, self.font_size), anchor=ctk.NW)
        motto.pack(pady=10)

        # features
        features_frame = ctk.CTkFrame(self.main_panel, border_color="green", border_width=0)
        features_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=20, pady=20)
        features_label = ctk.CTkLabel(features_frame, text="Features:", font=(self.font_type, self.header_size, "underline"))
        features_label.pack(padx=10, pady=10, side=ctk.TOP, anchor=ctk.NW)
        
        # buttons
        buttons_frame = ctk.CTkFrame(features_frame, border_color="cyan", border_width=0)
        buttons_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=10, pady=10)
        buttons_frame.rowconfigure(0, weight=1)
        buttons_frame.columnconfigure(list(range(4)), weight=1)
        exercises_btn = ctk.CTkButton(buttons_frame,
                                        text="Exercises",
                                        font=(self.font_type, self.font_size),
                                        anchor=ctk.N,
                                        border_spacing=20,
                                        command=self.exercises)
        exercises_btn.grid(row=0, column=0, sticky=ctk.NSEW, padx=15, pady=15)

        bmi_calculator_btn = ctk.CTkButton(buttons_frame,
                                           text="BMI calculator",
                                           font=(self.font_type, self.font_size),
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.bmi_calculator)
        bmi_calculator_btn.grid(row=0, column=1, sticky=ctk.NSEW, padx=15, pady=15)

        notes_btn = ctk.CTkButton(buttons_frame,
                                    text="Notes",
                                    font=(self.font_type, self.font_size),
                                    anchor=ctk.N,
                                    border_spacing=20,
                                    command=self.notes)
        notes_btn.grid(row=0, column=2, sticky=ctk.NSEW, padx=15, pady=15)

        settings_btn = ctk.CTkButton(buttons_frame,
                                    text="Settings",
                                    font=(self.font_type, self.font_size),
                                    anchor=ctk.N,
                                    border_spacing=20,
                                    command=self.settings)
        settings_btn.grid(row=0, column=3, sticky=ctk.NSEW, padx=15, pady=15)
    
    def clear_main_panel(self) -> None:
        print("Clearing main panel...")
        self.main_panel.destroy()
        self.main_panel = ctk.CTkFrame(self, corner_radius=0, border_color="red", border_width=0)
        self.main_panel.pack(expand=True, fill=ctk.BOTH, side=ctk.RIGHT)
        # for widget in self.main_panel.winfo_children():
        #     widget.destroy()

    def reset_config(self) -> None:
        self.main_panel.columnconfigure(list(range(100)), weight=0)
        self.main_panel.rowconfigure(list(range(100)), weight=0)

    def exercises(self) -> None:
        self.clear_main_panel()
        top_panel = ctk.CTkFrame(self.main_panel, corner_radius=0, border_color="orange", border_width=0)
        top_panel.pack(expand=False, fill=ctk.X, anchor=ctk.NW, padx=5, pady=5)
        exercises_label = ctk.CTkLabel(top_panel, text="Exercises", font=(self.font_type, self.header_size))
        exercises_label.pack(anchor=ctk.NW, padx=(10, 0), pady=(25, 10), side=ctk.LEFT)
        add_btn = ctk.CTkButton(top_panel,
                                text="+ Add Exercise",
                                width=45,
                                height=45,
                                font=(self.font_type, self.font_size, "bold"),
                                border_spacing=5,
                                fg_color="green",
                                command=self.add_exercise_window)
        add_btn.pack(anchor=ctk.NE, padx=(0, 10), pady=(20, 15), side=ctk.RIGHT)
        exercises_frame = ctk.CTkScrollableFrame(self.main_panel, corner_radius=0, border_color="yellow", border_width=0)
        exercises_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=5, pady=(0, 5), side=ctk.TOP)
        exercises_list = self.handler.exercises
        no_exercises = self.handler.is_csv_empty()
        if no_exercises:
            exercises_label.configure(text="No exercises added yet. Why not start by adding one?", text_color="red")
            return
        col = 0
        row = 0
        for exercise in exercises_list:
            exercise_btn = ctk.CTkButton(exercises_frame,
                                        text=exercise,
                                        width=250,
                                        font=(self.font_type, self.font_size),
                                        anchor=ctk.N,
                                        border_spacing=12,
                                        command=lambda ex=exercise: self.show_exercise(ex))
            exercise_btn.grid(column=col%5, row=row, sticky=ctk.NSEW, padx=19, pady=10)
            col += 1
            if col % 5 == 0:
                row += 1
        
        if col == 0:
            col = 1
        if row == 0:
            row = 1
        exercises_frame.columnconfigure(list(range(col)), weight=1)
        exercises_frame.rowconfigure(list(range(row)), weight=1)

    def add_exercise_window(self) -> None:
        def submit_exercise(name: str, category: str, units: str) -> None:
            name = name.capitalize()
            exercises_list = self.handler.exercises
            if name in exercises_list:
                name_label.configure(text=f"An entry for {name} already exists.", text_color="red")
            else:
                print(self.handler.add_exercise(name, category, units))
                new_exercise.destroy()
                self.exercises()
        
        x = (self.screen_width - 640) // 2
        y = (self.screen_height -360) // 2
        new_exercise = ctk.CTkToplevel(self)
        new_exercise.title("New exercise")
        new_exercise.geometry(f"640x480+{x}+{y}")
        new_exercise.resizable(False, False)
        # use after due to customtkinter's implementation where some data is set after 200ms
        new_exercise.after(300, new_exercise.focus)
        new_exercise.after(200, lambda: new_exercise.iconbitmap(r".\assets\FitArchiveLogo1.ico"))
        name_label = ctk.CTkLabel(new_exercise, text="Enter your exercise name", font=(self.font_type, self.header_size))
        name_label.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 20))
        name_entry = ctk.CTkEntry(new_exercise, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=350, height=40)
        name_entry.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(0, 20))
        category_label = ctk.CTkLabel(new_exercise, text="Enter the category", font=(self.font_type, self.header_size))
        category_label.pack(side=ctk.TOP, anchor=ctk.CENTER)
        category_entry = ctk.CTkEntry(new_exercise, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=350, height=40)
        category_entry.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 0))
        units_label = ctk.CTkLabel(new_exercise, text="Enter the units", font=(self.font_type, self.header_size))
        units_label.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20,0))
        units_entry = ctk.CTkEntry(new_exercise, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=350, height=40)
        units_entry.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 0))

        submit_btn = ctk.CTkButton(new_exercise,
                                   text="Submit",
                                   width=100,
                                   height=50,
                                   font=(self.font_type, self.font_size),
                                   command=lambda: submit_exercise(name_entry.get(), category_entry.get(), units_entry.get()))
        submit_btn.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 15))

    def show_exercise(self, exercise_name: str) -> None:
        self.clear_main_panel()
        self.reset_config()
        def list_scores(sort_type: str="Index ascending"):
            print(f"{sort_type=}")
            data = self.handler.sort_records(exercise_name, sort_type=sort_type)
            special_rows = data[1]
            df = data[0]
            col = 0
            row_num = 0
            unit = special_rows[0][1].split("|")[1]
            pb = special_rows[0][1].replace("|", "")
            category = special_rows[1][1]
            note = special_rows[2][1]
            label.configure(text=f"{exercise_name}\n({category})")
            notes_box.delete("0.0", ctk.END)
            notes_box.insert("0.0", text=note)
            pb_label.configure(text=f"PB: {pb}")
            if df.empty:
                return
            for index, row in df.iterrows():
                date = row[1].date().strftime("%d.%m.%Y")
                score_label = ctk.CTkLabel(scorebox, text=f"{index - 2}. {row[0]}{unit} ({date})", font=(self.font_type, self.font_size))
                score_label.grid(column=col%4, row=row_num, padx=(50, 0), pady=15, sticky=ctk.NW)
                col += 1
                if col%4 == 0:
                    row_num += 1 

        exercise_name = exercise_name.capitalize()
        # left side
        label = ctk.CTkLabel(self.main_panel, text=exercise_name, font=(self.font_type, self.header_size))
        label.grid(column=0, row=0, padx=15, pady=15, sticky=ctk.NW)
        notes_label = ctk.CTkLabel(self.main_panel, text="Notes", font=(self.font_type, self.header_size))
        notes_label.grid(column=0, row=1, padx=15, pady=15, sticky=ctk.NW)
        notes_box = ctk.CTkTextbox(self.main_panel, font=(self.font_type, self.font_size), wrap="word", width=300, height=500)
        notes_box.grid(column=0, row=2, padx=15, rowspan=2, sticky=ctk.NW)
        self.main_panel.grid_rowconfigure(2, weight=1)
        save_notes_btn = ctk.CTkButton(self.main_panel,
                                       text="Save",
                                       font=(self.font_type, self.header_size),
                                       command=lambda: self.save_exercise_note(exercise_name, notes_box.get("0.0", ctk.END)))
        save_notes_btn.grid(column=0, row=4, sticky=ctk.NW, padx=15, pady=15, rowspan=2)
        remove_exercise_btn = ctk.CTkButton(self.main_panel,
                                            text="Delete exercise",
                                            font=(self.font_type, self.header_size),
                                            fg_color="red",
                                            command=lambda: self.delete_exercise(exercise_name))
        remove_exercise_btn.grid(column=0, row=6, padx=15, pady=15, sticky=ctk.SW)

        # right side
        sort_label = ctk.CTkLabel(self.main_panel, text="Sort records:", font=(self.font_type, self.header_size))
        sort_label.grid(column=1, row=0, padx=30, pady=15, sticky=ctk.NW, columnspan=2)
        sort_var = ctk.StringVar(value="Index ascending")
        sort = ctk.CTkComboBox(self.main_panel,
                               values=["Index ascending", "Index descending", "Score ascending", "Score descending", "Date ascending", "Date descending"],
                               font=(self.font_type, self.font_size),
                               width=250,
                               height=35,
                               state="readonly",
                               variable=sort_var,
                               command=lambda s: list_scores(sort_type=sort_var.get()))
        sort.grid(column=1, row=1, padx=30, sticky=ctk.NW, columnspan=3)
        pb_label = ctk.CTkLabel(self.main_panel, text="PB: ", font=(self.font_type, self.header_size))
        pb_label.grid(column=4, row=0, padx=30, pady=15, sticky=ctk.NW)

        scorebox = ctk.CTkScrollableFrame(self.main_panel, border_color="orange", border_width=0, orientation="horizontal")
        scorebox.grid(column=1, row=2, padx=30, columnspan=5, sticky=ctk.NSEW, rowspan=3)
        self.main_panel.grid_columnconfigure(1, weight=1)
        self.main_panel.rowconfigure(4, weight=1)

        visualise_btn = ctk.CTkButton(self.main_panel,
                                      text="Visualise",
                                      font=(self.font_type, self.header_size),
                                      command=lambda: self.handler.visualise(exercise_name),
                                      fg_color="#3F8CFF")
        visualise_btn.grid(column=1, row=5, padx=(0, 30), pady=15, sticky=ctk.NE)
        add_score_btn = ctk.CTkButton(self.main_panel,
                                      text="Add score",
                                      font=(self.font_type, self.header_size),
                                      command=lambda: self.add_exercise_data(exercise_name),
                                      fg_color="#50FFD6")
        add_score_btn.grid(column=2, row=5, padx=(0, 30), pady=15, sticky=ctk.NE)
        edit_score_btn = ctk.CTkButton(self.main_panel,
                                      text="Edit score",
                                      font=(self.font_type, self.header_size),
                                      command=lambda: self.edit_exercise_data(exercise_name),
                                      fg_color="#FF9350")
        edit_score_btn.grid(column=3, row=5, padx=(0, 30), pady=15, sticky=ctk.NE)
        remove_score_btn = ctk.CTkButton(self.main_panel,
                                      text="Remove score",
                                      font=(self.font_type, self.header_size),
                                      command=lambda: self.delete_exercise_data(exercise_name),
                                      fg_color="#FF5050")
        remove_score_btn.grid(column=4, row=5, padx=(0, 30), pady=15, sticky=ctk.NE)

        list_scores()

    def delete_exercise_data(self, exercise_name: str) -> None:
        def validate_index(index: str):
            try:
                index = int(index)
            except ValueError:
                delete_scr_label.configure(text="Invalid index", text_color="red")
                return
            if index < 1:
                delete_scr_label.configure(text="Invalid index", text_color="red")
                return
            index += 2
            response = self.handler.remove_record(exercise_name, index)
            if response:
                delete_scr.destroy()
                self.show_exercise(exercise_name)
            else:
                delete_scr_label.configure(text="Invalid index", text_color="red")

        delete_scr = ctk.CTkToplevel(self)
        x = (self.screen_width - 640) // 2
        y = (self.screen_height -360) // 2
        delete_scr.title("Remove score")
        delete_scr.geometry(f"500x280+{x}+{y}")
        delete_scr.resizable(False, False)
        # use after due to customtkinter's implementation where some data is set after 200ms
        delete_scr.after(300, delete_scr.focus)
        delete_scr.after(200, lambda: delete_scr.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        delete_scr_label = ctk.CTkLabel(delete_scr, text="Enter the index to be removed:", font=(self.font_type, self.header_size))
        delete_scr_label.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 15))
        sure_label = ctk.CTkLabel(delete_scr, text="This action is irreversible", font=(self.font_type, self.font_size), text_color="red")
        sure_label.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(0, 20))
        
        index_entry = ctk.CTkEntry(delete_scr, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=150, height=40)
        index_entry.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(0, 20))
        submit_btn = ctk.CTkButton(delete_scr, text="Submit", font=(self.font_type, self.header_size), command=lambda: validate_index(index_entry.get()))
        submit_btn.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(10, 0))

    def add_exercise_data(self, exercise_name: str) -> None:
        def validate_score(score: str, day: str, month: str, year: str):
            try:
                score = float(score)
                day = int(day)
                month = int(month)
                year = int(year)
                date = datetime(year=year, month=month, day=day)
            except ValueError:
                add_scr_label.configure(text="Invalid score or date", text_color="red")
                return
            if score < 0:
                add_scr_label.configure(text="Your score cannot be negative", text_color="red")
                return

            date = date.strftime("%d.%m.%Y")
            if self.handler.is_date_duplicate(exercise_name, date):
                add_scr_label.configure(text=f"No duplicate dates!", text_color="red")
                return
            unit = self.handler.get_dataset()[exercise_name].tolist()[0].split("|")[1]
            print(self.handler.add_exercise_data(exercise_name, score, date, unit))
            add_scr.destroy()
            self.show_exercise(exercise_name)

        add_scr = ctk.CTkToplevel(self)
        x = (self.screen_width - 640) // 2
        y = (self.screen_height - 360) // 2
        add_scr.title("Add score")
        add_scr.geometry(f"500x400+{x}+{y}")
        add_scr.resizable(False, False)
        # use after due to customtkinter's implementation where some data is set after 200ms
        add_scr.after(300, add_scr.focus)
        add_scr.after(200, lambda: add_scr.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        add_scr_label = ctk.CTkLabel(add_scr, text="Enter new score:", font=(self.font_type, self.header_size))
        add_scr_label.grid(column=1, row=0, sticky=ctk.N, pady=(15, 0))
        info_label = ctk.CTkLabel(add_scr, text="Do not include units!", font=(self.font_type, self.font_size), text_color="red")
        info_label.grid(column=1, row=1, sticky=ctk.N, pady=(15, 0))

        score_entry = ctk.CTkEntry(add_scr, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=150, height=40)
        score_entry.grid(column=1, row=2, sticky=ctk.N, pady=15)

        day_label = ctk.CTkLabel(add_scr, text="Day", font=(self.font_type, self.font_size))
        day_label.grid(column=0, row=3, sticky=ctk.N, pady=(15, 0), padx=(75, 0))
        month_label = ctk.CTkLabel(add_scr, text="Month", font=(self.font_type, self.font_size))
        month_label.grid(column=1, row=3, sticky=ctk.N, pady=(15, 0))
        year_label = ctk.CTkLabel(add_scr, text="Year", font=(self.font_type, self.font_size))
        year_label.grid(column=2, row=3, sticky=ctk.N, pady=(15, 0))

        day_entry = ctk.CTkEntry(add_scr, placeholder_text="0-31", font=(self.font_type, self.font_size), width=100)
        day_entry.grid(column=0, row=4, sticky=ctk.N, pady=(15, 0), padx=(20, 0))
        month_entry = ctk.CTkEntry(add_scr, placeholder_text="1-12", font=(self.font_type, self.font_size), width=100)
        month_entry.grid(column=1, row=4, sticky=ctk.N, pady=(15, 0))
        year_entry = ctk.CTkEntry(add_scr, placeholder_text="YYYY", font=(self.font_type, self.font_size), width=100)
        year_entry.grid(column=2, row=4, sticky=ctk.N, pady=(15, 0))

        submit_btn = ctk.CTkButton(add_scr,
                                   text="Submit",
                                   font=(self.font_type, self.header_size),
                                   command=lambda: validate_score(score_entry.get(), day_entry.get(), month_entry.get(), year_entry.get()))
        submit_btn.grid(column=1, row=5, sticky=ctk.N, pady=(40, 0))

    def edit_exercise_data(self, exercise_name: str) -> None:
        def validate_score(score: str, index: int):
            try:
                score = float(score)
                index = int(index)
            except ValueError:
                add_scr_label.configure(text="Invalid score or index", text_color="red")
                return
            if score < 0 or index <= 0:
                add_scr_label.configure(text="Invalid score or index", text_color="red")
                return
            
            index += 2
            edit = self.handler.edit_record(exercise_name, index, score)
            if edit:
                edit_scr.destroy()
                self.show_exercise(exercise_name)
                return
            add_scr_label.configure(text="Invalid index", text_color="red")

        edit_scr = ctk.CTkToplevel(self)
        x = (self.screen_width - 640) // 2
        y = (self.screen_height - 360) // 2
        edit_scr.title("Edit score")
        edit_scr.geometry(f"400x400+{x}+{y}")
        edit_scr.resizable(False, False)
        # use after due to customtkinter's implementation where some data is set after 200ms
        edit_scr.after(300, edit_scr.focus)
        edit_scr.after(200, lambda: edit_scr.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        add_scr_label = ctk.CTkLabel(edit_scr, text="Enter new score:", font=(self.font_type, self.header_size))
        add_scr_label.grid(column=0, row=0, pady=(15, 0), padx=(80, 0))
        info_label = ctk.CTkLabel(edit_scr, text="Do not include units!", font=(self.font_type, self.font_size), text_color="red")
        info_label.grid(column=0, row=1, pady=(15, 0), padx=(80, 0))

        score_entry = ctk.CTkEntry(edit_scr, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=150, height=40)
        score_entry.grid(column=0, row=2, pady=15, padx=(80, 0))
        
        index_label = ctk.CTkLabel(edit_scr, text="Index", font=(self.font_type, self.header_size))
        index_label.grid(column=0, row=3, pady=(15, 0), padx=(80, 0))
        index_entry = ctk.CTkEntry(edit_scr, font=(self.font_type, self.font_size), width=100, height=40, placeholder_text="...")
        index_entry.grid(column=0, row=4, pady=15, padx=(80, 0))

        submit_btn = ctk.CTkButton(edit_scr,
                                   text="Submit",
                                   font=(self.font_type, self.header_size),
                                   command=lambda: validate_score(score_entry.get(), index_entry.get()))
        submit_btn.grid(column=0, row=7, pady=(40, 0), padx=(80, 0))

    def save_exercise_note(self, exercise_name: str, note: str) -> None:
        note = note.rstrip()[:200]
        self.handler.save_note(exercise_name, note)
        self.show_exercise(exercise_name)

    def delete_exercise(self, exercise_name: str) -> None:
        def submit(choice: int):
            print(choice)
            if choice:
                del_exercise_label.configure(text=choice, text_color="green")
                self.handler.remove_exercise(exercise_name)
                del_exercise.destroy()
                self.exercises()
                return
            del_exercise_label.configure(text=choice, text_color="red")
            del_exercise.destroy()

        del_exercise = ctk.CTkToplevel(self)
        x = (self.screen_width - 640) // 2
        y = (self.screen_height -360) // 2
        del_exercise.title(f"Delete {exercise_name}")
        del_exercise.geometry(f"450x300+{x}+{y}")
        del_exercise.resizable(False, False)
        # use after due to customtkinter's implementation where some data is set after 200ms
        del_exercise.after(300, del_exercise.focus)
        del_exercise.after(200, lambda: del_exercise.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        del_exercise_label = ctk.CTkLabel(del_exercise, text="Are you sure?", font=(self.font_type, self.header_size))
        del_exercise_label.pack(side=ctk.TOP, pady=(10, 0))
        info_label = ctk.CTkLabel(del_exercise, text="This action is irreversible", font=(self.font_type, self.font_size), text_color="red")
        info_label.pack(side=ctk.TOP, pady=(10, 0))

        radio_var = ctk.IntVar(value=0)
        yes_btn = ctk.CTkRadioButton(del_exercise, text="Yes", font=(self.font_type, self.font_size), variable=radio_var, value=1)
        yes_btn.pack(side=ctk.TOP, pady=(25, 0))
        no_btn = ctk.CTkRadioButton(del_exercise, text="No", font=(self.font_type, self.font_size), variable=radio_var, value=0)
        no_btn.pack(side=ctk.TOP, pady=(15, 0))

        submit_btn = ctk.CTkButton(del_exercise, text="Submit", font=(self.font_type, self.header_size), command=lambda: submit(radio_var.get()))
        submit_btn.pack(side=ctk.TOP, pady=(45, 10))

    def bmi_calculator(self) -> None:
        self.reset_config()
        self.clear_main_panel()
        def calculate_bmi(weight: str, height: str):
            try:
                weight = float(weight)
                height = float(height)
            except ValueError:
                result_lbl.configure(text="Invalid weight or height", text_color="red")
                return
            height /= 100
            bmi = weight / (height ** 2)
            result_lbl.configure(text=f"Result: {bmi:.2f}", text_color="white")

        self.main_panel.columnconfigure(list(range(2)), weight=10)
        self.main_panel.rowconfigure(4, weight=1)

        # right side
        about_label = ctk.CTkLabel(self.main_panel, text="About", font=(self.font_type, self.header_size))
        about_label.grid(row=0, column=1, sticky=ctk.S, pady=(20, 25))
        abt = """BMI (Body Mass Index) is a simple measure used to determine if a person’s\nweight is appropriate for their height. Monitoring BMI helps track overall\nfitness and maintain healthy habits."""
        about = ctk.CTkLabel(self.main_panel, text=abt, font=(self.font_type, self.font_size))
        about.grid(row=1, column=1, sticky=ctk.N, padx=15)

        index_label = ctk.CTkLabel(self.main_panel, text="Index", font=(self.font_type, self.header_size))
        index_label.grid(row=2, column=1, sticky=ctk.N, pady=15)

        index_frame = ctk.CTkFrame(self.main_panel, border_width=0, border_color="purple")
        index_frame.grid(row=4, column=1, sticky=ctk.NSEW, padx=15, pady=(0, 20))

        index_frame.columnconfigure(list(range(2)), weight=1)
        index_frame.rowconfigure(list(range(1, 7)), weight=1)

        bmi_score = ctk.CTkLabel(index_frame, text="BMI score", font=(self.font_type, self.header_size))
        bmi_score.grid(row=0, column=0, padx=15, pady=15)

        weight_status = ctk.CTkLabel(index_frame, text="Weight status", font=(self.font_type, self.header_size))
        weight_status.grid(row=0, column=1, padx=15, pady=15)

        # scores
        score1 = ctk.CTkLabel(index_frame, text="Below 18.5", font=(self.font_type, self.font_size))
        score1.grid(row=1, column=0, pady=20)
        score2 = ctk.CTkLabel(index_frame, text="18.5 - 24.9", font=(self.font_type, self.font_size))
        score2.grid(row=2, column=0, pady=20)
        score3 = ctk.CTkLabel(index_frame, text="25.0 - 29.9", font=(self.font_type, self.font_size))
        score3.grid(row=3, column=0, pady=20)
        score4 = ctk.CTkLabel(index_frame, text="30 - 34.9", font=(self.font_type, self.font_size))
        score4.grid(row=4, column=0, pady=20)
        score5 = ctk.CTkLabel(index_frame, text="35.0 - 39.9", font=(self.font_type, self.font_size))
        score5.grid(row=5, column=0, pady=20)
        score6 = ctk.CTkLabel(index_frame, text="Above 40", font=(self.font_type, self.font_size))
        score6.grid(row=6, column=0, pady=20)

        # score labels
        under = ctk.CTkLabel(index_frame, text="Underweight", font=(self.font_type, self.font_size))
        under.grid(row=1, column=1, pady=20)
        healthy = ctk.CTkLabel(index_frame, text="Healthy weight", font=(self.font_type, self.font_size))
        healthy.grid(row=2, column=1, pady=20)
        over = ctk.CTkLabel(index_frame, text="Overweight", font=(self.font_type, self.font_size))
        over.grid(row=3, column=1, pady=20)
        ob1 = ctk.CTkLabel(index_frame, text="Obesity class 1", font=(self.font_type, self.font_size))
        ob1.grid(row=4, column=1, pady=20)
        ob2 = ctk.CTkLabel(index_frame, text="Obesity class 2", font=(self.font_type, self.font_size))
        ob2.grid(row=5, column=1, pady=20)
        ob3 = ctk.CTkLabel(index_frame, text="Obesity class 3", font=(self.font_type, self.font_size))
        ob3.grid(row=6, column=1, pady=20)

        # left side
        main_label = ctk.CTkLabel(self.main_panel, text="BMI Calculator", font=(self.font_type, self.header_size))
        main_label.grid(row=0, column=0, pady=(20, 25), sticky=ctk.S, padx=15)

        calc_frame = ctk.CTkFrame(self.main_panel, border_width=0, border_color="white")
        calc_frame.grid(row=1, column=0, sticky=ctk.NSEW, padx=15, rowspan=4, pady=(0, 20))
        calc_frame.columnconfigure(list(range(2)), weight=1)

        weight = ctk.CTkLabel(calc_frame, text="weight", font=(self.font_type, self.font_size, "bold"))
        weight.grid(row=0, column=0, padx=15, pady=(15, 10), sticky=ctk.W)
        weight_entry = ctk.CTkEntry(calc_frame, width=150, height=40, placeholder_text="kg", font=(self.font_type, self.font_size))
        weight_entry.grid(row=0, column=1, padx=10, pady=(15, 10), sticky=ctk.W)
        height = ctk.CTkLabel(calc_frame, text="height", font=(self.font_type, self.font_size, "bold"))
        height.grid(row=1, column=0, padx=15, pady=10, sticky=ctk.W)
        height_entry = ctk.CTkEntry(calc_frame, width=150, height=40, placeholder_text="cm", font=(self.font_type, self.font_size))
        height_entry.grid(row=1, column=1, padx=10, pady=10, sticky=ctk.W)

        calculate_btn = ctk.CTkButton(calc_frame,
                                      width=150,
                                      height=40,
                                      font=(self.font_type, self.font_size),
                                      text="Calculate",
                                      command=lambda: calculate_bmi(weight_entry.get(), height_entry.get()))
        calculate_btn.grid(row=2, column=1, padx=10, pady=10, sticky=ctk.W)
        result_lbl = ctk.CTkLabel(calc_frame, text="Result:", font=(self.font_type, self.font_size))
        result_lbl.grid(row=3, column=0, padx=15, pady=50, sticky=ctk.W, columnspan=2)

    def measurements(self) -> None:
        self.clear_main_panel()
        self.under_construction()
        raise NotImplementedError("Measurements page")
    
    def notes(self) -> None:
        self.clear_main_panel()
        self.reset_config()
        top_panel = ctk.CTkFrame(self.main_panel, corner_radius=0, border_color="orange", border_width=0)
        top_panel.pack(expand=False, fill=ctk.X, anchor=ctk.NW, padx=5, pady=5)
        notes_label = ctk.CTkLabel(top_panel, text="Notes", font=(self.font_type, self.header_size))
        notes_label.pack(anchor=ctk.NW, padx=(10, 0), pady=(25, 10), side=ctk.LEFT)
        add_btn = ctk.CTkButton(top_panel,
                                text="+ Add Note",
                                width=45,
                                height=45,
                                font=(self.font_type, self.font_size, "bold"),
                                border_spacing=5,
                                fg_color="green",
                                command=self.add_note)
        add_btn.pack(anchor=ctk.NE, padx=(0, 10), pady=(20, 15), side=ctk.RIGHT)
        notes_frame = ctk.CTkScrollableFrame(self.main_panel, corner_radius=0, border_color="yellow", border_width=0)
        notes_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=5, pady=(0, 5), side=ctk.TOP)

        notes_list = os.listdir(r".\notes")
        no_notes = len(notes_list) == 0
        if no_notes:
            notes_label.configure(text="No notes added yet. Why not start by adding one?", text_color="red")
            return
        
        col = 0
        row = 0
        for note in notes_list:
            note_name = note.split(".")[0]
            note_btn = ctk.CTkButton(notes_frame,
                                        text=note_name,
                                        width=250,
                                        font=(self.font_type, self.font_size),
                                        anchor=ctk.N,
                                        border_spacing=12,
                                        command=lambda n=note_name: self.show_note(n))
            note_btn.grid(column=col%5, row=row, sticky=ctk.NSEW, padx=19, pady=10)
            col += 1
            if col % 5 == 0:
                row += 1
        
        if col == 0:
            col = 1
        if row == 0:
            row = 1
        notes_frame.columnconfigure(list(range(col)), weight=1)
        notes_frame.rowconfigure(list(range(row)), weight=1)

    def add_note(self) -> None:
        def submit_note(note_name: str) -> None:
            print("current directory: adding a new note")
            print(os.getcwd())
            illegal_chars: str = string.punctuation
            note_name = note_name.lower().rstrip()
            is_name_legal = not(any((char in illegal_chars for char in note_name)) or note_name == "")
            notes = os.listdir(r".\notes")
            name_exists = f"{note_name}.txt" in notes
            
            if name_exists:
                name_label.configure(text=f"An entry for {note_name} already exists.", text_color="red")
                return
            if not is_name_legal:
                name_label.configure(text=f"Name contains illegal characters", text_color="red")
                return
            
            with open(fr".\notes\{note_name}.txt", "x") as new_note_file:
                print(os.listdir(fr".\notes"))
                print(f"{new_note_file.name} created")
            new_note.destroy()
            self.notes()
        print(os.getcwd())
        x = (self.screen_width - 640) // 2
        y = (self.screen_height -360) // 2

        new_note = ctk.CTkToplevel(self)
        new_note.title("Add note")
        new_note.geometry(f"500x250+{x}+{y}")
        new_note.resizable(False, False)

        # use after due to customtkinter's implementation where some data is set after 200ms
        new_note.after(300, new_note.focus)
        new_note.after(200, lambda: new_note.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        name_label = ctk.CTkLabel(new_note, text="Enter your note name", font=(self.font_type, self.header_size))
        name_label.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 20))
        name_entry = ctk.CTkEntry(new_note, placeholder_text="Type here...", font=(self.font_type, self.font_size), width=350, height=40)
        name_entry.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(0, 20))

        submit_btn = ctk.CTkButton(new_note,
                                   text="Submit",
                                   width=100,
                                   height=50,
                                   font=(self.font_type, self.font_size),
                                   command=lambda: submit_note(name_entry.get()))
        submit_btn.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(20, 15))

    def show_note(self, note_name: str) -> None:
        self.clear_main_panel()
        def save_note():
            content = note_box.get("0.0", ctk.END)
            with open(fr".\notes\{note_name}.txt", "w") as note_file:
                note_file.write(content)
            self.clear_main_panel()
            self.show_note(note_name)

        self.main_panel.rowconfigure(1, weight=1)
        self.main_panel.columnconfigure(0, weight=1)
        label = ctk.CTkLabel(self.main_panel, text=note_name, font=(self.font_type, self.header_size))
        label.grid(row=0, column=0, pady=15, padx=15, sticky=ctk.W)
        note_box = ctk.CTkTextbox(self.main_panel, wrap="word", font=(self.font_type, self.font_size))
        note_box.grid(row=1, column=0, pady=15, padx=15, sticky=ctk.NSEW, columnspan=2)
        with open(fr".\notes\{note_name}.txt", "r") as note_file:
            note_box.insert("0.0", note_file.read())
        delete_note = ctk.CTkButton(self.main_panel, text="Delete note", fg_color="red", font=(self.font_type, self.header_size), command=lambda: self.delete_note(note_name))
        delete_note.grid(row=2, column=0, pady=15, padx=15, sticky=ctk.W)
        save_note = ctk.CTkButton(self.main_panel, text="Save", font=(self.font_type, self.header_size), command=save_note)
        save_note.grid(row=2, column=1, pady=15, padx=15, sticky=ctk.E)

    def delete_note(self, note_name: str):
        def submit(choice: int):
            print(choice)
            if choice:
                del_note_label.configure(text=choice, text_color="green")
                os.remove(fr".\notes\{note_name}.txt")
                del_note.destroy()
                self.notes()
                return
            del_note_label.configure(text=choice, text_color="red")
            del_note.destroy()
        del_note = ctk.CTkToplevel(self)
        x = (self.screen_width - 640) // 2
        y = (self.screen_height -360) // 2
        del_note.title(f"Delete {note_name}")
        del_note.geometry(f"450x300+{x}+{y}")
        del_note.resizable(False, False)
        # use after due to customtkinter's implementation where some data is set after 200ms
        del_note.after(300, del_note.focus)
        del_note.after(200, lambda: del_note.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        del_note_label = ctk.CTkLabel(del_note, text="Are you sure?", font=(self.font_type, self.header_size))
        del_note_label.pack(side=ctk.TOP, pady=(10, 0))
        info_label = ctk.CTkLabel(del_note, text="This action is irreversible", font=(self.font_type, self.font_size), text_color="red")
        info_label.pack(side=ctk.TOP, pady=(10, 0))

        radio_var = ctk.IntVar(value=0)
        yes_btn = ctk.CTkRadioButton(del_note, text="Yes", font=(self.font_type, self.font_size), variable=radio_var, value=1)
        yes_btn.pack(side=ctk.TOP, pady=(25, 0))
        no_btn = ctk.CTkRadioButton(del_note, text="No", font=(self.font_type, self.font_size), variable=radio_var, value=0)
        no_btn.pack(side=ctk.TOP, pady=(15, 0))

        submit_btn = ctk.CTkButton(del_note, text="Submit", font=(self.font_type, self.header_size), command=lambda: submit(radio_var.get()))
        submit_btn.pack(side=ctk.TOP, pady=(45, 10))
        
    # def placeholder(self) -> None:
        self.clear_main_panel()
        self.clear_main_panel()

    def settings(self) -> None:
        def save_settings():
            return

        x = (self.screen_width - 920) // 2
        y = (self.screen_height - 600) // 2

        settings_window = ctk.CTkToplevel(self)
        settings_window.title("Settings")
        settings_window.geometry(f"900x540+{x}+{y}")
        settings_window.resizable(False, False)

        # use after due to customtkinter's implementation where some data is set after 200ms
        settings_window.after(300, settings_window.focus)
        settings_window.after(200, lambda: settings_window.iconbitmap(r".\assets\FitArchiveLogo1.ico"))

        settings_window.columnconfigure(0, weight=1)
        settings_window.rowconfigure(0, weight=1)
        settings_frame = ctk.CTkScrollableFrame(settings_window, corner_radius=0)
        settings_frame.grid(column=0, row=0, sticky=ctk.NSEW)

        appearance_label = ctk.CTkLabel(settings_frame, text="Appearance", font=(self.font_type, self.header_size))
        appearance_label.grid(column=1, row=0, pady=35, sticky=ctk.N, padx=80)


        # main screen appearance
        main_panel_label = ctk.CTkLabel(settings_frame, text="Main Screen", font=(self.font_type, self.font_size, "bold"))
        main_panel_label.grid(column=1, row=2, pady=15, sticky=ctk.N, padx=80)
        # font size
        main_font_size_label = ctk.CTkLabel(settings_frame, text="Font size", font=(self.font_type, self.font_size))
        main_font_size_label.grid(column=0, row=3, pady=25, padx=40)
        main_font_sizes = [str(x) for x in range(12, 36, 2)]
        main_font_sizes.insert(0, str(self.font_size))
        main_font_size_entry = ctk.CTkOptionMenu(settings_frame, font=(self.font_type, self.font_size), values=main_font_sizes, width=85, height=35)
        main_font_size_entry.grid(column=1, row=3, pady=25, padx=40)
        # header size
        main_header_size_label = ctk.CTkLabel(settings_frame, text="Header size", font=(self.font_type, self.font_size))
        main_header_size_label.grid(column=0, row=4, pady=25, padx=40)
        header_sizes = [str(x) for x in range(12, 36, 2)]
        header_sizes.insert(0, str(self.header_size))
        main_header_size_entry = ctk.CTkOptionMenu(settings_frame, font=(self.font_type, self.font_size), values=header_sizes, width=85, height=35)
        main_header_size_entry.grid(column=1, row=4, pady=25, padx=40)
        # font types
        fonts = list(font.families())
        fonts.insert(0, self.font_type)
        fonts.append("Sans Serif")
        main_font_label = ctk.CTkLabel(settings_frame, text="Font", font=(self.font_type, self.font_size))
        main_font_label.grid(column=0, row=5, pady=25, padx=40)
        main_font_entry = ctk.CTkOptionMenu(settings_frame, font=(self.font_type, self.font_size), values=fonts, width=110, height=35)
        main_font_entry.grid(column=1, row=5, pady=25, padx=40)
        

        # side panel appearance
        side_panel_label = ctk.CTkLabel(settings_frame, text="Side Panel", font=(self.font_type, self.font_size, "bold"))
        side_panel_label.grid(column=1, row=6, pady=15, sticky=ctk.N, padx=80)
        side_font_size_label = ctk.CTkLabel(settings_frame, text="Font size", font=(self.font_type, self.font_size))
        # font sizes
        side_font_size_label.grid(column=0, row=7, pady=25, padx=40)
        side_font_sizes = [str(x) for x in range(12, 36, 2)]
        side_font_sizes.insert(0, str(self.side_panel.font_size))
        side_size_entry = ctk.CTkOptionMenu(settings_frame, font=(self.font_type, self.font_size), values=side_font_sizes, width=85, height=35)
        side_size_entry.grid(column=1, row=7, pady=25, padx=40)
        # font types
        side_font_label = ctk.CTkLabel(settings_frame, text="Font", font=(self.font_type, self.font_size))
        side_font_label.grid(column=0, row=8, pady=25, padx=40)
        side_font_entry = ctk.CTkOptionMenu(settings_frame, font=(self.font_type, self.font_size), values=fonts, width=110, height=35)
        side_font_entry.grid(column=1, row=8, pady=25, padx=40)


        # display themes
        display_label = ctk.CTkLabel(settings_frame, text="Display", font=(self.font_type, self.font_size, "bold"))
        display_label.grid(column=1, row=9, pady=15, sticky=ctk.N, padx=80)
        # appearance themes
        theme_font_label = ctk.CTkLabel(settings_frame, text="Appearance Theme", font=(self.font_type, self.font_size))
        theme_font_label.grid(column=0, row=10, pady=25, padx=40)
        appearance_themes = ["system", "dark", "light"]
        appearance_themes.insert(0, THEME)
        theme_entry = ctk.CTkOptionMenu(settings_frame, font=(self.font_type, self.font_size), values=appearance_themes, height=35)
        theme_entry.grid(column=1, row=10, pady=25, padx=40)
        # colour themes
        colour_theme_font_label = ctk.CTkLabel(settings_frame, text="Colour Theme", font=(self.font_type, self.font_size))
        colour_theme_font_label.grid(column=0, row=11, pady=25, padx=40)
        themes = [theme.replace(".json", "") for theme in os.listdir(r".\themes")]
        themes.append("blue")
        themes.append("green")
        themes.insert(0, COLOUR_SCHEME)
        colour_theme = ctk.CTkOptionMenu(settings_frame, values=themes, font=(self.font_type, self.font_size), height=35)
        colour_theme.grid(column=1, row=11, padx=40)

        # saving settings
        info_label = ctk.CTkLabel(settings_frame, text="Changes will be applied after restarting FitArchive", font=(self.font_type, self.font_size), text_color="red")
        info_label.grid(column=1, row=12, padx=40, pady=(40, 0))
        save_button = ctk.CTkButton(settings_frame, text="Save", font=(self.font_type, self.font_size), height=45)
        save_button.grid(column=1, row=13, padx=40, pady=40)

    def under_construction(self) -> None:
        lbl = ctk.CTkLabel(self.main_panel, text="Under Construction...", font=(self.font_type, self.header_size, "bold"))
        self.main_panel.columnconfigure(0, weight=1)
        lbl.grid(pady=20, sticky=ctk.N)
