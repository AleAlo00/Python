"""
8)
Dichiara una classe Automobile con attributi: targa, marca, numero_porte, cilindrata, numero_telaio. 
Oltre ai metodi di base (inizializzatore, modifica, visualizza) aggiungi un metodo per l’immatricolazione. 
Deriva dalla classe Automobile due classi: la classe Monovolume (e aggiungi l’attributo lunghezza) e la classe StationWagon (e aggiungi l’attributo capacità), insieme ai relativi metodi per la loro gestione.
Realizza il diagramma UML della gerarchia di classi, quindi aggiungi alla tua libreria di
classi l’implementazione della classe Automobile. 
Scrivi uno script Python che implementa le due classi derivate e permette la creazione di istanze delle classi sia base sia derivate.
"""

class Automobile:
    targa = ""
    marca = ""
    numero_porte = 0
    cilindrata = 0
    numero_telaio = ""


    def __init__(self, targa, marca, numero_porte, cilindrata, numero_telaio):
        self.targa = targa
        self.marca = marca
        self.numero_porte = numero_porte
        self.cilindrata = cilindrata
        self.numero_telaio = numero_telaio

    def modifica(self, targa, marca, numero_porte, cilindrata, numero_telaio):
        if targa != "":
            self.targa = targa
        if marca != "":
            self.marca = marca
        if numero_porte != 0:
            self.numero_porte = numero_porte
        if cilindrata != 0:
            self.cilindrata = cilindrata
        if numero_telaio != "":
            self.numero_telaio = numero_telaio

    def visualizza(self):
        print(f"Targa: {self.targa}")
        print(f"Marca: {self.marca}")
        print(f"Numero Porte: {self.numero_porte}")
        print(f"Cilindrata: {self.cilindrata}")
        print(f"Numero Telaio: {self.numero_telaio}")

    def immatricolazione(self, data):
        print(f"L'auto con targa {self.targa} è stata immatricolata il {data}.")


class Monovolume(Automobile):
    lunghezza = 0

    def __init__(self, targa, marca, numero_porte, cilindrata, numero_telaio, lunghezza):
        super().__init__(targa, marca, numero_porte, cilindrata, numero_telaio)
        self.lunghezza = lunghezza

    def modifica(self, targa, marca, numero_porte, cilindrata, numero_telaio, lunghezza):
        super().modifica(targa, marca, numero_porte, cilindrata, numero_telaio)
        if lunghezza != 0:
            self.lunghezza = lunghezza

    def visualizza(self):
        super().visualizza()
        print(f"Lunghezza: {self.lunghezza} metri")
    
    def immatricolazione(self, data):
        return super().immatricolazione(data)


class StationWagon(Automobile):
    capacita = 0
    def __init__(self, targa, marca, numero_porte, cilindrata, numero_telaio, capacita):
        super().__init__(targa, marca, numero_porte, cilindrata, numero_telaio)
        self.capacita = capacita

    def modifica(self, targa, marca, numero_porte, cilindrata, numero_telaio, capacita):
        super().modifica(targa, marca, numero_porte, cilindrata, numero_telaio)
        if capacita != 0:
            self.capacita = capacita

    def visualizza(self):
        super().visualizza()
        print(f"Capacità: {self.capacita} litri")

    def immatricolazione(self, data):
        return super().immatricolazione(data)




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

veicoli = []

