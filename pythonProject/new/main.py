from conta import ContaCorrente
import time

l = []
c1 = ContaCorrente('miriam',4447,200.00)
c4 = ContaCorrente('Nelza',6009,50000.00)
c2 = ContaCorrente('Carlos',4428,300.00)
c3 = ContaCorrente('Carla',4509,400.00)
c5 = ContaCorrente('Marcos',4169,9900.00)
c6 = ContaCorrente('Mirela',4249,10000.00)
c7 = ContaCorrente('Ranildo',4108,2000.00)
c8 = ContaCorrente('Joao',4349,20000.00)
c9 = ContaCorrente('Silvio',4269,1000000.00)
c10 = ContaCorrente('Severina',4589,4000.00)

l.append(c1)
l.append(c2)
l.append(c3)
l.append(c4)
l.append(c5)
l.append(c6)
l.append(c7)
l.append(c8)
l.append(c9)
l.append(c10)

# compressão de lista
for i in range(len(l)):
    print(f'Conta: {i+1}')
    print(str(l[i]))

while True:
    print(c1.menu_operacao())
    operacao = int(input('Selecione Uma Operacao: '))
    if operacao == 4:
        print('+----------------------------+')
        print('Programa Encerrando...')
        time.sleep(1)
        break
    if operacao < 1 or operacao > 4:
        print('Selecione uma Operação Válida!')
    else:
        number = int(input('Número da conta (sem o digito):'))
        if number == c1.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c1.depositar(deposito)
                print(c1)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c1.sacar(saque)
                print(c1)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c1.nome_titular} ')
                print('Saldo Atual: ',c1.saldo)
                continue
        elif number == c2.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c2.depositar(deposito)
                print(c2)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c2.sacar(saque)
                print(c2)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c2.nome_titular} ')
                print('Saldo Atual: ',c2.saldo)
                continue
        elif number == c3.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c3.depositar(deposito)
                print(c3)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c3.sacar(saque)
                print(c3)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c3.nome_titular} ')
                print('Saldo Atual: ',c3.saldo)
                continue
        elif number == c4.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c4.depositar(deposito)
                print(c4)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c4.sacar(saque)
                print(c4)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c4.nome_titular} ')
                print('Saldo Atual: ',c4.saldo)
                continue
        elif number == c5.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c5.depositar(deposito)
                print(c5)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c5.sacar(saque)
                print(c5)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c5.nome_titular} ')
                print('Saldo Atual: ',c5.saldo)
                continue
        elif number == c6.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c6.depositar(deposito)
                print(c6)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c6.sacar(saque)
                print(c6)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c6.nome_titular} ')
                print('Saldo Atual: ',c6.saldo)
                continue
        elif number == c7.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c7.depositar(deposito)
                print(c7)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c7.sacar(saque)
                print(c7)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c7.nome_titular} ')
                print('Saldo Atual: ',c7.saldo)
                continue
        elif number == c8.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c8.depositar(deposito)
                print(c8)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c8.sacar(saque)
                print(c8)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c8.nome_titular} ')
                print('Saldo Atual: ',c8.saldo)
                continue
        elif number == c9.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c9.depositar(deposito)
                print(c9)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c9.sacar(saque)
                print(c9)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c9.nome_titular} ')
                print('Saldo Atual: ',c9.saldo)
                continue
        elif number == c10.numero:
            print('Conta Verificada!')
            if operacao == 1:
                deposito = float(input('Deposito: '))
                c10.depositar(deposito)
                print(c10)
                continue
            elif operacao == 2:
                saque = float(input('Valor de Saque: '))
                c10.sacar(saque)
                print(c10)
                continue
            elif operacao == 3:
                print('+------------------------------+')
                print(f'Titular: {c10.nome_titular} ')
                print('Saldo Atual: ',c10.saldo)
                continue
        else:
            print('\nNúmero Da Conta Inexistente! Tente Novamente...')
