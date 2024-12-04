class MinhaClasse:
    def __init__(self, info, elem): # metodo construtor
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.new_atribute_novo = info
        print(self.new_atribute_novo)

    def metodo_1(self):
        print("minha acao 1")
        print("minha acao 2")
        print(self.atributo_2)
        return "Ola Mundo"
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)

minha_classe = MinhaClasse("info aqui no contrutor", 213)

# response = minha_classe.metodo_1()
# print(response)

minha_classe.metodo_2(4)