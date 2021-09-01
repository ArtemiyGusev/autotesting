from selenium import webdriver


class d():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("http://127.0.0.1/sp/")
    #driver.implicitly_wait(10)
    print("Переход в СП успешен")

class t():
    tclass = d.driver.implicitly_wait(5)

def login_admin():
    login_adminx = d.driver.find_element_by_css_selector('div.login-grid>input:nth-child(2)').send_keys("admin")

def login_password():
    login_passwordx = d.driver.find_element_by_css_selector('div.login-grid>input:nth-child(4)').send_keys("admin")

def login_button():
    login_buttonx = d.driver.find_element_by_xpath('//button').click()

login_admin()
login_password()
login_button()

print("Admin - Успешно авторизировался")