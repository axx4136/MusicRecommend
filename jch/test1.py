from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score # 这里修改一下老师代码的返回值，只返回要用到的ACC

def auto_text(rects):
    for rect in rects:
        ax.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=22)
# 训练样本数1797  特征数64=8×8

# plt.gray()
# plt.matshow(digits.images[0])  # 显示0的图
# plt.show()

fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
# 绘制数字：每张图像8*8像素点
for i in range(64):
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])  # 给空列表为了把坐标值去了
    ax.imshow(digits.images[i])  # interpolation='nearest'设置像素点边界模糊程度  cmap=plt.cm.binary设置颜色类型
    # 用目标值标记图像
    ax.text(0, 7, str(y_train[i]))

A_PCA = []
A_LDA = []
for i in range(1, 10):
    # PCA + KNN
    pca = PCA(n_components=i).fit(X_train)  # pca模型训练
    # 将输入数据投影到特征面正交基上
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    knn = KNeighborsClassifier()
    knn.fit(X_train_pca, y_train)
    y_sample = knn.predict(X_test_pca)
    ACC_PCA = accuracy_score(y_test, y_sample)
    A_PCA.append(ACC_PCA)
    # LDA + KNN
    lda = LinearDiscriminantAnalysis(n_components=i).fit(X_train, y_train)  # lda模型训练 记得加上y_train训练集的标签
    # 将输入数据投影到特征面正交基上
    X_train_lda = lda.transform(X_train)
    X_test_lda = lda.transform(X_test)
    knn = KNeighborsClassifier()
    knn.fit(X_train_lda, y_train)
    y_sample = knn.predict(X_test_lda)
    ACC_LDA = accuracy_score(y_test, y_sample)
    A_LDA.append(ACC_LDA)
list_ori = list(A_LDA)  #原始列表
mid_np = np.array(list_ori)                    #列表转数组
mid_np_2f = np.round(mid_np,2)                 #对数组中的元素保留两位小数
list_new_LDA = list(mid_np_2f)
list_ori_PCA = list(A_PCA)  #原始列表
mid_np_PCA = np.array(list_ori_PCA)                    #列表转数组
mid_np_2f_PCA = np.round(mid_np_PCA,2)                 #对数组中的元素保留两位小数
list_new_PCA = list(mid_np_2f)
# 画柱状图
fig, ax = plt.subplots()
bar_width = 0.35
opacity = 0.6  # 不透明度
index = np.arange(9)
ax.set_xticks(index + bar_width / 2)

cylinder1 = ax.bar(index, list_new_PCA, bar_width, alpha=opacity, color='y', label='PCA')
cylinder2 = ax.bar(index + bar_width, list_new_LDA, bar_width, alpha=opacity, color='g', label='LDA')
auto_text(cylinder1)
auto_text(cylinder2)
label = []  # 横坐标标签
for j in range(1, 10):
    label.append(j)
ax.set_xticklabels(label)
ax.legend()  # 图例标签
plt.show()
