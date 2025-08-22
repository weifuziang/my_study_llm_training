import numpy as np

from deep_learning.common.functions import sigmoid,identity


#初始化网络：模型参数的初始化（权重W和偏置b），神经网络的层级架构
def init_network():
    network = {}
    #第一层参数 : 该层有三个神经元，且上一层是输入层（第零层）是两个输入特征x1,x2，即可得到一个2*3的矩阵，具体公式查看《2.神经网络基础》-> 神经网路的简单实现 ->代码实现
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1'] = np.array([0.1,0.2,0.3])

    #第二层数：该层有两个神经元，且上一层是三个神经元，即可得到一个3*2的矩阵
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])

    #第三层数：该层是输出层，有两个数据y1 y2，且上一次是两个神经元，即可得到一个2*2的矩阵
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])

    return network

# 向前传播
def forward(network ,x):
    """
    :param network: 模型参数
    :param x: 特征数据
    :return:
    """
    #获取模型参数
    w1,w2,w3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    #逐层计算
     # 输入x是1*2的向量，权重w1是2*3的矩阵，点乘得到1 * 3的向量
    a1 = np.dot(x,w1)+b1
     # 对1*3的向量做离散化处理（激活），并作为下一层的输入
    z1 = sigmoid(a1)
     # 输入z1是1*3的向量，权重2是3*2的矩阵，得到1*2的向量
    a2 = np.dot(z1,w2)+b2
     #对1*2的向量做离散化处理（激活）
    z2 = sigmoid(a2)
     # 输入z2是1*2的向量，权重w3是2*2的矩阵，得到1*2的向量
    a3 = np.dot(z2,w3)+b3
     #恒等激活函数对1*2的向量做输出
    y =  identity(a3)

    return y








