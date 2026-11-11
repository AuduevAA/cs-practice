import numpy as np

print("--- Задание 1. Создание векторов и матриц ---")
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print()


print("--- Задание 2. Индексы и срезы в векторе ---")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])
print()


print("--- Задание 3. Строки и столбцы таблицы ---")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Значение из 2-й строки и 3-го столбца:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[0:2, 1:3])
print()


print("--- Задание 4. Прямоугольные срезы ---")
matrix = np.arange(1, 26).reshape(5, 5)

first_three = matrix[:3, :]
print("Первые три строки:\n", first_three, "\nshape:", first_three.shape)

last_two = matrix[-2:, :]
print("Последние две строки:\n", last_two, "\nshape:", last_two.shape)

first_two_cols = matrix[:, :2]
print("Первые два столбца:\n", first_two_cols, "\nshape:", first_two_cols.shape)

fragment = matrix[1:4, 2:5]
print("Фрагмент из строк 1–3 и столбцов 2–4:\n", fragment, "\nshape:", fragment.shape)

corner = matrix[-2:, -2:]
print("Угловой блок 2x2:\n", corner, "\nshape:", corner.shape)
print()


print("--- Задание 5. Изменение массива с помощью срезов ---")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("исходный hours:", hours)
"""
Комментарий: .copy() нужен, чтобы не изменить исходный массив hours. 
Без него changed_hours был бы просто ссылкой на те же данные в памяти, 
и изменения в changed_hours испортили бы исходный hours.
"""

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Итоговая changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)
print()


print("--- Задание 6. Изменение формы ---")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)

"""
Комментарий: reshape(3, 4) работает, потому что 3 * 4 = 12, 
что совпадает с общим числом элементов в исходном массиве numbers.
reshape(5, 3) вызовет ошибку, так как 5 * 3 = 15, а элементов всего 12. 
NumPy не может создать матрицу, где не хватает элементов.
"""