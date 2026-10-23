
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
#TODO COMMENTER AVANT D'ENVOYER

## commencer par prendre donnees ncecessaire a la creation du graphique dans __init__



class GraphControl(tk.Frame):

    def __init__(self,parent,modele):
        super().__init__(parent)
        self.modele = modele
        self.creation_image()

    def creation_image(self):
        self.figure = Figure(figsize=(6, 3.5))
        ##ligne inutile, veux dire ligne 1, colonne 1, graphique selectionner 1
        self.axis = self.figure.add_subplot(111)
        ##
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)


    def mise_a_jour_image(self, titre, donneesChargees,
                           col_x, col_y="P/h", ##CHANGER NOM DE COLX ET COLY, ainsi que les legendes
                           label_x="", label_y="Nombre de personne par heure"):
        ## DOIT PRENDRE EN PARAMETRE TITRE?
        ## DOIT PRENDRE EN PARAMETRE FONCTION QUI VERIFIER SI DONNÉES ONT CHARGER CORRECTEMENT
        self.axis.clear()

        #TODO Bloc de if pour trouver le titre de l'axe des x



        #TODO CHANGER TITRE AXES
        self.axis.set(title= titre,
                      xlabel="", ylabel="")
        if donneesChargees.empty or donneesChargees is None:
            self.axis.text(0.5,0.5,"Aucune données", transform=self.axis.transAxes,
                           ha="center", va="center")
        elif col_x not in donneesChargees or col_y not in donneesChargees:
            #TODO Trouver nom de colonnes
            self.axis.text(0.5,0.5,"Colonnes manquantes", transform=self.axis.transAxes,
                            ha="center", va="center")
            
        else:
            self.axis.plot(donneesChargees[col_x], donneesChargees[col_y], label=titre)
            self.axis.legend()
    
        self.axis.grid(alpha=0.3)
        self.canvas.draw_idle()

import pandas as pd
root = tk.Tk()
g = GraphControl(root, modele=None)
g.pack(fill="both", expand=True)
g.mise_a_jour_image("Test", pd.DataFrame({"t": [0, 1, 2, 3], "P/h": [0, 2, 1, 4]}),"t")
root.mainloop()