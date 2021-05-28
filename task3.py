from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestConv:
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 20)

    def __init__(self, converter_type_xpath, converter_xpath):
        self.converter_type = f'//*[@id="typeMenu"]/a[{converter_type_xpath}]'
        self.converter = f'//*[@id="popLinks"]/ol/li[{converter_xpath}]/a'

    def test(self):
        self.main_page()
        self.open_conv(self.converter_type)
        self.open_conv(self.converter)
        self.check_conv(self.check_is_num())

    def main_page(self):
        self.browser.get('https://www.metric-conversions.org/')

    def open_conv(self, xpath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        calc = self.browser.find_element_by_xpath(xpath)
        calc.click()

    def check_conv(self, data):
        field = self.browser.find_element_by_xpath('//*[@id="argumentConv"]')
        field.send_keys(data)

    def check_is_num(self):
        inp = input('Enter test data: ')
        if inp.count('.') <= 1 and inp.replace('.', '').isdigit():
            return str(float(inp))
        else:
            print('You should enter number. Try again.')
            return self.check_is_num()

    def quit_browser(self):
        self.browser.quit()




