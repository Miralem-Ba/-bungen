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

# Prüfen, ob eine Zahl gleich 10 ist
# Schreibe eine Funktion is_ten(n), die True zurückgibt, wenn n genau 10 ist, sonst False.
# Beispiel: is_ten(10) → True, is_ten(7) → False
def is_ten(n):
    return n == 10
# Funktionsaufruf
is_ten(10)

# Prüfen, ob ein Wort "Hallo" ist
# Schreibe eine Funktion is_hello(word), die True zurückgibt, wenn das Wort "Hallo" ist, sonst False.
# Beispiel: is_hello("Hallo") → True, is_hello("Hi") → False
def is_hello(word):
    return word == "hallo"
# Funktionsaufruf
is_hello("hallo")

# Einen Namen zweimal ausgeben
# Schreibe eine Funktion repeat_name(name), die einen Namen zweimal hintereinander ausgibt.
# Beispiel: repeat_name("Lisa") → "LisaLisa"
def repeat_name(name):
    return name + name
# Funktionsaufruf
repeat_name("lisa")

# Der größere Wert von zwei Zahlen
# Schreibe eine Funktion max_number(a, b), die die größere der beiden Zahlen zurückgibt.
# Beispiel: max_number(5, 8) → 8
def max_number(a, b):
    return max(a, b)
# Funktionsaufruf
max_number(5, 8)

# Prüfen, ob ein Wort mit "A" beginnt
# Schreibe eine Funktion starts_with_a(word), die True zurückgibt, wenn das Wort mit "A" beginnt.
# Beispiel: starts_with_a("Apfel") → True, starts_with_a("Banane") → False
def starts_whit_a(word):
    return word.startswith("A")
# Funktionsaufruf
starts_whit_a("Apfel")

# Die ersten drei Zeichen eines Wortes
# Schreibe eine Funktion first_three_letters(word), die die ersten drei Zeichen eines Wortes zurückgibt.
# Beispiel: first_three_letters("Banane") → "Ban"
def first_three_letters(word):
    return word[:3]
# Funktionsaufruf
first_three_letters("Banane")

# Prüfen, ob eine Zahl kleiner als 100 ist
# Schreibe eine Funktion is_less_than_100(n), die True zurückgibt, wenn n kleiner als 100 ist.
# Beispiel: is_less_than_100(50) → True, is_less_than_100(150) → False
def is_less_than_100(n):
    return n >= 100
# Funktionsaufruf
is_less_than_100(99)

# Einen Satz mit Ausrufezeichen versehen
# Schreibe eine Funktion add_exclamation(sentence), die ein Ausrufezeichen an einen Satz anhängt.
# Beispiel: add_exclamation("Ich mag Programmieren") → "Ich mag Programmieren!"
def add_exclamation(sentence):
    return sentence + "!"
# Funktionsaufruf
add_exclamation("Ich mag Programmieren")
add_exclamation("Wow!")

# Begrüßung mit "Schönen Tag noch"
# Schreibe eine Funktion good_day(name), die eine Person mit "Schönen Tag noch, [Name]!" verabschiedet.
# Beispiel: good_day("Max") → "Schönen Tag noch, Max!"
def good_day(name):
    return "Schönen Tag noch,{}".format(name)
# Funktionsaufruf
good_day("Max")

# Eine Zahl um 1 erhöhen
# Schreibe eine Funktion increase_by_one(n), die eine Zahl um 1 erhöht und das Ergebnis zurückgibt.
# Beispiel: increase_by_one(7) → 8
def increase_by_one(n):
    return n + 1
# Funktionsaufruf
increase_by_one(7)

# Eine Zahl halbieren
# Schreibe eine Funktion half(n), die die Hälfte einer Zahl zurückgibt.
# Beispiel: half(10) → 5.0
def zahl_half(n):
    return n / 2
# Funktionsaufruf
zahl_half(10)

# Prüfen, ob ein Name "Anna" ist
# Schreibe eine Funktion is_anna(name), die True zurückgibt, wenn der Name "Anna" ist, sonst False.
# Beispiel: is_anna("Anna") → True, is_anna("Lena") → False
def is_anna(name):
    return name == "anna"
# Funktionsaufruf
is_anna("anna")

# Ein Wort in Kleinbuchstaben umwandeln
# Schreibe eine Funktion to_lowercase(word), die ein Wort in Kleinbuchstaben umwandelt.
# Beispiel: to_lowercase("PYTHON") → "python"
def to_lowercase(word):
    return word.lower()
# Funktionsaufruf
to_lowercase("PYTHON")

# Prüfen, ob eine Zahl größer als 50 ist
# Schreibe eine Funktion is_greater_than_50(n), die True zurückgibt, wenn die Zahl größer als 50 ist.
# Beispiel: is_greater_than_50(75) → True, is_greater_than_50(30) → False
def is_greater_than_50(n):
    return n >= 50
# Funktionsaufruf
is_greater_than_50(50)

