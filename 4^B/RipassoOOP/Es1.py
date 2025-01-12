"""
1)
Implementa una classe Calciatore con attributi nome, cognome, età e una lista di compagni di squadra. 
Gli unici due metodi della classe calciatore sono:
• il metodo aggiungi_compagno, che aggiunge un compagno alla lista dei compagni;
• il metodo visualizza_squadra, che stampa a video nome, cognome ed età dell’istanza e i compagni di squadra nella lista.
Esegui un main con due squadre di calcio diverse, visualizzando almeno una volta le due squadre.
Salva i dati su file di testo.

"""

class Calciatore:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.compagni = []

    def aggiungi_compagno(self, compagno):
        if compagno not in self.compagni and compagno != self:
            self.compagni.append(compagno)

    def visualizza_squadra(self):
        print(f"\nNome: {self.nome}\nCognome: {self.cognome}\nEtà: {self.eta}")
        print("Compagni di squadra:")
        for compagno in self.compagni:
            print(f"{compagno.nome} {compagno.cognome} ({compagno.eta} anni)")


def controllo_input(stringa, valori_validi):
    corretto = False
    while corretto == False:
        try:
            risposta = int(input(stringa))
            if risposta in valori_validi:
                corretto = True
                return risposta
            else:
                print("Valore non valido. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

percorso = "squadre.txt"
punta = open(percorso, "a")
punta.close()

punta = open(percorso, "r")
lista_record = punta.readlines()
punta.close()

for record in lista_record:
    nome, cognome, eta, compagni, eol = record.split(",")
    istanza_calciatore = Calciatore(nome, cognome, eta)
    if compagni != "":
        compagni = compagni.split(";")



calciatore1 = Calciatore("Marco", "Rossi", 25)
calciatore2 = Calciatore("Luca", "Bianchi", 27)
calciatore3 = Calciatore("Giovanni", "Verdi", 24)
calciatore4 = Calciatore("Andrea", "Neri", 28)

giocatori_liberi = [calciatore1, calciatore2, calciatore3, calciatore4]
squadra1 = []
squadra2 = []
percorso = "squadre.txt"

scelta = 0
while scelta != 3:
    print("\nMenu:")
    print("1. Aggiungi calciatore a una squadra")
    print("2. Visualizza squadre")
    print("3. Esci")
    scelta = controllo_input("Scegli un'opzione: ", [1, 2, 3])

    if scelta == 1:
        print("\nScegli la squadra:")
        squadra = controllo_input("1. Squadra 1\n2. Squadra 2\n -->| ", [1, 2])

        print("\nScegli il calciatore:")
        for i, giocatore in enumerate(giocatori_liberi):
            print(f"{i + 1}. {giocatore.nome} {giocatore.cognome} ({giocatore.eta} anni)")

        indice_giocatore = controllo_input("\nInserisci il numero del giocatore -->|  ", range(1, len(giocatori_liberi) + 1)) - 1
        giocatore_scelto = giocatori_liberi.pop(indice_giocatore)

        if squadra == 1:
            squadra1.append(giocatore_scelto)
            for giocatore in squadra1:
                giocatore.aggiungi_compagno(giocatore_scelto)
                giocatore_scelto.aggiungi_compagno(giocatore)  
        else:
            squadra2.append(giocatore_scelto)
            for giocatore in squadra2:
                giocatore.aggiungi_compagno(giocatore_scelto)
                giocatore_scelto.aggiungi_compagno(giocatore)  


    elif scelta == 2:
        print("\nSquadra 1:")
        for giocatore in squadra1:
            giocatore.visualizza_squadra()


        print("\nSquadra 2:")
        for giocatore in squadra2:
            giocatore.visualizza_squadra()


    elif scelta == 3:
        punta = open(percorso, "w")
        for giocatore in squadra1:
            if giocatore.compagni != []:
                compagni = ";".join([f"{compagno.nome} {compagno.cognome}" for compagno in giocatore.compagni])
            else:
                compagni = ""
            
            record = f"{giocatore.nome},{giocatore.cognome},{giocatore.eta},{compagni},\n"
            punta.write(record)

        for giocatore in squadra2:
            if giocatore.compagni != []:
                compagni = ";".join([f"{compagno.nome} {compagno.cognome}" for compagno in giocatore.compagni])
            else:
                compagni = ""
            
            record = f"{giocatore.nome},{giocatore.cognome},{giocatore.eta},{compagni},\n"
            punta.write(record)
        
        punta.close()


        

