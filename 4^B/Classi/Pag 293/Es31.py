from ClassPersona import Persona

class Cliente(Persona):
    # Aggiungo nuovi attributi per il Cliente
    telefono = ""
    partita_iva = ""
    
    # Costruttore della classe Cliente, che chiama il costruttore della classe Persona
    def __init__(self, nome, cognome, data_nascita, indirizzo, telefono, partita_iva):
        super().__init__(nome, cognome, data_nascita, indirizzo, telefono)  # Inizializza gli attributi della classe Persona
        self.partita_iva = partita_iva  # Aggiungo il nuovo attributo partita_iva

    # Metodo per modificare i dati del cliente (incluso il numero di telefono e la partita IVA)
    def modifica(self, nome, cognome, data_nascita, indirizzo, telefono, partita_iva):
        super().modifica(nome, cognome, data_nascita, indirizzo, telefono)  # Modifica i dati della classe Persona
        if partita_iva != "":
            self.partita_iva = partita_iva  # Modifica la partita IVA se fornita

    # Metodo per visualizzare i dati del cliente
    def visualizza(self):
        super().visualizza()  # Visualizza i dati della persona (nome, cognome, ecc.)
        print("Partita IVA: ", self.partita_iva)  # Aggiungo la visualizzazione della partita IVA


from ClassPersona import Persona

class Cliente(Persona):
    telefono = ""
    partita_iva = ""
    
    def __init__(self, nome, cognome, data_nascita, indirizzo, telefono, partita_iva):
        super().__init__(nome, cognome, data_nascita, indirizzo, telefono)
        self.partita_iva = partita_iva
    
    def modifica(self, nome, cognome, data_nascita, indirizzo, telefono, partita_iva):
        super().modifica(nome, cognome, data_nascita, indirizzo, telefono)
        if partita_iva != "":
            self.partita_iva = partita_iva
    
    def visualizza(self):
        super().visualizza()
        print("Partita IVA: ", self.partita_iva)


def aggiungi_cliente():
    nome = input("\nInserisci il nome del cliente: ")
    cognome = input("Inserisci il cognome del cliente: ")
    data_nascita = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    indirizzo = input("Inserisci l'indirizzo del cliente: ")
    telefono = input("Inserisci il telefono del cliente: ")
    partita_iva = input("Inserisci la partita IVA del cliente: ")
    return Cliente(nome, cognome, data_nascita, indirizzo, telefono, partita_iva)


# Main
lista_clienti = []  # Lista per contenere solo i clienti

scelta = 0
while scelta != 6:
    try:
        scelta = int(input("""
        <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Gestione Clienti ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
        Scegli un'operazione:
                [ 1 ] Inserisci nuovo cliente
                [ 2 ] Modifica cliente
                [ 3 ] Visualizza cliente
                [ 4 ] Visualizza tutti i clienti
                [ 5 ] Esci

        --->| """))

        if scelta not in range(1, 6):
            print("Errore! Inserire un numero tra 1 e 5")

    except ValueError:
        print("Errore! Inserire un numero intero")

    # Inserimento nuovo cliente
    if scelta == 1:
        cliente_nuovo = aggiungi_cliente()
        lista_clienti.append(cliente_nuovo)
        print("Cliente aggiunto con successo!")

    # Modifica cliente
    elif scelta == 2:
        nome_cliente = input("Inserisci il nome del cliente da modificare: ")
        trovato = False
        for cliente in lista_clienti:
            if cliente.nome == nome_cliente:
                cognome = input("Nuovo cognome: ")
                data_nascita = input("Nuova data di nascita (gg/mm/aaaa): ")
                indirizzo = input("Nuovo indirizzo: ")
                telefono = input("Nuovo telefono: ")
                partita_iva = input("Nuova partita IVA: ")
                cliente.modifica(cognome, data_nascita, indirizzo, telefono, partita_iva)
                print("Cliente modificato con successo!")
                trovato = True
        if not trovato:
            print(f"Cliente con nome '{nome_cliente}' non trovato.")

    # Visualizza un cliente
    elif scelta == 3:
        nome_cliente = input("Inserisci il nome del cliente da visualizzare: ")
        trovato = False
        for cliente in lista_clienti:
            if cliente.nome == nome_cliente:
                cliente.visualizza()
                trovato = True
        if not trovato:
            print(f"Cliente con nome '{nome_cliente}' non trovato.")

    # Visualizza tutti i clienti
    elif scelta == 4:
        if lista_clienti:
            print("\n<~~~ Elenco Clienti ~~~>")
            for cliente in lista_clienti:
                cliente.visualizza()
        else:
            print("Nessun cliente presente.")

    # Esci
    elif scelta == 5:
        print("Grazie per aver utilizzato il programma!")
