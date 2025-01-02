def sphere_function(position):
    return sum(x ** 2 for x in position)

def rosenbrock_function(position):
    return sum(100 * (position[i + 1] - position[i] ** 2) ** 2 + (1 - position[i]) ** 2 for i in range(len(position) - 1))

def constraint_example(position):
    return all(x >= 0 for x in position)
import math  # Usamos el módulo estándar de matemáticas

def rastrigin(x):
    return 10 * len(x) + sum([(xi**2 - 10 * math.cos(2 * math.pi * xi)) for xi in x])
