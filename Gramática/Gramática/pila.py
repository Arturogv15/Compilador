class Pila():
    def __init__(self):
        self.pila = []

    def push(self, item):
        self.pila.append(item)

    def pop(self):
        return self.pila.pop()

    def muestra(self):
        cadena = ""
        for i in range(len(self.pila)):
            cadena += " | " + str(self.pila[i])
        print(cadena)

    def top(self):
        return self.pila[len(self.pila)-1]
