# git 준비

### 초기 작업

1. sudo apt install git : git을 가상머신에 설치
2. mkdir <폴더 명> : repostitory 가져올 폴더 만듬
3. cd <폴더 명>
4. git init
5. git clone < ... > : repository를 가져옴

### git에 파일 올리기
1. git add <올릴 파일>
2. git commit -m "<할 말>"
3. git push origin master

<br>+ git push ( github 웹에서 수정시 꼭 해야함 )


### user 등록
+ user name을 등록<br> git config --global user.name <사용자명>

+ email을 등록
	git config --global user.email <이메일주소>

+ git 환경 설정 확인 명령어
	git config --global --list 

