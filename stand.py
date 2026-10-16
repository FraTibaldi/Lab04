
class Stand:
    def __init__(self, codice, metratura, padiglione, prezzo):
        self.codice = codice
        self.metratura = metratura
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.codiceEspositore = None
    def __str__(self):
        return f"{self.codice} Standard | {self.metratura} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo}"
    def disponibile(self):
        return self.codiceEspositore is None
    def assegna(self, codice_espositore):
        self.codiceEspositore = codice_espositore
    def libera(self):
        self.codiceEspositore = None

