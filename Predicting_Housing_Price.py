# -*- coding: utf-8 -*-
"""Task3_109306011

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zc2O7z9VfjUA28ZW_VAccQ7G_klbzZ2b
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
# %matplotlib inline

from sklearn.datasets import load_boston
boston_dataset = load_boston()

print(boston_dataset.keys())

print(boston_dataset.DESCR)

print(boston_dataset.keys())

boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston.head()

boston['MEDV'] = boston_dataset.target #MEDV is our target

boston['MEDV']

boston.isnull().sum()

###there is no missing value now we will check for correlation of features

sns.set(rc={'figure.figsize':(10,10)})
sns.distplot(boston['MEDV'])
plt.show()

correlation_matrix = boston.corr().round(2)
sns.heatmap(data=correlation_matrix, annot = True)

plt.figure(figsize=(20, 5))
features = ['LSTAT', 'RM']
target = boston['MEDV']
for i, col in enumerate(features):
 # 排版1 row, 2 columns, nth plot：在jupyter notebook上兩張並排 
 plt.subplot(1, len(features) , i+1)
 # add data column into plot
 x = boston[col]
 y = target
 plt.scatter(x, y, marker='o')
 plt.title(col)
 plt.xlabel(col)
 plt.ylabel('MEDV')

X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM']], columns = ['LSTAT','RM'])
Y = boston['MEDV']

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=5)
# 再用.shape看切出來的資料的長相（列, 欄）
print(X_train.shape) #(404, 2)
print(X_test.shape) #(102, 2)
print(Y_train.shape) #(404, )
print(Y_test.shape) #(102, )

# Modeling
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
# Fitting linear model
reg.fit(X_train,Y_train)
# Predicting using the linear model
reg.predict(X_test)
# Accuracy
print('R2: ', reg.score(X_test, Y_test))

### We can see that the R2 score is quite high.

# plotting the y_test vs y_pred
Y_pred = reg.predict(X_test)
plt.scatter(Y_pred, Y_test)
plt.xlabel('Y_pred')
plt.ylabel('Y_test')
plt.show()

reg.intercept_

coeff_df = pd.DataFrame(reg.coef_, X_train.columns, columns=['Coefficient'])  
coeff_df

# 關係式 MEDIV = reg.intercept_ ＋ (Coefficient_LSTAT) * LSTAT + (Coefficient_RM) * RM + error
# 關係式 MEDIV = 0.38437936780346504 ＋ (-0.659580) * LSTAT + 4.831976 * RM + error

"""####We use LSTAT(The proportion of low- and middle-income households in the local resident population) and RM(How many rooms in the house) two variables to predict the MEDIV (housing price) based on a multi-variables linear regression model. We can find that when other variables remain the same, when LSTAT increases 1 unit, MEDIV decrease about 0.66 unit. Also, when RM increases 1 unit, MEDIV would increase 4.83 units. It seems that RM has more effect on the MEDIV than the LSTAT. """