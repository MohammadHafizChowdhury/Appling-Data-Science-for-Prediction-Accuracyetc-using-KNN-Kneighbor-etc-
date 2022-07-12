# -*- coding: utf-8 -*-
"""6_19101067_Mohammad Hafiz-Ul-Islam Chowdhury.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10wZgsU_inj-30LRZXjWfYTFMyVGrBJii
"""

from google.colab import drive
drive.mount('/content/drive')

import os
directory = "/content/drive/MyDrive/Online semester/CSE422/dataset"
os.chdir(directory)

!ls

import pandas as pd

dataset = pd.read_csv("dataset.csv")

dataset

dataset.shape

dataset.shape[0]

dataset.head()

dataset.sample()

dataset.columns

dataset.isnull( )

dataset.isnull( ).sum()

dataset = dataset.fillna(50)
dataset.notnull()

obj_df = dataset.select_dtypes(include=['object']).copy()
obj_df.head()

import numpy as np

dataset.info()

dataset["gender"].unique()

obj_df["gender"].value_counts()

print(dataset["capital-gain"].max())
print(dataset["capital-gain"].min())

dataset['income_>50K'] = dataset['income_>50K']
print(dataset[['income_>50K']].head())

dataset.isnull().sum()

dataset

import seaborn as sns
co = dataset.corr() 
print(co)
sns.heatmap(co)

dataset.describe()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x1_column = dataset[["capital-gain","capital-loss","educational-num"]]
y1_column =dataset["income_>50K"]
X_train, X_test, y_train, y_test = train_test_split(x1_column,y1_column, random_state=1)
scaler.fit(X_train)

from sklearn.neighbors import KNeighborsClassifier
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn=KNeighborsClassifier()
knn.fit(X_train_scaled, y_train)

knn.fit(X_train_scaled, y_train)
knn.fit(X_train_scaled, y_train)
print("KNN test accuracy: {:.2f}".format(knn.score(X_test_scaled, y_test)))

"""ASSIGNMENT 5"""

import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

dataset['age'] = dataset['age'].astype(float)
dataset['fnlwgt'] = dataset['fnlwgt'].astype(float)
dataset['educational-num'] = dataset['educational-num'].astype(float)
dataset['capital-gain'] = dataset['capital-gain'].astype(float)
dataset['capital-loss'] = dataset['capital-loss'].astype(float)
dataset['hours-per-week'] = dataset['hours-per-week'].astype(float)
dataset['income_>50K'] = dataset['income_>50K'].astype(float)
dataset.info()

x = dataset[["age","fnlwgt","educational-num","capital-gain","capital-loss","educational-num"]]
y = dataset.iloc[:, 1].values
from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = .3, random_state = 0)
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)
yPrediction = clf.predict(X_test)
yPrediction

X = dataset[["age","fnlwgt","educational-num","capital-gain","capital-loss","educational-num"]]

y = dataset["income_>50K"]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
model = LogisticRegression()
model.fit(x_train, y_train) 
predictions = model.predict(x_test)
print(predictions)

print( accuracy_score(y_test, predictions))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
X = dataset[["age","fnlwgt","educational-num","capital-gain","capital-loss","educational-num"]]
y = dataset["income_>50K"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
clf = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=accuracy_score(y_pred,y_test)
print(score)

#Train the model
model = LogisticRegression()
model.fit(X_train, y_train) #Training the model
predictions = model.predict(X_test)
print(predictions)# printing predictions


clf = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=accuracy_score(y_pred,y_test)
print(score)

from sklearn import tree
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(clf,
               feature_names = X.columns, 
               class_names=['1','2','3','4','5','6','7'],
               filled = True);

import matplotlib.pyplot as plt
barWidth = 0.20
fig = plt.subplots(figsize =(8, 6))
model =['Logistic Regression','Desicion Tree']
values = [( accuracy_score(y_test, predictions)),score]
plt.bar(model,values,color = ["red","blue"])
plt.show()

"""ASSIGNMENT 06"""

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
enc = LabelEncoder()

dataset['Workclass'] = enc.fit_transform(dataset['workclass'])
list_of_features = ["capital-gain","capital-loss"]

scaler = MinMaxScaler()

scaler.fit(dataset[list_of_features])

scaled_data = scaler.transform(dataset[list_of_features])

def gradient_descent_logistic(b_val, m_val, x_val, y_val, learning_rate, num_iterations):


    vars = sp.symbols('x y m b n')
    x, y,m,b,n = vars
    n_val = float(len(x_val))
    error_function = -(1/(n)) * ((y * sp.log(1/ (1+(sp.exp(-(m*x+b)))))) + ((1-y) * sp.log(1 - (1/ (1+(sp.exp(-(m*x+b))))))))

    error_function_b = sp.diff(error_function, b)
    error_function_m = sp.diff(error_function, m)
    for j in range(num_iterations): 
        b_gradient = 0
        m_gradient = 0
        for i in range(0, len(x_val)):
            
            b_gradient += error_function_b.evalf(subs = {x:x_val[i], y:y_val[i], m:m_val, b:b_val,n:n_val})
            m_gradient += error_function_m.evalf(subs = {x:x_val[i], y:y_val[i], m:m_val, b:b_val,n:n_val})
   
        b_val -= (learning_rate * b_gradient)
        m_val -= (learning_rate * m_gradient)
        
        
    return [b_val, m_val]

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

list_of_features=['age','Workclass','capital-gain','capital-loss']
label_column_name=['income_>50K']
x_data = dataset[list_of_features]
y_data = dataset.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=1)
model = LogisticRegression()
model.fit(x_train, y_train) 
predictions = model.predict(x_test)
print(accuracy_score(y_test, predictions))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
x = dataset[list_of_features]
y = dataset.iloc[:, -1]
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
clf = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=accuracy_score(y_pred,y_test)
print(score)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

