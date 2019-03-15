import jieba
import jieba.posseg as pseg
import jieba.analyse
from optparse import OptionParser

s = '五年前，最美女教师张丽莉为救学生被车碾压双腿致高位截瘫，当时的张丽莉老师刚结婚不久，还没有孩子。在交通事故前，张丽莉与丈夫' \
    '曾经怀过一个孩子，但是由于工作劳累，孩子没有保住，本来打算送完学生毕业就打算要一个孩子，却不想出了车祸，之后张丽莉想着要跟丈夫离婚，但是丈夫不同意。'

word_flags = pseg.cut(s)

print(word_flags)
peoples = set()
n = set()
verb = set()
time = set()
num = set()
for word, flag in word_flags:
    print(word, flag)
    if len(word) < 2:
        continue
    if flag == 'nr':
        peoples.add(word)
    elif flag == 'n':
        n.add(word)
    elif flag == 'v':
        verb.add(word)
    elif flag == 'm':
        num.add(word)
    elif flag == 't':
        time.add(word)
print('peoples:', peoples)
print('n:', n)
print('verb:', verb)
print('num:', num)
print('time:', time)

topK = 3
tags = jieba.analyse.extract_tags(s, topK=topK)
print(','.join(tags))
