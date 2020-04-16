# Text Mining Project   
문서 수집 (crawling) > 형태소 분석 (koNLPy) > 시각화 (web, spring-boot, wordcloud, amcharts)
- Developent enviroment setting

> python 3.x ver study   
> database - elasticsearch, mysql   
> web - spring boot 2.x ver with mybatis, thymeleaf, AM chart   
   
- functions (python 3.x)
> crawiling naver news   
> data preprocessing    
> calculate tf (term frequency)   
> calculate ngram (related search terms)  
   
***
### naver news crawler
this is using Korean   
- BuautifulSoup - bs4 and selenium   
- upload 4 version of crawling   
> korean window os   
> korean linux os   
> english window os   
> english linux os   

***
### project
총 10개의 파일  
실제 테스트를 위해서는 ex.py, mysql.py 에서 host, port, user, passwd, db 등 정보 입력해야 함   

|파일|설명|
|------|---|
|[main.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/main.py)|project 전체 main 함수 실행 시, 모든 코드 실행|
|[crawler.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/crawler.py)|네이버 뉴스 크롤링 기능|
|[data_preprocessing.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/data_preprocessing.py)|형태소 분석, 명사 추출, 불용어 처리 등 데이터 정제|
|[es.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/es.py)|elasticsearch 저장 및 검색|
|[df_export.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/df_export.py)|dataframe export to csv, excel, txt|
|[mysql.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/mysql.py)|mysql 저장 및 검색|
|[ngram.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/ngram.py)|연관검색어 기능 구현|
|[tfidf.py](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/tfidf.py)|단어 빈도수 계산, sklearn tfidf 행렬 값 계산|
|[stop.txt](https://github.com/YEONGYEO/Text-Mining-Project/blob/master/project/stop.txt)|불용어 text file|

***
# spring-boot-study
- Development environment setting

> spring boot 2.x ver (java 1.8 ver or above ver) </br>
> mysql </br>
> mybatis - DB connection</br>
> maven </br>
> thymeleaf </br>

- AM chart word cloud 
- 

* * *
## 개념 스터디
- RESTful API 이해 </br>
참고 링크 : <https://imasoftwareengineer.tistory.com/35>

RESTful API(Respresentational State Trasfer)  HTTP 리퀘스트를 이용해 데이터를 GET, POST, PUT, DELETE 할 수 있도록 하는 API를 의미한다. <br/>
GET, POST, PUT, DELETE를 리퀘스트 메서드라고 부른다.
     
 > GET - 데이터를 가져온다. <br/>
 > POST - 데이터를 생성하거나 업데이트한다. <br/>
 > PUT - 데이터를 업데이트한다. <br/>
 > DELETE - 데이터를 삭제한다. <br/>
   
- Ajax request 이해 </br>
1. Ajax란?</br>
Java 라이브러리 중 하나이며 Asynchronous Javascript And Xml(비동기식 자바스크립트와 xml)의 약자.</br>
브라우저가 가지고 있는 XMLHttpRequest 객체를 이용하여 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위해 데이터를 로드하는 기법.</br>
즉, JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고 받는 기술</br>

참고 링크 ( Ajax란 무엇인가? ) : <https://coding-factory.tistory.com/143>

2. 기본 문법   
<pre>
<code>
$.ajax({
    url: "",
    type: "",
    cache: ,
    dataType: "",
    data: "",
    success: function(data){
    },
    error: function (request, status, error){        
    }
  });
</code>
</pre>
   
> url : 요청 url   
> type : 데이터 전송 방식 GET or POST   
> cache : 요청 페이지의 캐시 여부 (false or true)   
> datatype : 서버에서 받아올 데이터를 어떤 형태로 해석 할 것인지 (xml,json,html,script)   
> data : 서버로 데이터를 전송할 때 사용   
> success : Ajax 통신에 성공했을 때 실행되는 이벤트   
> error : Ajax 통신에 실패했을 때 실행되는 이벤트 (request, status, error로 에러 정보 확인 가능)   
    
- HashMap   
Map interface를 implements 한 클래스로서, key와 value 가 하나의 쌍으로 구성되며, Hash 알고리즘을 사용하는 클래스이다.    
key는 유일성을 가지기 때문에 중복은 허용되지 않지만, key와 value는 null 값을 허용한다.    
특징 : Map의 순서를 보장하지 않는다
   
 참고 링크 ( HashMap으로 데이터 조회 ) : <https://elvis-note.tistory.com/entry/10-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EB%8B%AC%EB%B0%A9%EC%8B%9D-2-HashMap%EC%9C%BC%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A1%B0%ED%9A%8C>   
 ( controller, service, mapper, xml 다 나와있음 )   
   
- String Boot
1. Anotation   
     - @ResponseBody   
     view가 아닌 JSON 형식의 값을 응답할 때 사용하는 애노테이션으로 문자열을 리턴하면 그 값을 http response header가 아닌 response body에 들어간다.   
     만약 객체를 return하는 경우 JACKSON 라이브러리에 의해 문자열로 변환되어 전송된다.   
     context에 설정된 resolver를 무시한다고 보면된다. (viewResolver)   
     - @

2. Service와 ServiceImpl</br>
     - ServiceImpl</br>
     비즈니스 로직을 수행하는 역할, 기능을 구현하는 구현부 ex) 글 작성, 글 수정, 글 삭제, 글 조회 등 기능을 비즈니스 로직이라고 함.   
     class 파일로 작성   
     - Service</br>
     Interface 파일로 추상클래스의 역할   
     Service의 메서드명을 보고 '어떤 기능이 구현되어 있다'라고 유추 가능   
     - 1:N 구조에서 Interface 사용하는 것이 좋음   </br>
     게시물 목록을 조회한 상태에서 제목을 클릭하여, 상세내용을 보도록 하는 게시물 상세보기 기능, 게시물 내용 조회, 조회수 증가 등   
     하나의 작업으로 인해 n개 이상의 작업을 수행하거나, 추가될 예정인 경우 Interface를 생성하여 관리하는 것이 좋음.   

* * *
마크다운 사용법 : <https://gist.github.com/ihoneymon/652be052a0727ad59601>
