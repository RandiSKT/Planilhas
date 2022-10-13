import pandas as pd

#Entradas do usuário, endereço do arquivo csv e Coluna a ser alterada
arquivo = input("Coloque o endereço do arquivo csv:")
erro = input('Coloque o nome da coluna ser alterada: ')

#Leitura do csv
csv = pd.read_csv(arquivo)

#Variaveis para lógica de programação
x = 0
y = 0

#Laço de repetição que transforma todas as leetras em minusculas
while y < len(csv[erro]):
  csv[erro][x] = csv[erro][x].lower()
  x += 1
  y+= 1

#Entrada do Usuário de qual coluna checar por repetidos
repete = input("Qual coluna quer checar por repetidos:")

#Devolve o csv alterado
print(csv)

#Cria lista bopoleana indicando quais são os duplicados
list = csv[repete].duplicated()

#Utilizado para lógica
x = 0

#Devolve indice e Valor da repetição
for a in list:
  if a==True:
    print(x,'-', csv[repete][x] )
    x+=1
  else:
    x+=1

  
