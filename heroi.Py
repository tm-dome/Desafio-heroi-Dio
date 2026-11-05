class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Dicionário mapeando tipo -> ataque
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }
        
        # Busca o ataque correspondente (ou padrão se não existir)
        ataque = ataques.get(self.tipo.lower(), "um ataque desconhecido")
        
        print(f"O {self.tipo} atacou usando {ataque}")


# --- Testando com laço de repetição ---
herois = [
    Heroi("Gandalf", 150, "mago"),
    Heroi("Aragorn", 35, "guerreiro"),
    Heroi("Lee", 28, "monge"),
    Heroi("Kakashi", 30, "ninja"),
]

for heroi in herois:
    heroi.atacar()