import customtkinter as ctk
from tkinter import IntVar

PADDING_EN_Y = 30
PADDING_EN_X = 10

class Sliders(ctk.CTkFrame) :

    def __init__(self, parent) :
        super().__init__(parent)
        
        self.creer_widgets()

    def creer_widgets(self) :

        # initialiser la variable pour les radiobutton, empeche que plusieurs soient cochés
        self.radio_var = IntVar(value=0)

        """LONGUEUR DU CABLE"""
        ctk.CTkLabel(self, text="Longueur du câble").grid(row=0, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_cable = ctk.CTkSlider(self, from_=0, to=3000, number_of_steps=3000)
        self.slider_cable.set(0)
        self.slider_cable.configure(command=self._quand_slider_cable)
        self.slider_cable.grid(row=0, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.text_cable = ctk.CTkLabel(self, text="0" + " m")
        self.text_cable.grid(row=0, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.case_cable = ctk.CTkRadioButton(self, text="", command=self._actualiser_slider, variable=self.radio_var, value=1)
        self.case_cable.grid(row=0, column=3, sticky="e")
        
        
        """NOMBRE DE CHAISE"""
        ctk.CTkLabel(self, text="Nombre de chaises").grid(row=1, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_chaise = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider_chaise.set(0)
        self.slider_chaise.configure(command=self._quand_slider_chaise)
        self.slider_chaise.grid(row=1, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_chaise = ctk.CTkLabel(self, text="0")
        self.text_chaise.grid(row=1, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.case_chaise = ctk.CTkRadioButton(self, text="", command=self._actualiser_slider, variable=self.radio_var, value=2)
        self.case_chaise.grid(row=1, column=3, sticky="e")

        """VITESSE"""
        ctk.CTkLabel(self, text="Vitesse").grid(row=2, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        #TODO ICI C'EST EN FLOAT
        self.slider_vitesse = ctk.CTkSlider(self, from_=0.0, to=8, number_of_steps=(8*10))
        self.slider_vitesse.set(0.0)
        self.slider_vitesse.configure(command=self._quand_slider_vitesse)
        self.slider_vitesse.grid(row=2, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_vitesse = ctk.CTkLabel(self, text="0" + " m/s")
        self.text_vitesse.grid(row=2, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.case_cable = ctk.CTkRadioButton(self, text="", command=self._actualiser_slider, variable=self.radio_var, value=3)
        self.case_cable.grid(row=2, column=3, sticky="e")

        """TEMPS EMBARQUEMENT"""
        ctk.CTkLabel(self, text="Temps d'embarquement").grid(row=3, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_embarque = ctk.CTkSlider(self, from_=0, to=30, number_of_steps=30)
        self.slider_embarque.set(0)
        self.slider_embarque.configure(command=self._quand_slider_embarque)
        self.slider_embarque.grid(row=3, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_embarque = ctk.CTkLabel(self, text="0" + " s")
        self.text_embarque.grid(row=3, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.case_embarque = ctk.CTkRadioButton(self, text="", command=self._actualiser_slider, variable=self.radio_var, value=4)
        self.case_embarque.grid(row=3, column=3, sticky="e")

        """TEMPS DEBARQUEMENT"""
        ctk.CTkLabel(self, text="Temps de débarquement").grid(row=4, column=0, sticky="w", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_debarque = ctk.CTkSlider(self, from_=0, to=30, number_of_steps=30)
        self.slider_debarque.set(0)
        self.slider_debarque.configure(command=self._quand_slider_debarque)
        self.slider_debarque.grid(row=4, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_debarque = ctk.CTkLabel(self, text="0" + " s")
        self.text_debarque.grid(row=4, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.case_debarque = ctk.CTkRadioButton(self, text="", command=self._actualiser_slider, variable=self.radio_var, value=5)
        self.case_debarque.grid(row=4, column=3, sticky="e")

        """CAPACITE CHAISES"""
        ctk.CTkLabel(self, text="Capacité des chaises").grid(row=5, column=0, sticky="w",  padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.slider_capacite = ctk.CTkSlider(self, from_=0, to=8, number_of_steps=8)
        self.slider_capacite.set(0)
        self.slider_capacite.configure(command=self._quand_slider_capacite)
        self.slider_capacite.grid(row=5, column=1, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)
        
        self.text_capacite = ctk.CTkLabel(self, text="0")
        self.text_capacite.grid(row=5, column=2, sticky="ew", padx=PADDING_EN_X, pady=PADDING_EN_Y)

        self.case_capacite = ctk.CTkRadioButton(self, text="", command=self._actualiser_slider, variable=self.radio_var, value=6)
        self.case_capacite.grid(row=5, column=3, sticky="e")


    def _quand_slider_cable(self, valeur) :
        self.taille_cable = int(valeur)
        self.text_cable.configure(text=str(self.taille_cable) + " m")
        #TODO avertir mainapp et recalculer????
    
    def _quand_slider_chaise(self, valeur) :
        self.nb_chaise = int(valeur)
        self.text_chaise.configure(text=str(self.nb_chaise))

    def _quand_slider_vitesse(self, valeur) :
        self.vitesse = round(float(valeur), 1)
        self.text_vitesse.configure(text=str(self.vitesse) + " m/s")

    def _quand_slider_embarque(self, valeur) :
        self.temps_embarquement = int(valeur)
        self.text_embarque.configure(text=str(self.temps_embarquement) + " s")

    def _quand_slider_debarque(self, valeur) :
        self.temps_debarquement = int(valeur)
        self.text_debarque.configure(text=str(self.temps_debarquement) + " s")

    def _quand_slider_capacite(self, valeur) :
        self.capacite_chaise = int(valeur)
        self.text_capacite.configure(text=str(self.capacite_chaise))


    def _actualiser_slider(self):
        selection = self.radio_var.get()

        if selection == 0 : 
            #TODO A VOIR????
            print("Ce qu'on met quand rien n'est selectionné...????")

        """LONGUEUR CABLE"""
        self.slider_cable.configure(state="disabled" if selection == 1 else "normal")
        if selection == 1 :
            print("Graph longeur cable dans la bonne place")

        """NOMBRE DE CHAISES"""
        self.slider_chaise.configure(state="disabled" if selection == 2 else "normal")
        if selection == 2 :
            print("Graph nombre chaise dans la bonne place")

        """VITESSE"""
        self.slider_vitesse.configure(state="disabled" if selection == 3 else "normal")
        if selection == 3 :
            print("Graph vitesse dans la bonne place")

        """TEMPS EMBARQUEMENT"""
        self.slider_embarque.configure(state="disabled" if selection == 4 else "normal")
        if selection == 4 :
            print("Graph temps embarquement dans la bonne place")

        """TEMPS DEBARQUEMENT"""
        self.slider_debarque.configure(state="disabled" if selection == 5 else "normal")
        if selection == 5 :
            print("Graph temps debarquement dans la bonne place")

        """CAPACITÉ CHAISE"""
        self.slider_capacite.configure(state="disabled" if selection == 6 else "normal")
        if selection == 6 :
            print("Graph capacité dans la bonne place")
        #TODO FAIRE LE GRAPH
    


#TODO COMMENTE TON CODE!
#TODO les set des sliders doivent se fier au csv ou bien 0 si pas d'importé (voir lignes 23 et 19 où c'est = à 0)

