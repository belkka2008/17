money = int (input('Введите сумму:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
A = per_cent.get('ТКБ')
Bank1 = money*A/100
B = per_cent.get('СКБ')
Bank2 = money*B/100
C = per_cent.get('ВТБ')
Bank3 = money*C/100
D = per_cent.get('СБЕР')
Bank4 = money*D/100
deposit = [Bank1, Bank2, Bank3, Bank4]
max_dep=int(max(deposit))
print(list(map(int, deposit)))
print('Максимальная сумма, которую вы можете заработать -',max_dep)
