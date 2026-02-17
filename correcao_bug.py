import random


class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian', 'Robert', 'Rossana', 'Ana']

    def Iniciar(self):
        print('Olá bem vindo a este site!')  # inicie o debug aqui (breakpoint)
        self.ChutarIdade(self.pessoas)       # pule essa linha no debug
        self.ChutarNome()                    # entre dentro desse método
        self.ChutarCor()                     # entre neste método
        print('Programa finalizado')

    def ChutarCor(self):
        cores = ['azul', 'rosa', 'verde']
        for cor in cores:
            print(f'as opções de cores são: {cor}')

        print('sua cor favorita é...')
        cor_preferida = random.choice(cores)
        print(cor_preferida)

    def ChutarNome(self):
        nome = f'bem vindo {random.choice(self.pessoas)}'
        print(nome)

    def ChutarIdade(self, pessoas):
        # entre aqui
        idade = random.randint(18, 50)
        print(idade)


email = EmailDeBoasVindas()
email.Iniciar()
