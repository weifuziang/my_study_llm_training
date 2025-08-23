import numpy as np

# Sigmoid函数
def sigmoid(x):
    return 1 / (1+ np.exp(-x))

#恒等函数
def identity(x):
    return x

#Softmax函数
def softmax0(x):
    return np.exp(x) / np.sum(np.exp(x))
#softmax函数：考虑输入可能是矩阵的情况
def softmax(x):
    #如果是二维矩阵
    if x.ndim == 2:
        # 为什么要进行转置？？？
        x=x.T
        # 溢出处理策略: 考虑到x较大时，指数会非常大，容易溢出，则可以将x中的每一个元素都减去x中的最大值；如果这样不会影响结果么？？？
        x= x - np.max(x,axis=0)
        y= np.exp(x) / np.sum(np.exp(x) ,axis=0)
        return y.T
    # 溢出处理策略: 考虑到x较大时，指数会非常大，容易溢出，则可以将x中的每一个元素都减去x中的最大值；如果这样不会影响结果么？？？
    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))
