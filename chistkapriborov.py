from autotesting.autotest import *
from autotesting import autotest

print("Начат - chistkapriborov")
vkladka_pribori_click()
otkrit_spisok_click()

nomerpibora = 0
while True:
    try:
        nomerpibora += 1
        vkladka_pribori_click()

        try:
            perviy_pribor_vspiske_kursor()
            knopka_udalit_click()
        except BaseException:
            print("Удаление приборов прошло успешно")
            break
        time.sleep(1)
        knopka_ok_click()
        time.sleep(3)
        print("Прибор удален " + str(nomerpibora))

    except BaseException as e:
        print("Прибор не удален произошла ошибка " + str(nomerpibora), e)
        autotest.peremlog2 = "Прибор не удален произошла ошибка " + str(nomerpibora), str(e)
        funclog()
        pass