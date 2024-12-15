#Calcolatrice con la classe

class Calcolatrice(object):
    #attributi
    x = 0
    y = 0
    #metodi
    #costruttore
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #addizzione
    def addizzione(self):
        add = self.x + self.y
        return add
    #sottrazione
    def sottrazione(self):
        sott =  self.x - self.y
        return sott
    #moltiplicazione
    def moltiplicazione(self):
        molt =  self.x * self.y
        return molt
    #divisione
    def divisione(self):
        try:
            div = self.x / self.y
        except ZeroDivisionError:
            print("Errore: Divisione per zero") 
        return div
    

#main
#input
x = float(input("\nInserisci il primo numero: \n --->| "))
y = float(input("\nInserisci il secondo numero: \n --->| "))
#istanza
calc = Calcolatrice(x, y)
#lista operazioni
operazioni = ["+", "-", "*", "/"]
#menu
scelta = input("""
Scegli un'operazione:

    [ + ] Addizzione
    [ - ] Sottrazione
    [ * ] Moltiplicazione
    [ / ] Divisione
               
--->| """)
#controllo scelta
try:
    scelta in operazioni
except:
    print("Errore: Scelta non valida")

#addizzione
if scelta == "+":
    print("Risultato: ", calc.addizzione())
#sottrazione
elif scelta == "-":
    print("Risultato: ", calc.sottrazione())
#moltiplicazione
elif scelta == "*":
    print("Risultato: ", calc.moltiplicazione())
#divisione
elif scelta == "/":
    print("Risultato: ", calc.divisione())
#errore
else:
    print("Errore: Scelta non valida")



