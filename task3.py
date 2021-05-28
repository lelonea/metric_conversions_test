from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)
temperature = '//*[@id="typeMenu"]/a[1]'
cf = '//*[@id="popLinks"]/ol/li[1]/a'
length = '//*[@id="typeMenu"]/a[3]'
mf = '//*[@id="popLinks"]/ol/li[1]/a'
weight = '//*[@id="typeMenu"]/a[2]'
og = '//*[@id="popLinks"]/ol/li[5]/a'


def main_page():
    browser.get('https://www.metric-conversions.org/')


def open_conv(xpath):
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    calc = browser.find_element_by_xpath(xpath)
    calc.click()


def check_conv(a):
    field = browser.find_element_by_xpath('//*[@id="argumentConv"]')
    field.send_keys(a)


def check_is_num():
    inp = input('Enter test data: ')
    if inp.count('.') <= 1 and inp.replace('.', '').isdigit():
        return str(float(inp))
    else:
        print('You should enter number. Try again.')
        return check_is_num()


def quit_browser():
    browser.quit()


def check(type_conv, conv_xpath):
    main_page()
    open_conv(type_conv)
    open_conv(conv_xpath)
    check_conv(check_is_num())


check(temperature, cf)
check(length, mf)
check(weight, og)
