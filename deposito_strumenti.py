from csv import reader
from strumenti import Strumenti
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti =  {}
        self.prestito = {}

    def responsabile_strumenti(self,responsabile):
        self.responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            fileIn= open(file_path, "r")
            file = reader(fileIn)
            for line in file:
                codice=line[0]
                tipologia=line[1]
                marca=line[2]
                anno_acquiso= int(line[3])
                valore=int(line[4])

                strumenti=Strumenti(codice,tipologia,marca,anno_acquiso,valore)
                self.strumenti[codice]=strumenti #adesso sono dizionario strumenti con chiavi codici, manca poi ordinamento2
        except FileNotFoundError:
            print(f"File {file_path} non trovato")


   def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        self

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
