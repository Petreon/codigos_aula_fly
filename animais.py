class Animal():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        return "auau"
    
class Ave():
    def __init__(self,asas,nome,idade):
        self.asas = asas
        self.animal = Animal(nome,idade)
        

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    def latir(self):
        return "Abanar o rabo"

class Gato(Animal):
    def __init__(self, nome, idade,comida):
        super().__init__(nome, idade)
        self.comida = comida
    def latir(self):
        return "miau"

class Pessoa():
    def __init__(self,cachorro):
        self.cachorro = cachorro

cachorro1 = Cachorro("fisco",8,"pitbull")
gato1 = Gato("fisco",8,"pitbull")

pessoa1 = Pessoa(cachorro1)


passaro = Ave("penas","tutu",20)


print()
