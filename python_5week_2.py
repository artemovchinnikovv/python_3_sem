import numpy as np
import matplotlib.pyplot as plt

# Определение целевого распределения
def target_distribution(x):
  return np.exp(-(x**2) / 2) / np.sqrt(2 * np.pi)

# Генерация данных для разных размеров выборок
n_samples = [10, 100, 1000, 10000]
data_sets = [np.random.normal(size=n) for n in n_samples]

# Создание фигуры и подграфиков
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Цикл по подграфикам и наборам данных
for i, ax in enumerate(axes.flatten()):
  # Генерация гистограммы
  ax.hist(data_sets[i], bins=20, density=True, alpha=0.7, label='Гистограмма')

  # Построение целевого распределения
  x = np.linspace(-3, 3, 100)
  ax.plot(x, target_distribution(x), 'r-', label='Целевое распределение')

  # Настройка подграфика
  ax.set_title(f'N = {n_samples[i]}')
  ax.set_xlabel('x')
  ax.set_ylabel('Плотность')
  ax.legend()

# Настройка общей фигуры
fig.suptitle('Сходимость гистограммы к целевому распределению')
plt.tight_layout()
plt.show()
