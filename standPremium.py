from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice, metratura, padiglione, prezzo, posizione):
        super().__init__(codice, metratura, padiglione, prezzo)
        self.prezzo = round(prezzo * 1.30, 1)
        self.posizione = posizione
        self.codiceEspositore = None
    def __str__(self):
        if self.codiceEspositore is None:
            return (f"{self.codice}: Premium | {self.metratura} mq - Padiglione: "
                    f"{self.padiglione} - Prezzo: {self.prezzo} - Posizione: {self.posizione} - Disponibile")
        else:
            return (f"{self.codice}: Premium | {self.metratura} mq - Padiglione: {self.padiglione} - "
                    f"Prezzo: {self.prezzo} - Posizione: {self.posizione} - Espositore: {self.codiceEspositore}")
