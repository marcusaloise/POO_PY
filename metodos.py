class Lampada:

    def __index__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        # self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0 

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__valor = valor
        self.__nome = nome
        self.__descricao = descricao
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do Produto com desconto"""
        return(self.__valor * (100 - porcentagem)) / 100

# from passlib.hash import pbkdf2_sha256 as lp

class User:

    counter = 0

    @classmethod
    def user_count(cls):
        print(f'We have {cls.counter} user on system')

    @staticmethod
    def status():
        return 'created'



    def __init__(self, nome, sobrenome, email, senha):
        self.__id = User.counter + 1
        self.__email = email
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__senha = senha
        #self.__senha = lp.hash(senha, round=2000, salt_size=16)
        User.counter = self.__id
        print(f'USer create: {self.__user_generate()}')


    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def chek_pass(self, senha):
        if  senha == self.__senha:
            return True
        return False
    
    def __user_generate(self):
        return self.__email.split('@')[0]
            
    # def chek_pass(self, senha):
    #     if  lp.verify(senha, self.__senha):
    #         return True
    #     return False

    # def __correr__(self, metros):
    #     print(f'{self.__nome} está correndo {metros} metros')




# p1 = Produto('Mesa', 'mesa gamer', 3000)
# print(p1.desconto(50))


user1 = User('Marcus', 'Aloise', 'marcus.aloise@gmail.com', 'eUmesmo0102030405060708090')
user2 = User('Lucas', 'Carvalho', 'lucas.carvalho@gmail.com', '1223344556677889')


print(user1._User__user_generate())

print(User.status())


# # print(user1.nome_completo())
# user1.user_count()
# User.user_count()
# # print(User.nome_completo())
# print(user2.nome_completo())
# print(User.nome_completo(user1))
# print(user1._User__senha)
# print(user2._User__senha)



# name = input('nome: ')
# sobrenome = input('sobrenome: ')
# email = input('email: ')
# senha = input('senha: ')
# confirma_senha = input('Confirma senha: ')

# if senha == confirma_senha:
#     user = User(name, sobrenome, email, senha)
# else:
#     print("senha errada amigão!")

# print('User create with sucess')   

# senha_login = input('Informe senha para acesso: ')
# #user.chek_pass(senha_login)

# if user.chek_pass(senha_login):
#     print('Acesso permetido')
# else:
#     print('Acesso negado')

# print(f'Senha: {user._User__senha}')