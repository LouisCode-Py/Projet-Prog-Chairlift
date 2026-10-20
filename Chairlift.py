class Chairlift:
    def __init__(self):
        self.__vitesse = 0
        self.__nombreDeChaise = 0
        self.__nombreDePersonnesParChaise = 0
        self.__longeurDuTrajet = 0
        self.__tempsEmbarquement = 0
        self.__tempsDebarquement = 0

        self.__parametreObserver = "none"


    def setVitesse(self, vitesse):
        if vitesse >= 0:
            self.__vitesse = vitesse
            return True
        else:
            return False

    def setNombreDeChaise(self,nombreDeChaise):
        if nombreDeChaise >= 0:
            self.__nombreDeChaise = nombreDeChaise
            return True
        else:
            return False

    def setLongeurDuTrajet(self,longeurDuTrajet):
        if longeurDuTrajet > 0:
            self.__longeurDuTrajet = longeurDuTrajet
            return True
        else:
            return False

    def setTempsEmbarquement(self, tempsEmbarquement):
        if tempsEmbarquement >= 0:
            self.__tempsEmbarquement = tempsEmbarquement
            return True
        else:
            return False

    def setTempsDebarquement(self,tempsDebarquement):
        if tempsDebarquement >= 0:
            self.__tempsDebarquement = tempsDebarquement
            return True
        else:
            return False

    def setNombreDePersonnesParChaise(self, nombreDePersonnesParChaise):
        if nombreDePersonnesParChaise >= 0:
            self.__nombreDePersonnesParChaise = nombreDePersonnesParChaise
            return True
        else:
            return False
        
    def setParametreObserver(self, parametreObserver):
        if parametreObserver in ["vitesse", "nombreDeChaise", "longeurDuTrajet", "tempsEmbarquement", "tempsDebarquement", "nombreDePersonnesParChaise", "none"]:
            self.__parametreObserver = parametreObserver
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

    def calculerNombreDePersonnesParHeure(self):
        tempsDeCycle = self.calculerTempsDeCycle()
        nombreDePersonnesParHeure = (3600 / tempsDeCycle) * self.__nombreDeChaise * self.__nombreDePersonnesParChaise
        return nombreDePersonnesParHeure

    def test(self):
        print("input vitesse: ")
        vitesse = float(input())
        self.setVitesse(vitesse)

        print("input nombre de chaises: ")
        nombreDeChaise = int(input())
        self.setNombreDeChaise(nombreDeChaise)

        print("input longueur du trajet: ")
        longeurDuTrajet = float(input())
        self.setLongeurDuTrajet(longeurDuTrajet)

        print("input temps d'embarquement: ")
        tempsEmbarquement = float(input())
        self.setTempsEmbarquement(tempsEmbarquement)

        print("input temps de débarquement: ")
        tempsDebarquement = float(input())
        self.setTempsDebarquement(tempsDebarquement)

        print("input nombre de personnes par chaise: ")
        nombreDePersonnesParChaise = int(input())
        self.setNombreDePersonnesParChaise(nombreDePersonnesParChaise)

        print(self)
        print(f"Nombre de personnes par heure: {self.calculerNombreDePersonnesParHeure()}")


    def __str__(self):
        return f"Vitesse: {self.__vitesse}, Nombre de chaises: {self.__nombreDeChaise}, Longueur du trajet: {self.__longeurDuTrajet}, Temps d'embarquement: {self.__tempsEmbarquement}, Temps de débarquement: {self.__tempsDebarquement}, Nombre de personnes par chaise: {self.__nombreDePersonnesParChaise}, Temps de trajet: {self.calculerTempsTrajet()}, Temps de monter: {self.calculerTempsDeMonter()}, Temps de cycle: {self.calculerTempsDeCycle()}"

#mon_chairlift = Chairlift()
#mon_chairlift.test()