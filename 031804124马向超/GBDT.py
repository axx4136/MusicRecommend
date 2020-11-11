from sklearn.neighbors import KNeighborsClassifier
from sklearn import naive_bayes, svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from prettytable import PrettyTable
import pickle
import numpy as np
from sklearn.neural_network import MLPClassifier


def MLP(*data):
    x_train, x_test, y_train, y_test = data
    mlp = MLPClassifier(solver='adam', hidden_layer_sizes=[100, 100], activation='relu',
                        random_state=62, max_iter=2000, learning_rate_init=0.0001)
    mlp.fit(x_train, x_test)
    y_pre = mlp.predict(x_test)
    acc = accuracy_score(y_test, y_pre)
    print(mlp.score(x_test, y_test))
    print(acc)
    return mlp.score(x_test, y_test)


def KNN(*data):
    x_train, x_test, y_train, y_test = data
    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)
    y_pre = knn.predict(x_test)
    acc = accuracy_score(y_test, y_pre)
    return acc


def naibayes(*data):
    x_train, x_test, y_train, y_test = data
    bayes = naive_bayes.GaussianNB()
    bayes.fit(x_train, y_train)
    return bayes.score(x_test, y_test)


def Logistic(*data):
    x_train, x_test, y_train, y_test = data
    logic = LogisticRegression()
    logic.fit(x_train, y_train)
    return logic.score(x_test, y_test)


def svmm(*data):
    x_train, x_test, y_train, y_test = data
    svmmm = svm.SVC(C=2, kernel='linear', gamma=10, decision_function_shape='ovo')
    svmmm.fit(x_train, y_train)
    return svmmm.score(x_test, y_test)


path = r'C:\Users\Administrator\Desktop\TechStudy\Ch6Bayes\cifar-100-batches-py/'


def unpickle(file):
    with open(file, 'rb') as f:
        cifar = pickle.load(f, encoding='bytes')
    return cifar


test_data = unpickle(path + 'test')
t1 = []
t2 = []
t3 = []
t4 = []

train_data = unpickle(path + 'train')
x_train, y_train = train_data[b'data'][0:10000], np.array(train_data[b'fine_labels'][0:10000])
x_test, y_test = test_data[b'data'][0:10000], np.array(test_data[b'fine_labels'][0:10000])
t4.append(svmm(x_train, x_test, y_train, y_test))
pre = PrettyTable(['分类方法', 'batch_1'])
pre.add_row(['svmm', '%.4f' % t4[0]])
print(pre)
