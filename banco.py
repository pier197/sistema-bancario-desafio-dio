
class ContaBancaria:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_extrato(self):
        print("\nExtrato Bancário\n")
        for transacao in self.extrato:
            print(transacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")

def menu():
    print("\nBem-vindo ao Banco Simples!\n")
    while True:
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver extrato")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == 3:
            conta.ver_extrato()
        elif opcao == 4:
            print("Obrigado por usar o banco Simples!")
            break
        else:
            print("Opção inválida.")

# Criando uma conta
titular = input("Digite o nome do titular da conta: ")
numero = input("Digite o número da conta: ")
conta = ContaBancaria(titular, numero)

# Iniciando o menu
menu()