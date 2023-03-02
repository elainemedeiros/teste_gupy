# Definindo o vetor com os valores de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

#Calculando o valor total mensal de todos os estados
total = sum(faturamento.values())

#Calculando e imprimindo o percentual equivalente a cada estado (formatado com duas casas decimais)
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(estado, "-", "{:.2f}".format(percentual), "%")