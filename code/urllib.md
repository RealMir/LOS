# urllib
: 파이썬은 URL과 웹 요청에 관련된 모듈들을 urllib(URL 관련 라이브러리라는 의미)이라는 패키지로 묶어 제공함
+ <strong>urllib.request</strong> : HTTP 요청 기능을 담은 모듈
+ <strong>urllib.parse</strong> : URL 해석·조작 기능을 담은 모듈

## urllib.request
```python
import urllib.request

# 요청할 URL 변수 선언
url = "< 요청할 URL >" 

/* urllib.request.urlopen() 함수는 웹 서버에 정보를 요청한 후, 돌려받은 응답을 저장하여 ‘응답 객체(HTTPResponse)’를 반환한다.
*/
response = urllib.request.urlopen(url)         
text_data = response.read()                    

print(text_data)
```

## urllib.parse


<참고> [Python urllib 참고 자료](https://python.bakyeono.net/chapter-11-5.html)
