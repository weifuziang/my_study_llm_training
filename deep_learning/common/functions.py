import numpy as np

# Sigmoid函数
def sigmoid(x):
    return 1 / (1+ np.exp(-x))

#恒等函数
def identity(x):
    return x