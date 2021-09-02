import requests
from autotesting.chistkapriborov import *

print("Начат - insertpriborgroup")
time.sleep(2)

indexnedob = 0

server_kursor()

try:
    knopka_dobavit_click()
except:
    pass

radio_click_viborgrup()

knopka_dalee()

try:
    vvod_comport_select()
except:
    print("Ошибка порт не выбран")
time.sleep(1)
knopka_ok_click()
response = requests.post("http://127.0.0.1/sp/#")
response_body = response
print(response.status_code)
print(response_body)
print(response.headers["Content-Type"])
time.sleep(1)
otkrit_spisok_click()
time.sleep(1)
kolvo_dobavlenih_priborov = 0
kolvo_nedobavlenih_priborov = 0
indexnedob = 0
while True:
    vkladka_pribori_click()
    perviy_pribor_vspiske_kursor()
    try:
        knopka_dobavit_click()
        kolvo_dobavlenih_priborov = kolvo_dobavlenih_priborov + 1
    except:
        pass
        kolvo_nedobavlenih_priborov = kolvo_nedobavlenih_priborov + 1
        print("Прибор не добавлен " + "/html/body/div/div[1]/main/div[1]/section[1]/div[2]/div[2]/div[3]/div[3]/div[" + str(indexnedob) + "]")

    indexnedob = indexnedob + 1
    try:
        model_pribora_select()
    except:
        print("Тест завершен")
        knopka_otmena_click()
        from autotesting.spiskipriborov import *
        break
    try:
        setevoy_addres()
    except:
        pass
        print("Нет сетевого адреса")
    try:
        zavodskoy_addres()
    except:
        pass
        print("Нет заводского номера")
    try:
        knopka_ok_click()
    except Exception as e:
        pass
        print("Ошибка при добавлении прибора")
        print(e)
        autotest.peremlog2 = str(e)
        funclog()
print("Конец теста")