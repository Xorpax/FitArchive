import customtkinter as ctk
from PIL import Image
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read(r".\config.ini")

class SidePanel(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
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
    def __init__(self) -> None:
        super().__init__()

        # config info
        self.font_type = CONFIG["UI"]["MainPanelFont"]
        self.header_size = int(CONFIG["UI"]["MainPanelHeaderSize"])
        self.font_size = int(CONFIG["UI"]["MainPanelFontSize"])

        # button functions
        self.btn_functions = {
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

    def show_landing_page(self):
        # welcome section
        self.header = ctk.CTkLabel(self.main_panel,
                                         text="Welcome to FitArchive!",
                                         font=(self.font_type, self.header_size, "bold"),
                                         anchor=ctk.NW)
        self.header.pack(pady=40)
        self.motto = ctk.CTkLabel(self.main_panel,
                                  text="Track your workouts, achieve your goals.",
                                  font=(self.font_type, self.font_size),
                                  anchor=ctk.NW)
        self.motto.pack(pady=10)

        # features
        self.features_frame = ctk.CTkFrame(self.main_panel, border_color="green", border_width=1)
        self.features_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=20, pady=20)
        self.features_label = ctk.CTkLabel(self.features_frame,
                                           text="Features:",
                                           font=(self.font_type, self.header_size, "underline"))
        self.features_label.pack(padx=10, pady=10, side=ctk.TOP, anchor=ctk.NW)
        
        # buttons
        # self.buttons_frame = ctk.CTkFrame(self.features_frame, border_color="cyan", border_width=1)
        # self.buttons_frame.pack(expand=True, fill=ctk.BOTH, anchor=ctk.NW, padx=10, pady=10)
        self.exercises_btn = ctk.CTkButton(self.features_frame,
                                           text="Exercises",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.exercises)
        self.exercises_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10)

        self.bmi_calculator_btn = ctk.CTkButton(self.features_frame,
                                           text="BMI calculator",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.bmi_calculator)
        self.bmi_calculator_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10)

        self.measurements_btn = ctk.CTkButton(self.features_frame,
                                           text="Measurements",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.measurements)
        self.measurements_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10)

        self.notes_btn = ctk.CTkButton(self.features_frame,
                                           text="Notes",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.notes)
        self.notes_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10)

        self.settings_btn = ctk.CTkButton(self.features_frame,
                                           text="Settings",
                                           font=(self.font_type, self.font_size),
                                           height=500,
                                           width=300,
                                           anchor=ctk.N,
                                           border_spacing=20,
                                           command=self.settings)
        self.settings_btn.pack(side=ctk.LEFT, anchor=ctk.NW, padx=15, pady=10)

        # experimental
        self.close_btn = ctk.CTkButton(self.main_panel, text="Clear this panel", font=(self.font_type, self.font_size), command=self.clear_main_panel, text_color="#000000", corner_radius=10)
        self.close_btn.pack(anchor=ctk.N, pady=20)
    
    def clear_main_panel(self):
        print("Clearing main panel...")
        for widget in self.main_panel.winfo_children():
            widget.destroy()
    
    def exercises(self):
        raise NotImplementedError("Exercises page")
    
    def bmi_calculator(self):
        raise NotImplementedError("BMI calculator page")
    
    def measurements(self):
        raise NotImplementedError("Measurements page")
    
    def notes(self):
        raise NotImplementedError("Notes page")
    
    def placeholder(self):
        self.clear_main_panel()

    def settings(self):
        raise NotImplementedError("Settings page")
