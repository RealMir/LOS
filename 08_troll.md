## Q8. troll _ php 취약점 ( preg_match )
<img src="/photo/prob_08.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: ' , admin(소문자) <br> 문제 사항: 쿼리에 id=admin을 만들어내라.
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
php의 preg_match함수에 /admin/i라고 되어 있지 않음
=> 대문자로 ADMIN 적을 시 막지 못함
```
```
해결 쿼리문: where id='ADMIN'
```
### CERT <br> ?id=ADMIN
