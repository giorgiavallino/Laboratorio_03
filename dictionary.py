# Inizializzare una classe Dictionary()
class Dictionary:

    # Definire il metodo __init__, i cui parametri sono un dizionario che è rappresentato da una lista inzialmente vuota
    # e la lingua che è, invece, rappresentata inizialmente da una stringa vuota
    def __init__(self, dizionario = [], lingua = ""):
        self._dizionario = dizionario
        self.lingua = lingua

    # Definire il metodo __str__ che potrebbe servire in seguito
    def __str__(self):
        return self._dizionario

    # Definire il metodo __repr__ che potrebbe servire in seguito
    def __repr__(self):
        return self._dizionario

    # Definire il metodo loadDictionary, il quale aggiunge al dizionario, inizializzato precedemente come una lista
    # vuota, le singole parole contenute nel file.txt relativo alla lingua scelta
    def loadDictionary(self,path):
        # Aprire il file in modalità lettura indicando nel momento in cui si chiama il metodo loadDictionary() il nome
        # del file da leggere
        with open(path, "r") as file:
            # Inzializzare il contenuto del file tramite il metodo .read()
            contenuto = file.read()
            # Inizializzare le parole contenute nel file tramite i metodi .strip().split()
            parole = contenuto.strip().split()
            # Per ogni parola contenuta in parole riscriverla usando una grafica minuscola e aggiungerla alla lista
            # inizialmente vuota chiamata dizionario
            for parola in parole:
                parola = parola.lower()
                self.dizionario.append(parola)
        # Restituire il dizionario sotto forma di lista ormai non più vuota
        return self.dizionario

    # Definire un metodo printAll che stampa ogni parola contenuta all'interno della lista chiamata dizionario
    def printAll(self):
        # Iterare il parametro i nel range che va da zero fino alla lunghezza del dizionario stesso e stampare ogni
        # parola corrispondente al valore i-esimo del dizionario
        for i in range(0, len(self.dizionario)):
            print(self.dizionario[i])

    # Definire il metodo getter attrvaerso @property: tramite questa dunzione, viene restituito il valore corrispondente
    # all'attributo, ossia viene restituito il valore del dizionario
    @property
    def dizionario(self):
        return self._dizionario