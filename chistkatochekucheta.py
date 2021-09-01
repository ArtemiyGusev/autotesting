import time

from selenium.common.exceptions import NoSuchElementException

from autotesting import autotest
from autotesting.autotest import *

vkladka_tochkiucheta_click()
#otkrit_spisok_tochekucheta_click()

nomertochki = 0
while True:
    try:
        nomertochki += 1
        vkladka_tochkiucheta_click()
        time.sleep(3)
        try:
            vkladka_tochkiucheta_click()
            tochka_ucheta_vspiske_kursor() #Курсор на первую точку учета
        except NoSuchElementException:
            pass

        try:
            knopka_udalit_click()
        except Exception as e:
            print("Все списки и Точка учета №1 удалены")
            autotest.peremlog2 = 'Все списки и Точка учета №1 удалены'
            funclog()
            break
        time.sleep(1)
        knopka_ok_click()

        print("Прибор удален " + str(nomertochki))
    except Exception as e:
        print(e)
        autotest.peremlog2 = str(e)
        funclog()