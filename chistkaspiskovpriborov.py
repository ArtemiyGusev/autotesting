from selenium.common.exceptions import NoSuchElementException
from autotesting import autotest
from autotesting.autotest import *

print("Начат - chistkaspiskovpriborov")
funclog_chistka()

vkladka_tochkiucheta_click()
vkladka_pribori_click()

nomerpribora = 0
while True:
    try:
        nomerpribora += 1
        vkladka_tochkiucheta_click()
        vkladka_pribori_click()
        time.sleep(3)
        try:
            spiski_pribori_kursor() #Курсор на первую точку учета
        except NoSuchElementException:
            pass
        time.sleep(3)
        try:
            knopka_udalit_click()
        except Exception:
             print("Все списки удалены")
             autotest.peremlog2 = 'Все списки удалены'
             funclog()
             break
        time.sleep(1)
        knopka_ok_click()

        print("Список удален " + str(nomerpribora))
    except Exception as e:
        print(e)
        autotest.peremlog2 = str(e)
        funclog()