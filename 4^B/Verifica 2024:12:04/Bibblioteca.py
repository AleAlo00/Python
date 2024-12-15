#Gestione Libreria


class ElementoBiblioteca(object):
    #attributi
    titolo = ""
    codice_identificativo = 0
    disponibilità = True

    #init
    def __init__(self,titolo,codice_identificativo):
        self.titolo = titolo
        self.codice_identificativo = codice_identificativo

    #descrizione
    def descrizione(self):
        print(f"Titolo: {self.titolo}")
        print(f"Codice: {self.codice_identificativo}")
        if self.disponibilità == True:
            print("Disponibile")
        else:
            print("Non disponibile")

    #prestito
    def presta(self):
        self.disponibilità = False

    #restituzione
    def restituisci(self):
        self.disponibilità = True


class Libro(ElementoBiblioteca):
    #init
    def __init__(self,titolo,codice_identificativo,autore):
        super().__init__(titolo,codice_identificativo)
        self.autore = autore

    #descrizione
    def descrizione(self):
        print("\n<~~~~~Libro~~~~~>")
        super().descrizione()
        print(f"Autore: {self.autore}")


class dvd(ElementoBiblioteca):
    #init
    def __init__(self,titolo,codice_identificativo,durata):
        super().__init__(titolo,codice_identificativo)
        self.durata = durata

    #descrizione
    def descrizione(self):
        print("\n<~~~~~DVD~~~~~>")
        super().descrizione()
        print(f"Durata: {self.durata} min")


class Rivista(ElementoBiblioteca):
    #init
    def __init__(self,titolo,codice_identificativo,numero_edizione):
        super().__init__(titolo,codice_identificativo)
        self.numero_edizione = numero_edizione
        

    #descrizione
    def descrizione(self):
        print("\n<~~~~~~Rivista~~~~~>")
        super().descrizione()
        print(f"Numero di edizione: {self.numero_edizione}")


def controllo_input(stringa,lista,valore):
    giusto = False
    while giusto != True:
        try:
            if valore == 1:
                domanda = int(input(stringa))
            elif valore == 2:
                domanda = float(input(stringa))
        except ValueError:
            print("Inserisci un numero")

        else:
            giusto = True
            return domanda
    

#istnza libro
titoloL = input("Inserisci il titolo del Libro -->| ")
codiceL = controllo_input("Inserisci il codice di identificazione del Libto -->| ",[range(0,100)],1)
autore = input("Inserisci l'autore del libro -->| ")
istanza_libro = Libro(titoloL,codiceL,autore)


#istanza dvd
titoloD = input("Inserisci il titolo del DVD -->| ")
codiceD = controllo_input("Inserisci il codice di identificazione del DVD -->| ",[range(0,100)],1)
durata = controllo_input("Inserisci la durata del dvd -->| ",[range(0,100)],2)
istanza_dvd = dvd(titoloD,codiceD,durata)

#istanza rivista
titoloR = input("Inserisci il titolo della Rivista -->| ")
codiceR = controllo_input("Inserisci il codice di identificazione della Rivista -->| ",[range(0,100)],1)
edizione = controllo_input("Inserisci il cnumero di edizione -->| ",[range(0,100)],1)
istanza_rivista = Rivista(titoloR,codiceR,edizione)


scelta = 0
while scelta != 4:
    print("""
    [ 1 ] Mostrare gli elementi
    [ 2 ] Effettuare prestito
    [ 3 ] Restituire
    [ 4 ] Esci
    """)

    scelta = controllo_input("Inserisci l'opzione -->| ",[1,2,3,4],1)


    if scelta == 1:
        istanza_libro.descrizione()
        istanza_dvd.descrizione()
        istanza_rivista.descrizione()

    elif scelta == 2:
        try:
            elemento = input("Cosa vuoi prendere in prestito (Libro,DVD,Rivista) -->| ").lower()

            if elemento not in ["libro","dvd","rivista"]:
                print("Elemento non valido")

        except ValueError:
            print("Elemento non valido")

        if elemento == "libro":
            istanza_libro.presta()
            print("Libro preso in prestito")
        elif elemento == "dvd":
            istanza_dvd.presta()
            print("DVD preso in prestito")
        else:
            istanza_rivista.presta()
            print("Rivista presa in prestito")

    elif scelta == 3:
        try:
            elemento = input("Cosa devi restituire (Libro,DVD,Rivista) -->| ").lower()

            if elemento not in ["libro","dvd","rivista"]:
                print("Elemento non valido")

        except ValueError:
            print("Elemento non valido")

        if elemento == "libro":
            istanza_libro.restituisci()
            print("Libro restituito")
        elif elemento == "dvd":
            istanza_dvd.restituisci()
            print("DVD restituito")
        else:
            istanza_rivista.restituisci()
            print("Rivista restituita")

    elif scelta == 4:
        print("Uscita")
        




            
