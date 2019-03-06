class intDict(object):
    """键为整数的字典"""

    def __init__(self, numBuckets):
        """创建一个空字典"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, key, dictVal):
        """假设key是整数。添加一个字典条目。"""
        hashBucket = self.buckets[key % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))

    def getValue(self, key):
        """假设key是整数。返回键为key的字典值"""
        hashBucket = self.buckets[key % self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'


import random

D = intDict(17)
for i in range(20):
    # 从0~10**5-1中选择一个随机整数
    key = random.choice(range(10 ** 5))
    D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets:
    # 破坏了抽象的屏障
    print(' ', hashBucket)
