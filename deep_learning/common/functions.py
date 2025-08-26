import numpy as np

#阶跃函数
def step_function(x):
    if x >0:
        return 1
    else:
        return 0

# Sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#reLu函数
def rulu(x):
    """
    算两个数组（或数组与标量）中​​对应位置元素的最大值
    :param x:
    :return:
    """
    return np.maximum(0, x)


# 恒等函数
def identity(x):
    return x


# Softmax函数
def softmax0(x):
    return np.exp(x) / np.sum(np.exp(x))


# softmax函数：考虑输入可能是矩阵的情况
def softmax(x):
    # 如果是二维矩阵
    if x.ndim == 2:
        # 为什么要进行转置？？？： 原因是，我要每次处理多个特征x1 x2 x3 x4....., 而原先的矩阵是一个数组代表一个特征x
        x = x.T
        # 溢出处理策略: 考虑到x较大时，指数会非常大，容易溢出，则可以将x中的每一个元素都减去x中的最大值；如果这样不会影响结果么？？？
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    # 溢出处理策略: 考虑到x较大时，指数会非常大，容易溢出，则可以将x中的每一个元素都减去x中的最大值；如果这样不会影响结果么？？？
    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x)) #本质是需要计算x1 x2 x3 x4 中每个x在指定函数作用下占所有x的比例


# 损失函数
# MSE: 均方误差函数 (前面的系数n不重要，因此公式有时也可以写成1/2)
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

#交叉熵函数
def cross_entropy(y,t):
    """
    :param y:
    :param t: ti中只有正确解标签对应的值为1，其它均为0（one-hot表示,即独热编码）
    :return:
    """
    #将y转为二维
    if y.ndim == 1:
        print("t.shape", t.shape)
        print("t.T.shape", t.T.shape)
        t = t.reshape(1,t.size)
        print("t: ",t)
        print("t.size: ",t.size)
        print("t.reshape: ",t.shape)
        y = y.reshape(1, y.size)
        print("y: ",y)
    # 将t转换为顺序编码（类别标签）：one-hot转为类别标签
    if t.size == y.size:
        t = t.argmax(axis = 1)
        print("t内部：: ",t)

    print("y.shape: ", y.shape)
    n = y.shape[0]
    print("n: ", n)
    print("np.arange(n): ", np.arange(n))
    print("t: ",t)
    print("y[0,t]: ",y[0,t])
    print("y[np.arange(n),t] : ",y[np.arange(n),t])
    # ti * logyi的处理方法：由于t_i是独热编码eg:[0,0,1,0,0] 所以在进行乘法的时候，有效值只有1*y，
    #对于这种情况，我们直接取出独热编码中1对应的矩阵索引号a，然后，取出y矩阵索引号为a的值，直接进行log即可；
    # np.arange(n):列表索引(理解为行号)，从0一直取到n,代表y有多少条数据；
    # t: 独热编码[0,0,0,1,0,0]中数值‘1’对应的索引号a；
    # 1e-7: 防止log0报错；
    return -np.sum(np.log(y[np.arange(n),t] + 1e-7)) / n


if __name__ == '__main__':

    # 交叉熵损失函数测试
    # y = np.array([1,4,6,9])
    # t = np.array([1,5,9,1])
    # entropy = cross_entropy(y, t)
    # print(entropy)

    #softmax函数测试
    X = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [-1, -2, -3]])
    print(softmax(X))

