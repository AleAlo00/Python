# Costanti per le tariffe
TARIFFA_AUTO_GIORNALIERA = 85  # Tariffa giornaliera per l'auto in €
KM_EXTRA_COSTO = 0.24  # Costo per chilometri extra (oltre i 3000 km al mese) in €/km
KM_COMPRESI_AUTO = 3000  # Chilometri inclusi nel noleggio per i noleggi oltre 20 giorni
GIORNI_INCLUSI_AUTO = 20  # Limite di giorni per cui i chilometri sono illimitati
TARIFFA_CAMPER_GIORNALIERA = 65  # Tariffa giornaliera per il camper in €
ASSICURAZIONE_CAMPER = 200  # Costo fisso dell'assicurazione e costi di servizio per il camper in €

# Classe base per il noleggio auto
class NoleggioAuto:
    def __init__(self, giorni_noleggio, km_extra=0):
        self.giorni_noleggio = giorni_noleggio
        self.km_extra = km_extra

    def calcola_costo(self):
        if self.giorni_noleggio <= GIORNI_INCLUSI_AUTO:
            return self.giorni_noleggio * TARIFFA_AUTO_GIORNALIERA
        else:
            # Calcolo per noleggi oltre i 20 giorni
            costo = GIORNI_INCLUSI_AUTO * TARIFFA_AUTO_GIORNALIERA
            if self.km_extra > KM_COMPRESI_AUTO:
                km_extra = self.km_extra - KM_COMPRESI_AUTO
                costo += km_extra * KM_EXTRA_COSTO
            return costo

# Classe derivata per il noleggio camper
class NoleggioCamper(NoleggioAuto):
    def __init__(self, giorni_noleggio, km_extra=0):
        super().__init__(giorni_noleggio, km_extra)

    def calcola_costo(self):
        # Calcolo per il noleggio camper con tariffa giornaliera e costo fisso per assicurazione
        costo = self.giorni_noleggio * TARIFFA_CAMPER_GIORNALIERA + ASSICURAZIONE_CAMPER
        if self.giorni_noleggio > GIORNI_INCLUSI_AUTO:  # se il noleggio supera i 20 giorni
            if self.km_extra > KM_COMPRESI_AUTO:
                km_extra = self.km_extra - KM_COMPRESI_AUTO
                costo += km_extra * KM_EXTRA_COSTO
        return costo

# Funzione per ottenere i dati dall'utente
def richiedi_dati():
    tipo = input("Inserisci il tipo di veicolo (auto/camper): ").strip().lower()
    giorni = int(input("Inserisci il numero di giorni di noleggio: "))
    km_extra = 0
    if giorni > GIORNI_INCLUSI_AUTO:
        km_extra = int(input("Inserisci il numero di chilometri percorsi oltre i 3000 km (0 se nessuno): "))
    return tipo, giorni, km_extra

# Funzione per calcolare il costo
def calcola_costo_noleggio(tipo, giorni, km_extra):
    if tipo == "auto":
        noleggio = NoleggioAuto(giorni, km_extra)
        return noleggio.calcola_costo()
    elif tipo == "camper":
        noleggio = NoleggioCamper(giorni, km_extra)
        return noleggio.calcola_costo()
    else:
        print("Tipo di veicolo non valido.")
        return None

# Funzione per gestire il menu
noleggi = []  # Lista per contenere i noleggi
scelta = 0
while scelta != 4:
    print("""
    <~~~~~~~~~~~~~~~~~~~~~~~~~~ Gestione Noleggio Veicoli ~~~~~~~~~~~~~~~~~~~~~~~~~~>
    Scegli un'operazione:
            [ 1 ] Aggiungi un nuovo noleggio
            [ 2 ] Calcola il costo di un noleggio
            [ 3 ] Visualizza tutti i noleggi
            [ 4 ] Esci
    --->| """)
    
    try:
        scelta = int(input("Scelta: "))
        
        if scelta not in range(1, 5):
            print("Errore! Inserire un numero tra 1 e 4")
    except ValueError:
        print("Errore! Inserire un numero valido.")

    if scelta == 1:
            tipo, giorni, km_extra = richiedi_dati()
            costo = calcola_costo_noleggio(tipo, giorni, km_extra)
            if costo is not None:
                noleggi.append({"tipo": tipo, "giorni": giorni, "km_extra": km_extra, "costo": costo})
                print(f"Noleggio aggiunto con successo! Costo: {costo} €")
    elif scelta == 2:
        tipo, giorni, km_extra = richiedi_dati()
        costo = calcola_costo_noleggio(tipo, giorni, km_extra)
        if costo is not None:
            print(f"Il costo per il noleggio è: {costo} €")
    elif scelta == 3:
        if not noleggi:
            print("Non ci sono noleggi registrati.")
        else:
            print("Noleggi registrati:")
            for noleggio in noleggi:
                print(f"Tipo: {noleggio['tipo']}, Giorni: {noleggio['giorni']}, "
                        f"Km Extra: {noleggio['km_extra']}, Costo: {noleggio['costo']} €")
    elif scelta == 4:
        print("Grazie per aver utilizzato il programma!")


