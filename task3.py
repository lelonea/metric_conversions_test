from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)


def main_page():
    browser.get('https://www.metric-conversions.org/')


def open_conv_cf():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainLinks"]/a[3]')))
    calc = browser.find_element_by_xpath('//*[@id="mainLinks"]/a[3]')
    calc.click()


def check_conv_cf(a):
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
