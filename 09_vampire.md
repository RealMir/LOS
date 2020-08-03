## Q9. vampire _ php 취약점 ( str_replace )
<img src="/photo/prob_09.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: ' / admin(소문자) <br> 문제 사항: 쿼리에 id=admin을 만들어내라.
### 해결책

```
싱글쿼터가 안되서 문자열을 벗아날 수 없음
admin을 사용할 수 없음
=> 초반에 어려웠음. 문제를 다시 한 번 해석함
```
```php
$_GET[id] = str_replace("admin","",$_GET[id]);
```
```
php의 str_replace함수 때문에 GET의 admin이 없어짐
but. admin만 없어짐
=> admin이 빈칸이 된다고 생각
=> aadmindmin으로 적으면 admin이 나옴
```
```
해결 쿼리문: where id='admin'
```
### CERT <br> ?id=aadmindmin

### 느낀점
```diff
+ str_replace( 변경될 문자, 변경하려는 문자, 변수 )로 구성됨을 알게됨.
+ 변경될 문자만 이 함수에 적용됨
+ => 변경될 문자를 제외한 문자를 통해 함수를 역이용
```
