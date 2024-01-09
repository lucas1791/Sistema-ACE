import pyodbc # Biblioteca que iremos utilizar em noso projeto para trabalhar com o banco de dados no Python.
from datetime import date # Biblioteca para utilizar o tipo de dados tempo (datetime)


def pedido():
    dados = (
        "Driver={SQL Server};" # Comunicação com o banco de dados SQL Server
        "Server=DESKTOP-ROVUD1F\SQLEXPRESS;" # Edereço do servior do meu banco de dados
        "Database=ACE;" # Nome do banco de dados
    )
    conet = pyodbc.connect(dados) # Conectando ao banco de dados
    print('FORMULAÇÃO DE PEDIDO')

    cursor = conet.cursor() # Cursor para executar comandos em SQL

    data_pedido = date.today() # Definindo a data atual
    data_pedido_str = data_pedido.strftime('%Y-%m-%d')

# Cadastro de dados da tabela pedido
    num_pedid = int(input('Digite o número do pedido: '))
    cod_cliente = int(input('Digite um número para o código do cliente: '))
    cod_vendedor = int(input('Digite qual o codigo do vendedor: '))
    co_produto = int(input('Digite o codigo do produto: '))
    qt_produto = int(input('Digite a quantidade: '))
    forma_pgto = input('Qual a forma de pagamento? ')
    prazo = input('Qual o prazo de entrega? ')
    co_transp = int(input('Digite o codigo da transportadora: '))

    cursor.execute("SELECT preco FROM produto WHERE cod_produto = ?", co_produto)
    roww = cursor.fetchone()
    if roww:
        preco_produto = roww.preco
    else:
        print("Produto não encontrado!")
        cursor.close()
        conet.close()
        exit()

    valor_total = preco_produto * qt_produto

# Cálculo para multiplicar a quantidade de produtos.
    comando = f"""INSERT INTO pedido(num_pedido, data_tempo, cod_cliente, cod_vendedor, cod_produto, qt_produto, 
    valor_total, forma_pgto, prazo_entrega, cod_transp )
    VALUES ({num_pedid}, {data_pedido_str}, {cod_cliente}, {cod_vendedor}, {co_produto}, {qt_produto}, {valor_total}, '{forma_pgto}', '{prazo}', {co_transp})"""

    cursor.execute(comando)
    cursor.commit()
    print('Pedido concluído')

# Comando join para juntar as informações de tabelas diferentes
    cursor.execute("""select p.num_pedido, p.data_tempo, c.cod_cliente, c.nome_razao, c.cpf_cnpj, c.rua, c.numero, 
    c.bairro, c.cidade, c.estado, c.cep, c.telefone, c.email,
    v.cod_vendedor, po.cod_produto, po.nome_produto, po.preco, p.qt_produto, 
    p.valor_total, p.forma_pgto, p.prazo_entrega, t.cod_transp, t.nome_transp
    from pedido p
    inner join	cliente c on c.cod_cliente = p.cod_cliente
    inner join	vendedor v on v.cod_vendedor = p.cod_vendedor
    inner join	produto po on po.cod_produto = p.cod_produto
    inner join	transportadora t on t.cod_transp = p.cod_transp
    where p.num_pedido = ?""", num_pedid)

# printando na tela as informações
    row = cursor.fetchone()
    if row:
        print('DADOS: ')
        print("NUMERO DO PEDIDO:", row.num_pedido)
        print("DATA DO PEDIDO:", row.data_tempo)
        print("CODIGO DO CLIENTE:", row.cod_cliente)
        print("NOME/RAZÃO SOCIAL:", row.nome_razao)
        print("CPF/CNPJ:", row.cpf_cnpj)
        print("ENDEREÇO:")
        print("RUA:", row.rua)
        print("NÚMERO:", row.numero)
        print("BAIRRO:", row.bairro)
        print("CIDADE:", row.cidade)
        print("ESTADO:", row.estado)
        print("CEP:", row.cep)
        print("TELEFONE:", row.telefone)
        print("EMAIL:", row.email)
        print("CODIGO DO VENDEDOR:", row.cod_vendedor)
        print("NOME DO PRODUTO:", row.nome_produto)
        print("CODIGO DO PRODUTO:", row.cod_produto)
        print("VALOR DO PRODUTO:", row.preco)
        print("QUANTIDADE DO PRODUTO:", row.qt_produto)
        print("VALOR TOTAL:", row.valor_total)
        print("FORMA DE PAGAMENTO:", row.forma_pgto)
        print("PRAZO DE ENTREGA:", row.prazo_entrega)
        print("NOME DA TRANSPORTADORA:", row.nome_transp)
        print("CODIGO DA TRANSPORTADORA:", row.cod_transp)
        print()
        print('PEDIDO EMITIDO COM SUCESSO!')


    else:
        print("Cliente não encontrado!")

    cursor.close()
    conet.close()