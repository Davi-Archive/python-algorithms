class ContaBancaria:
    def __init__(self, tipo, agencia, conta):
        self.tipo = tipo
        self.agencia = agencia
        self.conta = conta

    def exibirDadosConta(self):
        print(f'Tipo de Conta: {self.tipo}')
        print(f'Agência: {self.agencia}')
        print(f'Numero: {self.conta}')

if __name__ == '__main__':
    conta1 = ContaBancaria("Conta Corrente","001",201212)
    conta2 = ContaBancaria("Conta Poupanca","001",212)
    conta3 = ContaBancaria("Conta Corrente","001",2)

    conta1.exibirDadosConta()
    conta2.exibirDadosConta()
    conta3.exibirDadosConta()