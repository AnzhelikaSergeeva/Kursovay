# Дано число n. Найдите минимальное целое число x такое, что x≥n и x является k-красивым числом.
# Число называется k-красивым, если в его десятичной записи, не содержащей лидирующих нулей,
# встречается не более k различных цифр. Например, если k=2, числа 3434443, 55550, 777 и 21
# являются k-красивыми, а числа 120, 445435 и 998244353 — нет.

t = int(input())
some_list = []
for i in range(t):
    some_list.append(input())
for i in range(t):
    n_k = some_list[i].split()
    n = int(n_k[0])
    k = int(n_k[1])
    x = n
    while len(set(str(n))) > k:
        if n % 10 == 0:
            n = n // 10
        else:
            n += 1
    end = str(min(str(n))) * (len(str(x)) - len(str(n)))
    print(int(str(n) + end))




