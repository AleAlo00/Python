class Veicolo(object):
    modello = ""
    marca = ""
    anno = 0
    colore = ""

    def __init__(self, modello, marca, anno, colore):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.colore = colore

    def modifica(self, modello, marca, anno, colore):
        if modello != "":
            self.modello = modello
        if marca != "":
            self.marca = marca
        if anno != 0:
            self.anno = anno
        if colore != "":
            self.colore = colore

    def visualizza(self):
        print(f"Modello: {self.modello}")
        print(f"Marca: {self.marca}")
        print(f"Anno di Produzione: {self.anno}")
        print(f"Colore: {self.colore}")

    
