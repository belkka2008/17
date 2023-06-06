try:
    arr = list(map(int, input("Введите числа через пробел").split()))
    numb = int(input("Введите число"))
except ValueError:
    print('Это не число.')
arr.append(numb)
for i in range(len(arr)):
    idx_min =i
    for j in range(i, len(arr)):
        if arr[j] < arr[idx_min]:
            idx_min = j
    if i != idx_min:
        arr[i], arr[idx_min] = arr[idx_min], arr[i]
if arr.index(numb) > 0 and arr.index(numb)+1 != len(arr):
    print('Номер позиции элемента, который меньше введенного пользователем числа:', arr.index(numb)-1)
else:
    print('Число не соответствует условию')
