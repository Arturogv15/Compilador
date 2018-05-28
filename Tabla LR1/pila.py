class Pila():
    def __init__(self):
        self.pila = []

    def push(self, item):
        self.pila.append(item)

    def pop(self):
        return self.pila.pop()

    def muestra(self):
        for i in range(len(self.pila)):
                print(self.pila[i])

    def top(self):
        return self.pila[len(self.pila)-1]
