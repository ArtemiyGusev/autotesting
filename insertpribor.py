import sys

from autotesting import autotest
from autotesting.autotest import *

try:
    from autotesting.chistkapriborov import *
except BaseException as e:
    pass

indexnedob = 1

while True:
    server_kursor()
    try:
        knopka_dobavit_click()
    except:
        pass
        print("Прибор не добавлен " + "//div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/div/select/option["+ str(indexnedob) +"]")
    indexnedob = indexnedob + 1

    try:
        knopka_dalee()
    except:
        pass
        print("Провал на кнопке далее")

    try:
        model_pribora_select()
        print("Прибор выбран")
    except:
        print("Тест завершен")
        sys.exit()

    try:
        setevoy_addres()
    except:
        pass
        print("Нет сетевого адреса")

    zavodskoy_addres()

    try:
        tip_podlucheniya()
    except:
        pass
        print("Нет заводского номера")

    try:
        vvod_comport_select()
    except:
        pass
        print("Нет COM порта")

    try:
        knopka_ok_click()
    except Exception as e:
        pass
        print("Ошибка при добавлении прибора")
        print(e)
        autotest.peremlog2 = str(e)
        funclog()