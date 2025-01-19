# pandas

## Install 

1. install anaconda
2. open anaconda promot
3. run jupyter lab

## Loading Data

- read path

    ```py
    import pandas
    pandas.__version__
    path = 'Test/data/train.csv'
    myData = pandas.read_csv(path)
    myData.describe()
    ```

## split data

- 获取列

    ```py
    columns = myData.columns
    ```

- 选择列(series)

    ```py
    # select column
    loatArea = myData.LotArea
    yearBuilt = myData["YearBuilt"]
    ```

- 选择多列(DataFrame)

    ```py
    columns = ["MSSubClass", "LotArea"]
    myColumns = myData[columns]
    ```

### 操作数据集

method | demo | 功能
-|-|-
mean | data.mean() | 平均值
min | data.min() | 最小
max | data.max() | 最大
round | round(loatArea.mean()) | 四舍五入

### Serise

- default

    ```py
    # default
    pd.Series(
        data = None,    # 数组、字典、 不提供则为空
        index = None,   # 自定义index
        dtype = None,   # 指定Series 的数据类型
        name = None,    # 设置名字
        copy = False,  
        fastpath = False
    )
    ```

- create

    ```py
    # 使用 列表创建
    mySeries = pd.Series(['my','name','is','wei','bin'], 
                        index=['a','b','c','d','e'],
                        name= '这一列',
                        copy=True,
                        fastpath
                        )
    # 使用 np                        
    mySeries2 = pd.Series(np.array([1,2,3,4]))
    # 使用 字典
    mySeries3 = pd.Series({'name': 'weibin', 'age': '18', 'genal':'male'})
    ```
- opeartion


### DataFrame
