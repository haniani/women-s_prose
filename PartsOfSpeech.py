import glob, codecs, re, json
from os import path

'''
Считаем встречаемость и прочие характеристики
'''
PartsOfSpeech = {
'A' : 0, #прилагательное
'ADV' : 0, #наречие
'ADVPRO' : 0, #местоименное наречие
'ANUM' : 0, #числительное-прилагательное
'APRO' : 0, #местоимение-прилагательное
'COM' : 0, #часть композита - сложного слова
'CONJ' : 0, #союз
'INTJ' : 0, #междометие
'NUM' : 0, #числительное
'PART' : 0, #частица
'PR' : 0, #предлог
'S' : 0, #существительное
'SPRO' : 0, #местоимение-существительное
'V' : 0 #глагол
}

for file in glob.glob('/home/haniani/diploma/mmm/*.txt'):
    f = path.splitext(file)
    with codecs.open(file, 'r', encoding="utf-8", errors='ignore') as files:
        for line in files:
            line = str(line)
            result = re.search(r'[A-Z]+', line)
            if result:
                result = format(result.group(0))
                if result in PartsOfSpeech:
                    PartsOfSpeech[result] += 1
            
print(PartsOfSpeech)
