# -*- coding:utf-8 -*-
# 네이버 뉴스 크롤러
# linux os

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

def main():
    crawilng_result = crawling()
    print(crawilng_result)

# 검색 옵션
# 검색을 위한 url 을 만드는 함수
# 네이버 뉴스에서만 작성하며, 다른 검색엔진을 위한 테스트는 url 및 html 코드 파싱 부분을 변경해야 함
# query, max_page, sort, s_date(start date), e_date(end date)
# sort - 0 : 관련도순 1 : 최신순 2 : 오래된순
def crawling_set():
    # query = input("what you want to search : ")
    # max_page = input(" input the max page : ")

    # test setting
    # 검색 결과 - 서울 검색하여, 각 날짜별 관련도순으로 5페이지씩 크롤링
    query = "서울"
    max_page = 5
    sort = "0"
    s_date = datetime(2020,4,4)      # 달, 일 숫자 앞에 0을 입력 X # 하루 전 날짜 입력
    e_date = datetime(2020,4,6)         # 테스트 결과 검색하는 날짜는 2020.04.05 to 2020.04.06

    real_s_date = s_date + timedelta(days=1)
    day_list = []

    days = (e_date-s_date).days

    for i in range(days):
        s_date = s_date + timedelta(days=1)
        day = datetime.strftime(s_date, '%Y.%m.%d')
        day_list.append(day)

    date1 = datetime.strftime(real_s_date, '%Y.%m.%d')
    date2 = datetime.strftime(e_date, '%Y.%m.%d')

    return day_list, date1, date2, days, query, max_page, sort

# 크롤러 함수
# 실제 사용시 sleep 시간 늘려주기
def crawling():
    # Linux selenium setting
    # 리눅스에 chrome web driver 설치 후 excutable_path 수정하기
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)

    # 크롤링 검색 option 가져오기
    day_list, date1, date2, days, query, max_page, sort = crawling_set()

    print("*************크롤러를 실행 하였습니다*********************")
    print("검색 날짜 : %s ~ %s (총 %d일)" %(date1, date2, days))
    print("검색어 : %s / 각 날짜 별 페이지 수 : %d" %(query, max_page))
    print("")

    # declare
    article_data = [] # 크롤링 후 결과 저장 리스트 초기화

    try:
        # crawling_set() 에서 가져온 정보
        # 입력한 기간동안 크롤러 실행
        for day in day_list:
            page = 0    # page count 초기화
            day_str = day.replace(".", "")      # ex) 20200403
            store_day = day.replace(".", "-")   # ex) 2020-04-03
            driver.implicitly_wait(5)

            print("")
            print("%s 날짜의 기사 크롤링 시작 -> "%day)

            # 각 날짜의 max page 수 만큼
            # 각 페이지 html 소스 받아오기
            # 필요한 데이터 별 리스트 만들기
            # - 리스트 목록 : 신문사, 기사 제목, 기사 링크, 네이버 뉴스 링크, 요약문
            while page < max_page:
                print("%d 번째 페이지 크롤링 중" %(page+1))

                driver.implicitly_wait(3)
                url = "https://search.naver.com/search.naver?where=news" \
                      "&query=" + query \
                      + "&sort=" + sort \
                      + "&ds=" + day \
                      + "&de=" + day \
                      + "&nso=so%3Ar%2Cp%3Afrom" + day_str \
                      + "to" + day_str \
                      + "%2Ca%3A" \
                      + "&start=" + str(page * 10 + 1)

                # print(url)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                # time.sleep(1)

                # 각 html data 저장할 리스트 초기화
                journal_list = []
                date_list = []
                title_list = []
                summary_list = []
                urls_list = []

                # soup select -> html 코드를 가지고 있음
                journal_list.extend(soup.select('span._sp_each_source'))   # 신문사
                date_list.extend(soup.select('dd.txt_inline')) # 기사 날짜
                title_list.extend(soup.select('a._sp_each_title'))  # 기사 제목 + 신문사 기사 url 등
                summary_list.extend(soup.select('.type01 > li > dl > dd:nth-of-type(2)'))  # 요약문
                urls_list.extend(soup.select('a._sp_each_url'))  # 네이버 뉴스 기사 url

                article_num = len(journal_list)
                page += 1

                # 기사의 각 리스트 값
                # text, url 등 원하는 값을 뽑아 각 기사 별 하나의 리스트로 정리
                # 총 기사 개수만큼, 각 데이터를 통합하여 새로운 리스트
                # article_num = 10, 네이버 뉴스는 한페이지 당 10개의 기사를 가지고 있음
                for num in range(article_num):
                    c_journal = journal_list[num].text
                    c_date = store_day
                    c_title = title_list[num].text
                    c_summary = summary_list[num].text
                    c_article_url = title_list[num].get('href')
                    c_naver_url = urls_list[num].get('href')

                    # 현재는 입력받은 날짜로 리스트에 값을 추가하지만, html에서 가져온 날짜로 값을 추가하고 싶다면
                    # 아래 data_cleasing() 함수 테스트
                    # 네이버 기사 날짜에서 표현하는 1시간 전과 같은 날짜를 변환 함
                    # c_date = date_cleansing(date_list[num].text)

                    # 추출 한 내용으로 새로운 리스트 생성
                    article = [c_journal, c_date, c_title, c_summary, c_article_url, c_naver_url]
                    article_data.append(article) # 최종 리스트에 저장
            # print("*"*80)
            # 각 날짜의 max page 수 만큼 end

        # 검색을 원한 모든 날짜 크롤링 end

        # print (json.dumps(article_data, ensure_ascii=False, indent=3))
        print("")
        print("총 %d개의 기사를 크롤링 하였습니다"%len(article_data))
        return article_data

    except:
        print ("crawler error")

# 날짜 정규표현식
def date_cleansing(test):
    try:
        # print("date cleansing start")
        pattern = '\d+.(\d+).(\d+).'  # 정규표현식
        r = re.compile(pattern)
        match = r.search(test).group(0)  # ex) 2018.11.05.
        return match

    except AttributeError:
        # 위와 같은 type 이 아닐시 ex) 1시간 전
        # 오늘 날짜 기입
        return datetime.today().strftime("%Y-%m-%d")


if __name__ == "__main__":
    main()