import pygame
from ClassPersonaggio import Personaggio

pygame.init()

# Dimensioni della finestra
WIDTH, HEIGHT = 1200, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Font per il testo
font = pygame.font.SysFont("Arial", 36)

def VerificaMangia(Elementi, Contadino):
    for elemento1 in Elementi:
        for elemento2 in Elementi:
            if elemento1.sponda == elemento2.sponda and elemento1.sponda != Contadino.sponda:
                if (elemento1.genere == "carnivoro" and elemento2.genere == "erbivoro") or (elemento1.genere == "erbivoro" and elemento2.genere == "vegetale"):
                    elemento1.mangia(elemento2)
                    
                    # Mostra chi ha mangiato chi
                    mostra_messaggio(f"{elemento1.nome} ha mangiato {elemento2.nome} Hai perso", 2000)                  
                    return True
    return False



def VerificaVittoria(Elementi):
    for componente in Elementi:
        if componente.sponda != 1:  # Se un elemento non è nella sponda destra
            return False
    mostra_messaggio("Hai Vinto",2000)  # Visualizza il messaggio di vittoria
    return True


def mostra_messaggio(text, durata):
    # Creazione del messaggio
    messaggio = font.render(text, True, WHITE)
    messaggio_width, messaggio_height = messaggio.get_width(), messaggio.get_height()

    # Posizione del messaggio in basso al centro
    x_pos = WIDTH // 2 - messaggio_width // 2
    y_pos = HEIGHT - messaggio_height - 20  # Distanza dal basso

    # Creazione di un background semitrasparente per il testo
    overlay = pygame.Surface((messaggio_width + 20, messaggio_height + 20))
    overlay.fill((0, 0, 0))  # Colore di sfondo
    overlay.set_alpha(150)  # Trasparenza (valore tra 0 e 255)

    # Disegnare il background trasparente
    screen.blit(overlay, (x_pos - 10, y_pos - 10))
    
    # Disegna il testo sopra il background
    screen.blit(messaggio, (x_pos, y_pos))
    
    # Aggiorna la finestra
    pygame.display.flip()

    # Memorizza il tempo di inizio del messaggio
    start_time = pygame.time.get_ticks()

    # Pausa per la durata del messaggio
    while pygame.time.get_ticks() - start_time < durata:
        # Permetti al gioco di aggiornarsi, in modo che il messaggio possa essere visualizzato
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Rendi l'aggiornamento dello schermo
        pygame.display.flip()

    pygame.display.flip()



def PosizionePersonaggi(contadino, capra, lupo, cavolo, elementi):
    for personaggio in elementi:
        if personaggio.sponda == 0:
            if personaggio == contadino:
                personaggio.x = 50
            elif personaggio == capra:
                personaggio.x = 20  # Più a sinistra
            elif personaggio == lupo:
                personaggio.x = 250
            elif personaggio == cavolo:
                personaggio.x = 200
        else:  # Se il personaggio è sulla sponda 1
            if personaggio == contadino:
                personaggio.x = WIDTH - 250  # Più a destra
            elif personaggio == capra:
                personaggio.x = WIDTH - 220  # Più a destra rispetto a "Contadino"
            elif personaggio == lupo:
                personaggio.x = WIDTH - 450
            elif personaggio == cavolo:
                personaggio.x = WIDTH - 400  # Posizione opposta per gli altri personaggi


