
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from Chairlift import Chairlift
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


    def mise_a_jour_image(self, titre,titrey,titrex):
        ## DOIT PRENDRE EN PARAMETRE TITRE?
        ## DOIT PRENDRE EN PARAMETRE FONCTION QUI VERIFIER SI DONNÉES ONT CHARGER CORRECTEMENT
        
        donnee = self.modele.getGraphData(11,0,10)
        print(donnee)

        self.axis.clear()
        self.axis.set(title= titre,
                xlabel=titrex, ylabel=titrey)

        if donnee is None or donnee.size == 0:
            self.axis.text(0.5,0.5,"Aucune données", transform=self.axis.transAxes,
                ha="center", va="center")
        else:
            x,y = donnee.T
            self.axis.plot(x, y, label=titre)
            self.axis.legend()

        self.axis.grid(alpha=0.3)
        self.canvas.draw_idle()

import pandas as pd

root = tk.Tk()
mon_Chairlift = Chairlift()
mon_Chairlift.test()
mon_Chairlift.setParametreObserver("vitesse")

g = GraphControl(root, modele=mon_Chairlift)

g.pack(fill="both", expand=True)
g.mise_a_jour_image("Test","P/h","Temps")
root.mainloop()