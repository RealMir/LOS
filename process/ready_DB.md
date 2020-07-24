# DB 기초지식

## DB 준비
+ apt install mysql-server : mysql 설치 <br>
<참고>[Ubuntu에 APM 구성하기](https://blog.lael.be/post/7264)<br>

+ mysql -u root -p : 접속 방법 <br>
<주의> 초기에는 비밀번호 설정 안되어 있음 => 그냥 enter치면 접속 됨

## mysql 기본 명령어
### DataBase 관리 명령어
* show databases; : 현재 존재하는 DB 종류 출력
* create database < DB 이름 >; : DB 생성
* drop database < DB 이름 >; : DB 제거
* use < DB 이름 >; : 관리할 DB 지정

### Table 관리 명령어
+ create table < Table 이름 > (열 이름 타입 속성 ... ,  ... ); : DB내에 테이블 생성하기
```
열
no - 회원번호 ( 식별자로 사용할 것 -> primary key )
user_id - 아이디
user_pw - 비밀번호
email - 이메일
속성
auto_increment : 자동으로 1부터 숫자가 지정된다c
primary key : 중복이 불가능하다
not null : 빈 값입력시 오류발생
```
+ drop table < Table 이름 >; : DB내에 테이블 삭제
+ show tables; :  DB내의 테이블들 확인
+ desc < 테이블 명 >; : 해당 테이블의 상세정보 확인
