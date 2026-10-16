from stand import Stand

class StandPrese(Stand):
    def __init__(self, codice, metratura, padiglione, prezzo, numeroPrese):
        super().__init__(codice, metratura, padiglione, prezzo)
        self.numeroPrese = numeroPrese
        self.prezzo = round(prezzo * (1 + 0.07 * numeroPrese), 1)
        self.codiceEspositore = None

    def __str__(self):
        if self.codiceEspositore is None:
            return (f"{self.codice}: Prese Extra | {self.metratura} mq - Padiglione: "
                    f"{self.padiglione} - Prezzo: {self.prezzo} - Prese aggiuntive: {self.numeroPrese} - Disponibile")
        else:
            return (f"{self.codice}: Prese Extra | {self.metratura} mq - Padiglione: {self.padiglione} - "
                    f"Prezzo: {self.prezzo} - Prese aggiuntive: {self.numeroPrese} - Espositore: {self.codiceEspositore}")