## Q7. orge _ 
<img src="/photo/prob_07.PNG" width="100%" height="100%" alt="problem"></img>

### 제한 문자: or / and <br> 문제 사항: admin의 패스워드를 찾아라.
### 해결책

```
패스워드를 찾아야 하는 문제이므로 먼저, 길이를 찾음
=> length()함수를 사용
=> 반복 작업을 해야하므로 파이썬 코드를 이용함
```
```diff
# 현재 쿼리문: where id='guest' and pw='' || length(pw)=8-- '
```
<참고> Python 코드 : [패스워드 길이 탐색](code/07_pwlength.py)
```
패스워드 길이가 8인 것을 찾아냄
이제 패스워드를 한글자씩 찾아봄
=> substr()함수를 사용
=> 반복 작업을 해야하므로 파이썬 코드를 이용함
```
```diff
# 현재 쿼리문: where id='guest' and pw=''||ascii(substr(pw,1,1))=55-- '
```
<참고> Python 코드 : [패스워드 문자 탐색](code/07_pw.py)
```
해결 쿼리문: where id='guest' and pw='7b751aec'
```
### CERT <br> Python 코드 : [패스워드 길이 탐색](code/07_pwlength.py) / [패스워드 문자 탐색](code/07_pw.py)
