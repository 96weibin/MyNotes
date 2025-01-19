# Ml

## Build Model

- 获取 fit 数据

```py
    import pandas
    pandas.__version__
    path = 'Test/data/train.csv'
    myData = pandas.read_csv(path)
    columns = ["MSSubClass", "LotArea"]
    X = myData[columns]
    y = myData.SalePrice
```

- predict

```py
from sklearn.tree import DecisionTreeRegressor

myModel = DecisionTreeRegressor(random_state=1)
myModel.fit(X, y)
myModel.predict(X.head())
```

- Validatiaon 