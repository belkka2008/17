ticket_count  = int(input("При покупке от 4-х билетов действует скидка 10% от стоимости заказа!\n"
                   "Введите количество билетов, которое хотите приобрести на мероприятие:"))
ages = input("Укажите через пробел возраст посетителей: ").split()

total_cost = 0

for age in ages:
    if int(age) < 18:
        total_cost += 0
    elif 18 <= int(age) < 25:
        total_cost += 990
    else:
        total_cost += 1390
if ticket_count > 3:
  total_cost *= 0.9

print("Общая стоимость билетов:", total_cost, "руб.")


