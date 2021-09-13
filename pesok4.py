import requests

payload = {'user': 'admin', 'password': 'admin'}
url = "http://127.0.0.1/sp/account/login"
a = requests.Session()
result1 = a.post(url, data=payload)
cook = a.cookies
print(cook)
print(result1.text)
qwe = 1400
f = open('ppp.txt', encoding='utf-8')
#print(f.read())
while True:
    qwe = qwe + 1
    url2 = "http://127.0.0.1/sp/groupConnection/edit?id=" + str(qwe)
    result = a.get(url2, cookies=cook)
    print(result.text)
    if not result.text == '{}':
        print(result.text)
        try:
            assert result.text == f.read()
            print('Проверка успешна')
            break
        except:
            print("Провал")
            break
