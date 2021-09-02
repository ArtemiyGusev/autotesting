from autotesting import autotest
from autotesting.autotest import *

d.driver.refresh()

print("Начат - chistkatochekucheta")
vkladka_tochkiucheta_click()
#otkrit_spisok_tochekucheta_click()

nomertochki = 0
while True:
    try:
        nomertochki += 1
        time.sleep(3)
        vkladka_pribori_click()
        vkladka_tochkiucheta_click()

        try:
            tochka_ucheta_vspiske_kursor()
            knopka_udalit_click()
        except Exception as e:
            print("Все списки и Точка учета №1 удалены")
            autotest.peremlog2 = 'Все списки и Точка учета №1 удалены'
            funclog()
            break
        time.sleep(1)
        knopka_ok_click()

        print("Точка учета удалена " + str(nomertochki))
    except Exception as e:
        print(e)
        autotest.peremlog2 = str(e)
        funclog()