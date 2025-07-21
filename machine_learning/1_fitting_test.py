import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #画布
from  sklearn.linear_model import LinearRegression #线性回归模型
from sklearn.preprocessing import PolynomialFeatures #构建多项式特征
from sklearn.model_selection import train_test_split # 划分训练集和测试集
from sklearn.metrics import mean_squared_error # 均方误差损失函数

#设置画布
plt.rcParams["font.sans-serif"]=["KaiTi"]
plt.rcParams["axes.unicode_minus"] =False

#生成随机数
#-3到3之间的300个向量数据，且reshape做转置，-1代表行转列
X = np.linspace(-3,3,300).reshape(-1,1)
# sin()函数的数据分布，并加上均匀分布的噪声
y = np.sin(X) + np.random.uniform(-0.5,0.5,300).reshape(-1,1)
# 创建三个子图
fig, ax =plt.subplots(1,3,figsize=(15,4))
ax[0].plot(X,y,"yo")
ax[1].plot(X,y,"yo")
ax[2].plot(X,y,"yo")
# plt.show()



