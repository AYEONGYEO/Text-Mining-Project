# -*- coding:utf-8 -*-
# naver news crawler
# linux os

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json

# Search options
# Make URL for what you want to search
# only for Naver news - The URL form is different depends on search engine
# query, max_page, sort, s_date(start date), e_date(end date)
# sort - 0 : Relevance 1 : Newest 2 : Oldest
def crawling_set():
    # query = input("what you want to search : ")
    # max_page = input(" input the max page : ")

    # test setting
    # Search result : Search "query" and crawl "max_page" in order of "sort" by date
    query = "서울"
    max_page = 5
    sort = "0"
    s_date = datetime(2020,4,4)      # Remove 0 in front of months, days  # Write a day ago
    e_date = datetime(2020,4,6)         # the result to search from 2020.04.05 to 2020.04.06

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

# crwaler function
# Increase sleep time when you use for real like scarp lots of data
def crawling():
    # Install chrome web driver in your computer or server
    # And check the path and edit excutable_path in Linux selenium setting
    # path = "D:/chromedriver"  # in my case, for window test
    # driver = webdriver.Chrome(path)

    # Linux selenium setting
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)

    # get crawling search options from craling_set()
    day_list, date1, date2, days, query, max_page, sort = crawling_set()

    print("*************start crawler*********************")
    print("Search date : %s ~ %s (total %d days)" %(date1, date2, days))
    print("Search word : %s / Number of pages : %d" %(query, max_page))
    print("")


    # declare
    article_data = []   # list reset for storing result after crawling

    try:
        # the data from crawling_set()
        # Start crawling repeatedly for the entered period
        for day in day_list:
            page = 0                            # page count reset
            day_str = day.replace(".", "")      # ex) 20200403
            store_day = day.replace(".", "-")   # ex) 2020-04-03
            driver.implicitly_wait(5)

            print("")
            print("article of %s crawling start -> "%day)

            # repeat numbers of max page by each date
            # get each html page source
            # make the list for each data you need
            # - the result list catalog
            # = journal(newspaper), article title, link of article, link of naver news, summary
            while page < max_page:
                print("Crawling %d page" %(page+1))

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

                # reset list for storing each html data
                journal_list = []
                date_list = []
                title_list = []
                summary_list = []
                urls_list = []

                # soup select -> have html code
                journal_list.extend(soup.select('span._sp_each_source'))   # newspaper
                date_list.extend(soup.select('dd.txt_inline'))              # date of article
                title_list.extend(soup.select('a._sp_each_title'))       # article title + url of article and etc
                summary_list.extend(soup.select('.type01 > li > dl > dd:nth-of-type(2)'))    # summary
                urls_list.extend(soup.select('a._sp_each_url'))      # url of naver news article

                article_num = len(journal_list)
                page += 1

                # value of each article list
                # make one list to get specific value like text, url or etc
                # create a new list by combining each data repeat by the total number of articles
                # number of articles = 10 / there are 10 articles in one page of naver news section
                for num in range(article_num):
                    c_journal = journal_list[num].text
                    c_date = store_day
                    c_title = title_list[num].text
                    c_summary = summary_list[num].text
                    c_article_url = title_list[num].get('href')
                    c_naver_url = urls_list[num].get('href')

                    # If you want to refine the data of article date from crawling result
                    # Test data_cleansing() function
                    # It made to refine the sentence like one hour ago
                    # c_date = date_cleansing(date_list[num].text)

                    # Create a new list with the extracted content
                    article = [c_journal, c_date, c_title, c_summary, c_article_url, c_naver_url]
                    article_data.append(article)        # Append to the final result list

            # print("*"*80)
            # repeat numbers of max page by each date end

        # crawling repeatedly for the entered period end

        # print (json.dumps(article_data, ensure_ascii=False, indent=3))
        print("")
        print("We crawled a total of %d articles"%len(article_data))
        return article_data

    except:
        print ("crawler error")

# date type regular expression
def date_cleansing(test):
    try:
        # print("date cleansing start")
        pattern = '\d+.(\d+).(\d+).'    # make regular expression for date type
        r = re.compile(pattern)
        match = r.search(test).group(0)  # ex) 2018.11.05.
        return match

    except AttributeError:
        # If the date type is not like pattern  ex) one hour ago
        # Write today's date
        return datetime.today().strftime("%Y-%m-%d")

