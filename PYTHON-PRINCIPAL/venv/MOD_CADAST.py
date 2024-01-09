# Criando a função para a conexão com o banco de dados e executar o cadastro das entidades.
import pyodbc # Biblioteca que iremos utilizar em noso projeto para trabalhar com o banco de dados no Python.
def cad_vendedor():
    '''
    Essa função é responsvel pela comunicação com o Banco de dados,
    para que haja o cadastro de informações na coluna determinada abaixo
    :return: Retorna solicitação de entrada de dados para o cadastro no banco de dados
    '''
    dados = (
        "Driver={SQL Server};"  # Comunicação com o banco de dados SQL Server
        "Server=DESKTOP-ROVUD1F\SQLEXPRESS;" # Edereço do servior do meu banco de dados
        "Database=ACE;" # Nome do banco de dados
    )
    conet = pyodbc.connect(dados) # Conectando ao banco de dados
    print('CADASTRO DE VENDEDOR')

    cursor = conet.cursor() # Cursor para executar comandos em SQL
    co_vendedor = int(input('Digite o codigo do vendedor: '))
    nom_vendedor = input('Digite o nome do vendedor: ')
    comando = f"""INSERT INTO vendedor(cod_vendedor, nome_vendedor)
    VALUES ({co_vendedor}, '{nom_vendedor}')"""

    cursor.execute(comando)
    cursor.commit()
    print('Cadastro concluído')



#Abaixo outras funções com o mesmo propósito da anterior, mas cada uma com sua tabela.

def cad_transportadora():
    dados = (
        "Driver={SQL Server};"
        "Server=DESKTOP-ROVUD1F\SQLEXPRESS;"
        "Database=ACE;"
    )
    conet = pyodbc.connect(dados)
    print('CADASTRO DE TRANSPORTADORA')

    cursor = conet.cursor()
    co_transp = int(input('Digite o codigo da transportadora: '))
    nom_transp = input('Digite o nome da transportadora: ')
    comando = f"""INSERT INTO transportadora(cod_transp, nome_transp)
    VALUES ({co_transp}, '{nom_transp}')"""

    cursor.execute(comando)
    cursor.commit()
    print('Cadastro concluído')


def cad_produto():
    dados = (
        "Driver={SQL Server};"
        "Server=DESKTOP-ROVUD1F\SQLEXPRESS;"
        "Database=ACE;"
    )
    conet = pyodbc.connect(dados)
    print('CADASTRO DE PRODUTO')

    cursor = conet.cursor()
    co_produto = int(input('Digite o codigo do produto: '))
    nom_produto = input('Digite o nome do produto: ')
    tip_produto = input('Digite o tipo do produto: ')
    fabricant = input('Digite o fabricante (marca) do produto: ')
    prec = float(input('Digite o preço do produto: '))
    cust = float(input('Digite o custo do produto: '))
    comando = f"""INSERT INTO produto(cod_produto, nome_produto, tipo_produto, fabricante, preco, custo)
    VALUES ({co_produto}, '{nom_produto}', '{tip_produto}', '{fabricant}', {prec}, {cust} )"""

    cursor.execute(comando)
    cursor.commit()
    print('Cadastro concluído')



def cad_cliente():
    dados = (
        "Driver={SQL Server};"
        "Server=DESKTOP-ROVUD1F\SQLEXPRESS;"
        "Database=ACE;"
    )
    conet = pyodbc.connect(dados)
    print('CADASTRO DE CLIENTE')

    cursor = conet.cursor()
    cod_cliente = int(input('Digite um número para o código do cliente: '))
    nome_razao = input('Digite o nome ou razão social do cliente: ')
    cpf_cnpj = input('Digite o CPF ou CNPJ do cliente: ')
    cod_vendedor = int(input('Digite qual o codigo do vendedor: '))
    rua = input('Digite o nome da rua: ')
    numero = input('Digite o número: ')
    bairro = input('Digite o nome do bairro: ')
    cidade = input('Digite o nome da cidade: ')
    estado = input('Digite a UF do estado: ')
    cep = input('Digite o cep: ')
    telefone = input('digite o numero do telefone: ')
    email = input('digite o e-mail: ')

    comando = f"""INSERT INTO cliente(cod_cliente, nome_razao, cpf_cnpj, cod_vendedor, rua, numero, bairro, cidade, estado, 
    cep, telefone, email) VALUES ({cod_cliente},'{nome_razao}', '{cpf_cnpj}', {cod_vendedor}, '{rua}', '{numero}', '{bairro}', '{cidade}', '{estado}', 
    '{cep}', '{telefone}', '{email}')"""

    cursor.execute(comando)
    cursor.commit()
    print('Cadastro concluído')