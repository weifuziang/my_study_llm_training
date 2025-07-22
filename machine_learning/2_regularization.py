import numpy as np
import matplotlib.pyplot as plt #画布
from sklearn.preprocessing import PolynomialFeatures #构建多项式特征
from sklearn.model_selection import train_test_split # 划分训练集和测试集
from sklearn.linear_model import LinearRegression , Lasso,Ridge
from sklearn.metrics import mean_squared_error # 均方误差损失函数

#设置画布
plt.rcParams["font.sans-serif"]=["KaiTi"]
plt.rcParams["axes.unicode_minus"] =False

#生成随机数
#-3到3之间的300个向量数据，且reshape做转置，-1代表行转列
X = np.linspace(-3,3,300).reshape(-1,1)
# sin()函数的数据分布，并加上均匀分布的噪声
y = np.sin(X) + np.random.uniform(-0.5,0.5,300).reshape(-1,1)
# 创建(2 * 3)个子图
fig, ax =plt.subplots(2,3,figsize=(15,8))
ax[0,0].plot(X,y,"yo")
ax[0,1].plot(X,y,"yo")
ax[0,2].plot(X,y,"yo")

#划分训练集和测试集
x_train ,x_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#模型训练（过拟合）：数据集特征工程的构建和模型训练
poly20 = PolynomialFeatures(degree=20)
x_train= poly20.fit_transform(x_train) #构建20阶的多项式（泰勒展开在x=0的位置）:本质就是特征工程的构建，每一项代表一个特征
x_test= poly20.fit_transform(x_test)

#======不加正则化项的线性模型======
#定义模型
model = LinearRegression() #线性回归模型

#模型训练
model.fit(x_train,y_train) #模型训练

#预测结果，计算误差（过拟合）
y_pred1= model.predict(x_test) #模型预测
test_loss1 = mean_squared_error(y_test,y_pred1) #测试集的误差

#画出拟合曲线，并写出训测试误差
ax[0,0].plot(X,model.predict(poly20.fit_transform(X)),"r") #绘制曲线
ax[0,0].text(-3,1,f"测试集均方误差：{test_loss1:.4f}")

#画出所有系数的直方图

ax[1, 0].bar(np.arange(21),model.coef_.reshape(-1))

#======L1正则化-Lass0回归======
#定义模型
#L1正则化-Lass0回归： alpha正则化系数（超参数）
lasso = Lasso(alpha=0.01)

#模型训练
lasso.fit(x_train,y_train)

#预测结果，计算误差（过拟合）
y_pred2= lasso.predict(x_test) #模型预测
test_loss2 = mean_squared_error(y_test,y_pred2) #测试集的误差

#画出拟合曲线，并写出训测试误差
ax[0,1].plot(X,lasso.predict(poly20.fit_transform(X)),"r") #绘制曲线
ax[0,1].text(-3,1,f"测试集均方误差：{test_loss2:.4f}")

#画出所有系数的直方图
ax[0,1].text(-3,1.2,"Lass0回归")
ax[1, 1].bar(np.arange(21),lasso.coef_.reshape(-1))

#======L2正则化Ridge岭回归======
#定义模型
#L1正则化-Lass0回归： alpha正则化系数（超参数）
ridge = Ridge(alpha=1)

#模型训练
ridge.fit(x_train,y_train)

#预测结果，计算误差（过拟合）
y_pred3= ridge.predict(x_test) #模型预测
test_loss3 = mean_squared_error(y_test,y_pred3) #测试集的误差

#画出拟合曲线，并写出训测试误差
ax[0,2].plot(X,ridge.predict(poly20.fit_transform(X)),"r") #绘制曲线
ax[0,2].text(-3,1,f"测试集均方误差：{test_loss3:.4f}")

#画出所有系数的直方图
ax[0,2].text(-3,1.2,"岭回归")
ax[1, 2].bar(np.arange(21),ridge.coef_.reshape(-1))

plt.show()



