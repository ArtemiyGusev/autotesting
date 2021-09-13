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
indexnedob = 0
def setevoy_addres_error():
    if not hasattr(setevoy_addres_error, '_state'):  # инициализация значения
        setevoy_addres_error._state = 0
    setevoy_addres_errorx = d.driver.find_element_by_xpath('//label[1]/input[@class="validation-error"]')
    setevoy_addres_error._state = setevoy_addres_error._state + 1
    setevoy_addres_errorx.send_keys(Keys.CONTROL + "a")
    setevoy_addres_errorx.send_keys(Keys.DELETE)
    setevoy_addres_errorx.send_keys(setevoy_addres_error._state)

while True:
    vkladka_pribori_click()
    perviy_pribor_vspiske_kursor()
    try:
        knopka_dobavit_click()
    except:
        pass
        print("Прибор не добавлен " + "/html/body/div/div[1]/main/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div/select/option[" + str(indexnedob) + "]")

    indexnedob = indexnedob + 1
    try:
        model_pribora_select()
    except:
        print("Тест завершен")
        knopka_otmena_click()
        from autotesting.spiskipriborov import *
        break
    setevoy_addres()
    zavodskoy_addres()
    try:
        knopka_ok_click()
        d.driver.implicitly_wait(5)
    except Exception as e:
        print("Ошибка при добавлении прибора")
        print(e)
        autotest.peremlog2 = str(e)
        funclog()
    try:
        setevoy_addres_error()
        try:
            knopka_ok_click()
        except Exception as e:
            print("Ошибка при добавлении прибора")
            print(e)
            autotest.peremlog2 = str(e)
            funclog()
    except:
        pass
print("Конец теста")