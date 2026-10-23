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

        self.slider_cable = ctk.CTkSlider(self, from_=0, to=3000, number_of_steps=3000)
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_cable)
        self.slider_cable.grid(row=0, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.text_cable = ctk.CTkLabel(self, text="0" + " m")
        self.text_cable.grid(row=0, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        
        #NOMBRE DE CHAISE
        ctk.CTkLabel(self, text="Nombre de chaises").grid(row=1, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_cable = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_chaise)
        self.slider_cable.grid(row=1, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_chaise = ctk.CTkLabel(self, text="0")
        self.text_chaise.grid(row=1, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        #VITESSE
        ctk.CTkLabel(self, text="Vitesse").grid(row=2, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        #TODO ICI C'EST EN FLOAT
        self.slider_cable = ctk.CTkSlider(self, from_=0, to=8, number_of_steps=(8*10))
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_vitesse)
        self.slider_cable.grid(row=2, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_cable = ctk.CTkLabel(self, text="0" + " m/s")
        self.text_cable.grid(row=2, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        #TEMPS EMBARQUEMENT
        ctk.CTkLabel(self, text="Temps d'embarquement").grid(row=3, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_cable = ctk.CTkSlider(self, from_=0, to=30, number_of_steps=30)
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_cable)
        self.slider_cable.grid(row=3, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_cable = ctk.CTkLabel(self, text="0" + " s")
        self.text_cable.grid(row=3, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        #TEMPS DEBARQUEMENT
        ctk.CTkLabel(self, text="Temps de débarquement").grid(row=4, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_cable = ctk.CTkSlider(self, from_=0, to=30, number_of_steps=30)
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_cable)
        self.slider_cable.grid(row=4, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_cable = ctk.CTkLabel(self, text="0" + " s")
        self.text_cable.grid(row=4, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        #CAPACITE CHAISES
        ctk.CTkLabel(self, text="Capacité des chaises").grid(row=5, column=0, sticky="w",  padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_cable = ctk.CTkSlider(self, from_=0, to=8, number_of_steps=8)
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_cable)
        self.slider_cable.grid(row=5, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_cable = ctk.CTkLabel(self, text="0")
        self.text_cable.grid(row=5, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

    def _quand_slider_cable(self, valeur) :
        self.taille_cable = int(valeur)
        self.text_cable.configure(text=str(self.taille_cable) + " m")
        #TODO avertir mainapp et recalculer????
    
    def _quand_slider_chaise(self, valeur) :
            self.nb_chaise = int(valeur)
            self.text_chaise.configure(text=str(self.nb_chaise))


#TODO COMMENTE TON CODE!
#TODO les set des sliders doivent se fier au csv ou bien 0 si pas d'importé (voir lignes 23 et 19 où c'est = à 0)

