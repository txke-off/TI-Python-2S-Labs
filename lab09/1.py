import numpy as np
import matplotlib.pyplot as plt

# Задаем диапазон значений n
n = np.linspace(1, 6, 100)

# Определяем функции сложности
O1 = np.ones_like(n)           # O(1)
O_log = np.log(n)               # O(log n)
O_n2 = n**2                     # O(n^2)
O_2n = 2**n                    # O(2^n)

# Построение графика
plt.figure(figsize=(10,6))
plt.plot(n, O1, label="O(1)")
plt.plot(n, O_log, label="O(log n)")
plt.plot(n, O_n2, label="O(n^2)")
plt.plot(n, O_2n, label="O(2^n)")
plt.xlabel("n (количество элементов)")
plt.ylabel("количество шагов (условные единицы)")
plt.title("Сравнение асимптотической сложности алгоритмов")
plt.legend()
plt.yscale("log")  # Логарифмическая шкала по оси Y для лучшей наглядности
plt.grid(True)
plt.show()