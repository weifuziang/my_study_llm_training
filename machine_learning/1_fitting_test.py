import numpy as np
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
#划分训练集和测试集
x_train ,x_test,y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#定义模型（创建线性回归模型）
model = LinearRegression()

#训练模型（欠拟合）：数据集特征工程的构建和模型训练，此次欠拟合训练基本上是没有对数据做特征工程的构建的
x_train1= x_train
x_test1= x_test
model.fit(x_train1,y_train) #模型训练：训练出来的model里，已经确定了模型的参数，即函数的参数

#预测结果，计算误差
y_pred1 = model.predict(x_test1) #模型预测：使用测试集，使用训练出来的model，来做测试集的预测标签
test_loss = mean_squared_error(y_test,y_pred1) #测试集的误差
train_loss = mean_squared_error(y_train,model.predict(x_train1)) #训练集的误差

ax[0].plot(np.array([[-3],[3]]),model.predict(np.array([[-3],[3]])),"c") #绘制曲线
ax[0].text(-3,1,f"测试集均方误差：{test_loss:.4f}")
ax[0].text(-3,1.3,f"训练集均方误差：{train_loss:.4f}")

#模型训练（恰好拟合）: 数据集特征工程的构建和模型训练
poly5 = PolynomialFeatures(degree=5)
x_train2= poly5.fit_transform(x_train) #构建5次的多项式，且总共是6项式，其中一项是常数项（泰勒展开在x=0的位置）:本质就是特征工程的构建，每一项代表一个特征
x_test2= poly5.fit_transform(x_test)
model.fit(x_train2,y_train) #模型训练

#预测结果，计算误差（恰好拟合）
y_pred2 = model.predict(x_test2) #模型预测
test_loss2 = mean_squared_error(y_test,y_pred2) #测试集的误差
train_loss2 = mean_squared_error(y_train,model.predict(x_train2)) #训练集的误差

ax[1].plot(X,model.predict(poly5.fit_transform(X)),"k") #绘制曲线
ax[1].text(-3,1,f"测试集均方误差：{test_loss2:.4f}")
ax[1].text(-3,1.3,f"训练集均方误差：{train_loss2:.4f}")


#模型训练（过拟合）：数据集特征工程的构建和模型训练
poly20 = PolynomialFeatures(degree=20)
x_train3= poly20.fit_transform(x_train) #构建20阶的多项式（泰勒展开在x=0的位置）:本质就是特征工程的构建，每一项代表一个特征
x_test3= poly20.fit_transform(x_test)
model.fit(x_train3,y_train) #模型训练

#预测结果，计算误差（过拟合）
y_pred3 = model.predict(x_test3) #模型预测
test_loss3 = mean_squared_error(y_test,y_pred3) #测试集的误差
train_loss3 = mean_squared_error(y_train,model.predict(x_train3)) #训练集的误差

ax[2].plot(X,model.predict(poly20.fit_transform(X)),"r") #绘制曲线
ax[2].text(-3,1,f"测试集均方误差：{test_loss3:.4f}")
ax[2].text(-3,1.3,f"训练集均方误差：{train_loss3:.4f}")

print(model.coef_)
print(model.intercept_)
plt.show()









