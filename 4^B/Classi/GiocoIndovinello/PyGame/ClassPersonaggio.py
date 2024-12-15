import  pygame
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Personaggio:
    nome = ""
    sponda = 0
    mangiato = False
    genere = ""
    immagine = ""
    x = 0
    y = 0
    larghezza = 200
    altezza = 200
    hoverabile = True
    selezionato = False  # Variabile per tracciare se il personaggio è selezionato

    def __init__(self, nome, genere, immagine, x, y, altezza=200, hoverabile=True, evidenzia=False):
        self.nome = nome
        self.genere = genere
        self.immagine = immagine
        self.x = x
        self.y = y
        self.larghezza = 200
        self.altezza = altezza
        self.sponda = 0
        self.mangiato = False
        self.hoverabile = hoverabile
        self.selezionato = False  # Inizialmente il personaggio non è selezionato
        self.evidenzia = evidenzia

    def is_hovered(self, mouse_pos):
        if not self.hoverabile:
            return False
        return (self.x <= mouse_pos[0] <= self.x + self.larghezza and
                self.y <= mouse_pos[1] <= self.y + self.altezza)

    def disegna_sagoma(self):
        if not self.hoverabile:
            return
        if self.immagine:
            image = pygame.image.load(self.immagine).convert_alpha()
            image = pygame.transform.scale(image, (self.larghezza, self.altezza))
            mask = pygame.mask.from_surface(image)
            mask_surface = mask.to_surface(setcolor=(255, 255, 0, 150), unsetcolor=(0, 0, 0, 0))
            if self.sponda == 0:
                mask_surface = pygame.transform.flip(mask_surface, True, False)
            screen.blit(mask_surface, (self.x - 5, self.y - 5))

    def disegna_info(self, mouse_pos):
    # Mostra le informazioni quando il mouse è sopra il personaggio
        if self.is_hovered(mouse_pos):
            # Posizione e dimensioni del rettangolo delle informazioni
            info_width, info_height = 200, 100
            rect_x = self.x + self.larghezza + 10
            rect_y = self.y

            # Disegna il rettangolo bianco per le informazioni
            pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, info_width, info_height))
            pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, info_width, info_height), 2)  # Bordo del rettangolo

            # Disegna il testo con le informazioni
            font = pygame.font.SysFont("Arial", 18)
            text_nome = font.render(f"Nome: {self.nome}", True, (0, 0, 0))
            text_genere = font.render(f"Genere: {self.genere}", True, (0, 0, 0))
            if self.genere == "carnivoro":
                text_mangia = font.render(f"Mangia: erbivori", True, (0, 0, 0))
            elif self.genere == "erbivoro":
                text_mangia = font.render(f"Mangia: vegetali", True, (0, 0, 0))
            else:
                text_mangia = font.render(f"Mangia: nulla", True, (0, 0, 0))

            # Posiziona il testo all'interno del rettangolo
            screen.blit(text_nome, (rect_x + 10, rect_y + 10))
            screen.blit(text_genere, (rect_x + 10, rect_y + 30))
            screen.blit(text_mangia, (rect_x + 10, rect_y + 50))




    def disegna(self, evidenzia=False):
        if self.immagine:
            image = pygame.image.load(self.immagine).convert_alpha()
            image = pygame.transform.scale(image, (self.larghezza, self.altezza))
            if self.nome == "Barca":
                if hasattr(self, 'orientamento') and self.orientamento == "sinistra":
                    image = pygame.transform.flip(image, True, False)

            if self.sponda == 0:
                image = pygame.transform.flip(image, True, False)
            if evidenzia or self.selezionato:  # Mostra la sagoma se il personaggio è selezionato
                self.disegna_sagoma()
                self.disegna_info(pygame.mouse.get_pos())
            screen.blit(image, (self.x, self.y))
        
    def mangia(self, other):
        print(f"{self.nome} ha mangiato {other.nome}\nHai perso!")
        other.mangiato = True
        if (self.genere == "carnivoro" and other.genere == "erbivoro") or (self.genere == "erbivoro" and other.genere == "vegetale"):
            other.mangiato = True