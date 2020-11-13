from math import sqrt

"""
    1    2    3    4    5   6    7    8    9    10  11   12   13  14    15
    欧美 华语 流行 伤感 治愈 摇滚 工作 地铁 民谣 电子 夜晚 兴奋 说唱 浪漫 轻音乐
    16   17   18   19   20  21   22   23  24   25   26   27   28  29    30
    孤独 感动 怀旧 运动 学习 安静 驾车 清晨 放松 午休 思念 快乐 清新 酒吧 下午茶
"""

f = open(r"C:\Users\家住海边所以浪\Desktop\songData.txt", "r", encoding="UTF-8")
data = f.read().split("\n")
f.close()

"""
余弦相似度:用户的偏好:收藏了30首摇滚,20首运动,20首电子,20首说唱,20首放松,和歌曲标签计算余弦相似度
此算法对收藏少的标签影响大,后续引入TF-IDF解决
"""
nameList = []
tagList = []
# 用整数来做,用户
userLove = {6:30,10:20,13:20,19:20,24:10}
user_mod = sqrt(sum([v*v for v in userLove.values()]))
recommend = {}

for song in data:
    sData = eval(song)
    nameList.append(sData["name"])
    tagList.append(sData["tag"])

tagLength = len(tagList)
for i in range(tagLength):
    tag = tagList[i]
    # 也未引入权重,默认都为1,后面可以修改
    fz = sum([v for k,v in userLove.items() if k in tag])
    # 有几个标签,就是几个1²相加
    fm = user_mod * sqrt(len(tag))
    similar = fz/fm
    recommend[nameList[i]] = similar

recommend = dict(sorted(recommend.items(), key=lambda kv: (
    kv[1], kv[0]), reverse=True))

cnt = 0
for k,v in recommend.items():
    print(k,v)
    cnt += 1
    if cnt==20:
        break