class ContaBancaria:
    def __init__(self, titular, tipo, agencia, conta, saldo):
        self.titular = titular
        self.tipo = tipo
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def exibirDadosConta(self):
        print(f'titular: {self.titular}')
        print(f'Tipo de Conta: {self.tipo}')
        print(f'Agência: {self.agencia}')
        print(f'Numero conta: {self.conta}')
        print(f'Saldo: {self.saldo}')

    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo insulficiente")
        else:
            self.saldo -= valor  # saldo = saldo-valor
            print(f"Saque realizado com sucesso {valor} saldo atual: {self.saldo}")

    def depositar(self, valor):
        if valor < 0:
            print("O valor precisa ser maior que zero")
        else:
            self.saldo += valor
            print(f'O deposito de {valor} foi realizado com sucesso, novo saldo {self.saldo}')


if __name__ == '__main__':
    conta1 = ContaBancaria("Davi", "Conta Corrente", "001", 201212, 500)
    conta2 = ContaBancaria("Ok", "Conta Poupanca", "001", 212, 1000)
    conta3 = ContaBancaria("Teste", "Conta Corrente", "001", 2, 2000)

    conta1.exibirDadosConta()
    conta1.saque(100)
    conta1.depositar(1000)
