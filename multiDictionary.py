import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self._english = d.Dictionary([], "english")
        self._italian = d.Dictionary([], "italian")
        self._spanish = d.Dictionary([], "spanish")
        self._english.loadDictionary("resources/English.txt")
        self._italian.loadDictionary("resources/Italian.txt")
        self._spanish.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        language = input("Insert the language that you will use: ")
        language = language.lower()
        if language == "english":
            self._english.printAll()
        elif language == "italian":
            self._italian.printAll()
        elif language == "spanish":
            self._spanish.printAll()
        else:
            print("Invalid input...try again")

    def searchWord(self, words, language):
        parole = words.strip().split()
        for parola in parole:
            rich_word = rw.RichWord(parola)
            if language == "english":
                if self._english._dizionario.contains(rich_word):
                    pass
                else:
                    print(rich_word)
            elif language == "italian":
                if self._italian._dizionario.contains(rich_word):
                    pass
                else:
                    print(rich_word)
            elif language == "spanish":
                if self._spanish._dizionario.contains(rich_word):
                    pass
                else:
                    print(rich_word)