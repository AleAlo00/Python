#Classi

#Classe Foto
class Foto(object):
    #attributi
    codice = 0
    descrizione = ""
    luogo = ""
    data = ""
    amici = []

    #metodi
    def __init__(self,luogo,data,descrizione,persona,codice):
        self.luogo = luogo
        self.data = data
        self.descrizione = descrizione
        self.amici = persona
        self.codice = codice

    def modifica(self,luogo,data,descrizione,persona):
        if luogo != "":
            self.luogo = luogo
        if data != "":
            self.data = data
        if descrizione != "":
            self.descrizione = descrizione
        if persona != "":
            self.amici = persona

    def visualizza(self):
        print(f"\nCodice Foto: {self.codice}")
        print(f"Descrizione Foto: {self.descrizione}")
        print(f"Luogo Foto: {self.luogo}")
        print(f"Data Foto: {self.data}")
        print(f"Persone nella Foto: {self.amici}\n")
    

#Classe Persona
class Persona(object):
    #attributi
    nome = ""
    cognome = ""
    data_nascita = ""
    indirizzo = ""
    telefono = ""
    cf = ""

    #metodi
    #costruttore
    def __init__(self, nome, cognome, data_nascita, indirizzo, telefono, cf):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.cf = cf
    
    #modifica
    def modifica(self, nome, cognome, data_nascita, indirizzo, telefono, cf):
        #controllo
        if nome != "":
            #modifica
            self.nome = nome
        #controllo
        if cognome != "":
            #modifica
            self.cognome = cognome
        #controllo
        if data_nascita != "":
            #modifica
            self.data_nascita = data_nascita
        #controllo
        if indirizzo != "":
            #modifica
            self.indirizzo = indirizzo
        #controllo
        if telefono != "":
            #modifica
            self.telefono = telefono
        #controllo
        if cf != "":
            #modifica
            self.cf = cf

    #visualizza
    def visualizza(self):
        print("\n<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
        print("Nome: ", self.nome)
        print("Cognome: ", self.cognome)
        print("Data di nascita: ", self.data_nascita)
        print("Indirizzo: ", self.indirizzo)
        print("Telefono: ", self.telefono)
        print("Codice Fiscale: ", self.cf)
        print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")


        


        