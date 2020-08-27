import sys
import re
import xml.etree.ElementTree as ET
import json.decoder as DE
sys.path.append('C:\jupyter_notebook\pyhanspell')
from hanspell import spell_checker

def refine_sentence(text):
    text = re.sub(pattern='([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' , repl='', string=text)#E-mail제거
    text = re.sub(pattern='(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', repl='', string=text)#URL 제거
    text = re.sub(pattern='([ㄱ-ㅎㅏ-ㅣ]+)' , repl='', string=text)#한글 자음 모음 제거     
    text = re.sub(pattern='<[^>]*>' , repl='', string=text)#태그 제거
    text = re.sub(pattern=r'\([^)]*\)', repl='', string=text)#괄호와 괄호안 글자 제거
    #text = re.sub(pattern='[^\w\s]' , repl='', string=text)#특수기호 제거
    return text

#ratings_test.txt에서 data를 read하고 pyhanspell을 적용
#preprocessing된 data를 preprocessed_ratings_test.txt에 write
with open('preprocessed_ratings_test.txt','w',encoding='utf-8') as fd:
    with open('ratings_test.txt','r',encoding='utf-8') as fdd:
        texts = fdd.readlines()[1:]
        for i,text in enumerate(texts):
            try:
                text_split = text.split()
                first = text_split[0]
                last = text_split[-1]
                text = refine_sentence(' '.join(text.split()[1:-1]))
                text.encode('utf-8')
                fd.write(first + ' ' + spell_checker.check(text).checked + ' ' + last +'\n')
            except (ET.ParseError, DE.JSONDecodeError) as e:
                fd.write(first + ' ' + text + ' ' + last +'\n')