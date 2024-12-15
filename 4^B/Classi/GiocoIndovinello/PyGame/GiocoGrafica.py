import pygame
from LibreriaFunzioni import VerificaMangia, VerificaVittoria, PosizionePersonaggi, mostra_menu, inizializza_gioco, disegna_regola, mostra_regole

# Inizializza Pygame
pygame.init()

# Dimensioni della finestra
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gioco di Ruolo")

# Ciclo principale
# Ciclo principale
inizio = True
while inizio:
    # Mostra il menù
    if mostra_menu(screen):
        # Mostra le regole del gioco
        
        # Inizializza il gioco
        background_image, contadino, capra, lupo, cavolo, barca, Elementi = inizializza_gioco()
        
        # Variabili di stato del gioco
        running = True
        selected_character = None
        barca_selezionata = False  # Variabile per verificare se la barca è selezionata

        # Ciclo principale del gioco
        while running:
            # Ottieni la posizione del mouse
            mouse_pos = pygame.mouse.get_pos()

            # Gestione degli eventi
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    inizio = False  # Esce anche dal ciclo esterno

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Se viene cliccata la barca (sempre selezionabile)
                    x, y, raggio = WIDTH - 70, 50, 30
                    if (mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2 <= raggio ** 2:
                        mostra_regole(screen)
                    if barca.is_hovered(mouse_pos):
                        if selected_character:  # Se un personaggio è selezionato
                            barca_selezionata = True  # La barca è ora selezionata
                            print("Hai selezionato la barca.")
                        else:
                            # Se nessun personaggio è selezionato, sposta solo il contadino
                            nuova_sponda = 1 if contadino.sponda == 0 else 0
                            contadino.sponda = nuova_sponda
                            print(f"{contadino.nome} è stato spostato alla sponda {nuova_sponda}")

                    # Se viene cliccato un personaggio (solo quelli sulla stessa sponda del contadino)
                    if not barca_selezionata:
                        for personaggio in [capra, lupo, cavolo]:
                            if personaggio.is_hovered(mouse_pos) and personaggio.sponda == contadino.sponda:
                                if selected_character != personaggio:  # Cambia la selezione solo se il personaggio è diverso
                                    selected_character = personaggio
                                    print(f"Hai selezionato: {personaggio.nome}")

                    # Se la barca è selezionata e un personaggio è selezionato, sposta entrambi
                    if barca_selezionata and selected_character:
                        nuova_sponda = 1 if contadino.sponda == 0 else 0
                        contadino.sponda = nuova_sponda
                        selected_character.sponda = nuova_sponda
                        print(f"{contadino.nome} e {selected_character.nome} sono stati spostati alla sponda {nuova_sponda}")

                        # Resetta la selezione dopo il movimento
                        selected_character = None
                        barca_selezionata = False  # Deseleziona la barca

                        # Verifica se la vittoria è raggiunta
                        if VerificaVittoria(Elementi):
                            print("Hai vinto!")
                            running = False  # Termina il gioco se vince

                    # Verifica se si perde
                    if VerificaMangia(Elementi, contadino):
                        print("Hai perso!")
                        running = False  # Termina il gioco se perde


            # Disegna lo sfondo
            screen.blit(background_image, (0, 0))  # Disegna l'immagine come sfondo

            disegna_regola(screen)

            # Posiziona i personaggi in base alla loro sponda
            PosizionePersonaggi(contadino, capra, lupo, cavolo, Elementi)


            # Aggiorna l'orientamento della barca
            if contadino.sponda == 0:
                # Contadino sulla sponda sinistra, barca orientata verso destra
                barca.orientamento = "destra"
            else:
                # Contadino sulla sponda destra, barca orientata verso sinistra
                barca.orientamento = "sinistra"

            # Disegna i personaggi con la sagoma visibile per il personaggio selezionato
            for personaggio in [contadino, capra, lupo, cavolo, barca]:
                evidenzia = False
                if personaggio == selected_character:  # Mantieni la sagoma visibile per il personaggio selezionato
                    evidenzia = True
                elif personaggio.is_hovered(mouse_pos) and (personaggio.sponda == contadino.sponda or personaggio == barca):
                    evidenzia = True
                personaggio.disegna(evidenzia=evidenzia)

            # Mostra il personaggio selezionato in alto a destra
            if selected_character:
                font = pygame.font.Font(None, 36)
                text = font.render(f"Selezionato: {selected_character.nome}", True, (255, 255, 255))
                screen.blit(text, (20, 20))  # Posiziona il testo in alto a destra

            # Aggiorna la finestra
            pygame.display.flip()

    else:
        # Esce dal ciclo principale se il menù restituisce False
        inizio = False

# Esci dal programma
pygame.quit()
