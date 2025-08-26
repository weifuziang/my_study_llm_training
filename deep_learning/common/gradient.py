import numpy as np

#数值微分求导，传入x是一个标量
def numerical_diff(f,x):
    h = 1e-4
    #使用中心差分的方法
    return (f(x+h)-f(x-h)) /(2*h)

# 数值微分求梯度，传入x是一个向量
def _numerical_gradient(f,x):
    h = 1e-4
    # Return an array of zeros with the same shape and type as a given array.
    grad = np.zeros_like(x)
    print("numerical gradient grad.shap",grad.shape)
    #遍历x中的特征xi:逐个做中心差分
    print("numerical gradient x.size=",x.size,x.shape)
    for i in range(x.size):
        #为了，不改变原有的x向量，先做一个临时值的存储，后面在不x[i]恢复回来
        tmp = x[i]
        #巧妙的使用 x[i]作为差分方法x轴方向开始点的存储
        x[i]=tmp + h
        #必须将整个x向量都带进去，而不是x[i]，其实就偏导的思想，x中未做差分的元素其实就是常数
        fxh1= f(x)
        #巧妙的使用 x[i]作为差分方法x轴方向结束点的存储
        x[i] = tmp -h
        #必须将整个x向量都带进去,而不是x[i]，其实就偏导的思想，x中未做差分的元素其实就是常数
        fxh2= f(x)
        grad[i] = (fxh1-fxh2)/(2*h)
        #x[i]的恢复
        x[i] = tmp
    return grad

# 数值微分求梯度，传入x是一个矩阵
def numerical_gradient(f,X):
    #判断维度
    if X.ndim == 1:
        return _numerical_gradient(f,X)
    else:
        grad = np.zeros_like(X)
        #遍历X中每一行数据，分别求梯度
        for i , x in enumerate(X):
            grad[i] = _numerical_gradient(f,x)
        return grad

