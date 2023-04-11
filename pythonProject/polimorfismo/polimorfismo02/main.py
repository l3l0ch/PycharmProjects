from administrador import *
from fornecedor import *
from operario import *
from vendedor import *

fornecedor = Fornecedor('Carlos','R. Amaro, N 20',83988888888, 20_000.00, 40_000.00)
# print(fornecedor)
# print("Saldo: ",fornecedor.obterSaldo())

operario = Operario ( 'Marcos', 'R. Francisco, N 100', 88828314, 1, 2000.00, 0.2, 10_000, 5 )
# print ( operario )
# # print ('valor monetário dos artigos: ', operario.valor_producao )
# print ( 'Salário: ', operario.calcularSalario () )

vendedor = Vendedor('Lucas','R. Melo, N 300',9888320090, 1,2000.00, 0.2, 20000, 5)
# print(vendedor)
# print('        Salário + comissão: ',vendedor.calcularSalario())

adm = Administrador ( 'Andrezza', 'R. Francisco, N 100', 988820965, 1, 2000.00, 0.2, 1000.00 )
# print ( adm )
# print ( 'Salário Descontado: ', adm.calcularSalario () )
# print ( 'Salario Com ajuda de custos: ', adm.calcularSalario () )
for pessoas in [operario, vendedor, adm]:
    print(pessoas,f'\nSalário + benefícios:{pessoas.calcularSalario()}')