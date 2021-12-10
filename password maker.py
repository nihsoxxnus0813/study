url = "http://naver.com"
url = url.replace("http://", "")
url = url[:url.index(".")]
print("생성된 비밀번호 : " + url[:3] + str(len(url)) + str(url.count("e")) + "!" )