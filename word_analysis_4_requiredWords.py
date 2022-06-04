import pandas as pd
import csv
import pprint
import matplotlib.pyplot as plt
import datetime
import dateutil.parser
import collections
#import neologdn
import emoji 
import re
import time
import MeCab

start_time = time.perf_counter()


text_list = []
times_list = []
num_date = []
all_text = []
required_words = []

with open('kafun0215.csv',  encoding= 'UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row != ['', 'ID', 'text', 'time']:
            text_list.append(row)
#print(text_list)
print(len(text_list))

# ISO8601形式の文字列をdatetimeに変換する。
JST = datetime.timezone(datetime.timedelta(hours =+9), "JST")

for i in text_list:
    i[3] = dateutil.parser.parse(i[3]).astimezone(JST)

for times in text_list:
    times_list.append(times[3])

#print(times_list)
#print(len(times_list))
tweet_num = len(times_list)

#削除する絵文字のunicode
emoji_pattern = re.compile("["
    u"\U00002700-\U000027BF"
    u"\U0001F650-\U0001F67F"
    u"\U0001F600-\U0001F64F"
    u"\U0001F300-\U0001F5FF"
    u"\U0001F680-\U0001F6FF"
    u"\U0001F1E0-\U0001F1FF"
    u"\U0001F900-\U0001F9FF"
    u"\U0001FA70-\U0001FAFF"

    "]+", flags=re.UNICODE)

for i in range(10):
    #print(text_list[i][2])
    text_list[i][2] = emoji_pattern.sub("", text_list[i][2])
    text_list[i][2] = re.sub(r"@(\w+) ", "", text_list[i][2]) 
    text_list[i][2] = re.sub(r"http\S+", "", text_list[i][2])
    text_list[i][2] = re.sub(r"\n","",text_list[i][2])
    text_list[i][2] = re.sub(r"\d+","0",text_list[i][2])  
    #all_text.append(text_list[i][2])

for i in range(1): 

    #MeCabでツイートひとつづつを形態素解析している。
    print(text_list[i][2])
    mecab = MeCab.Tagger()
    sent = text_list[i][2]
    sentense_analyzed = mecab.parse(sent)
    print(sentense_analyzed)
    #print(mecab.parse(sent))

    #"名詞-普通名詞-一般"の数を数えている。
    cnt = sentense_analyzed.count("名詞-普通名詞-一般")
    print(cnt)
    print(type(sent))

    #"助詞","助動詞","補助記号"を外す
    words_1 = sentense_analyzed.split("\n")[:-2]
    for j in words_1:
        if "助動詞" not in j and "助詞" not in j and "補助記号" not in j:       
            required_words.append(j)
    print(required_words)
    
end_time = time.perf_counter()
elapsed_time = end_time - start_time 
print(elapsed_time)


# 数字を０に 
#doc = re.sub(r'\d+', '0', doc)
# メンション除去 
#doc = re.sub(r"@(\w+) ", "", doc) 
# url除去 
#doc = re.sub(r"http\S+", "", doc)
#リツイートを消す
#doc = re.sub(r"(^RT.*)", "", doc, flags=re.MULTILINE | re.DOTALL)
# 大文字・小文字変換 
#doc = doc.lower()
#改行を消す
#doc = re.sub(r"\n","",doc)


#normalized_text = neologdn.normalize(text_list[0][2])
#print(text_list[0][2])
#print(doc)