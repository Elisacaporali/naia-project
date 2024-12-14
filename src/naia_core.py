class NAIA:
    def __init__(self):
        self.name = "NAIA"
        print(f"Iniciando {self.name}: Nurturing Adaptive Intelligence Assistant")

    def greet(self):
        return f"Olá! Eu sou {self.name}, sua assistente de IA adaptativa."

if __name__ == "__main__":
    naia = NAIA()
    print(naia.greet())

