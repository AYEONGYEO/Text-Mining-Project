# -*- coding:utf-8 -*-
# ngram 
# top 키워드로 앞 뒤 단어들 찾아서 tf 값 계산하기 = 연관검색어

def top_word(corpus, search_word):
    # corpus = 기사 전체, search_word = 검색 할 키워드
    print("ngram top word start -  ( %s ) 에 대해 모든 기사에서 검색 합니다" %search_word)
    word_ngram = []           # 모든 기사에서 ngram 검색하여 결과 저장
    # article_num = len(corpus)         # 기사 총 개수

    count = 0
    try:
        # 가져온 전체 기사
        # 각 기사 별
        for article in corpus:
            word_list = article.split()          # spilt -> list

            # 한개의 기사 안에 있는 단어 리스트
            for i, word in enumerate(word_list):       # enumerate 연산자 - list index, value 동시에 가져올 수 있음

                if word == search_word:
                    count += 1    # search word 검색된 수
                    word_ngram.extend(store(i, word_list))

        # print("총 %d 개의 기사 중 %d 번 검색 되었습니다(중복 허용)" %(article_num, count))
        # print (word_ngram)
        return word_ngram

    except:
        print ("ngram, top_word error")

    # ngra, 키워드 양옆에 있는 단어 저장
def store(i, word_list):
    find_word = []

    if i == 0:
        find_word.append(word_list[i + 1])
        find_word.append(word_list[i + 2])
    elif i == 1:
        find_word.append(word_list[i - 1])
        find_word.append(word_list[i + 1])
        find_word.append(word_list[i + 2])
    elif i == len(word_list) - 1:
        find_word.append(word_list[i - 1])
        find_word.append(word_list[i - 2])
    elif i == len(word_list) - 2:
        find_word.append(word_list[i - 1])
        find_word.append(word_list[i - 2])
        find_word.append(word_list[i + 1])
    else:
        find_word.append(word_list[i - 1])
        find_word.append(word_list[i - 2])
        find_word.append(word_list[i + 1])
        find_word.append(word_list[i + 2])

    # print("한개의 기사 안에서 가져온 단어")
    # print(find_word)
    
    return find_word