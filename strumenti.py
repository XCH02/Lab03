
class Strumenti:
    def __init__(self,codice, tipologia, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipologia = tipologia
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = int(valore)

    def __str__(self):
        return f"{self.codice}, {self.tipologia}, {self.marca}, {self.anno_acquisto}"