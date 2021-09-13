import time
import traceback
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from autotesting.Login import d

peremlog2 = ""
filename = 'Result-test.txt'
vremyafile = datetime.now()

def funclog():
    with open(filename, "a") as filelog:
        abzper = 0
        while abzper < 150:
            abzper += 1
            filelog.write("_")
        filelog.write(vremyafile.strftime('\n%Y-%m-%d %H:%M:%S ||  '))
        filelog.write(peremlog2)
        traceback.print_exc(file=filelog)
        d.driver.save_screenshot("C:/Users/gusevaa/Pictures/Camera Roll/scren1.png")
        d.driver.save_screenshot("screen1.png")

def funclog_chistka():
    open(filename, 'w').close()

def vkladka_information_click():
    vkladka_information_clickx = d.driver.find_element_by_xpath('//div[1]/li[1]/div/span')

def vkladka_pribori_click():  # 3 #2
    vkladka_priborix = d.driver.find_element_by_css_selector('li:nth-child(3)>div>span').click()


def vkladka_tochkiucheta_click():  # 3 #2
    vkladka_tochkiucheta_clickx = d.driver.find_element_by_css_selector('li:nth-child(2)>div>span').click()
    d.driver.implicitly_wait(5)


def otkrit_spisok_click():  # 3
    otkrit_spisokx = d.driver.find_element_by_xpath('//*[@id="18_1"]/div[1]').click()
    d.driver.implicitly_wait(10)
    print("Список сервера открыт")


def otkrit_spisok_tochekucheta_click():
    otkrit_spisok_tochekucheta_clickx = d.driver.find_element_by_xpath('//*[@id="5_0"]/div[1]').click()
    d.driver.implicitly_wait(10)

def otkrit_spiskov_tochekucheta_click():
    otkrit_spiskov_tochekucheta_clickx = d.driver.find_element_by_xpath('//*[@id="3_0"]/div[@class="toggle fas"]').click()
    d.driver.implicitly_wait(10)

def perviy_pribor_vspiske_kursor():  # 3
    perviy_pribor_vspiske_kursorx = d.driver.find_element_by_xpath('//div[3]/div[3]/div')
    d.driver.implicitly_wait(5)
    Hover3 = ActionChains(d.driver).move_to_element(perviy_pribor_vspiske_kursorx)
    d.driver.implicitly_wait(5)
    Hover3.perform()
    d.driver.implicitly_wait(3)

def tochka_ucheta_vspiske_kursor():
    time.sleep(1)
    tochka_ucheta_vspiske_kursorx = d.driver.find_element_by_xpath('//div[contains(text(),"Точка №1")]')
    tochka_ucheta_vspiske_kursorx.click()
    time.sleep(1)
    Hover3 = ActionChains(d.driver).move_to_element(tochka_ucheta_vspiske_kursorx)
    Hover3.perform()
    d.driver.implicitly_wait(3)

def spisok_vspiske_kursor():
    time.sleep(1)
    spisok_tochka_ucheta_vspiske_kursorx = d.driver.find_element_by_xpath('//div[contains(text(),"Список №1")]')
    spisok_tochka_ucheta_vspiske_kursorx.click()
    time.sleep(1)
    Hover3 = ActionChains(d.driver).move_to_element(spisok_tochka_ucheta_vspiske_kursorx)
    Hover3.perform()
    d.driver.implicitly_wait(3)

def spisok_priborov_vspiske():
    spisok_priborov_vspiskex = d.driver.find_element_by_xpath('//*[@id="2_0"]/div[3]/div')
    d.driver.implicitly_wait(5)
    spisok_priborov_vspiskex.click()
    d.driver.implicitly_wait(5)
    Hover4 = ActionChains(d.driver).move_to_element(spisok_priborov_vspiskex)
    d.driver.implicitly_wait(5)
    Hover4.perform()
    d.driver.implicitly_wait(5)

def knopka_udalit_click():  # 3
    knopka_udalitx = d.driver.find_element_by_css_selector('div.ui-fab.fas.fa-times').click()
    d.driver.implicitly_wait(5)


