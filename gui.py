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
        self.state = ""
        self.font = CONFIG["UI"]["SidePanelFont"]
        self.font_size = int(CONFIG["UI"]["SidePanelFontSize"])
        self.text_color = CONFIG["UI"]["SidePanelTextColor"]
        self.buttons = []
        self.btn_height = int(CONFIG["UI"]["SidePanelBtnHeight"])
        
        self.initialise_buttons()
    
    def initialise_buttons(self) -> None:
        self.state = "expanded"

        self.title_img = ctk.CTkImage(Image.open(self.collapse_path), size=(25, 25))
        self.title_btn = ctk.CTkButton(self,
                                       corner_radius=0,
                                       text="Side Panel",
                                       image=self.title_img,
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
        self.notes_btn = ctk.CTkButton(self, corner_radius=0,
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
                                             image=self.title_img,
                                             compound=ctk.RIGHT,
                                             text_color=self.text_color,
                                             font=(self.font, self.font_size),
                                             height=self.btn_height,
                                             anchor=ctk.W,
                                             textvariable=ctk.StringVar(value="Placeholder"))
        self.placeholder_btn.pack(anchor=ctk.N, fill=ctk.X)
        self.buttons.append(self.placeholder_btn)

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

class Content(ctk.CTkFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

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

        # main panel
        self.main_panel = Content(self, corner_radius=0, border_color="red", border_width=1)
        self.main_panel.pack(expand=True, fill=ctk.BOTH, side=ctk.RIGHT)
