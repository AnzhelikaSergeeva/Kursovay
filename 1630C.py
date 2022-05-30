# Дано n элементов, пронумерованных от 1 до n. Элемент i имеет значение ai и цвет ci.
# Изначально ci=0 для всех i.
# Можно выполнять следующую операцию: Выбрать три элемента i, j и k (1≤i<j<k≤n) такие,
# что ci, cj и ck равны 0 и ai=ak, и затем присвоить cj=1.
# Найдите максимальное значение сумму ci, которое можно получить,
# выполнив описанную операцию некоторое (любое) количество раз.

n = int(input())
a = [int(i) for i in input().split()]

last = {x: i for i, x in enumerate(a)}
# print(last)

lastest, covered, summa = 0, 0, 0
for i, x in enumerate(a):
    lastest = max(lastest, last[x])
    if covered > i:
        summa += 1
    else:
        covered = lastest

print(summa)