list_of_features=['age','Workclass','capital-gain','capital-loss']
label_column_name=['income_>50K']
x_data = dataset[list_of_features]
y_data = dataset.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data,test_size = 0.2,random_state=1)

from sklearn.svm import SVC
m1 = SVC(kernel="linear")
m1.fit(X_train, y_train)
y_pred1 = m1.predict(x_test)
score_1 = accuracy_score(y_pred1, y_test)
score_1

from sklearn.neural_network import MLPClassifier
m2 = MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)
m2.fit(X_train, y_train)
y_pred2 = m2.predict(x_test)
score_2 = accuracy_score(y_pred2, y_test)
score_2

from sklearn.ensemble import RandomForestClassifier
m3 = RandomForestClassifier(n_estimators=50)
m3.fit(X_train, y_train)
y_pred3 = m3.predict(x_test)
score_3 = accuracy_score(y_pred3, y_test)
score_3

half = (dataset.columns.shape[0]-1)//2
half

from sklearn.decomposition import PCA 
pca = PCA(n_components=4)

principal_components = pca.fit_transform(x_data)
principal_components
pca.explained_variance_ratio_ 
sum(pca.explained_variance_ratio_)
principal_df = pd.DataFrame(data=principal_components, columns=["Component 1", "Component 2", "Component 3", "Component 4" ])
main_df=pd.concat([principal_df, dataset[["income_>50K"]]], axis=1)
main_df.head()

x_data = main_df.drop("income_>50K" , axis=1)
y_data = main_df["income_>50K"]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data,test_size = 0.2,random_state=1)

from sklearn.svm import SVC
m1 = SVC(kernel="linear")
m1.fit(x_train, y_train)
y_pred1 = m1.predict(x_test)
score_4 = accuracy_score(y_pred1, y_test)
score_4

from sklearn.neural_network import MLPClassifier
m2 = MLPClassifier(hidden_layer_sizes=(7), activation="relu", max_iter=10000)
m2.fit(x_train, y_train)
y_pred2 = m2.predict(x_test)
score_5 = accuracy_score(y_pred2, y_test)
score_5

from sklearn.ensemble import RandomForestClassifier
m3 = RandomForestClassifier(n_estimators=50)
m3.fit(X_train, y_train)
y_pred3 = m3.predict(x_test)
score_6 = accuracy_score(y_pred3, y_test)
score_6

import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.20
fig = plt.subplots(figsize =(8, 6))
svm = [score_1, score_4]
mlp = [score_2, score_5]
rfc = [score_3, score_6]

br1 = np.arange(len(svm))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.ylabel('Score', fontweight ='normal', fontsize = 10)
plt.xticks([r + barWidth for r in range(len(svm))],['pre-PCA', 'post-PCA'])
 
plt.bar(br1, svm, color ='r', width = barWidth,edgecolor ='grey', label ='SVM')
plt.bar(br2, mlp, color ='g', width = barWidth,edgecolor ='grey', label ='MLP')
plt.bar(br3, rfc, color ='b', width = barWidth, edgecolor ='gray', label ='RFC')

plt.legend()
plt.show()