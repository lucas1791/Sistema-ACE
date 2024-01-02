from MOD_CADAST import cad_vendedor
from MOD_CADAST import cad_cliente
from MOD_CADAST import cad_produto
from MOD_CADAST import cad_transportadora
print('BEM VINDO AO ACE v1.0!')
print('Digite um dos números do menu a qual deseja ter acesso:')
print('[1] PARA CADASTRO DE CLIENTE')
print('[2] PARA CADASTRO DE PRODUTO')
print('[3] PARA CADASTRO DE VENDEDOR')
print('[4] PARA CADASTRO DE TRANSPORTADORA')
print('[5] PARA ELABORAR PEDIDO')
x = int(input('Digite um numero: '))
if x == 3:
    cad_vendedor()
elif x == 1:
    cad_cliente()
elif x == 4:
    cad_transportadora()
elif x == 2:
    cad_produto()