def knopka_ok_click():  # 3 #1 #2
    knopka_ok_clickx = d.driver.find_element_by_css_selector('div.modal-footer>button:nth-child(1)').click()


def knopka_otmena_click():
    knopka_otmena_clickx = d.driver.find_element_by_xpath('//button[contains(text(),"Отмена")]').click()


def server_kursor():  # 1
    server_kursorx = d.driver.find_element_by_id('18_1')
    d.driver.implicitly_wait(10)
    Hover1 = ActionChains(d.driver).move_to_element(server_kursorx)
    d.driver.implicitly_wait(10)
    Hover1.perform()
    d.driver.implicitly_wait(3)


def tochkiucheta_kursor():
    tochkiucheta_kursorx = d.driver.find_element_by_id('5_0')
    d.driver.implicitly_wait(10)
    Hover2 = ActionChains(d.driver).move_to_element(tochkiucheta_kursorx)
    d.driver.implicitly_wait(10)
    Hover2.perform()
    d.driver.implicitly_wait(3)

def spiski_pribori_kursor():
    spiski_pribori_kursorx = d.driver.find_element_by_id('2_0')
    d.driver.implicitly_wait(10)
    Hover5 = ActionChains(d.driver).move_to_element(spiski_pribori_kursorx)
    d.driver.implicitly_wait(10)
    Hover5.perform()
    d.driver.implicitly_wait(3)

def spiski_tochkiucheta_kursor():
    spiski_tochkiucheta_kursorx = d.driver.find_element_by_id('3_0')
    d.driver.implicitly_wait(10)
    Hover4 = ActionChains(d.driver).move_to_element(spiski_tochkiucheta_kursorx)
    d.driver.implicitly_wait(10)
    Hover4.perform()
    d.driver.implicitly_wait(3)

def tochkiuchuta_click():
    tochkiucheta_clickx = d.driver.find_element_by_xpath('/html/body/div/div[1]/main/div[1]/section[1]/div[2]/div[1]/div').click()
    d.driver.implicitly_wait(5)


def knopka_dobavit_click():  # 1
    knopka_dobavit_clickx = d.driver.find_element_by_css_selector('div.ui-fab.fas.fa-plus').click()
    d.driver.implicitly_wait(3)


def knopka_dobavit_podvkladka_click():
    knopka_dobavit_podvkladka_clickx = d.driver.find_element_by_css_selector('div.button.fas.fa-plus-circle').click()
    d.driver.implicitly_wait(3)


def knopka_dalee():  # 1 #2
    knopka_daleex = d.driver.find_element_by_xpath('//button[contains(text(),"Далее")]').click()
    d.driver.implicitly_wait(3)

def parametri_podvkladka_click():
    parametri_podvkladka_clickx = d.driver.find_element_by_xpath('//div[@class="tab"][contains(text(),"Параметры")]').click()

def pribori_podvkladka_click():
    pribori_podvkladka_clickx = d.driver.find_element_by_xpath('//div[@class="tab"][contains(text(),"Приборы")]').click()
    d.driver.implicitly_wait(3)

def tochkiucheta_podvkladka_click():
    tochkiucheta_podvkladka_clickx = d.driver.find_element_by_xpath('//div[@class="tab"][contains(text(),"Точки учета")]')
    tochkiucheta_podvkladka_clickx.click()

def knopka_save_click():
    knopka_save_clickx = d.driver.find_element_by_xpath('//div[contains(text(),"Сохранить")]').click()
    d.driver.implicitly_wait(10)

def knopka_save_click2():
    knopka_save_click2x = d.driver.find_element_by_xpath('//div[3]/div/div/div[2]/button/div').click()
    d.driver.implicitly_wait(10)


def model_pribora_select():  # 1 #2
    if not hasattr(model_pribora_select, '_state'):  # инициализация значения
        model_pribora_select._state = 0
    model_pribora_selectx = Select(d.driver.find_element_by_css_selector("div.component-detail > div > div > div:nth-child(2) > div > div > select")).select_by_index(model_pribora_select._state)
    model_pribora_select._state = model_pribora_select._state + 1
    d.driver.implicitly_wait(3)

