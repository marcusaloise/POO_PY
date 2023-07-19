
class Lampada:
    
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def check_lamp(self):
        return self.__ligada
    
    def turn_lamp(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class ContaCorrente:

    contador = 999

    def __init__(self, limite, saldo, client):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__client = client
        ContaCorrente.contador = self.__numero

    def show_client(self):
        print(self.__client._Client__nome)

class Client:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


class User:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        
        
lampada1 = Lampada('amarela', 120, 60)
lampada1.turn_lamp()

print(lampada1.check_lamp())

cl1 = Client('Marcus Aloise', '051047989923')
cc1 = ContaCorrente(5000, 200000, cl1)

user01= User('Marcus', 'Aloise', 'marcus.aloise@gmail.com', 'eUmesmo0102030405060708090')

cc1.show_client()

print(cl1.__dict__)