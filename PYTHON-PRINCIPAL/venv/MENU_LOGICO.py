# Importando as bibliotecas das funções para cadastro no banco de dados
from MOD_CADAST import cad_vendedor
from MOD_CADAST import cad_cliente
from MOD_CADAST import cad_produto
from MOD_CADAST import cad_transportadora
from MOD_PEDIDO import pedido
# Título do sfotware
print('\033[34mBEM VINDO AO ACE v1.0!\033[m')
while True:
    try:
        menu = 0
# Menu pricipal
        print('\033[36mDigite um dos números do menu a qual deseja ter acesso:\033[m')
        print('\033[32m[1] PARA CADASTRO DE CLIENTE')
        print('[2] PARA CADASTRO DE PRODUTO')
        print('[3] PARA CADASTRO DE VENDEDOR')
        print('[4] PARA CADASTRO DE TRANSPORTADORA')
        print('[5] PARA ELABORAR PEDIDO')
        print('[6] PARA FINALIZAR')

        menu = int(input('\033[33mDigite um numero: \033[m'))
# logicas para execução dos modulos importados. Cada número irá representar uma função
        if menu == 6:
            break
        elif menu == 3:
            cad_vendedor()
        elif menu == 1:
            cad_cliente()
        elif menu == 4:
            cad_transportadora()
        elif menu == 2:
            cad_produto()
        elif menu == 5:
            pedido()
# Tratamentos de erros e exceções
        else:
            print('\033[31mOpção inválida!\033[m')
    except:
        print('\033[31mOpção inválida!\033[m')