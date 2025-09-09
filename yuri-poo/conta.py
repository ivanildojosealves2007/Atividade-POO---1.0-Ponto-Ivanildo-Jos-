class Conta:
    def __init__(self, agencia, tipo, numero, saldo, cliente):
        self.agencia = agencia
        self.tipo = tipo
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        
    def exibir_dados_conta(self):
        print("Dados da Conta:")
        print(f"Sua agência é: {self.agencia}")
        print(f"O tipo da conta é: {self.tipo}")
        print(f"O número da conta: {self.numero}")
        print(f"O saldo disponível: {self.saldo:.2f}")