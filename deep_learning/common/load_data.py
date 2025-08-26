import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler #最小-最大归一工具，用于将数据按特征（列）缩放到指定的范围内（默认[0, 1]）

def get_data():
    #1.从文件加载数据集
    data = pd.read_csv(r"F:\MyStudy\LLM\my_codes\data\deep_learning\day06\train.csv")

    #2. 划分数据集
    X = data.drop('label', axis=1)
    y = data['label']
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

    #3. 特征工程： 归一化
    scaler = MinMaxScaler()
    train_X = scaler.fit_transform(train_X) #缩放到[0,1]
    test_X = scaler.transform(test_X) # 会超出[0,1]

    #4. 将数据都转成ndarray
    y_train = train_y.values
    test_y = test_y.values

    return train_X, test_X, train_y, test_y
