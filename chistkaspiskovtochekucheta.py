from selenium.common.exceptions import NoSuchElementException
from autotesting import autotest
from autotesting.autotest import *

print("Начат - chistkaspiskovtochekucheta")
funclog_chistka()
time.sleep(1)
vkladka_tochkiucheta_click()
vkladka_information_click()
time.sleep(1)
vkladka_tochkiucheta_click()

nomertochki = 0
while True:
    try:
        nomertochki += 1
        vkladka_tochkiucheta_click()
        time.sleep(3)
        try:
            vkladka_tochkiucheta_click()
            spiski_tochkiucheta_kursor() #Курсор на первую точку учета
        except NoSuchElementException:
            pass
        time.sleep(3)
        try:
            knopka_udalit_click()
        except Exception as e:
            print("Все списки удалены")
            autotest.peremlog2 = 'Все списки удалены'
            funclog()
            break
        time.sleep(1)
        knopka_ok_click()

        print("Список удален " + str(nomertochki))
    except Exception as e:
        print(e)
        autotest.peremlog2 = str(e)
        funclog()