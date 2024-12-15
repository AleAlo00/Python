#Gestioni Classi Azienda
# Versione 1.0
# Autore: Alessandro Aloe

#Classe Dipendente
class Dipendente(object):
    #Attributi
    nome = ""
    cognome = ""
    età = 0
    Sesso = ""
    ID = 0
    Esperienza = ""
    Disponibilità = True
    Codice_Progetto = ""

    #Costruttore
    def __init__(self, nome, cognome, età, Sesso, ID, Esperienza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.Sesso = Sesso
        self.ID = ID
        self.Esperienza = Esperienza

    #Metodo per la modifica 
    def modifica(self, nome, cognome, età, Sesso, ID, Esperienza):
        #Controllo se i parametri sono vuoti
        if nome != "":
            #Modifica attributo
            self.nome = nome
    
        if cognome != "":
            self.cognome = cognome

        if età != 0:
            self.età = età
        
        if Sesso != "":
            self.Sesso = Sesso

        if ID != "":
            self.ID = ID
        
        if Esperienza != "":
            self.Esperienza = Esperienza
        
    #Metodo per la visualizzazione
    def visualizza(self):
        print("\n<~~~~~~~~~~~Dipendente~~~~~~~~~~~>")
        print("Nome: ", self.nome)
        print("Cognome: ", self.cognome)
        print("Età: ", self.età)
        print("Sesso: ", self.Sesso)
        print("ID: ", self.ID)
        print("Esperienza: ", self.Esperienza)
        if self.Disponibilità == True:
            print("Disponibile")
        else:
            print("Non Disponibile")
        if self.Codice_Progetto == "":
            print("Non assegnato a nessun progetto")
        else:
            print("Assegnato al progetto: ", self.Codice_Progetto)
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    
    #metodo per la disponibilità
    def cambia_disponibilità(self):
        if self.Disponibilità == True:
            self.Disponibilità = False

    



#Classe Progetto
class Progetto(object):
    #Attributi
    Codice = 0
    Descrizione = ""
    data_inizio = ""
    data_fine = ""
    Dipendenti = []

    #Costruttore
    def __init__(self, Codice, Descrizione, data_inizio, data_fine):
        self.Codice = Codice
        self.Descrizione = Descrizione
        self.data_inizio = data_inizio
        self.data_fine = data_fine
    
    #Metodo per la modifica
    def modifica(self, Codice, Descrizione, data_inizio, data_fine):
        #Controllo se i parametri sono vuoti
        if Codice != "":
            #Modifica attributo
            self.Codice = Codice
    
        if Descrizione != "":
            self.Descrizione = Descrizione

        if data_inizio != "":
            self.data_inizio = data_inizio
        
        if data_fine != "":
            self.data_fine = data_fine

    #Metodo per la visualizzazione
    def visualizza(self):
        print("\n<~~~~~~~~~~~Progetto~~~~~~~~~~~>")
        print("Codice: ", self.Codice)
        print("Descrizione: ", self.Descrizione)
        print("Data Inizio: ", self.data_inizio)
        print("Data Fine: ", self.data_fine)
        if len(self.Dipendenti) == 0:
            print("Nessun dipendente assegnato")
        else:
            print("Dipendenti assegnati:")
            for dipendente in self.Dipendenti:
                print(dipendente)
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")

    #Metodo per l'aggiunta di un dipendente
    def assegna_dipendente(self, dipendente, other):
        self.Dipendenti.append(dipendente)
        other.Codice_Progetto = self.Codice

