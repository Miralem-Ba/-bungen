# Begrüßung mit Namen 
# Schreibe eine Funktion greet(name), die eine Person mit ihrem Namen begrüßt.
# Beispiel: greet("Anna") → "Hallo, Anna!"
# Variante1
def greet(name):
    return f"Hallo, {name}!"
# Funktionsaufruf
greet("Anna")

# Variante2
def greet(name):
    return "Hallo,{}".format(name)
# Funktionsaufruf
greet("Anna")

# Quadrat einer Zahl
# Schreibe eine Funktion square(n), die das Quadrat einer Zahl zurückgibt.
# Beispiel: square(4) → 16
def square(n):
    return n * n
# Funktionsaufruf
square(4)

# Verdopple eine Zahl
# Schreibe eine Funktion double(n), die das Doppelte einer Zahl zurückgibt.
# Beispiel: double(6) → 12
def double(n):
    return n * 2
# Funktionsaufruf
double(7)

# Längste von zwei Wörtern finden
# Schreibe eine Funktion longer_word(word1, word2), die das längere der beiden Wörter zurückgibt.
# Beispiel: longer_word("Haus", "Auto") → "Haus"
def longer_word(word1, word2):
    if len(word1) > len(word2):
        return word1
    elif len(word1) < len(word2):
        return word2
    else:
        return "Gleich gross"
# Funktionsaufruf
longer_word("Haus","Auto")

# Ein Wort mehrmals ausgeben
# Schreibe eine Funktion repeat_word(word, times), die ein Wort mehrmals hintereinander ausgibt.
# Beispiel: repeat_word("Hallo", 3) → "HalloHalloHallo"
def repeat_word(word, times):
    return word *times
# Funktionsaufruf
repeat_word("Hallo",3)

# Prüfen, ob eine Zahl positiv ist
# Schreibe eine Funktion is_positive(n), die True zurückgibt, wenn eine Zahl positiv ist, sonst False.
# Beispiel: is_positive(7) → True, is_positive(-3) → False
def is_positive(n):
    return n > 0
# Funktionsaufruf
is_positive(1)

# Erster Buchstabe eines Wortes
# Schreibe eine Funktion first_letter(word), die den ersten Buchstaben eines Wortes zurückgibt.
# Beispiel: first_letter("Banane") → "B"
def first_letter(word):
    return word[0]
# Funktionsaufruf
first_letter("finale")

# Zwei Wörter zu einem Wort verbinden
# Schreibe eine Funktion combine_words(word1, word2), die zwei Wörter aneinanderhängt.
# Beispiel: combine_words("Super", "markt") → "Supermarkt"
def combine_words(word1, word2):
    return word1 + word2
# Funktionsaufruf
combine_words("Super","markt")

# Letztes Zeichen einer Zeichenkette
# Schreibe eine Funktion last_character(text), die das letzte Zeichen eines Textes zurückgibt.
# Beispiel: last_character("Hallo") → "o"
def last_character(text):
    return text[-1]
# Funktionsaufruf
last_character("Hallo")

# Einfache Begrüßung mit Alter
# Schreibe eine Funktion greet_with_age(name, age), die eine Person mit Namen und Alter begrüßt.
# Beispiel: greet_with_age("Lena", 25) → "Hallo Lena, du bist 25 Jahre alt!"
# Variante1
def greet_with_age(name, age):
    return f"Hallo {name}, du bist {age} Jahre alt!"
# Funktionsaufruf
print(greet_with_age("Miralem", 35))

# Variante2
def greet_with_age(name, age):
    return "Hallo {}, du bist {} Jahre alt!".format(name, age)
# Funktionsaufruf
print(greet_with_age("Miralem", 35))

# Begrüßung mit "Guten Morgen"
# Schreibe eine Funktion good_morning(name), die eine Person mit "Guten Morgen, [Name]!" begrüßt.
# Beispiel: good_morning("Paul") → "Guten Morgen, Paul!"
def good_morning(name):
    return f"guten Morgen, {name}"
# Funktionsaufruf
good_morning("paul")

# Subtrahiere zwei Zahlen
# Schreibe eine Funktion subtract(a, b), die zwei Zahlen subtrahiert und das Ergebnis zurückgibt.
# Beispiel: subtract(10, 4) → 6
def subrtact(a, b):
    return a + b
# Funktionsaufruf
subrtact(50,35)
