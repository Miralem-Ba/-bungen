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