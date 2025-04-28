import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

iris = datasets.load_iris()

x_df = pd.DataFrame(iris.data)
x_df.info()
y_df = pd.DataFrame(iris.target)
y_df.info()

# Визуализация данных

plt.scatter(iris.data[:,:1],iris.data[:,1:2],c=iris.target,cmap=plt.cm.Dark2)
plt.title('Sepal plot')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()

plt.scatter(iris.data[:,2:3],iris.data[:,3:4],c=iris.target,cmap=plt.cm.Dark2)
plt.title('Petal plot')
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.show()

# Обучение на обучающей выборке

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.33, random_state=42)

knn1 = KNeighborsClassifier(1)
knn1.fit(X_train,y_train)
pred1 = knn1.predict(X_test)
print(accuracy_score(y_test, pred1))

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5))
ax1.scatter(X_test[:,2:3],X_test[:,3:4],c=y_test,cmap=plt.cm.Dark2)
ax1.set_title('Petal plot (test data)')
ax1.set_xlabel('Petal length')
ax1.set_ylabel('Petal width')
ax2.scatter(X_test[:,2:3],X_test[:,3:4],c=pred1,cmap=plt.cm.Dark2)
ax2.set_title('Petal plot (prediction)')
ax2.set_xlabel('Petal length')
ax2.set_ylabel('Petal width')
plt.show()

knn11 = KNeighborsClassifier(11)
knn11.fit(X_train, y_train)
pred11 = knn11.predict(X_test)
print(accuracy_score(y_test, pred11))

# Кластеризация

kmeans2 = KMeans(n_clusters=2, random_state=42, n_init='auto')
kmeans2.fit(X_train)
pred2 = kmeans2.predict(X_test)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5))
ax1.scatter(X_test[:,2:3],X_test[:,3:4],c=y_test,cmap=plt.cm.Dark2)
ax1.set_title('Petal plot (test data)')
ax1.set_xlabel('Petal length')
ax1.set_ylabel('Petal width')
ax2.scatter(X_test[:,2:3],X_test[:,3:4],c=pred2,cmap=plt.cm.Dark2)
ax2.set_title('Petal plot (prediction)')
ax2.set_xlabel('Petal length')
ax2.set_ylabel('Petal width')
plt.show()

kmeans3 = KMeans(n_clusters=3, random_state=42, n_init='auto')
kmeans3.fit(X_train)
pred3 = kmeans3.predict(X_test)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,5))
ax1.scatter(X_test[:,2:3],X_test[:,3:4],c=y_test,cmap=plt.cm.Dark2)
ax1.set_title('Petal plot (test data)')
ax1.set_xlabel('Petal length')
ax1.set_ylabel('Petal width')
ax2.scatter(X_test[:,2:3],X_test[:,3:4],c=pred3,cmap=plt.cm.Dark2)
ax2.set_title('Petal plot (prediction)')
ax2.set_xlabel('Petal length')
ax2.set_ylabel('Petal width')
plt.show()