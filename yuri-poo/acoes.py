def exibir_saldo(conta):
    print("O saldo Atual:")
    print(f"Saldo: R$ {conta.saldo:.2f}")
    
def exibir_dados_pessoais(conta):
    conta.cliente.exibir_dados_pessoais()
    
def exibir_dados_conta(conta):
    conta.exibir_dados_conta()