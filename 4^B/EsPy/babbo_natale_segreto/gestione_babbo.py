from libreria_babbo import *
from classe_babbo import *
lista_amici = []
scelta = 0

print("\n-----------------------------------------------------------------------\n")
print("\nBenvenuto nel programma di gestione degli amici di Babbo Natale!\n")
print("\n-----------------------------------------------------------------------\n")

while scelta != 4:
    print("\n-----------------------------------------------------------------------\n")
    print("1) Aggiungi amico")
    print("2) fai regalo ")
    print("3) Visualizza amici e regali ")
    print("4) Esci")
    print("\n-----------------------------------------------------------------------\n")
    scelta = controlla_input("Inserisci il numero corrispondente all'operazione da eseguire:\n--> ", "int", [1, 2, 3, 4])

    if scelta == 1:

        opt = controlla_input("Vuoi inserire un nuovo amico o caricare gli amici da un file ? (nuovo amico 1 , carica da lista 2 )  \n--> ", "int", [1, 2])

        if opt == 1:
            nome = input("Inserisci il nome dell'amico:\n--> ")
            cognome = input("Inserisci il cognome dell'amico:\n--> ")
            data = controlla_input("Inserisci la data di nascita dell'amico (gg/mm/aaaa):\n--> ", "date")
            indirizzo = input("Inserisci l'indirizzo dell'amico:\n--> ")
            telefono = input("Inserisci il numero di telefono dell'amico:\n--> ")
            regalo_comprato = input("Inserisci il regalo comprato per l'amico:\n--> ")

            amico = Amico(nome, cognome, data, indirizzo, telefono, )
            lista_amici.append(amico)

        elif opt == 2:
            lista_amici = read_from_file("amici.txt")
            for amico in lista_amici:
                amico.compra_regalo(input(f"Inserisci il regalo comprato da {amico.nome} {amico.cognome}:\n--> "))

    elif scelta == 2:
        print("fai regalo")
        scambia_regali(lista_amici)

    elif scelta == 3:
        for amico in lista_amici:
            amico.visualizza()


    elif scelta == 4 :
        opt = controlla_input("Vuoi salvare la lista degli amici su file ? ( 1 / 2 )\n--> ", "int", [1, 2])
        if opt == 1:
            write_to_file("amici.txt", lista_amici, "amici")
        print("\nArrivederci!\n")


            



