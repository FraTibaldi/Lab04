from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, metratura, padiglione, prezzo, codiceEspositore, Posizione):
        super().__init__(codice, metratura, padiglione, codiceEspositore)
        self.prezzo = prezzo * 1.30
        self.Posizione = Posizione
    def __str__(self):
        return f""
