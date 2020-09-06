## Q14. giant _ Q5
<img src="/photo/prob_14.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: 공백문자 / \n / \r / \t <br> 문제 사항: 테이블 인식 시키기
### 해결책

```
현재 쿼리문에서 fromprob_giant로 from과 테이블명이 붙어있음
=> 테이블이 인식 X
=> from과 테이블간에 간격이 있어야함
=> +는 공백문자로 제한됨
=> 아스키코드의 공백문자인 0b, 0c 이용
```
```
해결 쿼리문: select 1234 fromrob_giant where 1
```
### CERT <br> ?shit=%0b
