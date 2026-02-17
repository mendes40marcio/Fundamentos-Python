class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian', 'Robert', 'Rossana', 'Ana']

    def Iniciar(self):
        print('Olá bem vindo a este site!')
        emails_apresentacao = self.MontarCredencial(self.pessoas)
        for email in emails_apresentacao:
            print(email)

    def MontarCredencial(self, pessoas):
        credenciais = []
        for pessoa in pessoas:
            credenciais.append(
                f'A empresa gostaria de dar as boas vindas para o(a) {pessoa}'
            )
        return credenciais


email = EmailDeBoasVindas()
email.Iniciar()
