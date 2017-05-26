# coding=utf-8
from functools import reduce
import re

'''
Считаем знаки препинания и количество предложений в тексте
'''
 
punkt = {
    '!' : 0,
    '?' : 0,
    ',' : 0,
    '.' : 0,
    '"' : 0,
    ':' : 0,
    ';' : 0,
    '…' : 0,
    '–' : 0,
    '—' : 0

}

file = open("m19.txt",)
s = reduce(lambda a, b : a + b, file.readlines())
sentences = filter(lambda a : a!="", re.split('[!.?]', s))
print(len(sentences))

result = re.findall(r'\.|\?|\,|\!|\:|\;|\…|\–|\—', s)
if result:
    result = [[i, ] for i in result]
    for elem in result:
        elem = str(elem).replace('[', '').replace(']', '').replace('\'', '')
        if str(elem) in punkt:
            punkt[elem] += 1

print(punkt)