## Q6. darkelf _ OR/AND 우회
<img src="/photo/prob_06.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: or / and <br> 문제 사항: 쿼리에 id=admin을 만들어내라.
### 해결책

```
현재 쿼리문에서 id='guest'로 고정되어 있음
=> pw에 id컬럼 만들어 admin 적용
=> or이 제한됨 
=> || 이용
```
```
해결 쿼리문: where id='guest' and pw=''||id='admin'
```
### CERT <br> ?pw=''||id='admin

### 느낀점
```diff
+ OR  -> ||
+ AND -> &&( %26%26 )
+ OR / AND 우회 방법을 배웠다.
```
