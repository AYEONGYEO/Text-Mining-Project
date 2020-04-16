# -*- coding:utf-8 -*-
# 엘라스틱서치 모듈
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pandas as pd
import json
import sys

# elasticsearh 주소
es = Elasticsearch("http://0.0.0.0:9200")

# 엘라스틱 서치 저장
def store(index_name, article_data):
    # index 이름 중복 검사
    # if es.indices.exists(index = index_name):
    #     print("같은 이름의 index가 저장되어 있습니다")
    #     anwser = input("덮어 쓰기를 원하시면 y / 데이터를 추가 하길 원하시면 a / 나가기를 원하시면 n 를 입력하시오 \n>")
    #
    #     if anwser=='y':
    #         es.indices.delete(index=index_name)
    #         es.indices.create(index=index_name)
    #         # es.indices.refresh(index=index_name)
    #         print("같은 이름의 index 덮어쓰기를 완료하였습니다")
    #     elif anwser == 'a':
    #         print("데이터 추가를 입력하셨습니다")
    #         pass
    #     else:
    #         print("나가기를 입력하셨습니다")
    #         sys.exit(0)
    # else:
    #     es.indices.create(index = index_name, body={})

    es.indices.delete(index=index_name)
    es.indices.create(index=index_name)

    # 가져온 article_date list -> df 로 변환
    df = pd.DataFrame(article_data,
                      columns=[
                          "journal",
                          "date",
                          "title",
                          "summary",
                          "article_url",
                          "naver_url"
                      ])
    documents = df.to_dict(orient = 'records')
    print("%d개의 기사를 저장하였습니다" %len(documents))

    helpers.bulk(es, documents, index = index_name, doc_type='article', raise_on_error=True)
    print("elasticsearch 저장 완료 하였습니다")

# 엘라스틱 서치 - 인덱스 이름으로 데이터 검색
def search(index_name):
    # if es.indices.exists(index = index_name):
    # elasticsearch 검색 쿼리는 일치하는 항복이 더 있더라고 10개의 적중만 반환
    # 더 많은것을 반환하게 하려면 size 매개변수를 전달해야 한다
    res = es.search(
        index = index_name,
        body={
            "query": {"match_all": {}}
        },
        size = 10000
    )

    # res = es.search(
    #     index=index_name,
    #     body={
    #         "query": {
    #             "bool": {
    #               "should": [
    #                 { "match": { "date": "2020-04-03" } },
    #                 { "match": { "date": "2020-04-04" } },
    #                 { "match": { "date": "2020-04-05" } }
    #               ]
    #             }
    #           }
    #     },
    #     size=10000
    # )
    # print(res)
    print("elasticsearch 에서 입력한 index 데이터를 가져왔습니다")
    return res

# data_preprocessing 을 위해 엘라스틱서치에서 가져온 데이터 list로 변환
def convert_to_list(res):
    data_list = []
    index_data = res['hits']['hits']

    count = len(index_data)
    # index에 저장된 총 기사 개수 만큼
    # for index in index_data:
    #     # print(index['_source'])
    #     # print("*" * 50 + "\n")
    #     sen = index['_source']['title'] + index['_source']['summary']
    #     data_list.append(sen)

    for index in index_data:
        # print(index['_source'])
        # print("*" * 50 + "\n")
        sen = index['_source']['title'] + index['_source']['summary']
        date = index['_source']['date']
        url = index['_source']['article_url']
        data_list.append([sen, date, url])


    # + 엘라스틱 서치에서 가져온 dic 중 특정 값 하나 가져오기
    # print(res['hits']['hits'][0]['_source']['date'])
    # print(data_list)
    print ("엘라스틱에서 가져온 기사 개수 : %d" %count )
    return data_list



