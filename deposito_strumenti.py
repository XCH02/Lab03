from csv import reader
from strumenti import Strumenti
from operator import attrgetter
from prestiti import Prestiti
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
                tipo=line[1]
                marca=line[2]
                anno_acquiso= int(line[3])
                valore=float(line[4])

                strumenti=Strumenti(codice,tipo,marca,anno_acquiso,valore)

                self.strumenti[codice]= strumenti #adesso sono dizionario strumenti con chiavi codici
            fileIn.close()
        except FileNotFoundError:
            print(f"file {file_path} non trovato")



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""

        if not self.strumenti:  #se strumenti vuoto cod uguale cod iniziale
            nuovo_cod = "S1"

        else:
            strumenti_presenti=len(self.strumenti)
            nuovo_cod= f"S{strumenti_presenti+1}"
        #dopo che ho gestito il codice identificativo creo il nuovo strumento e lo aggiungo nel diz strumenti
        stumenti_nuovo = Strumenti(nuovo_cod, tipo, marca, anno_acquisto, valore)
        self.strumenti[nuovo_cod] = stumenti_nuovo

        return stumenti_nuovo

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        strumenti_ordinati = sorted(self.strumenti.values(), key=attrgetter('marca'))
        return strumenti_ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        #strumento esiste?
        if id_strumento not in self.strumenti:
            raise Exception(f"{id_strumento} non trovato")
        #strumento è in prestito?

        for prestito in self.prestito.values(): # mi legge i valori del dizionario e non la key
            if prestito.id_strumento == id_strumento:
                raise Exception(f"{id_strumento} è già in prestito")

        #creo un nuovo codice prestito
        nuovo_id_prestito =f"P{len(self.prestito)+1}"

        #creo il prestito con il nuovo codice
        nuovo_prestito= Prestiti(nuovo_id_prestito,data, id_strumento, cognome_allievo)

        self.prestito[nuovo_id_prestito] = nuovo_prestito
        return nuovo_prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        #controllo prima che id prestito sia presente
        if id_prestito not in self.prestito:
            raise Exception(f"{id_prestito}  non trovato")

        rimuovi_prestito = self.prestito.pop(id_prestito)
        return rimuovi_prestito

