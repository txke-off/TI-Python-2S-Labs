n = 100
for i in range(n):
    print(i)
# Цикл проходит от 0 до n–1, поэтому сложность — O(n)

n = 100
for i in range(n):
    for j in range(n):
        print(i, j)
# Внешний цикл — n итераций, внутренний — n итераций, итого O(n^2)

n = 100
x = 5 + 3
print(x)
# Операция сложения и вывод выполняется один раз, сложность — O(1)

n = 100
sum = 0
for i in range(n):
    for j in range(i, n):
        sum += 1
print(sum)
# Внутренний цикл зависит от i (число итераций равно n–i), суммарное число итераций ~ n(n+1)/2, то есть сложность - O(n^2)

n = 100
result = 0
for i in range(n):
    result += i
print(result)
# Простой цикл с суммированием, сложность — O(n)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
# Рекурсивный вызов происходит n раз, сложность — O(n)

n = 100
count = 0
i = 1
while i <= n:
    count += 1
    i *= 2
print(count)
# Переменная i удваивается каждый раз, количество итераций ≈ log₂(n), сложность — O(log n)