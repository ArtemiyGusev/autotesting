from selenium.common.exceptions import NoSuchElementException
from autotesting import autotest
from autotesting.autotest import *

def shesterenka_sbora_click():
    shesterenka_sbora_clickx = d.driver.find_element_by_xpath(
        '//div[@title="Настройки"][@class="button fas fa-cog"]').click()
    time.sleep(3)

def paramauto_sbora_checkbox():
    paramauto_sbora_checkboxx = d.driver.find_element_by_xpath(
        '//div[@class="poll-data-settings-grid"]/label[@class="checkbox-wrapper"]/span[@class="checkbox-container is-checked"]/span[@class="checkbox-checkbox"]').click()

def paramautopod_sbora_checkbox():
    if not hasattr(paramautopod_sbora_checkbox, '_state'):  # инициализация значения
        paramautopod_sbora_checkbox._state = 1
    paramautopod_sbora_checkboxx = d.driver.find_element_by_xpath('//div[@class="poll-data-settings-grid two"]/div/label[@class="checkbox-wrapper"][' + str(paramautopod_sbora_checkbox._state) + ']').click()

class sbor_dannih():
    print("Начат - nastroykasboradannih")
    try:
    #__init__(): ??? 26.08
        shesterenka_sbora_click()
        knopka_ok_click()
        parametri_podvkladka_click()
        try:
            tochkiucheta_podvkladka_click()
        except NoSuchElementException:
            pribori_podvkladka_click()
        shesterenka_sbora_click()
        paramauto_sbora_checkbox()
        knopka_ok_click()
        parametri_podvkladka_click()
        try:
            tochkiucheta_podvkladka_click()
        except NoSuchElementException:
            pribori_podvkladka_click()
        shesterenka_sbora_click()
        paramautopod_sbora_checkbox()

        while True: #Снимаем все галки
            if paramautopod_sbora_checkbox._state == 4 or paramautopod_sbora_checkbox._state == 6:
                paramautopod_sbora_checkbox()
                paramautopod_sbora_checkbox._state = paramautopod_sbora_checkbox._state + 1
            elif paramautopod_sbora_checkbox._state == 1 or paramautopod_sbora_checkbox._state == 2 or paramautopod_sbora_checkbox._state == 3 or paramautopod_sbora_checkbox._state == 5:
                paramautopod_sbora_checkbox._state = paramautopod_sbora_checkbox._state + 1
                pass
            elif paramautopod_sbora_checkbox._state == 7:
                paramautopod_sbora_checkbox._state = 1
                break

        knopka_ok_click()
        parametri_podvkladka_click()
        try:
            tochkiucheta_podvkladka_click()
        except NoSuchElementException:
            pribori_podvkladka_click()
        shesterenka_sbora_click()

        while True:
            paramautopod_sbora_checkbox()
            paramautopod_sbora_checkbox._state = paramautopod_sbora_checkbox._state + 1
            knopka_ok_click()
            parametri_podvkladka_click()
            try:
                tochkiucheta_podvkladka_click()
            except NoSuchElementException:
                pribori_podvkladka_click()
            shesterenka_sbora_click()
            if paramautopod_sbora_checkbox._state == 6:
                knopka_ok_click()
                parametri_podvkladka_click()
                try:
                    tochkiucheta_podvkladka_click()
                except NoSuchElementException:
                    pribori_podvkladka_click()
                shesterenka_sbora_click()
                paramautopod_sbora_checkbox._state = 1
                break
        knopka_ok_click()
        autotest.peremlog2 = ("\nТест настроек сбора данных ПРОЙДЕН")
        print("Тест настроек сбора данных ПРОЙДЕН")
    except Exception as e:
        print(e)
        autotest.peremlog2 = str(e)
        funclog()