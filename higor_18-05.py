cliente={}#Lista que vai guardar os clientes cadastrados

print('\nSeja bem-vindo(a) ao Café da Tia Joana!\n')

#Loop de Cadastro
while True:
  cpf=int(input("Digite seu CPF:"))   #Solicita o CPF do usuário

  if cpf in cliente:
    #Se o cpf já estiver cadastrado, deseja boas vindas de volta
    print(f"\nSeja bem vindo(a) de volta!")
    break
  else:
    #se não estiver cadastrado, oferece desconto para se cadastrar
    print("\nVocê ainda não está cadastrado(a)\nDeseja realizar seu cadastro e ganhar 10% de desconto?")
    resposta = int(input("\n[1]SIM\n[2]NAO\n"))

    if resposta == 1:
      nome = input("\nDigite seu nome:")
      cliente[cpf] = nome #cadastra um novo cliente e amrazena o cpf e o nome
      print("\nCadastro Realizado")
      print(f"\nSeja bem vindo(a) {nome}!")
      break
    else:
      #se o cliente optar por não se cadastrar, pula para o cardápio
      print("\nCadastro não realizado\nSeja Bem-Vindo(a)")
      break

#dicionários dentro de dicionários para o cardápio
cardapio = {
    1:{'nome':'Pão de Queijo R$1,00','preco':1.00},
    2:{'nome':'Pão de Françês R$1,00','preco':1.00},
    3:{'nome':'Misto Quente R$4,00','preco':4.00},
    4:{'nome':'Pão com Ovo R$4,00','preco':4.00},
    5:{'nome':'Sanduiche Natual R$5,00','preco':5.00},
    6:{'nome':'Café R$1,00','preco':1.00},
    7:{'nome':'Pingado R$2,00','preco':2.00},
    8:{'nome':'Suco de Laranja R$6,00','preco':6.00},
    9:{'nome':'Coca-Cola 600ml R$7,00','preco':7.00}
}

print("\n----------Cardápio----------\n")

total = 0   #acumula o total do pedido

for codigo,item in cardapio.items():    #exibe o cardápio
    print(f'{codigo} - {item['nome']}')
print('0 - Sair\n')

while True:   #loop para escolher o pedido
    pedido = int(input("Digite o número do item ou 0 para sair: "))
    if pedido==0:
        break   #finaliza o pedido
    
    if pedido in cardapio: #usuário escolhe a quantidade
        quantidade = int(input(f'Quantidade: '))
        valor_item = cardapio[pedido]['preco'] * quantidade #multiplica o valor do item pela quantidade
        total+=valor_item #soma o valor do item e a quantidade ao total
    
    else:   #caso a opção seja inválida
        print('Pedido inválido, tente novamente\n')

if cpf in cliente:  #aplica desconto para clientes cadastrados
   print(f'Total:{total}')
   desconto = total*0.1 #10% de desconto
   total-=desconto
   print(f'\nTotal com desconto: {total}')
else: #valor sem o desconto
   print(f'\nTotal: R${total:.2f}\n')

print("\n-----Forma de Pamento-----\n")

    #opções de pagamento
payform = [
    '1 - Dinheiro','2 - Cartão'
]
for pay in payform:
    print(f'{pay}')

    #loop para escolher a forma de pagamento
while True:
    pagamento =int(input("\nForma de pagamento:\n"))

    if pagamento == 1:    #pagamento em dinheiro
        dinheiro = float(input("\nQuantidade em dinheiro: "))
        if dinheiro < total:  #Caso o dinheiro seja insuficiente
           print("\nQuantidade insuficiente, selecione outra forma de pagamento")  #solicita outra forma de pagamento
        else:
          troco = dinheiro - total
          print(f'\nTroco: {troco:.2f}')  #Informa o troco do usuário
          break
    elif pagamento == 2:    #pagamento em cartão
        cartao = int(input('\n1 - Débito\n2 - Crédito:'))
        print('\nInsira ou aproxime o cartão')
        print('Transação aprovada!')
        break
    else:
        print('\nNúmero inválido, tente novamente\n') #caso formaa de pagemento seja inválida
    print("\nTenha um ótimo dia, volte sempre!\n")