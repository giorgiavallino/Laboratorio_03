# Importare le classi Dictionary e RichWord
from dictionary import Dictionary
from richWord import RichWord

# Inizializzare la classe MultiDictionary
class MultiDictionary:

    # Definire il metodo __init__, nel quale vengono creati i dizionari relativi alla lingua italiana, inglese e
    # spagnola: viene prima creato il dizionario per ogni lingua e viene poi implementata la funzione loadDictionary,
    # creata nella classe Dictionary, per caricare in una lista le parole del dizionario
    def __init__(self):
        self._english = Dictionary([], "english")
        self._italian = Dictionary([], "italian")
        self._spanish = Dictionary([], "spanish")
        self._english.loadDictionary("resources/English.txt")
        self._italian.loadDictionary("resources/Italian.txt")
        self._spanish.loadDictionary("resources/Spanish.txt")

    # Definire il metodo printDic che stampa il dizionario in base al linguaggio scelto
    def printDic(self, language):
        # Richiedere che la lingua sia scritta in caratteri minuscoli (al fine di evitare errori e numerosi costrutti if)
        language = language.lower()
        if language == "english":
            self._english.printAll()
        elif language == "italian":
            self._italian.printAll()
        elif language == "spanish":
            self._spanish.printAll()
        # Se la lingua non corrisponde a nessuna delle precedenti, allora verrà stampato che la lingua scelta non è
        # valida per lo svolgimento del programma
        else:
            print("Invalid language")

    # Definire il metodo searchWord, il quale ricerca una parola all'interno del dizionario della lingua scelta e
    # restituisce se la parola è scritta correttamente o no
    def searchWord(self, parole, language):
        # Inizializzare due liste vuote: una lista in cui verranno appese le parole scritte in maniera corretta e una
        # lista in cui verranno appese le parole scritte in maniera sbagliata
        parole_corrette = []
        parole_sbagliate = []
        # Per ogni parola contenuta in parole è necessario renderla in termini minuscoli e definirla come una RichWord
        for parola in parole:
            parola = parola.lower()
            parola = RichWord(parola)
            # In base alla lingua della parola richiedere se il suo dizionario relativo la contiene: se è contenuta nel
            # dizionario, allora parola.corretta sarà vera, altrimenti sarà falsa
            if language == "english":
                if self._english._dizionario.__contains__(parola):
                    parola.corretta = True
                else:
                    parola.corretta = False
            elif language == "italian":
                if self._italian._dizionario.__contains__(parola):
                    parola.corretta = True
                else:
                    parola.corretta = False
            elif language == "spanish":
                if self._spanish._dizionario.__contains__(parola):
                    parola.corretta = True
                else:
                    parola.corretta = False
            # Se la parola è corretta, allora viene appesa alla lista, inizilamente vuota, delle parole corrette;
            # altrimenti se la parola è scritta in maniera sbagliata, essa viene appesa alla lista delle parole
            # sbagliate
            if parola.corretta == True:
                parole_corrette.append(parola)
            else:
                parole_sbagliate.append(parola)
        return print(parole_sbagliate)

