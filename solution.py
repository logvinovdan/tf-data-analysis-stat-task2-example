import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.083
    alpha = 1 - p
    loc = x.max()
    n = len(x)
    d = np.power(alpha,(1/n))
    return loc, \
           ((loc - a) / d + a + 0.005)
