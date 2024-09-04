
import datetime

class ContaBancaria:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0.0
        self.extrato = []
        self.transacoes_hoje = 0
        self.limite_transacoes_diarias = 10
        self.ultima_transacao = datetime.date.today()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            self.transacoes_hoje += 1
            self._verificar_limite_transacoes()
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.transacoes_hoje += 1
            self._verificar_limite_transacoes()
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_extrato(self):
        print("\nExtrato Bancário\n")
        for transacao in self.extrato:
            print(transacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")

    def _verificar_limite_transacoes(self):
        data_atual = datetime.date.today()
        if self.transacoes_hoje > self.limite_transacoes_diarias:
            raise Exception(f"Limite de transações diárias ({self.limite_transacoes_diarias}) excedido para hoje.")
        elif data_atual != self.ultima_transacao:
            self.transacoes_hoje = 1
            self.ultima_transacao = data_atual

def menu(conta):
    while True:
        print("\nBem-vindo ao Banco Simples!\n")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver extrato")
        print("4 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            try:
                conta.depositar(valor)
            except Exception as e:
                print(e)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            try:
                conta.sacar(valor)
            except Exception as e:
                print(e)
        elif opcao == '3':
            conta.ver_extrato()
        elif opcao == '4':
            print("Obrigado por usar o banco Simples!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    titular = input("Digite o nome do titular: ")
    numero = input("Digite o número da conta: ")
    conta = ContaBancaria(titular, numero)

    menu(conta)