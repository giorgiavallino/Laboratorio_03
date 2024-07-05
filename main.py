# Importare la classe SpellChecker dal modulo spellcheker
from spellchecker import SpellChecker

# Inizializzare uno spellchecker attraverso la sua relativa classe
spell_checker = SpellChecker()

while(True):
    # Stampare il menù per l'utente
    spell_checker.printMenu()

    # Inizializzare un input che richieda all'utente quale operazione vuole svolgere
    numero = input("Inserire il numero dell'operazione che si vuole compiere: ")

    # Introdurre un insieme di condizioni if mediante le quali è possibile svolgere le rispettive funzionalità

    # Se il numero inserito corrisponde a caratteri alfabetici, allora il programma viene bloccato poiché quanto
    # inserito dall'utente non rispecchia quanto richiesto dal codice stesso... il codice continuerà a stampare il menù
    # iniziale tramite il metodo printMenu e continuerà a chiedere l'inserimento di un input numerico fino a che
    # l'utente non inserirà il valore corretto per il giusto funzionamento del programma
    if numero.isnumeric() == False:
        while numero.isnumeric() == False:
            spell_checker.printMenu()
            print(ValueError(f'Non è stato inserito un numero, ma sono state inserite delle lettere... riprovare!'))
            numero = input("Inserisci il numero dell'operazione che vuoi svolgere: ")

    # Se il numero inserito dall'utente è maggiore di 4 o minore di 1, allora il valore immesso non corrisponde a
    # nessuna funzione e, quindi, bisognerà fornire un nuovo numero al quale viene associata un'operazione
    if int(numero) > 4 and int(numero) < 1:
        print("Il numero inserito non è adatto allo svolgimento del programma")

    # Se il numero è uguale a 1, allora viene inserita una frase italiana da controllare
    if int(numero) == 1:
        frase = input("Inserisci la frase in italiano da controllare: ")
        spell_checker.handleSentence(frase,"italian")
        continue

    # Se il numero è uguale a 2, allora viene inserita una frase inglese da controllare
    if int(numero) == 2:
        frase = input("Inserisci la frase in inglese da controllare: ")
        spell_checker.handleSentence(frase,"english")
        continue

    # Se il numero è uguale a 3, allora viene inserita una frase spagnola da controllare
    if int(numero) == 3:
        txtIn = input("Inserisci la frase in spagnolo da controllare: ")
        spell_checker.handleSentence(txtIn,"spanish")
        continue

    # Se il numero è uguale a 4, allora il programma cessa di funzionare
    if int(numero) == 4:
        break