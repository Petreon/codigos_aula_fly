class Animal():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        return "auau"
    
class Ave():
    def __init__(self,asas):
        self.asas = asas
        

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

class Gato(Animal):
    def __init__(self, nome, idade,comida):
        super().__init__(nome, idade)
        self.comida = comida

class Pessoa():
    def __init__(self,cachorro):
        self.cachorro = cachorro

cachorro1 = Cachorro("fisco",8,"pitbull")
gato1 = Gato("fisco",8,"pitbull")

pessoa1 = Pessoa(cachorro1)

print()
