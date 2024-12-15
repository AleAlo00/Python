class Foto(object):
    #attributi
    nome_foto = ""
    luogo = ""
    data = ""
    descrizione = ""
    amici = []

    #metodi
    def __init__(self,nome,luogo,data,descrizione,persona):
        self.nome_foto = nome
        self.luogo = luogo
        self.data = data
        self.descrizione = descrizione
        self.amici = persona

    def modifica(self,nome,luogo,data,descrizione,persona):
        if nome != "":
            self.nome_foto = nome
        if luogo != "":
            self.luogo = luogo
        if data != "":
            self.data = data
        if descrizione != "":
            self.descrizione = descrizione
        if persona != "":
            self.amici = persona

    def visualizza(self):
        print(f"\nNome Foto: {self.nome_foto}")
        print(f"Luogo Foto: {self.luogo}")
        print(f"Data Foto: {self.data}")
        print(f"Descrizione Foto: {self.descrizione}")
        print(f"Persone nella Foto: {self.amici}\n")
    

    

lista_foto = []
punta = open("Aloe_foto.txt","a")
punta.close()
#lettura iniziale file delle canzoni
punta = open("Aloe_foto.txt", "r")
lista_record = punta.readlines()
punta.close()

for record in lista_record:
    nome,luogo,data,descrizione,amici_str,eol = record.split(",")
    istanza_foto = Foto(nome,luogo,data,descrizione,amici_str)
    if amici_str != "":
        persone = amici_str.split('-')
        istanza_foto.persone = persone
    lista_foto.append(istanza_foto)


scelta = 0
while scelta != 7:
    print('''
            1. Inserisci una foto
            2. Modificare foto
            3. Cercare foto di un luogo
            4. Visualizzare le foto
            5. Cercare foto di un data
            6. Visualizzare amici in una foto
            7. Salva ed Esci\n  
''')
    try:
        scelta = int(input("Inserisci la tua scelta -->| "))
        if scelta not in [1,2,3,4,5,6,7]:
            print("Inserisci valore valido")
    except ValueError:
        print("Inserisci valore valido")

    if scelta == 1:
        nome = input("Inserisci il nome per la foto -->| ")
        luogo = input("Inserisci il luogo in cui è stata scattata la foto -->| ")
        data = input("Inserisci la data della foto -->| ")
        descrizione = input("Inserisci la descrizione della foto -->| ")
        persona = input("Inserisci gli amici nella foto  -->| ")
        istanza_foto = Foto(nome,luogo,data,descrizione,persona)
        lista_foto.append(istanza_foto)

    elif scelta == 2:
        titolo = input("Inserisci il nome della foto da modificare: ")
        trovato = False
        for foto in lista_foto:
            if foto.nome_foto == titolo:
                nome = input("Inserisci il nome per la foto -->| ")
                luogo = input("Inserisci il luogo in cui è stata scattata la foto -->| ")
                data = input("Inserisci la data della foto -->| ")
                descrizione = input("Inserisci la descrizione della foto -->| ")
                persona = input("Inserisci gli amici nella foto  -->| ")
                foto.modifica(nome,luogo,data,descrizione,persona)
                trovato = True
        if not trovato:
            print(f"La foto {titolo} non esiste")
            
    elif scelta == 3:
        luogo = input("Inserisci il luogo della foto da cercare -->| ")
        trovato = False
        for foto in lista_foto:
            if foto.luogo == luogo:
                trovato = True
                foto.visualizza()
        if not trovato:
            print("Non ci sono foto in quel preciso luogo")

    elif scelta == 4:
        for foto in lista_foto:
            foto.visualizza()

    elif scelta == 5:
        data = input("Inserisci la data della foto da cercare -->| ")
        trovato = False
        for foto in lista_foto:
            if foto.data == data:
                trovato = True
                foto.visualizza()
        if not trovato:
            print("Non ci sono foto in quella specifica data")

    elif scelta == 6:
        titolo = input("Inserisci il nome della foto da modificare -->| ")
        trovato = False
        for foto in lista_foto:
            if foto.nome_foto == titolo:
                for i,amico in enumerate(foto.amici):
                    print(f"[{i}] {amico}")
                    trovato = True

        if not trovato:
            print(f"La foto {titolo} non esiste")

    elif scelta == 7:
        print("Grazie per aver usato il programma")

    else:
        print("Scelta non valida")


punta = open("Aloe_foto.txt", "w")
for foto in lista_foto:
    if foto.amici != []:
        amici_str = '-'.join(foto.amici)
    else:
        amici_str = ""
    record = foto.nome_foto + ',' + foto.luogo + ',' + foto.data + ',' + foto.descrizione + ',' + amici_str + ',\n'
    punta.write(record)
punta.close()