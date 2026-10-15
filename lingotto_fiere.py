from stand import Stand
from standPrese import StandPrese
from standPremium import StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.listaStand = []
        self.listaEspositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path, "r") as filein:
                for line in filein:
                    line = line.rstrip().split()
                    if line[0][:2] == "ST":
                        codiceStand = line[0]
                        metraturaStand = int(line[1])
                        padiglione = line[2]
                        prezzo = float(line[3])
                        if line[4].isnumeric():
                            prese = int(line[4])
                            stand = StandPrese(codiceStand, metraturaStand, padiglione, prezzo, prese)
                        elif line[4].isdigit():
                            posizione = line[4]
                            stand = StandPremium(codiceStand, metraturaStand, padiglione, prezzo, posizione)
                        else:
                            stand = Stand(codiceStand, metraturaStand, padiglione, prezzo)
                        self.listaStand.append(stand)
                    elif line[0][:2] == "ES":
                        codice = line[0]
                        nome = line[1]
                        cognome = line[2]
                        espositore = Espositore(codice, nome, cognome)
                        self.listaEspositori.append(espositore)

        except FileNotFoundError:
            return "Errore: file non trovato"

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand = None
        for s in self.listaStand:
            if s.codice == codice_stand:
                stand = s
                break
        if stand is None:
            return "Errore: stand non trovato"
        if not any(e.codice == codice_espositore for e in self.listaEspositori):
            return "Errore: espositore non trovato"
        if not stand.disponibile():
            raise Exception("Errore: stand non disponibile")
        if any(s.codiceEspositore == codice_espositore for s in self.listaStand):
            raise Exception("Errore: stand già associato ad un altro espositore")
        stand.assegna(codice_espositore)

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
