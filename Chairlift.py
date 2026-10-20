class Chairlift:
    def __init__(self):
        self.__vitesse = 0
        self.__nombreDeChaise = 0
        self.__nombreDePersonnesParChaise = 0
        self.__longeurDuTrajet = 0
        self.__tempsEmbarquement = 0
        self.__tempsDebarquement = 0


    def setVitesse(vitesse):
        if vitesse >= 0:
            __vitesse = vitesse
            return True
        else:
            return False

    def setNombreDeChaise(nombreDeChaise):
        if nombreDeChaise >= 0:
            __nombreDeChaise = nombreDeChaise
            return True
        else:
            return False

    def setLongeurDuTrajet(longeurDuTrajet):
        if longeurDuTrajet > 0:
            __longeurDuTrajet = longeurDuTrajet
            return True
        else:
            return False

    def setTempsEmbarquement(tempsEmbarquement):
        if tempsEmbarquement >= 0:
            __tempsEmbarquement = tempsEmbarquement
            return True
        else:
            return False

    def setTempsDebarquement(tempsDebarquement):
        if tempsDebarquement >= 0:
            __tempsDebarquement = tempsDebarquement
            return True
        else:
            return False

    def setNombreDePersonnesParChaise(nombreDePersonnesParChaise):
        if nombreDePersonnesParChaise >= 0:
            __nombreDePersonnesParChaise = nombreDePersonnesParChaise
            return True
        else:
            return False

    def calculerTempsTrajet(self):
        tempsTrajet = self.__longeurDuTrajet / self.__vitesse
        return tempsTrajet
    
    def calculerTempsDeMonter(self):
        tempsTrajet = self.calculerTempsTrajet()
        tempsDeMonter = tempsTrajet + self.__tempsEmbarquement + self.__tempsDebarquement
        return tempsDeMonter

    def calculerTempsDeCycle(self):
        tempsTrajet = self.calculerTempsTrajet()
        tempsDeCycle = 2*tempsTrajet + self.__tempsEmbarquement + self.__tempsDebarquement
        return tempsDeCycle

    

    def __str__(self):
        return f"Vitesse: {self.__vitesse}, Nombre de chaises: {self.__nombreDeChaise}, Longueur du trajet: {self.__longeurDuTrajet}, Temps d'embarquement: {self.__tempsEmbarquement}, Temps de débarquement: {self.__tempsDebarquement}"

