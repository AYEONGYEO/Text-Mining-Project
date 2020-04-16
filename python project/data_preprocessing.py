# -*- coding:utf-8 -*-
# 데이터 정체 - 형태소 분석, 명사 추출, 불용어 처리
# 엘라스틱서치에서 가져온 index는 dic type
import pandas as pd
import json
from konlpy.tag import Mecab
import MeCab
import os

# mecab - 형태소 분석
def m_analysis(data_list):
    print("morpheme analysis start")
    morpheme_list = []
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic')

    # for data in data_list:
    #     morpheme = m.parse(data)
    #     morpheme_list.append(morpheme)

    for data in data_list:
        morpheme = m.parse(data[0])
        morpheme_list.append([morpheme, data[1], data[2]])

    print(morpheme_list)
    return morpheme_list

# konlpy - 명사 추출
def noun_extraction(data_list):
    print("noun_extraction start")
    nouns_list = []
    mecab = Mecab()

    for data in data_list:
        noun = mecab.nouns(data[0])
        nouns_list.append([noun, data[1], data[2]])

    # print(json.dumps(nouns_list, ensure_ascii=False, indent=3))
    return nouns_list

# stop word(불용어) 처리
# stop word file 수정해야 함!
def stopword(nouns_list):
    print("stopword start")
    stopwords_path = '/home/ayyeo/ayProject/trunk/demo/stop.txt'
    f = open(stopwords_path, encoding='cp949')
    stopwords = f.read()
    stopwords = stopwords.split('\n')
    # print("#"*50)
    # print(stopwords)

    num = len(nouns_list)

    result = []
    i =0

    # 각 기사마다 불용어 제거
    while i < num:
        nouns = nouns_list[i][0]
        tem = [word for word in nouns if not word in stopwords]
        result.append([tem, nouns_list[i][1], nouns_list[i][2]]) ### url 추가 중

        i += 1

    # print(json.dumps(result, ensure_ascii=False, indent=3))
    print("stopword process success")
    return result