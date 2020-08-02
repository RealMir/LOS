## Q8. troll _ php 취약점 ( preg_match )
<img src="/photo/prob_08.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: ' / admin(소문자) <br> 문제 사항: 쿼리에 id=admin을 만들어내라.
### 해결책

```
싱글쿼터가 안되서 문자열을 벗아날 수 없음
admin을 사용할 수 없음
=> 초반에 어려웠음. 문제를 다시 한 번 해석함
```
```php
if(preg_match("/admin/", $_GET[id])) exit("HeHe");
```
```
php의 preg_match함수안의 정규표현식에 flag에 i가 없음
=> 대소문자 식별됨
=> 대문자로 ADMIN 적을 시 막지 못함
```
```
해결 쿼리문: where id='ADMIN'
```
### CERT <br> ?id=ADMIN

### 느낀점
```diff
+ preg_match( 정규표현식, 검색 대상 문자열, 배열 변수 반환 )로 구성됨을 알게됨.
+ 정규표현식 뒤의 flag 값 i는 대상 문자열에 대해서 대/소문자를 식별하지 않는 것을 의미함.
+ => i 없으면 대/소문자로 우회 가능
```
