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