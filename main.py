from Sliders import Sliders

import customtkinter as ctk

class MainApp(ctk.CTk) :

    def __init__(self) :
        super().__init__()
        self.title("Gestionnaire de remonte-pente mécanique")
        self.geometry("1200x600")

        self.grid_rowconfigure(0, weight=1)
        self.sliders = Sliders(self)
        self.sliders.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)


if __name__ == "__main__" :
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")
    application = MainApp()
    application.mainloop()