import customtkinter as ctk
from PIL import Image
import configparser
from csv_handler import Handler
import pandas as pd
from datetime import datetime

CONFIG = configparser.ConfigParser()
CONFIG.read(r".\config.ini")

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

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
        self.state = ""
        self.font = CONFIG["UI"]["SidePanelFont"]
        self.font_size = int(CONFIG["UI"]["SidePanelFontSize"])
        self.text_color = CONFIG["UI"]["SidePanelTextColor"]
        self.buttons = []
        self.btn_height = int(CONFIG["UI"]["SidePanelBtnHeight"])
        
        self.initialise_buttons()
    
    def initialise_buttons(self) -> None:
        self.state = "expanded"

        self.fitarchive_img = ctk.CTkImage(Image.open(self.fitarchive_path), size=(25, 25))
        self.fitarchive_btn = ctk.CTkButton(self,
                                       corner_radius=0,
                                       text="Side Panel",
                                       image=self.fitarchive_img,
                                       compound=ctk.RIGHT,
                                       text_color=self.text_color,
                                       font=(self.font, self.font_size),
                                       height=self.btn_height,
                                       anchor=ctk.W, 
                                       command=self.collapse, 
                                       textvariable=ctk.StringVar(value="FitArchive"))
        self.fitarchive_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.fitarchive_btn)

        self.title_btn = ctk.CTkButton(self,
                                       corner_radius=0,
                                       text="Side Panel",
                                       image=self.collapse_img,
                                       compound=ctk.RIGHT,
                                       text_color=self.text_color,
                                       font=(self.font, self.font_size),
                                       height=self.btn_height,
                                       anchor=ctk.W, 
                                       command=self.collapse, 
                                       textvariable=ctk.StringVar(value="Side Panel"))
        self.title_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.title_btn)

        self.exercises_img = ctk.CTkImage(Image.open(self.exercises_path), size=(25, 25))
        self.exercises_btn = ctk.CTkButton(self,
                                           corner_radius=0,
                                           text="Exercises",
                                           image=self.exercises_img,
                                           compound=ctk.RIGHT,
                                           text_color=self.text_color,
                                           font=(self.font, self.font_size),
                                           height=self.btn_height,
                                           anchor=ctk.W,
                                           textvariable=ctk.StringVar(value="Exercises"))
        self.exercises_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.exercises_btn)

        self.bmi_calculator_img = ctk.CTkImage(Image.open(self.bmi_calculator_path), size=(25, 25))
        self.bmi_calculator_btn = ctk.CTkButton(self,
                                                corner_radius=0,
                                                text="BMI calculator",
                                                image=self.bmi_calculator_img,
                                                compound=ctk.RIGHT,
                                                text_color=self.text_color,
                                                font=(self.font, self.font_size),
                                                height=self.btn_height,
                                                anchor=ctk.W,
                                                textvariable=ctk.StringVar(value="BMI Calculator"))
        self.bmi_calculator_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.bmi_calculator_btn)

        self.measurements_img = ctk.CTkImage(Image.open(self.measurements_path), size=(25, 25))
        self.measurements_btn = ctk.CTkButton(self,
                                              corner_radius=0,
                                              text="Measurements",
                                              image=self.measurements_img,
                                              compound=ctk.RIGHT,
                                              text_color=self.text_color,
                                              font=(self.font, self.font_size),
                                              height=self.btn_height,
                                              anchor=ctk.W,
                                              textvariable=ctk.StringVar(value="Measurements"))
        self.measurements_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.measurements_btn)

        self.notes_img = ctk.CTkImage(Image.open(self.notes_path), size=(25, 25))
        self.notes_btn = ctk.CTkButton(self,
                                       corner_radius=0,
                                       text="Notes",
                                       image=self.notes_img,
                                       compound=ctk.RIGHT,
                                       text_color=self.text_color,
                                       font=(self.font, self.font_size),
                                       height=self.btn_height,
                                       anchor=ctk.W,
                                       textvariable=ctk.StringVar(value="Notes"))
        self.notes_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.notes_btn)

        self.placeholder_img = ctk.CTkImage(Image.open(self.collapse_path), size=(25, 25))
        self.placeholder_btn = ctk.CTkButton(self,
                                             corner_radius=0,
                                             text="Placeholder",
                                             image=self.collapse_img,
                                             compound=ctk.RIGHT,
                                             text_color=self.text_color,
                                             font=(self.font, self.font_size),
                                             height=self.btn_height,
                                             anchor=ctk.W,
                                             textvariable=ctk.StringVar(value="Placeholder"))
        self.placeholder_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.placeholder_btn)

        self.settings_img = ctk.CTkImage(Image.open(self.settings_path), size=(25, 25))
        self.settings_btn = ctk.CTkButton(self,
                                             corner_radius=0,
                                             text="Settings",
                                             image=self.settings_img,
                                             compound=ctk.RIGHT,
                                             text_color=self.text_color,
                                             font=(self.font, self.font_size),
                                             height=self.btn_height,
                                             anchor=ctk.W,
                                             textvariable=ctk.StringVar(value="Settings"))
        self.settings_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.settings_btn)

    def collapse(self) -> None:
        self.state = "collapsed"
        for btn in self.buttons:
            txt_var = btn.cget("textvariable").get()
            if txt_var == "Side Panel":
                btn.configure(image=self.expand_img, command=self.expand)
            btn.configure(text="", width=45)

    def expand(self) -> None:
        self.state = "expanded"
        for btn in self.buttons:
            txt_var = btn.cget("textvariable").get()
            if txt_var == "Side Panel":
                btn.configure(image=self.collapse_img, command=self.collapse)
            btn.configure(text=btn.cget("textvariable"))

