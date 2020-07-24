## Q4. orc _ 
<img src="/photo/prob_04.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: X <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책

```
먼저 쿼리문이 참이 되도록 만들어 봄
=> 논리를 이용
```
```diff
# 현재 쿼리문: where id='admin' and pw='' || 1--+ '
```
```
but. admin은 표시되나 문제가 해결되지는 않음
문제 해결을 위해서는 admin의 패스워드가 필요함
=> 패스워드가 문자열이므로 sql 문자열 관련함수를 찾아봄
<참고> [sql 문자열 관련 함수](https://rh-cp.tistory.com/60) 
```
