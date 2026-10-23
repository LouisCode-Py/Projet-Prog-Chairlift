import customtkinter as ctk

PADDING_EN_Y = 30
PADDING_EN_X = 10

class Sliders(ctk.CTkFrame) :

    def __init__(self, parent) :
        super().__init__(parent)
        
        self.creer_widgets()

    def creer_widgets(self) :

        #LONGUEUR DU CABLE
        ctk.CTkLabel(self, text="Longueur du câble").grid(row=0, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)



        #NOMBRE DE CHAISE
        ctk.CTkLabel(self, text="Nombre de chaises").grid(row=1, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)


        #VITESSE
        ctk.CTkLabel(self, text="Vitesse").grid(row=2, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)


        #TEMPS EMBARQUEMENT
        ctk.CTkLabel(self, text="Temps d'embarquement").grid(row=3, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)


        #TEMPS DEBARQUEMENT
        ctk.CTkLabel(self, text="Temps de débarquement").grid(row=4, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)


        #CAPACITE CHAISES
        ctk.CTkLabel(self, text="Capacité des chaises").grid(row=5, column=0, sticky="w",  padx=PADDING_EN_X, pady=PADDING_EN_Y)




#TODO COMMENTE TON CODE!

