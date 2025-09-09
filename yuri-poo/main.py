from cliente import Cliente
from conta import Conta
import acoes

cliente1 = Cliente(
    nome="Lavinia",
    sobrenome="Soares",
    cpf="123.456.789-00",
    email="laviniasoares@gmail.com",
    telefone="(81)93458910"
)

conta1 = Conta(
    agencia="0001",
    tipo="Corrente",
    numero="12345-6",
    saldo=1500.00,
    cliente=cliente1
)

acoes.exibir_saldo(conta1)
acoes.exibir_dados_pessoais(conta1)
acoes.exibir_dados_conta(conta1)