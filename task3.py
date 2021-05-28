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


class TestConvertions:
    def __init__(self, converter_type_xpath, convertion_xpath):
        self.converter_type = converter_type_xpath
        self.convertion = convertion_xpath

    def test(self):
        self.main_page()
        self.open_conv(self.converter_type)
        self.open_conv(self.convertion)
        self.check_conv(self.check_is_num())

    @staticmethod
    def main_page():
        browser.get('https://www.metric-conversions.org/')

    @staticmethod
    def open_conv(xpath):
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        calc = browser.find_element_by_xpath(xpath)
        calc.click()

    @staticmethod
    def check_conv(a):
        field = browser.find_element_by_xpath('//*[@id="argumentConv"]')
        field.send_keys(a)

    def check_is_num(self):
        inp = input('Enter test data: ')
        if inp.count('.') <= 1 and inp.replace('.', '').isdigit():
            return str(float(inp))
        else:
            print('You should enter number. Try again.')
            return self.check_is_num()

    @staticmethod
    def quit_browser():
        browser.quit()


first = TestConvertions(temperature, cf)
first.test()
