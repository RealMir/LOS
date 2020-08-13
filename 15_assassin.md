## Q15. assassin _ LIKE 활용
<img src="/photo/prob_15.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: ' <br> 문제 사항: id='admin' 호출하기
### 해결책

```
싱글쿼터가 제한됨
=> 문자열을 탈출 X
=> 평소에 못봤던 LIKE에 대해 조사함
=> LIKE 조건에 대해 알게됨
=> llie '<문자>%'로 패스워드 찾음
=> 문자 여러개 넣어봄
=> 반복되는 작업이므로 파이썬 코드를 이용함
```
```diff
# 현재 쿼리문: where pw like '9%'
```
<참고> Python 코드 : [패스워드 문자 탐색](code/15_pw.py)
```
해결 쿼리문: where pw like '902%'
```
### CERT <br> Python 코드 : [패스워드 문자 탐색](code/15_pw.py)

### 느낀점
```diff
+ LIKE에 대해 새롭게 알게 되었다.
+ LIKE조건
+ '_' : 글자 숫자를 정함 ex) A_ ( A로 시작하는 두글자 문자열 )
+ '%' : 글자 숫자를 안정함 ex) A% ( A로 시작하는 문자열 )
```
