from re import * 
from datetime import *
from classe_babbo import *
from random import  choice

def controlla_input(messaggio, tipo='int', lista_opzioni=None):
    while True:
        valore = input(messaggio)

        try:
            if tipo == 'int':
                if not valore.isdigit():
                    raise ValueError("Il valore deve essere un numero intero.")
                valore = int(valore)
                if valore < 0:
                    raise ValueError("Inserire un numero intero positivo.")
            elif tipo == 'float':
                valore = float(valore)
                if valore < 0:
                    raise ValueError("Inserire un numero positivo.")
                
            elif tipo == 'date':
                regex = r"(\d{2})/(\d{2})/(\d{4})"
                if not match(regex, valore):
                    raise ValueError("Il formato della data deve essere gg/mm/aaaa.")
                
                giorno, mese, anno = map(int, valore.split('/'))
                valore = date(anno, mese, giorno)
                
            if lista_opzioni is not None and valore not in lista_opzioni:
                raise ValueError(f"Il valore deve essere uno tra: {', '.join(map(str, lista_opzioni))}")

            return valore

        except ValueError as e:
            print(f"\nATTENZIONE: {e}\n")




def read_from_file(file_name, ):
    lista = []
    try:
        with open(file_name, 'r') as file:
            risposta = input(f"Vuoi caricaretutti i gli amici  dal file {file_name} ? ( Y / N )\n--> ").strip().upper()
            if risposta == 'Y':

                for line in file:
                    nome , cognome , data_nascita , indirizzo , telefono , eol = line.split(',')
                    amico = Amico(nome, cognome, data_nascita, indirizzo, telefono)
                    lista.append(amico)
            
    except FileNotFoundError:
        print(f"Il file {file_name} non esiste.")
        open(file_name, 'w').close()
        print(f"Creato il file {file_name}.")
    return lista

def write_to_file(file_name, lista, tipo):
    try:
        with open(file_name, 'w') as file:
            for amico in lista:
                file.write(f"{amico.nome},{amico.cognome},{amico.data},{amico.indirizzo},{amico.telefono},\n")
    except Exception as e:
        print(f"Errore durante il salvataggio su file: {e}")


def scambia_regali(lista_amici):

    if len(lista_amici) < 2:
        print("Non ci sono abbastanza amici nella lista per scambiare regali.")
    else : 
        mancante = False
        for amico in lista_amici :
            if  not amico.ricevuto:
                mancante = True
                
        if mancante :
            amico1 = choice([amico for amico in lista_amici if not amico.donato])
            amico2 = choice([amico for amico in lista_amici if not amico.ricevuto and amico != amico1])
            
            amico1.regala(amico2)

            print(f"{amico1.nome} ha regalato a {amico2.nome} un {amico1.regalo_comprato}.")
        
        else : 
            print(f"Ogni amico ha ricevuto un regalo.")

