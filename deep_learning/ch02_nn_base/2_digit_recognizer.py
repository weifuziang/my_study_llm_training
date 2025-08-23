import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from deep_learning.common.functions import sigmoid, softmax


# 读取数据："F:\MyStudy\LLM\07_尚硅谷大模型技术之深度学习核心\2.资料\data"
def get_date():
    # 1.从文件加载数据
    data = pd.read_csv(r"F:\MyStudy\LLM\my_codes\data\deep_learning\day06\train.csv")
    # print(data)

    # 2. 划分数据集 axis: 0代表行，1代表列
    X = data.drop("label", axis=1)
    y = data["label"]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # print(x_train)
    # print(y_train)

    # 3. 特征工程归一化
    scaler = MinMaxScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    return x_test, y_test


# 初始化神经网络： 个人理解只是模型的权重和偏置参数，缺少了承载模型参数的传递骨架
def init_network():
    # 直接从文件中加载字典对象
    network = joblib.load(r"F:\MyStudy\LLM\my_codes\data\deep_learning\day06\nn_sample")
    return network


# 前向传播： 个人理解其实就是模型的一部分：即模型的传递骨架（affine函数 sigmoid函数 softmax函数）
def forward(network, x):
    # 获取到模型的权重和偏置
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 逐层计算传递
    # 第一个神经元：affine线性函数 + sigmoid二分类函数
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)

    # 第二个神经元: 将第一个神经元的输出作为输入x
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)

    # 第三个神经元：其实就是输出层： affine函数 + softmax多分类函数
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)

    return y


if __name__ == '__main__':
    # 主流程

    # 1. 获取测试数据
    x, y = get_date()

    # 2. 创建模型：个人理解有点牵强
    network = init_network()

    # 3. 前向传播（测试）：个人理解是创建模型的一部分，完全可以归纳到“创建模型”中
    # 得到的是可能是0~9这个十个数字，每一个数字的概率值，即 1260 * 10 也就是说每一行有十个概率值
    y_proba = forward(network, x)
    # print(x.shape, y.shape)
    print(y_proba.shape)
    print(y_proba)

    # 4. 将分类概率转化为分类标签:
    # argmax()函数中 axis=1代表列，该函数意思就是从每一行数据中，按列的位置做比较，获取最大的概率值对应的index
    # y_proba的二维矩阵中：索引就是要预测的数字，值就是预测的概率值大小
    y_pred = np.argmax(y_proba, axis=1)  # 返回沿轴的最大值的索引。
    # y_pred_0 = np.argmax(y_proba, axis=0)
    # y_pred_default = np.argmax(y_proba)
    # print(y_pred)
    # print(y_pred_0)
    # print(y_pred_default)

    # 5. 计算分类准确率
    #获取正确结果的个数
    accuracy_cnt = np.sum(y_pred == y)
    #获取总共的数据条数
    n = y_pred.shape[0]
    print(accuracy_cnt / n)
