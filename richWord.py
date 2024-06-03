# Definire una classe RichWord
class RichWord:

    # Definire il metodo __init__, i cui parametri sono costituiti da una parola
    def __init__(self, parola):
        self._parola = parola # è una stringa
        self._corretta = None # è un valore booleano: vero o falso?

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola