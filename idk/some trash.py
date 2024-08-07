# Нейронная сеть из одного нейрона, чтобы уаааэээ

import numpy as np

# Это моя функция активации хе-хе
# Она нужна для нелинейности и преобразования входных значений в интервал от 0 до 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# А это мой очень большой массив тренировочных данных
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

# Целевые выходные значения. метод Т для транспонирования
training_outputs = np.array([[0,1,1,0]]).T

# Хуярим рандомные веса и определенный сид для повторяемости результатов!
np.random.seed(1)
weights = 2 * np.random.random((3,1)) - 1

# Зафиксировали
print("starting weights:")
print(weights)

# Цикл обучения
for i in range(20000):
    input_layer = training_inputs # Подаем наш бальшой-пребальшой тренировочный сет на вход
    outputs = sigmoid(np.dot(input_layer, weights)) # Вычисление выходных значений

    err = training_outputs - outputs # Вычисляется ошибка (разница между целевыми и предсказанными значениями)

    # Вычисляются корректировки весов. Ошибка умножается на производную сигмоиды, чтобы учесть нелинейность.
    # Затем результат умножается на входные данные (транспонированные), чтобы распространить ошибку обратно через сеть.
    adjustments = np.dot( input_layer.T, err*(outputs*(1 - outputs)) )

    # Корректируем веса
    weights += adjustments

# Вывод финальных весов
print("weights after e:")
print(weights)

# Вывод финальных показаний
print("answers after e:")
print(outputs)