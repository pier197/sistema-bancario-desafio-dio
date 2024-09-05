import datetime

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, titular, numero, agencia):
        self.titular = titular
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0.0
        self.extrato = []
        self.data_abertura = datetime.date.today()

    def depositar(self, valor):
        # ...

     def sacar(self, valor):
        # ...

       def extrato(self):
        # ...

          if __name__ == "__main__":
            banco = Banco()  # Criar um objeto Banco para gerenciar clientes e contas

    while True:
        print("1 - Criar cliente")
        print("2 - Criar conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Extrato")
        print("6 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            # Criar um cliente
            pass
        elif opcao == '2':
            # Criar uma conta
            pass
        # ... outras opções