def inizializza_gioco():
    # Carica l'immagine dello sfondo
    background_image = pygame.image.load("PyGame/img/sfondo.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Adatta l'immagine alla finestra

    # Posiziona i personaggi in modo distribuito sul verde
    contadino = Personaggio("Contadino", "umano", "PyGame/img/contadino.png", 50, 200, altezza=250,hoverabile=False ,evidenzia=False)
    capra = Personaggio("Capra", "erbivoro", "PyGame/img/capra.png", 50, 450, altezza=120, evidenzia=True)
    lupo = Personaggio("Lupo", "carnivoro", "PyGame/img/lupo.png", 190, 250, altezza=120, evidenzia=True)
    cavolo = Personaggio("Cavolo", "vegetale", "PyGame/img/cavolo.png", 230, 350, altezza=100, evidenzia=True)
    barca = Personaggio("Barca", "Neutro", "PyGame/img/barca.png", 400, 600, altezza=350, evidenzia=True)
    barca.larghezza = 500

    # Lista degli elementi (personaggi e oggetti)
    Elementi = [contadino, capra, lupo, cavolo]

    return background_image, contadino, capra, lupo, cavolo, barca, Elementi

def mostra_menu(screen):
    # Colori
    bianco = (255, 255, 255)
    nero = (0, 0, 0)
    rosso = (255, 0, 0)

    # Font
    pygame.font.init()
    font_titolo = pygame.font.Font(None, 80)
    font_opzioni = pygame.font.Font(None, 50)

    # Titolo del menù
    titolo = font_titolo.render("Menù Principale", True, bianco)
    titolo_rect = titolo.get_rect(center=(screen.get_width() // 2, 150))

    # Opzioni e rettangoli dei bottoni
    opzioni = ["Inizia Gioco", "Esci"]
    bottoni = []
    for i, opzione in enumerate(opzioni):
        rect = pygame.Rect(screen.get_width() // 2 - 150, 300 + i * 100, 300, 50)
        bottoni.append((opzione, rect))

    running = True
    while running:
        screen.fill(nero)

        # Disegna titolo
        screen.blit(titolo, titolo_rect)

        # Disegna bottoni
        for opzione, rect in bottoni:
            colore = rosso if rect.collidepoint(pygame.mouse.get_pos()) else bianco
            pygame.draw.rect(screen, colore, rect, border_radius=10)
            testo = font_opzioni.render(opzione, True, nero)
            testo_rect = testo.get_rect(center=rect.center)
            screen.blit(testo, testo_rect)

        pygame.display.flip()

        # Gestione eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Tasto sinistro del mouse
                    for i, (_, rect) in enumerate(bottoni):
                        if rect.collidepoint(event.pos):
                            if i == 0:  # Se l'utente ha scelto "Inizia Gioco"
                                return True
                            else:  # Se l'utente ha scelto "Esci"
                                pygame.quit()
                                exit()
    return False


# Funzione per disegnare l'icona delle regole
def disegna_regola(screen):
    # Colori
    bianco = (255, 255, 255)

    # Posizione e dimensione del cerchio
    x, y, raggio = WIDTH - 70, 50, 30

    # Disegna il cerchio trasparente (senza riempimento, solo bordo)
    pygame.draw.circle(screen, bianco, (x, y), raggio, 4)  # Bordo blu con spessore di 4px

    # Disegna la "i" al centro del cerchio
    font = pygame.font.SysFont("Arial", 36)
    testo = font.render("i", True, bianco)
    testo_rect = testo.get_rect(center=(x, y))
    screen.blit(testo, testo_rect)


# Funzione per mostrare le regole
def mostra_regole(screen):
    # Colore di sfondo e testo
    bianco = (255, 255, 255)
    nero = (0, 0, 0)

    # Dimensioni del rettangolo
    larghezza, altezza = 600, 400
    x = WIDTH // 2 - larghezza // 2
    y = HEIGHT // 2 - altezza // 2

    # Disegna il rettangolo
    pygame.draw.rect(screen, bianco, (x, y, larghezza, altezza))
    pygame.draw.rect(screen, nero, (x, y, larghezza, altezza), 5)  # Bordo nero

    # Testo delle regole
    font = pygame.font.SysFont("Arial", 24)
    regole = [
        "Regole del gioco:",
        "- Trasporta tutti gli elementi sulla sponda destra.",
        "- Non lasciare insieme erbivoro e carnivoro.",
        "- Non lasciare insieme erbivoro e vegetale.",
        "",
        "Controlli:",
        "- Clicca sugli elementi per selezionarli.",
        "- Usa la barca per attraversare il fiume."
    ]

    # Disegna il testo delle regole
    for i, riga in enumerate(regole):
        testo = font.render(riga, True, nero)
        screen.blit(testo, (x + 20, y + 20 + i * 30))

    # Aggiorna lo schermo
    pygame.display.flip()

    # Attendi che l'utente chiuda le regole
    chiusura = True
    while chiusura:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                chiusura = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
