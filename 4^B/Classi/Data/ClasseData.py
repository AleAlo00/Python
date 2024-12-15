# ClasseData.py

from datetime import date

class Data(object):
    # Attributi
    giorno = 0
    mese = 0
    anno = 0
    controllo_bisestile = False
    valida = False


    def __init__(self, giorno, mese, anno):
        self.giorno = giorno
        self.mese = mese
        self.anno = anno

    # Visualizza data
    def visualizza_data(self):
        print(f"{self.giorno:02}/{self.mese:02}/{self.anno}")

    #controllo data
    def controllo_data(self):
        if self.anno % 400 == 0:
            self.controllo_bisestile = True
        elif self.anno % 4 == 0 and self.anno % 100 != 0:
            self.controllo_bisestile = True
        else:
            self.controllo_bisestile = False
        
        return self.controllo_bisestile
    
    # Controllo giorno
    def controllo_giorno(self, giorno, mese):
        if mese == 2:
            if self.controllo_data():
                return 1 <= giorno <= 29
            else:
                return 1 <= giorno <= 28
        
        if mese in [4, 6, 9, 11]:
            return 1 <= giorno <= 30
        else:
            return 1 <= giorno <= 31
            
    def controllo_mese(self, mese):
        return 1 <= mese <= 12
        
    def controllo_anno(self, anno):
        return 0 < anno < date.today().year
    
    def validita(self):
        if self.controllo_giorno(self.giorno, self.mese) == True and self.controllo_mese(self.mese) == True and self.controllo_anno(self.anno) == True:
            self.valida = True
        else:
            self.valida = False
        return self.valida
    
