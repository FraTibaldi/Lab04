from stand import Stand

class StandPrese(Stand):
    def __init__(self, codice, metratura, padiglione, prezzo, codiceEspositore, numeroPrese):
        super().__init__(codice, metratura, padiglione, codiceEspositore)
        self.numeroPrese = numeroPrese
        self.prezzo = prezzo * (1 + 0.07 * numeroPrese)

    def __str__(self):
        return f""