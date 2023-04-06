import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 834639322 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    b = 2 * x - 0.083
    b_up = np.quantile(b, p)
    b_down = 2*B.mean() - b_up
    return b_down, b_up
