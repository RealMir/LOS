## Q23.hell_fire _ order by 활용 (2)
<img src="/photo/prob_23.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: proc / union <br> 문제 사항: admin의 이메일을 찾아라.
### 해결책
```
이전 문제들과 달리 테이블을 보여줌
order by 뒤에 GET값을 보낼 수 있음
=> 조건을 이용해 참일 때는 정렬후 위쪽에 표시됨 
=> 거짓일 때는 정렬후 아래쪽에 표시되야한다고 생각함 
```
```diff
# 현재 쿼리문: where 1 order by (id='admin') desc
```
```
위의 쿼리에 email길이에 대한 쿼리문 추가
=> length()함수 이용 ( 파이썬 사용 )
=> 밑의 쿼리가 위에 정렬되므로 이메일 길이 = 28
```
```diff
# 현재 쿼리문: where 1 order by (id='admin' and length(email)=28) desc
```
<참고> Python 코드 : [이메일 길이 탐색](code/23_pwlength.py)
```
다음으로 이메일 각자리의 문자 확인
=> substr()함수, ascii()함수 이용 ( 파이썬 사용 )
```
```diff
# 현재 쿼리문: where 1 order by (id='admin' and ascii(substr(email,1,1))=97) desc
```
<참고> Python 코드 : [이메일 길이 탐색](code/23_pw.py)
```
해결 쿼리문: where id='admin' and email='admin_secure_email@emai1.com'
```
### CERT <br> Python 코드 : [이메일 길이 탐색](code/23_pwlength.py) / [이메일 문자 탐색](code/23_pw.py)
