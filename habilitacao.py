rodas = int(input('Quantas rodas tem o veículo?'))
peso = float(input('Quanto pesa o veiculo?'))
pessoas = int(input('Quantas pessoas cabem no veículo?'))

if rodas < 4 and pessoas < 3:
    print('A melhor categoria de habilitação pra você será a: A')
elif rodas ==4 and pessoas <=8 and peso <=3500:
    print ('A melhor categoria de habilitação pra você será a: B')
elif rodas >= 4 and peso >= 3500 and peso <= 6000:
    print('A melhor categoria de habilitação pra você será a: C')
elif rodas >= 4 and pessoas > 8:
    print('A melhor categoria de habilitação pra você será a:D')
elif rodas >= 4 and peso >= 6000:
    print('A melhor categoria de habilitação pra você será a:E')