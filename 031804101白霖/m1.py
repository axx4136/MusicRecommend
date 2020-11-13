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
Jaccard相似系数:一首歌曲的标签A和用户喜欢的标签B (A∩B)/(A∪B)
这里没有考虑权重 而有的标签是具有相似性的
如:学习和安静,工作和放松,后续可做调整
"""
nameList = []
tagList = []
userLove = {1, 6}
recommend = {}

for song in data:
    sData = eval(song)
    nameList.append(sData["name"])
    tagList.append(sData["tag"])

tagLength = len(tagList)
for i in range(tagLength):
    tag = tagList[i]
    same = tag & userLove
    union = tag | userLove
    similar = len(same)/len(union)
    recommend[nameList[i]] = similar

recommend = dict(sorted(recommend.items(), key=lambda kv: (
    kv[1], kv[0]), reverse=True))

cnt = 0
for k,v in recommend.items():
    print(k,v)
    cnt += 1
    if cnt==20:
        break