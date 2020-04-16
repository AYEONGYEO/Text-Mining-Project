# -*- coding:utf-8 -*-
# mysql 연결 및 저장
# mysql 저장 or 새로운 table 만들때 미리 작업해두고 character set = utf8mb4 지정하기
import pymysql
from sqlalchemy import create_engine
from datetime import datetime, timedelta

pymysql.install_as_MySQLdb()
import MySQLdb

# database connection setting
def db_info():
    db = pymysql.connect(
        host='0.0.0.0',
        port=3306,
        user='root',
        passwd='passwd',
        db='dbname',
        charset='utf8',
        use_unicode=True
    )
    return db

# mysql module 중 info 다음 첫번째로 실행
# ES 에서 index 선택 후 가져온 데이터
# 데이터 정제 후 결과(단어들) mysql 저장
def nouns_store(nouns_result):
    db = db_info()

    try:
        # coursor = control structure of database
        # column이름만 참조변수로 가져 올 수 있음
        with db.cursor() as cursor:
            sql_c ="""
                CREATE TABLE CRAWLINGRESULT_TB (
                    id integer auto_increment primary key,
                    nouns VARCHAR(300),
                    date DATE,
                    url VARCHAR(300)
                )
            """
            sql = """
                INSERT INTO CRAWLINGRESULT_TB(nouns, date, url)
                VALUES(%s, %s, %s)
            """

            cursor.execute(sql_c)

            for nouns in nouns_result:
                sen = " ".join(nouns[0]) # list to string with space
                cursor.execute(sql, (sen, nouns[1], nouns[2]))

            db.commit()
    finally:
        print("nouns_store() 실행 - 데이터 정제 후, mysql에 각 기사의 명사들 저장")
        db.close()

# 날짜 선택해서 검색 -> 이 데이터를 가지고 tf 값 계산
# es -> 정제 후 mysql에 저장 = crawlingResult table
# mysql에서 단어 검색
def search_in_crawlingResult_by_date():
    db = db_info()

    s_date = datetime(2020, 3, 30)  #  숫자 앞의 0은 빼야함
    e_date = datetime(2020, 4, 5)
    s_date = datetime.strftime(s_date, '%Y%m%d')
    e_date = datetime.strftime(e_date, '%Y%m%d')

    # datetime.strftime(s_date, '%Y%m%d')

    date = "from" + s_date + "to" + e_date
    try:
        # with db.cursor(pymysql.cursors.DictCursor) as cursor: # rows data - dic type
        with db.cursor() as cursor:
            sql = """
                SELECT nouns
                FROM CRAWLINGRESULT_TB
                WHERE date BETWEEN %s AND %s
            """

            cursor.execute(sql, (s_date, e_date)) # 기간 설정하고 싶을 때
            rows = cursor.fetchall() # rows type = tuple

            # for row in rows:
            #     print(row)
            print("mysql에서 가져온 기사의 개수 : %d"%len(rows))
    finally:
        db.close()

    return rows, date

#  tf 값 계산 하기 위해 mysql에서 단어 검색
# crawlingResult 전체 값 계산
def search_in_crawlingResult_oneday(day):
    db = db_info()

    try:
        # with db.cursor(pymysql.cursors.DictCursor) as cursor: # rows data - dic type
        with db.cursor() as cursor:
            sql = """
                SELECT nouns
                FROM CRAWLINGRESULT_TB
                WHERE date = %s
            """

            cursor.execute(sql, day)
            rows = cursor.fetchall() # rows type = tuple
            # for row in rows:
            #     print(row)
    finally:
        db.close()
    return rows

# tf 계산시 원하는 날짜 만큼 계산하기 위해
# 날짜 값 입력
def search_by_date():

    s_date = datetime(2020,3,8)   # 하루 전 날짜 입력, 다음날 부터 계산됨 / 숫자 앞의 0은 빼야함
    e_date = datetime(2020,4,9)

    # real_s_date = s_date + timedelta(days=1)
    day_list = []

    days = (e_date-s_date).days

    for i in range(days):
        s_date = s_date + timedelta(days=1)
        day = datetime.strftime(s_date, '%Y%m%d')
        day_list.append(day)

    # date1 = datetime.strftime(real_s_date, '%Y-%m-%d')
    # date2 = datetime.strftime(e_date, '%Y-%m-%d')

    return day_list

# tf 계산한 값 dataframe type -> store to mysql
def store_tf_value(df_tf, date):
    try:
        table_name = "WORDTF_" + date + "_TB"
        engine = create_engine("mysql://root:password@ipadress:portnumber/dbname?charset=utf8mb4",
                               pool_pre_ping=True,
                               encoding='utf8'
                               )
        con = engine.connect()
        df_tf.to_sql(table_name, con, if_exists="append", index=False)  # if_exists options - append, fail, replace
        # ALTER TABLE table_name CONVERT TO character SET utf8; # 한글 값 입력시 테이블 char type 한번 더 확인

        print(table_name + "  mysql 저장 완료")

    except:
        print("store TF value fail")
    finally:
        con.close()

def store_topword_ngram(df_tf):
    try:
        engine = create_engine("mysql://root:password@ipadress:portnumber/dbname?charset=utf8mb4",
                               pool_pre_ping=True,
                               encoding='utf8'
                               )
        con = engine.connect()
        df_tf.to_sql('TOPWORDNGRAM_TB', con, if_exists="append", index=False)  # if_exists options - append, fail, replace
        # ALTER TABLE table_name CONVERT TO character SET utf8; # 한글 값 입력시 테이블 char type 한번 더 확인

        print("top word ngram TF mysql 저장 완료")

    except:
        print("store top word ngram fail")
    finally:
        con.close()


# word TF 에서 top 10 단어 가져오기
def search_top():
    db = db_info()

    try:
        with db.cursor() as cursor:
            sql = """
                SELECT noun
                FROM WORDTF_from20200309to20200409_TB
                LIMIT 10
            """

            cursor.execute(sql)
            rows = cursor.fetchall() # tuple type

            # for row in rows:
            #     print(row)

    finally:
        db.close()

    return rows

def make_list(word_data):
    try:
        # word_data = tuple
        corpus = []
        for row in word_data:
            tem = list(row)
            corpus.extend(tem)

        # print(corpus)
        return corpus

    except:
        print("error in make list function")
