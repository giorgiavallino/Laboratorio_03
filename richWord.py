# Definire una classe RichWord
class RichWord:

    # Definire il metodo __init__, i cui parametri sono costituiti da una parola
    def __init__(self, parola):
        self._parola = parola # è una stringa
        self._corretta = None # è un valore booleano: vero o falso?

    # Definire il metodo getter attraverso @property: tramite questa funzione, viene restituito il valore corrispondente
    # all'attributo, ossia viene restituito il valore di corretta (che è o vero o falso)
    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    # Definire il metodo settere attrverso @name.property: tramite questa funzione, il setter prende il valore boolValue
    # e lo salva nella proprietà corretta
    @corretta.setter
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    # Definire il metodo __str__ che potrebbe servire in seguito
    def __str__(self):
        return self._parola