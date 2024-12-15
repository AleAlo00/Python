import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from classe_babbo import Amico
import random
from datetime import  datetime
import re

def valida_data(data_str, formato="%d/%m/%Y"):

    try:
        datetime.strptime(data_str, formato)
        return True
    except ValueError:
        return False


def read_from_file(file_name, lista_amici, finestra):
    try:
        with open(file_name, 'r') as file:
            # Finestra di conferma per caricare gli amici
            risposta= messagebox.askyesno("Importa amici", f"Vuoi caricare tutti gli amici dal file {file_name}?")
            if risposta:
                for line in file:
                    try:
                        # Separazione dei dati dal file (assumendo che ogni amico sia separato da una virgola)
                        nome, cognome, data_nascita, indirizzo, telefono, eol = line.split(',')
                        amico = Amico(nome, cognome, data_nascita, indirizzo, telefono)

                        # Aggiungi l'amico alla lista
                        lista_amici.append(amico)
                        print(f"Amico {nome} {cognome} aggiunto.")

                    except ValueError:
                        print(f"Errore nel formato della riga: {line.strip()} (formato non valido).")
            
    except FileNotFoundError:
        messagebox.showerror("Errore", f"Il file {file_name} non esiste. Creane uno per continuare.")
        open(file_name, 'w').close()  # Crea il file se non esiste
        print(f"Creato il file {file_name}.")


class Finestra(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.lista_amici = []  # Lista degli amici
        self.background_image = None  # Per mantenere l'immagine di sfondo
        self.inizia_button = None  # Variabile per memorizzare il pulsante "Inizia"
        self.crea_widgets()

    def crea_widgets(self):
        # Carica e configura il background
        original_image = Image.open("babbo.png")
        self.background_image = ImageTk.PhotoImage(original_image.resize((self.master.winfo_width(), self.master.winfo_height())))
        self.label_sfondo = tk.Label(self, image=self.background_image)
        self.label_sfondo.place(relwidth=1, relheight=1)

        # Etichetta del titolo
        self.etichetta = tk.Label(self, text="Secret Santa", font=("Comic Sans MS", 28), fg="red")
        self.etichetta.place(relx=0.5, rely=0.4, anchor="center")

        # Pulsante Avvia
        self.bottone_avvia = tk.Button(self, text="Avvia", command=self.avvia, padx=20, pady=10, font=("Comic Sans MS", 16),fg="darkblue", activeforeground="lightblue")
        self.bottone_avvia.place(relx=0.5, rely=0.6, anchor="center")



    def avvia(self):
        print("Avvio in corso...")
        self.bottone_avvia.destroy()  # Rimuovi il pulsante Avvia
        self.mostra_menu_principale()

    def mostra_menu_principale(self):
        # Rimuove tutti i widget nella finestra
        for widget in self.winfo_children():
            widget.destroy()

        # Aggiungi la GIF animata come sfondo
        self.sfondo_gif_animata()

        # Pulsanti per le funzionalità
        tk.Button(self, text="Aggiungi Amico", command=self.richiesta_amici, padx=20, pady=10, font=("Comic Sans MS", 16),fg="darkblue", activeforeground="lightblue").place(relx=0.3, rely=0.5, anchor="center")
        tk.Button(self, text="Importa amici da file", command=self.import_amici, padx=20, pady=10, font=("Comic Sans MS", 16),fg="darkblue", activeforeground="lightblue").place(relx=0.7, rely=0.5, anchor="center")
        tk.Button(self, text="Visualizza amici", command=self.visualizza_amici, padx=20, pady=10, font=("Comic Sans MS", 16),fg="darkblue", activeforeground="lightblue").place(relx=0.5, rely=0.7, anchor="center")
        tk.Button(self, text="Inserisci regali", command=self.mostra_chiedi_regali, padx=20, pady=10, font=("Comic Sans MS", 16),fg="darkblue", activeforeground="lightblue").place(relx=0.5, rely=0.8, anchor="center")
        tk.Button(self, text="Esci", command=self.exit_gioco, padx=20, pady=10, font=("Comic Sans MS", 16),fg="darkblue", activeforeground="lightblue").place(relx=0.5, rely=0.9, anchor="center")

    def visualizza_amici(self):
        # Mostra la lista degli amici
        for widget in self.winfo_children():
            widget.destroy()

        scrollable_frame = self.scroll_bar()

        # Titolo centrato
        tk.Label(scrollable_frame, text="Elenco amici", font=("Comic Sans MS", 30), anchor="center").pack(pady=10)

        # Etichette degli amici centrate
        for amico in self.lista_amici:
            tk.Label(scrollable_frame, font=("Verdana", 20), text=f"{amico.nome} {amico.cognome} - Regalo: {amico.regalo_comprato}", anchor="center").pack()

        # Pulsante centrato
        tk.Button(scrollable_frame, text="Torna al menu principale", font=("Comic Sans MS", 16), command=self.mostra_menu_principale, fg="darkblue", activeforeground="lightblue", anchor="center").pack(pady=10)



    def richiesta_amici(self):
        for widget in self.winfo_children():
            widget.destroy()


        tk.Label(self, text="Aggiungi un nuovo amico", font=("Helvetica", 18)).pack(pady=10)

        # Campi di input
        fields = {
            "Nome": tk.Entry(self),
            "Cognome": tk.Entry(self),
            "Data di nascita (gg/mm/aaaa)": tk.Entry(self),
            "Indirizzo": tk.Entry(self),
            "Telefono": tk.Entry(self),
        }
        for label, entry in fields.items():
            tk.Label(self, text=label).pack()
            entry.pack()

        tk.Label(self, text="", fg="red").pack()  # Etichetta per messaggi di errore

    # Bottone per salvare
        def salva_amico():
            try:
                nome = fields["Nome"].get().strip()
                cognome = fields["Cognome"].get().strip()
                data_nascita = fields["Data di nascita (gg/mm/aaaa)"].get().strip()
                indirizzo = fields["Indirizzo"].get().strip()
                telefono = fields["Telefono"].get().strip()

                # Validazioni
                if not nome or not cognome:
                    raise ValueError("Nome e cognome sono obbligatori.")
                regex = r"(\d{2})/(\d{2})/(\d{4})"
                if not re.match(regex, data_nascita) :
                    raise ValueError("Il formato della data deve essere gg/mm/aaaa.")
                if not valida_data(data_nascita):
                    raise ValueError("Data di nascita non valida.")
                
                regex_telefono = r"\+(\d{2})\s(\d{3})\s(\d{3})\s(\d{4})"

                if not re.match(regex_telefono, telefono):
                    raise ValueError("Il formato del telefono deve essere +xx xxx xxx xxxx")
                
                amico = Amico(nome, cognome, data_nascita, indirizzo, telefono)
                self.lista_amici.append(amico)
                messagebox.showinfo("Successo", "Amico aggiunto con successo!")
                self.mostra_menu_principale()
            except ValueError as e:
                messagebox.showerror("Errore", str(e))

        tk.Button(self, text="Salva", font=("Comic Sans MS",16),fg="darkblue", activeforeground="lightblue", command=salva_amico).pack(pady=10)
        tk.Button(self, text="Torna al menu principale", font=("Comic Sans MS",16), command=self.mostra_menu_principale,fg="darkblue", activeforeground="lightblue").pack(pady=10)


        errore_label = tk.Label(self, text="", fg="red")
        errore_label.pack()


    def sfondo_gif_animata(self):
        # Carica la GIF animata usando PIL
        self.sfondo_gif = Image.open("snowman-4944.gif")
        
        # Crea una lista dei fotogrammi e delle rispettive durate
        self.frames = []
        self.durations = []  # Durate in millisecondi
        for i in range(self.sfondo_gif.n_frames):
            self.sfondo_gif.seek(i)
            frame = ImageTk.PhotoImage(self.sfondo_gif.copy())
            self.frames.append(frame)
            duration = self.sfondo_gif.info.get("duration", 100)  # Default a 100ms se non specificato
            self.durations.append(duration)

        # Crea un'etichetta con la GIF come sfondo e posizionala
        self.sfondo_label = tk.Label(self, image=self.frames[0])
        self.sfondo_label.place(relwidth=1, relheight=1)  # Copre tutta la finestra

        # Funzione per aggiornare la GIF
        self.update_gif(0)

    def update_gif(self, frame):
        # Aggiorna l'immagine sul label
        self.sfondo_label.configure(image=self.frames[frame])
        # Calcola il tempo di aggiornamento in base alla durata del fotogramma corrente
        next_frame = (frame + 1) % len(self.frames)
        self.after(self.durations[frame], self.update_gif, next_frame)

    def import_amici(self):
        print("Importazione amici in corso...")
        read_from_file("amici.txt", self.lista_amici, self)
        self.mostra_menu_principale()


    def scroll_bar(self):
        # Creazione del Canvas e della Scrollbar
        canvas = tk.Canvas(self, bg="#ADD8E6")
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        scrollable_frame = tk.Frame(canvas, bg="#ADD8E6")

        # Configurazione dello scroll dinamico
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        return scrollable_frame

    def mostra_chiedi_regali(self):
        # Crea una nuova finestra (o pagina) per chiedere i regali
        for widget in self.winfo_children():
            widget.destroy()

        self.config(bg="#ADD8E6")

        
        scrollable_frame = self.scroll_bar()
        # Intestazione
        tk.Label(scrollable_frame, text="Inserisci il regalo che hai comprato", font=("Comic Sans MS", 25),fg="black",bg="#ADD8E6").pack(pady=10)

        # Mostra un campo di input per ogni amico senza regalo
        self.regalo_entries = {}  # Dizionario per memorizzare gli input
        for amico in self.lista_amici:
            if not amico.regalo_comprato:  # Solo se l'amico non ha un regalo
                tk.Label(scrollable_frame, text=f"Regalo comprato da {amico.nome} {amico.cognome}:", fg="black",font=("Helvetica", 18), bg="#ADD8E6").pack(pady=5)
                entry = tk.Entry(scrollable_frame)
                entry.pack(pady=5)
                self.regalo_entries[amico] = entry  # Aggiungi l'input nel dizionario

        # Bottone per salvare i regali
        tk.Button(scrollable_frame, text="Salva regali", font=("Comic Sans MS",16), command=self.salva_regali,fg="darkblue", activeforeground="lightblue").pack(pady=10)


    def salva_regali(self):
        # Salva i regali per tutti gli amici
        for amico, entry in self.regalo_entries.items():
            regalo = entry.get()
            if regalo:
                amico.compra_regalo(regalo)
                print(f"Regalo che ha comprato {amico.nome} {amico.cognome}: {regalo}")
            else:
                print(f"Nessun regalo inserito per {amico.nome} {amico.cognome}.")

        # Verifica se tutti gli amici hanno un regalo
        if all(amico.regalo_comprato for amico in self.lista_amici):
            # Se tutti gli amici hanno un regalo, mostra il pulsante "Esci"
            self.mostra_scambio_regali()
        else:
            # Se non tutti gli amici hanno un regalo, mostra ancora la finestra per i regali
            self.mostra_chiedi_regali()

    def mostra_scambio_regali(self):
        # Pulisce la finestra attuale
        for widget in self.winfo_children():
            widget.destroy()

        scrollable_frame = self.scroll_bar()

        tk.Label(scrollable_frame, text="Scambio Regali", font=("Helvetica", 18)).pack(pady=10)

    # Lista temporanea per garantire che ogni amico doni a un altro
        amici_non_donatori = [amico for amico in self.lista_amici if not amico.donato]
        amici_non_ricevitori = [amico for amico in self.lista_amici if not amico.ricevuto]

    # Simula lo scambio dei regali
        while amici_non_donatori:
            donatore = random.choice(amici_non_donatori)  # Seleziona un donatore a caso
            amici_non_donatori.remove(donatore)  # Rimuovilo dalla lista dei donatori

            ricevitore = random.choice([amico for amico in amici_non_ricevitori if amico != donatore])  # Seleziona un ricevitore casuale diverso dal donatore
            amici_non_ricevitori.remove(ricevitore)  # Rimuovilo dalla lista dei riceventi

            donatore.regala(ricevitore)  # Effettua lo scambio
    # Mostra l'assegnazione in un'etichetta nella GUI
            tk.Label(scrollable_frame, text=f"{donatore.nome} {donatore.cognome} ha regalato '{donatore.regalo_comprato}' a {ricevitore.nome} {ricevitore.cognome}", font=("Helvetica", 14)).pack(pady=5)
 

    # Bottone per terminare
        tk.Button(scrollable_frame, text="Torna al menu principale", command=self.mostra_menu_principale, font=("Comic Sans MS",16),fg="darkblue", activeforeground="lightblue").pack(pady=20)


    def exit_gioco(self):
        # Salva i dati su un file
        with open("amici.txt", 'w') as file:
            for amico in self.lista_amici:
                file.write(f"{amico.nome},{amico.cognome},{amico.data},{amico.indirizzo},{amico.telefono},\n")
        self.master.destroy()

    def aggiorna_sfondo(self, width, height):
        # Aggiorna il background quando la finestra viene ridimensionata
        original_image = Image.open("babbo.png")
        self.background_image = ImageTk.PhotoImage(original_image.resize((width, height)))
        self.label_sfondo.config(image=self.background_image)


# Creazione della finestra principale
root = tk.Tk()
root.title("Finestra di Avvio")
root.geometry("1024x624")

def ridimensiona(event):
    if hasattr(app, "label_sfondo") and app.label_sfondo.winfo_exists():
        app.aggiorna_sfondo(event.width, event.height)

app = Finestra(master=root)
root.bind("<Configure>", ridimensiona)
app.mainloop()