class App(ctk.CTk):
    def __init__(self, csv_path) -> None:
        super().__init__()

        # config info
        self.font_type = CONFIG["UI"]["MainPanelFont"]
        self.header_size = int(CONFIG["UI"]["MainPanelHeaderSize"])
        self.font_size = int(CONFIG["UI"]["MainPanelFontSize"])

        # button functions
        self.btn_functions = {
            "FitArchive": self.show_landing_page,
            "Exercises": self.exercises,
            "BMI Calculator": self.bmi_calculator,
            "Measurements": self.measurements,
            "Notes": self.notes,
            "Placeholder": self.placeholder,
            "Settings": self.settings,
        }

        # information about user's display
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # window setup
        self.minsize(width=960, height=540)
        self.maxsize(width=self.screen_width, height=self.screen_height)
        self.geometry(f"{self.screen_width}x{self.screen_height}")
        self.title("FitArchive")
        self.iconbitmap(r".\assets\FitArchiveLogo1.ico")
        self.after(0, lambda: self.wm_state('zoomed'))

        # side panel
        self.side_panel = SidePanel(self, corner_radius=0, border_color="blue", border_width=1)
        self.side_panel.pack(expand=False, side=ctk.LEFT, fill=ctk.BOTH, anchor=ctk.NW, padx=1)
        for btn in self.side_panel.buttons:
            btn_val = btn.cget("textvariable").get()
            if btn_val != "Side Panel":
                btn.configure(command=self.btn_functions.get(btn_val))

        # main panel
        self.main_panel = ctk.CTkFrame(self, corner_radius=0, border_color="red", border_width=1)
        self.main_panel.pack(expand=True, fill=ctk.BOTH, side=ctk.RIGHT)
        self.show_landing_page()

        # file operations
        self.csv_path = csv_path
        self.handler = Handler(self.csv_path)

        # self.handler.add_exercise("hammer curls", "bicep")
        # print(self.handler.get_dataset())
        # for x in range(1, 80):
        #     self.handler.add_exercise_data("hammer curls", score=x, date=f"{x%30}.{x%12}.2024", units="kg")
        

    def show_landing_page(self) -> None:
        # welcome section
        self.clear_main_panel()
        self.header = ctk.CTkLabel(self.main_panel, text="Welcome to FitArchive!", font=(self.font_type, self.header_size, "bold"), anchor=ctk.NW)
        self.header.pack(pady=40)
        self.motto = ctk.CTkLabel(self.main_panel, text="Track your workouts, achieve your goals.", font=(self.font_type, self.font_size), anchor=ctk.NW)
        self.motto.pack(pady=10)

        # features
        self.features_frame = ctk.CTkFrame(self.main_panel, border_color="green", border_width=1)
        self.features_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=20, pady=20)
        self.features_label = ctk.CTkLabel(self.features_frame, text="Features:", font=(self.font_type, self.header_size, "underline"))
        self.features_label.pack(padx=10, pady=10, side=ctk.TOP, anchor=ctk.NW)
        
        # buttons
        self.buttons_frame = ctk.CTkFrame(self.features_frame, border_color="cyan", border_width=1)
        self.buttons_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=10, pady=10)
        self.exercises_btn = ctk.CTkButton(self.buttons_frame,
                                           text="Exercises",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.exercises)
        self.exercises_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10, fill=ctk.BOTH)

        self.bmi_calculator_btn = ctk.CTkButton(self.buttons_frame,
                                           text="BMI calculator",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.bmi_calculator)
        self.bmi_calculator_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10, fill=ctk.BOTH)

        self.measurements_btn = ctk.CTkButton(self.buttons_frame,
                                           text="Measurements",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.measurements)
        self.measurements_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10, fill=ctk.BOTH)

        self.notes_btn = ctk.CTkButton(self.buttons_frame,
                                           text="Notes",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.notes)
        self.notes_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10, fill=ctk.BOTH)

        self.settings_btn = ctk.CTkButton(self.buttons_frame,
                                           text="Settings",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.settings)
        self.settings_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10, fill=ctk.BOTH)

        # experimental
        self.close_btn = ctk.CTkButton(self.main_panel, text="Clear this panel", font=(self.font_type, self.font_size), command=self.clear_main_panel, text_color="#000000", corner_radius=10)
        self.close_btn.pack(anchor=ctk.N, pady=20)
    
    def clear_main_panel(self) -> None:
        print("Clearing main panel...")
        for widget in self.main_panel.winfo_children():
            widget.destroy()
    
    def exercises(self) -> None:
        self.clear_main_panel()
        top_panel = ctk.CTkFrame(self.main_panel,
                                 corner_radius=0,
                                 border_color="orange",
                                 border_width=1)
        top_panel.pack(expand=False, fill=ctk.X, anchor=ctk.NW, padx=5, pady=5)
        exercises_label = ctk.CTkLabel(top_panel,
                                       text="Exercises",
                                       font=(self.font_type, self.header_size))
        exercises_label.pack(anchor=ctk.NW, padx=(10, 0), pady=(25, 10), side=ctk.LEFT)
        if self.handler.is_csv_empty():
            exercises_label.configure(text="No exercises have been added yet. Why not add one to get started?", text_color="red")
        add_btn = ctk.CTkButton(top_panel,
                                text="+ Add Exercise",
                                width=45,
                                height=45,
                                font=(self.font_type, self.font_size, "bold"),
                                border_spacing=5,
                                fg_color="green",
                                command=self.add_exercise_window)
        add_btn.pack(anchor=ctk.NE, padx=(0, 10), pady=(20, 15), side=ctk.RIGHT)
        exercises_frame = ctk.CTkScrollableFrame(self.main_panel,
                                       corner_radius=0,
                                       border_color="yellow",
                                       border_width=1)
        exercises_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=5, pady=(0, 5), side=ctk.TOP)
        exercises_list = self.handler.exercises

        col = 0
        row = 0
        for exercise in exercises_list:
            exercise_btn = ctk.CTkButton(exercises_frame,
                                        text=exercise,
                                        width=300,
                                        height=200,
                                        font=(self.font_type, self.font_size),
                                        anchor=ctk.N,
                                        border_spacing=12,
                                        command=lambda ex=exercise: self.show_exercise(ex))
            exercise_btn.grid(column=col%5, row=row, sticky=ctk.NW, padx=19, pady=10)
            col += 1
            if col % 5 == 0:
                row += 1

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

    def show_exercise(self, exercise_name: str):
        self.clear_main_panel()
        def list_scores(exercise_name: str):
            data = self.handler.get_dataset()[exercise_name].dropna().tolist()
            col = 0
            row = 0
            category = data[1].split(":")[1]
            pb = data[0].split(":")[1].replace("|", "")
            label.configure(text=f"{exercise_name} ({category})")
            pb_label.configure(text=f"PB: {pb}")
            for index, score in enumerate(data[3:]):
                score_label = ctk.CTkLabel(scorebox, text=f"{index + 1}. {score}", font=(self.font_type, self.font_size))
                score_label.grid(column=col%4, row=row, padx=(50, 0), pady=15, sticky=ctk.NW)
                col += 1
                if col%4 == 0:
                    row += 1
                               
        exercise_name = exercise_name.capitalize()
        # left side
        label = ctk.CTkLabel(self.main_panel,
                             text=exercise_name,
                             font=(self.font_type, self.header_size))
        label.grid(column=0, row=0, padx=15, pady=15, sticky=ctk.NW)
        notes_label = ctk.CTkLabel(self.main_panel,
                                   text="Notes",
                                   font=(self.font_type, self.header_size))
        notes_label.grid(column=0, row=1, padx=15, pady=15, sticky=ctk.NW)
        notes_box = ctk.CTkTextbox(self.main_panel,
                                   font=(self.font_type, self.font_size))
                                #    width=400,
                                #    height=700)
        notes_box.grid(column=0, row=2, padx=15, sticky=ctk.NSEW, rowspan=2)
        self.main_panel.grid_rowconfigure(2, weight=1)
        save_notes_btn = ctk.CTkButton(self.main_panel,
                                       text="Save",
                                       font=(self.font_type, self.header_size))
        save_notes_btn.grid(column=0, row=4, sticky=ctk.NW, padx=15, pady=15)
        remove_exercise_btn = ctk.CTkButton(self.main_panel,
                                            text="Delete exercise",
                                            font=(self.font_type, self.header_size),
                                            fg_color="red")
        remove_exercise_btn.grid(column=0, row=6, padx=15, pady=15, sticky=ctk.SW)

        # right side
        sort_label = ctk.CTkLabel(self.main_panel,
                                  text="Sort records by date:",
                                  font=(self.font_type, self.header_size))
        sort_label.grid(column=1, row=0, padx=30, pady=15, sticky=ctk.NW)
        sort = ctk.CTkComboBox(self.main_panel,
                               values=["Ascending", "Descending"],
                               font=(self.font_type, self.font_size),
                               width=180,
                               height=35)
        sort.grid(column=1, row=1, padx=30, sticky=ctk.NW)
        pb_label = ctk.CTkLabel(self.main_panel, text="PB: ", font=(self.font_type, self.header_size))
        pb_label.grid(column=4, row=0, padx=30, pady=15, sticky=ctk.NW)

        scorebox = ctk.CTkScrollableFrame(self.main_panel,
                                border_color="orange",
                                border_width=1)
        scorebox.grid(column=1, row=2, padx=30, columnspan=5, sticky=ctk.NSEW, rowspan=3)
        self.main_panel.grid_columnconfigure(1, weight=1)
        self.main_panel.rowconfigure(4, weight=1)

        visualise_btn = ctk.CTkButton(self.main_panel,
                                      text="Visualise",
                                      font=(self.font_type, self.header_size),
                                      command=...,
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
                                      command=...,
                                      fg_color="#FF9350")
        edit_score_btn.grid(column=3, row=5, padx=(0, 30), pady=15, sticky=ctk.NE)
        remove_score_btn = ctk.CTkButton(self.main_panel,
                                      text="Remove score",
                                      font=(self.font_type, self.header_size),
                                      command=lambda: self.delete_exercise_data(exercise_name),
                                      fg_color="#FF5050")
        remove_score_btn.grid(column=4, row=5, padx=(0, 30), pady=15, sticky=ctk.NE)

        list_scores(exercise_name=exercise_name)

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

    def add_exercise_data(self, exercise_name: str):
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
            unit = self.handler.get_dataset()[exercise_name].tolist()[0].split("|")[1]
            print(self.handler.add_exercise_data(exercise_name, score, date, unit))
            add_scr.destroy()
            self.show_exercise(exercise_name)

        add_scr = ctk.CTkToplevel(self)
        x = (self.screen_width - 640) // 2
        y = (self.screen_height -360) // 2
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
    
    def bmi_calculator(self):
        self.clear_main_panel()
        self.under_construction()
        raise NotImplementedError("BMI calculator page")
    
    def measurements(self):
        self.clear_main_panel()
        self.under_construction()
        raise NotImplementedError("Measurements page")
    
    def notes(self):
        self.clear_main_panel()
        self.under_construction()
        raise NotImplementedError("Notes page")
    
    def placeholder(self):
        self.clear_main_panel()
        self.clear_main_panel()

    def settings(self):
        self.clear_main_panel()
        self.under_construction()
        raise NotImplementedError("Settings page")

    def under_construction(self):
        lbl = ctk.CTkLabel(self.main_panel, text="Under Construction...", font=(self.font_type, self.header_size, "bold"))
        lbl.pack(anchor=ctk.CENTER, pady=50)