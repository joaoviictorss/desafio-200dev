import csv
from datetime import datetime

def calcular_idade(data_nasc):

  # Converte a string em datetime
  data_nasc_obj = datetime.strptime(data_nasc, "%Y-%m-%d")
  data_atual = datetime.now()

  idade = data_atual.year - data_nasc_obj.year

  # Verificação se o aniversario ja ocorreu neste ano
  if (data_atual.month, data_atual.day) < (data_nasc_obj.month, data_nasc_obj.day):
    idade -= 1
  return idade

age = calcular_idade('2004-01-31')
print(f"A idade é: {age} anos")

# # Erro usando o encoding= 'utf-8'

# with open ('people.csv', encoding='utf-8') as csvfile:

#   leitor = csv.reader(csvfile)
#   for row in leitor:
#     print(row)

with open ('people.csv', encoding='utf-8-sig') as csvfile:

  # Cria o objeto de leitura
  leitor = csv.DictReader(csvfile)

  quantidade_maiores_18 = 0
  dados_maiores_18 = []

  for row in leitor:
    idade = calcular_idade(row['birthday'])
    if idade > 18:
      quantidade_maiores_18 += 1
      dados_maiores_18.append((row['name'], idade))

  # Guarda em uma lista os nomes e a idade de quem tem mais de 18 anos
  dados_maiores_18.sort()
  print(dados_maiores_18)

with open('maiores_18.txt', 'w', encoding='utf-8-sig') as txtfile:
    txtfile.write(f"Existem {quantidade_maiores_18} pessoas maiores de 18 anos.\n")
    for nome, idade in dados_maiores_18:
        txtfile.write(f"{nome} tem mais {idade - 18} anos.\n")