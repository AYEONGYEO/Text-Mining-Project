# -*- coding:utf-8 -*-
# dataframe export file - csv, excel, text
from datetime import datetime
import os

# 현재 시간, 저장 경로 설정
now = datetime.now()
output_time = '%s-%s-%s %sh %sm %ss ' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
path = '/home/ayyeo/ayProject/trunk/ '
# path = os.getcwd()  # 현재 파일 디렉토리 경로

def excel(df):
    df.to_excel(path + output_time + ".xlsx")
    print("excel 저장 완료")

def txt(df):
    df.to_csv(path + output_time +  ".txt", encoding="euc-kr")
    print("txt 저장 완료")

def csv(df):
    df.to_csv(path + output_time + ".csv", encoding="euc-kr")
    print("csv 저장 완료")


