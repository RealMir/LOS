# urllib
: 파이썬은 URL과 웹 요청에 관련된 모듈들을 urllib(URL 관련 라이브러리라는 의미)이라는 패키지로 묶어 제공함
+ <strong>urllib.request</strong> : HTTP 요청 기능을 담은 모듈
+ <strong>urllib.parse</strong> : URL 해석·조작 기능을 담은 모듈

## urllib.request
```python
import urllib.request

# 요청할 URL 변수 선언
url = "< 요청할 URL >" 

# urllib.request.urlopen() 함수는 웹 서버에 정보를 요청한 후,
# 돌려받은 응답을 저장하여 ‘응답 객체(HTTPResponse)’를 반환
response = urllib.request.urlopen(url)    

# read() 메서드는 웹 서버가 응답한 데이터를 읽어들임
text_data = response.read()                    

print(text_data)
```

## urllib.parse
```
URL : 인터넷 공간에 존재하는 자원을 가리키기 위한 절대 주소
URL에 사용할 수 있는 문자는 영문자, 숫자, 약간의 기호 뿐
그 밖의 문자(한글·한자·특수문자 등)는 사용 불가
=> URL에서 아스키 코드가 아닌 문자들을 퍼센트 인코딩(percent encoding) 형식으로 바꿔야함
=> urllib.parse.quote() : 한글 텍스트를 퍼센트 인코딩된 문자열로 변환
```

<참고> [Python urllib 참고 자료](https://python.bakyeono.net/chapter-11-5.html)
