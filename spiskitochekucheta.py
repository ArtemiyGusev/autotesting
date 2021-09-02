from autotesting.chistkaspiskovtochekucheta import *
d.driver.refresh()
print("Начат - spiskitochekucheta")
try:
    vkladka_tochkiucheta_click()
    spiski_tochkiucheta_kursor()
    knopka_dobavit_click()
    naimenovanie_spiskov()
    time.sleep(2)
    knopka_ok_click()
    time.sleep(2)
    d.driver.refresh()
    vkladka_tochkiucheta_click()
    spisok_vspiske_kursor()
    try:
        while True:
            knopka_dobavit_podvkladka_click()
            vibor_spiska_checkbox_click()
            knopka_ok_click()
    except NoSuchElementException:
        knopka_otmena_click()
    knopka_save_click2()
except Exception as e:
    print(e)
    autotest.peremlog2 = str(e)
    funclog()
from autotesting.nastroykasboradannih import sbor_dannih
sbor_dannih()