scelta = 0
while scelta != 7:
    print("\nMenu:")
    print("1. Aggiungi Automobile")
    print("2. Aggiungi Monovolume")
    print("3. Aggiungi StationWagon")
    print("4. Immatricola Veicolo")
    print("5. Modifica Veicolo")
    print("6. Visualizza Veicoli")
    print("7. Esci")
    scelta = controllo_input("Scegli un'opzione -->| ", [1, 2, 3, 4, 5, 6, 7])

    if scelta == 1:
        targa = input("Inserisci la targa dell'automobile -->| ")
        marca = input("Inserisci la marca dell'automobile -->| ")
        numero_porte = int(input("Inserisci il numero di porte dell'automobile -->| "))
        cilindrata = int(input("Inserisci la cilindrata dell'automobile -->| "))
        numero_telaio = input("Inserisci il numero di telaio dell'automobile -->| ")
        auto = Automobile(targa, marca, numero_porte, cilindrata, numero_telaio)
        veicoli.append(auto)

    elif scelta == 2:
        targa = input("Inserisci la targa del monovolume -->| ")
        marca = input("Inserisci la marca del monovolume -->| ")
        numero_porte = int(input("Inserisci il numero di porte del monovolume -->| "))
        cilindrata = int(input("Inserisci la cilindrata del monovolume -->| "))
        numero_telaio = input("Inserisci il numero di telaio del monovolume -->| ")
        lunghezza = float(input("Inserisci la lunghezza del monovolume (in metri) -->| "))
        monovolume = Monovolume(targa, marca, numero_porte, cilindrata, numero_telaio, lunghezza)
        veicoli.append(monovolume)

    elif scelta == 3:
        targa = input("Inserisci la targa della StationWagon -->| ")
        marca = input("Inserisci la marca della StationWagon -->| ")
        numero_porte = int(input("Inserisci il numero di porte della StationWagon -->| "))
        cilindrata = int(input("Inserisci la cilindrata della StationWagon -->| "))
        numero_telaio = input("Inserisci il numero di telaio della StationWagon -->| ")
        capacita = int(input("Inserisci la capacità del bagagliaio della StationWagon (in litri) -->| "))
        station_wagon = StationWagon(targa, marca, numero_porte, cilindrata, numero_telaio, capacita)
        veicoli.append(station_wagon)

    elif scelta == 4:
        targa = input("Inserisci la targa del veicolo da immatricolare -->| ")
        data = input("Inserisci la data di immatricolazione -->| ")
        veicolo_trovato = ""
        for veicolo in veicoli:
            if veicolo.targa == targa:
                veicolo_trovato = veicolo
                veicolo_trovato.immatricolazione(data)

    elif scelta == 5:
        targa = input("Inserisci la targa del veicolo da modificare -->| ")
        veicolo_trovato = ""
        for veicolo in veicoli:
            if veicolo.targa == targa:
                veicolo_trovato = veicolo
                

        if veicolo_trovato:
            if isinstance(veicolo_trovato, Automobile):
                targa = input("Inserisci la targa dell'automobile -->| ")
                marca = input("Inserisci la marca dell'automobile -->| ")
                numero_porte = int(input("Inserisci il numero di porte dell'automobile -->| "))
                cilindrata = int(input("Inserisci la cilindrata dell'automobile -->| "))
                numero_telaio = input("Inserisci il numero di telaio dell'automobile -->| ")
                veicolo_trovato.modifica(targa, marca, numero_porte, cilindrata, numero_telaio)

            elif isinstance(veicolo_trovato, Monovolume):
                targa = input("Inserisci la targa del monovolume -->| ")
                marca = input("Inserisci la marca del monovolume -->| ")
                numero_porte = int(input("Inserisci il numero di porte del monovolume -->| "))
                cilindrata = int(input("Inserisci la cilindrata del monovolume -->| "))
                numero_telaio = input("Inserisci il numero di telaio del monovolume -->| ")
                veicolo_trovato.modifica(targa, marca, numero_porte, cilindrata, numero_telaio, lunghezza)

            elif isinstance(veicolo_trovato, StationWagon):
                targa = input("Inserisci la targa della StationWagon -->| ")
                marca = input("Inserisci la marca della StationWagon -->| ")
                numero_porte = int(input("Inserisci il numero di porte della StationWagon -->| "))
                cilindrata = int(input("Inserisci la cilindrata della StationWagon -->| "))
                numero_telaio = input("Inserisci il numero di telaio della StationWagon -->| ")
                capacita = int(input("Inserisci la capacità del bagagliaio della StationWagon (in litri) -->| "))
                veicolo_trovato.modifica(targa, marca, numero_porte, cilindrata, numero_telaio, capacita)
                                  

    elif scelta == 6:
        for veicolo in veicoli:
            veicolo.visualizza()

    elif scelta == 7:
        print("Arrivederci!")