def model_pribora_vtochke_select():
    if not hasattr(model_pribora_vtochke_select, '_state'):  # инициализация значения
        model_pribora_vtochke_select._state = 0
    model_pribora_vtochke_selectx = Select(d.driver.find_element_by_css_selector("div.modal-content select:nth-child(8)")).select_by_index(model_pribora_vtochke_select._state)
    model_pribora_vtochke_select._state = model_pribora_vtochke_select._state + 1
    d.driver.implicitly_wait(3)


def shema_podklucheniya_select():
    shema_podklucheniya_selectx = Select(d.driver.find_element_by_css_selector("div.point-grid>select:last-child")).select_by_index(1)
    d.driver.implicitly_wait(3)


def naimenovanie_tochek(): #25.08 доделать
    naimenovanie_tochekx = d.driver.find_element_by_css_selector("input[type=text]:nth-child(2)")
    naimenovanie_tochekx.send_keys("Точка №1")
    d.driver.implicitly_wait(10)
    return naimenovanie_tochekx

def naimenovanie_spiskov(): #25.08 доделать
    naimenovanie_spiska_tochekx = d.driver.find_element_by_css_selector("input[type=text]:nth-child(2)")
    naimenovanie_spiska_tochekx.send_keys("Список №1")
    d.driver.implicitly_wait(10)


def naimenovanie():
    if not hasattr(naimenovanie, '_state'):  # инициализация значения
        naimenovanie._state = 0
    naimenovanie._state = naimenovanie._state + 1
    naimenovaniex = d.driver.find_element_by_xpath("//div[@class='point-grid']/input[1]")
    naimenovaniex.send_keys(Keys.CONTROL + "a")
    naimenovaniex.send_keys(Keys.DELETE)
    #naimenovaniex.send_keys("Наименование " + str(naimenovanie._state))
    naimenovaniex.send_keys(naimenovanie._state)
    d.driver.implicitly_wait(10)

def setevoy_addres():  # 1 #2
    if not hasattr(setevoy_addres, '_state'):  # инициализация значения
        setevoy_addres._state = 30
    setevoy_addres._state = setevoy_addres._state + 1
    setevoy_addresx = d.driver.find_element_by_xpath('//label[1]/input')
    setevoy_addresx.send_keys(Keys.CONTROL + "a")
    setevoy_addresx.send_keys(Keys.DELETE)
    setevoy_addresx.send_keys(setevoy_addres._state)


def zavodskoy_addres():  # 1 #2
    if not hasattr(zavodskoy_addres, '_state'):  # инициализация значения
        zavodskoy_addres._state = 30
    zavodskoy_addres._state = zavodskoy_addres._state + 1
    try:
        zavodskoy_addresx = d.driver.find_element_by_xpath('//label[2]/input')  # Поле зав. номера
    except BaseException:
        zavodskoy_addresx = d.driver.find_element_by_xpath('//label/input')
    zavodskoy_addresx.send_keys(Keys.CONTROL + "a")
    zavodskoy_addresx.send_keys(Keys.DELETE)
    zavodskoy_addresx.send_keys(zavodskoy_addres._state)
    pass


def tip_podlucheniya():  # 1
    tip_podlucheniyax = Select(d.driver.find_element_by_xpath("//div[3]/div[2]/div[2]/div/div/div[1]/select"))
    tip_podlucheniyax.select_by_index(1)


def vvod_comport_select():  # 1 #2//span[@class='radio_text'][contains(text(),'Группа')]
    vvod_comport_selectx = Select(
        d.driver.find_element_by_xpath("//div[2]/div[2]/div/div/div[2]/div[1]/select")).select_by_index(0)


def radio_click_viborgrup():  # 2
    radio_click_viborgrupx = d.driver.find_element_by_css_selector('div:last-child>label>span.radio-outer-circle').click()


def radio_click_objectucheta():
    radio_click_objectuchetax = d.driver.find_element_by_xpath(
        '//span[@class="radio_text"][contains(text(),"Объект учета")]').click()


def vibor_spiska_checkbox_click():
    vibor_spiska_checkbox_clickx = d.driver.find_element_by_xpath('//div[1]/span[@class="cell check"]/input[@type="checkbox"]').click()
    d.driver.implicitly_wait(5)
