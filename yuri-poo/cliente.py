class Cliente:
    def __init__(self, nome, sobrenome, cpf, email, telefone):
        self.nomecompleto = nome + ' ' + sobrenome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        
    def exibir_dados_pessoais(self):
        print("Dados pessoais: ")
        print(f"Nome: {self.nomecompleto} ")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")