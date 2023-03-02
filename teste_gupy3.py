import json

#Abrindo o arquivo JSON
with open('dados.json') as arquivo_json:
    # Carregando o vetor de dados utilizando o arquivo
    dados = json.load(arquivo_json)

#Filtrando os dias com valor não-zero
dados_filtrado = [d for d in dados if d['valor'] != 0.0]

#Encontrando o menor valor de faturamento diário (formatado com duas casas decimais)
menor_faturamento = min([d['valor'] for d in dados_filtrado])
print("O menor valor de faturamento ocorrido em um dia do mês é: R$", "{:.2f}".format(menor_faturamento))

#Encontrando o maior valor de faturamento diário (formatado com duas casas decimais)
maior_faturamento = max([d['valor'] for d in dados_filtrado])
print("O maior valor de faturamento ocorrido em um dia do mês é: R$", "{:.2f}".format(maior_faturamento))

#Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal

#Iniciando as variáveis
soma_faturamento = 0
dias_com_faturamento = 0

#Incluindo os valores nas variáveis soma_faturamento e dias_com_faturamento
for dia in dados:
    if dia['valor'] != 0.0:
        soma_faturamento += dia['valor']
        dias_com_faturamento += 1

#Calculando a média mensal (formatada com duas casas decimais)
media_mensal = soma_faturamento / dias_com_faturamento
print("A média mensal de faturamento diário é: ", "{:.2f}".format(media_mensal))

#Calculando a quantidade de dias em que o faturamento diário foi maior que a média do faturamento mensal
contagem = 0
for dia in dados:
    if dia['valor'] > media_mensal:
        contagem += 1
print("O número de dias no mês em que o valor de faturamento diário foi superior à média mensal é: ", contagem)


