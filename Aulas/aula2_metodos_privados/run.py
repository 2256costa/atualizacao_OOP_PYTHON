class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura 
        self.__cpf = cpf

    def apresentar(self):
        print(f'Ola! Minha altura - {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f'Meu documento - {self.__cpf}')

jorge = Pessoa("1.70", "Teste")
jorge.__cpf = "123teste"
print(jorge.__cpf)
jorge.apresentar()