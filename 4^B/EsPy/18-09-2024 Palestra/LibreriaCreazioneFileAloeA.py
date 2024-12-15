#Libreria per la creazione di file di testo

def CreazioneFileTesto(f):
    #Apre il file in modalità scrittura
    Punta = open(f, "w")
    return Punta

def RiempireFileTesto(f):
    #Apre il file in modalità append
    Punta = open(f, "a")
    return Punta

def LetturaFileTesto(f):
    #Apre il file in modalità lettura
    Punta = open(f, "r")
    return Punta

def StampaFile(f):
    try:
        Punta = open(f, "r")
        Riga = Punta.readline()
        print(Riga, end="")
        while Riga != "":
            Riga = Punta.readline()
            print(Riga, end="")
        Punta.close()
    except FileNotFoundError:
        print("File non trovato")
        print("Ricordati di creare il file")

def CercaElemento(f, elemento):
    Riga = f.readline()
    t = False
    while Riga != "":
        if elemento == Riga:
            t = True
            print(f"{elemento} è presente nel file")
        Riga = f.readline()
    if t == False:
        print("Non è presente nel file")


def salva_dati(lista,puntatore):
    for x in lista:
        puntatore.write(x)