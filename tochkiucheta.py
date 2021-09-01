import time

from autotesting import autotest
from autotesting.autotest import *
from autotesting.chistkatochekucheta import *

chet1 = 0
d.driver.refresh()
try:
    try:
        time.sleep(3)
        vkladka_tochkiucheta_click()
        time.sleep(1)
        tochkiucheta_kursor()
        time.sleep(1)
        knopka_dobavit_click()
        time.sleep(1)
        radio_click_objectucheta()
        time.sleep(1)
        knopka_dalee()
        time.sleep(1)
        naimenovanie_tochek()
        time.sleep(1)
        knopka_ok_click()
        time.sleep(1)
        print("Объект учета (Точка №1) создан")
    except Exception as e:
        print("Объект учета не создался", e)
        print(e)
        autotest.peremlog2 = str(e)
        funclog()

    time.sleep(1)
    d.driver.implicitly_wait(10)
    otkrit_spisok_tochekucheta_click()
    d.driver.implicitly_wait(10)
    tochka_ucheta_vspiske_kursor()
    d.driver.implicitly_wait(10)
    time.sleep(1)
    pribori_podvkladka_click()
    d.driver.implicitly_wait(10)
    knopka_dobavit_podvkladka_click()
    try:
        vibor_spiska_checkbox_click()
        print("Все приборы выбраны")
    except:
        print("Приборы не выбраны")
    knopka_ok_click()

    knopka_save_click()
    while True:
        chet1 += 1

        d.driver.refresh()
        vkladka_tochkiucheta_click()
        time.sleep(1)
        tochka_ucheta_vspiske_kursor()
        try:
            knopka_dobavit_click()
        except BaseException as e:
            pass
            print("FAIL1", e)
        try:
            model_pribora_vtochke_select()
        except Exception:
            print("Все точки учета успешно добавлены в соответствии с приборами")
           # from autotesting.spiskitochekucheta import *
            break
        try:
            shema_podklucheniya_select()
        except NoSuchElementException:
            pass
            d.driver.implicitly_wait(3)
            knopka_otmena_click()
        naimenovanie()
        knopka_ok_click()
except Exception as e:
    print(e)
    autotest.peremlog2 = str(e)
    funclog()
