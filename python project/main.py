# -*- coding:utf-8 -*-
# main 함수

import datetime

# 모듈 연결
import es
import crawler
import df_export
import data_preprocessing
import mysql
import tfidf
import ngram

# main 시작
def main():

    # 크롤러 실행
    article_data = crawler.crawling()
    
    # elasticsearh 크롤링 원문 데이터 저장
    sotre_index = input("엘라스틱 서치에 저장 할 index 이름을 입력하시오 :  ")
    es.store(sotre_index, article_data)
    
    # elastiesarch index 검색
    search_index = input("엘라스틱 서치에서 검색 할 index 이름을 입력하시오 :  ")
    index = es.search(search_index) # es에서 검색한 결과
    data_list = es.convert_to_list(index) # es _source(data value) 만 가져와서 list로 변환
    
    # datapreprocessing 1. 형태소 분석 2.명사 추출  2-1. 불용어 처리
    # 1. 형태소 분석
    # data_preprocessing.m_analysis(data_list)
    # 2. 명사 추출
    nouns_list = data_preprocessing.noun_extraction(data_list)
    # 2-1. 불용어 처리 ( 명사 추출 한 결과)
    result = data_preprocessing.stopword(nouns_list)

    # result store in mysql - 불용어 처리 결과 저장
    mysql.nouns_store(result)

    # tf 계산
    words = mysql.search_in_dataResult() # tf 계산하기 위한 noun column만 가져오기
    df_tf = tfidf.cal_tf(words) # tf 값 계산
    mysql.store_tf_value(df_tf) # tf dataframe(id, noun, count) 저장
   
    # TFIDF vector - sklearn
    # corpus = tfidf.make_list_for_tfidf(words)
    # tfidf.cal_vector(corpus)
    
    # ngram - top word 연관검색어 함수 실행
    realted_keyword()

def realted_keyword():
    print("search realted keyword and make TF of keyword ngram")
    words, date = mysql.search_in_crawlingResult_by_date() # 모든 기사 정보, ngram 비교 하기 위함
    corpus = mysql.make_list(words)

    top_words = mysql.search_top() # top word 10개
    top_words_list = mysql.make_list(top_words)

    # top word list - 10개
    for word in top_words_list:
        word_ngram = ngram.top_word(corpus, word)
        topword_ngram = tfidf.cal_ngram_tf(word_ngram, word)
        mysql.store_topword_ngram(topword_ngram)

def only_crawling():

    # 크롤러 실행
    article_data = crawler.crawling()

    # elasticsearh 크롤링 원문 데이터 저장
    # sotre_index = input("엘라스틱 서치에 저장 할 index 이름을 입력하시오 :  ")
    es.store("olympic", article_data)

def after_crawling():
    # elastiesarch index 검색
    # search_index = input("엘라스틱 서치에서 검색 할 index 이름을 입력하시오 :  ")
    index = es.search("olympic")  # es에서 검색한 결과
    data_list = es.convert_to_list(index)  # es _source(data value) 만 가져와서 list로 변환

    # datapreprocessing 1. 형태소 분석 2.명사 추출  2-1. 불용어 처리
    # 1. 형태소 분석
    # data_preprocessing.m_analysis(data_list)
    # 2. 명사 추출
    nouns_list = data_preprocessing.noun_extraction(data_list)
    # 2-1. 불용어 처리 ( 명사 추출 한 결과)
    result = data_preprocessing.stopword(nouns_list)

    # result store in mysql - 불용어 처리 결과 저장
    mysql.nouns_store(result)

def tf_func_oneday():
    # tf 계산
    day_list = mysql.search_by_date()

    for day in day_list:
        words = mysql.search_in_crawlingResult_oneday(day)  # tf 계산하기 위한 noun column만 가져오기
        df_tf = tfidf.cal_tf(words)  # tf 값 계산
        mysql.store_tf_value(df_tf, day)  # tf dataframe(id, noun, count) 저장

    # TFIDF vector - sklearn
    # corpus = tfidf.make_list_for_tfidf(words)
    # tfidf.cal_vector(corpus)

    # ngram - top word 연관검색어 함수 실행
    # realted_keyword()

def tf_func_by_date():

    words, date = mysql.search_in_crawlingResult_by_date()    # 함수 안에서 날짜 범위 입력하기
    df_tf = tfidf.cal_tf(words)  # tf 값 계산
    mysql.store_tf_value(df_tf, date)  # tf dataframe(id, noun, count) 저장


# only_crawling()
# 크롤링 이후 과정 쭉 실행 - 현재까지 성공
# after_crawling()
# tf_func_oneday()
tf_func_by_date()
# realted_keyword()

# if __name__ == "__main__":
#     main()
