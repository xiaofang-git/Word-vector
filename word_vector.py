import math


def get_cos(word_1, word_2, case=True):
    # case为真默认忽略大小写
    # 给定两个词计算余弦向量值
    if case:
        word_1 = word_1.upper()
        word_2 = word_2.upper()
    
    # 获取两个词中组成元素的并集
    word_set1 = set(word_1)
    word_set2 = set(word_2)
    word_union = word_set1.union(word_set2)

    # 分别循环判断各个词中元素有没有在集合中存在，存在为1， 不存在为0
    vector_1 = []
    for i in word_union:
        if i in word_1:
            vector_1.append(1)
        else:
            vector_1.append(0)

    vector_2 = []
    for i in word_union:
        if i in word_2:
            vector_2.append(1)
        else:
            vector_2.append(0)

    # 根据余弦公式计算余弦向量
    denominator = 0
    a = 0
    b = 0

    for x, y in zip(vector_1, vector_2):
        denominator += x * y
        a += x * x
        b += y * y
    
    return denominator / (math.sqrt(a) * math.sqrt(b))
