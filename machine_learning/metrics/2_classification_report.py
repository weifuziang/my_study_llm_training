from sklearn.datasets import make_classification #自动生成分类数据
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  #逻辑回归分类模型
from sklearn.metrics import classification_report #生成分类评估报告

#生成一个二分类数据集
X,y = make_classification(n_samples=1000,n_features=20 , n_classes=2 ,random_state=42)
print(X.shape)
print(y.shape)


#划分训练集和测试集
x_train , x_test,y_train , y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#定义模型
model = LogisticRegression()

#模型训练
model.fit(x_train,y_train)

#模型预测
y_pred = model.predict(x_test)

#生成报告
classification_report = classification_report(y_test,y_pred)
print(classification_report)

#获取预测值为正例的概率值[1]
y_pred_proba = model.predict_proba(x_test)[:,1]
print(y_pred_proba)

#计算 AUC值
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(roc_auc)