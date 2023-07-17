

class Lampada:
    
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

    #     self.__voltagem = voltagem
    #     self.__cor = cor
    #     self.__ligada = False

    # @property
    # def voltagem(self):
    #     return self.__voltagem

    # @property
    # def cor(self):
    #     return self.__cor

    # @property
    # def ligada(self):
    #     return self.__ligada

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo 

class Produto:

    imposto = 1.05 # Atributo de class
    contator = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contator + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)

        Produto.contator = self.id 

class User:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Acesso:
    
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def PasswordAcess(self):
        print(self.__senha)

    def EmailAcess(self):
        print(self.email)

user = Acesso('user@gmail.com', 'eumesmo0123456789')

print(user.email)

print(user._Acesso__senha)

user.PasswordAcess()
user.EmailAcess()


user1 = Acesso('user1@gmail.com', 'eumesmo123456789')

user2 = Acesso('user2@gmail.com', 'eumesmo123456789')

user1.EmailAcess()
user2.EmailAcess()

p1 = Produto('Teclado', 'Teclado Gamer HyperX', 4000)
p2 = Produto('Monitor', 'Monitor Gamer 144Hz', 3098)
p2.peso = '5Kg'
 
print(p1.valor)
print(p1.id)
print(p2.valor)
print(p2.id)
print(Produto.imposto)

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')



print(p1.__dict__)
print(p2.__dict__)
print(Produto.__dict__)

del p2.descricao

print(p2.__dict__)
print(Produto.__dict__)









