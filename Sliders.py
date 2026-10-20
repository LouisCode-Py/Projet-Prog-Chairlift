import customtkinter as ctk

class Sliders(ctk.CTkFrame) :

    def __init__(self, parent) :
        super().__init__(parent)
        self.grid_columnconfigure(1, weight=1)
        self.creer_widgets()

    def creer_widgets(self) :

        #LONGUEUR DU CABLE
        ctk.CTkLabel(self, text="Longueur du câble").grid(row=0, column=0, sticky="w", padx=12, pady=10)



        #NOMBRE DE CHAISE
        ctk.CTkLabel(self, text="Nombre de chaises").grid(row=1, column=0, sticky="w", padx=12, pady=10)


        #VITESSE
        ctk.CTkLabel(self, text="Vitesse").grid(row=2, column=0, sticky="w", padx=12, pady=10)


        #TEMPS EMBARQUEMENT
        ctk.CTkLabel(self, text="Temps d'embarquement").grid(row=3, column=0, sticky="w", padx=12, pady=10)


        #TEMPS DEBARQUEMENT
        ctk.CTkLabel(self, text="Temps de débarquement").grid(row=4, column=0, sticky="w", padx=12, pady=10)


        #CAPACITE CHAISES
        ctk.CTkLabel(self, text="Capacité des chaises").grid(row=5, column=0, sticky="w",  padx=12, pady=10)




#TODO COMMENTE TON CODE!

