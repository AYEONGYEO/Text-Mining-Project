# -*- coding:utf-8 -*-
# tf idf 값 계산
# sklearn vector 이용

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from collections import Counter
import pandas as pd
import json

# 문서 전체 단어 빈도수 계산
def cal_tf(word_data):
    #word_data = tuple type
    new = []

    for sen in word_data: # tupe type -> string , split ""
        test = " ".join(sen)    # test type = string
        new.append(test.split())    # 각 단어를 리스트에 추가, 완성된 new [] = 2차 리스트

    new = sum(new,[]) # 2차 리스트 -> 1차 리스트로 변환
    word_count_list = pd.Series(new)
    result = word_count_list.value_counts()
    percentage = (result.values / len(word_count_list)) * 100   # 전체 단어수에서 특정 단어 퍼센트

    df = result.to_frame() # series -> dataframe 변환
    df['percentage'] = percentage
    df = pd.DataFrame(df).reset_index() # index 초기화
    df.columns = ["noun", "count", "percentage"] # df column 지정

    return df

# top word ngram result - tf cal
def cal_ngram_tf(word_data, topword):
    try:
        word_count_liest = pd.Series(word_data)
        result = word_count_liest.value_counts()
        df = result.to_frame()  # series -> dataframe 변환
        df['topword'] = topword
        df = pd.DataFrame(df).reset_index()  # index 초기화
        df.columns = ["relatedword", "count", "topword"]  # df column 지정
        df = df[["topword", "relatedword", "count"]]

        return df

    except:
        print("error in calcurate ngram TF function")
    finally:
        print("calculate ngram TF start")




# sklearn(사이킷런) 으로 TF-IDF 값 계산
# 결과는 이차 행렬로 나타남
def cal_vector(corpus):
    # CountVectorizer
    # - 문서를 토큰 리스트로 변환
    # - 각 문서에서 토근의 출현 빈도 계산
    # - 각 문서를 BOW 인코딩 벡터로 변환 (array)
    vector = CountVectorizer()
    vector.fit_transform(corpus).toarray()
    print(vector.fit_transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
    # 각 단어의 인덱스가 어떻게 부여되었는지 보여줌
    print(sorted(vector.vocabulary_.items()))

    # TfidfVectorizer
    # - CountVectorizer 와 비슷하지만 TF-IDF 방식으로 단어의 가중치를 조정한 BOW 백터를 만든다
    tfidv = TfidfVectorizer().fit(corpus)
    tfidv.transform(corpus).toarray()
    print(tfidv.transform(corpus).toarray())
    # 각 단어의 인덱스가 어떻게 부여되었는지 보여줌
    # print(json.dumps(sorted(tfidv.vocabulary_.items()), ensure_ascii=False, indent=3))
