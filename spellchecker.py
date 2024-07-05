# Importare la funzione time per calcolare i tempi di elaborazione richiesti dall'esercizio
import time

# Importare la classe MultiDictionary dal modulo multiDictionary
from multiDictionary import MultiDictionary

# Definire una classe SpellChecker
class SpellChecker:

    # Definire un metodo __init__
    def __init__(self):
        self._multi_dictionary = MultiDictionary()

    # Definire la funzione handleSentence, che gestisce la frase visualizzata e ne ricerca le parole sbagliate tramite
    # il metodo searchWord
    def handleSentence(self, testo, language):
        # Vengono sostituiti i caratteri non validi, come i segni di punteggaitura, all'interno del testo che viene,
        # inoltre, reso tutto in termini minuscoli
        testo = replaceChars(testo)
        testo = testo.lower()
        # Viene diviso il testo in singole parole
        parole = testo.strip().split()
        # Per ogni parola contenuta in parole ne viene ricercata la sua correttezza
        for parola in parole:
            self._multi_dictionary.searchWord(parola, language)

    # Definire il metodo printMenu, che stampa il menù che visualizzerà l'utente del programma
    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

# Definire la funzione replaceChars che sostituisce i caratteri particolari, come i segni di punteggiatura o le
# parentesi, con un carattere nullo ("")
def replaceChars(testo):
    caratteri_particolari = "\/'{}[]()>#+-.!$%^;,=_"
    for carattere in caratteri_particolari:
        testo = testo.replace(carattere, "")
    return testo