from pymystem3 import Mystem
import os, re, json, sys
import codecs
import glob
from os import path

'''
Читаем txt с текстами, используем майстем для лемматизации и выделения грамматических признаков
'''

mystem = Mystem()
grammarTextMystem = open('grammarsM.json', 'w')
#lemmasTextMystem = open('lemmasW.json', 'w')

for file in glob.glob('/home/haniani/diploma/w/*.txt'):
    f = path.splitext(file)
    with codecs.open(file, 'r', encoding="utf-8", errors='ignore') as files:
        readFiles = files.readlines()
        readFiles = str(readFiles)
        readFiles = re.sub(r'\\n|\\r', ' ', readFiles)
        #lemmas = mystem.lemmatize(readFiles)
        #lemmasTextMystem.write(json.dumps(lemmas, ensure_ascii=False))
        #lemmasTextMystem.write(str(lemmas))
        grammar = mystem.analyze(readFiles)
        grammarTextMystem.write(json.dumps(grammar, ensure_ascii=False))

grammarTextMystem.close()
#lemmasTextMystem.close()
sys.exit()