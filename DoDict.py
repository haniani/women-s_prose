import glob, codecs, re, json
from os import path

WomenDictionary = open('MenDictionary.json', 'w')

d = "{"

for file in glob.glob('/home/haniani/diploma/*.txt'):
    f = path.splitext(file)
    with codecs.open(file, 'r', encoding="utf-8", errors='ignore') as files:
        for line in files:
            line = str(line)
            result = re.search(r'{[а-яА-Я]*=\w', line)
            reList = ''
            if result:
                result = format(result.group(0))
                perestanovka = re.sub(r'{', '\"', str(result))
                perestanovka2 = re.sub(r'=', '\":\"', str(perestanovka))
                perestanovka2 = perestanovka2 + '\"'
                d = d + perestanovka2  
                
d = d + "}"
WomenDictionary.write(json.dumps(d, ensure_ascii=False))