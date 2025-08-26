import numpy as np
import matplotlib.pyplot as plt
from deep_learning.common.gradient import numerical_gradient

# 定义梯度下降的函数
def gradient_descent(f, init_x, lr=0.01 ,num_iter=100):
    #初始化x，对应后面的神经网络训练其实就是权重和偏置
    x=init_x

    #定义数组保存x的变化，直观的观察
    x_history = []
    for i in range(num_iter):
        x_history.append(x)
        #计算梯度
        grad = numerical_gradient(f, x)
        #更新参数
        x -= lr * grad

    return x, np.array(x_history)

#定义目标函数 f(x1,x2) = x1**2 + x2**2
def f(x):
    return x[0]**2 + x[1]**2

if __name__ == '__main__':
    # 1. 定义初始值
    init_x = np.array([-3.0,4.0])

    #2. 定义超参数
    l=0.5
    num_iter=100

    #3. 使用梯度下降法，计算最小值点
    x, x_history = gradient_descent(f, init_x, lr=l, num_iter=num_iter)
    print("最小值点",x)


    #画图
    plt.plot([-5,5],[0,0],'--b')
    plt.plot([0,0],[-5,5],'--b')
    plt.scatter(x_history[:,0],x_history[:,1])
    print(x_history[:,0])
    print('==============================')
    print(x_history[:,0])
    print('---------------------------')
    print(x_history)
    # plt.xlim([-3.5,3.5])
    # plt.ylim([-4.5,4.5])
    # plt.xlabel('X[0]')
    # plt.ylabel('X[1]')
    plt.show()