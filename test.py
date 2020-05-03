from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PAGE = 'https://24h.pchome.com.tw/prod/DGBJCP-A9008W6P4'
class pchomebot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self):

        self.driver.get(PAGE)

        t = self.safe_find_by_xpath('//*[@id="ButtonContainer"]/button').text
        print(t)
        

    def login(self):
        print('login ...')
        self.wait_page_by_check_xpath('//*[@id="loginAcc"]')

        account_input = self.driver.find_element_by_xpath('//*[@id="loginAcc"]')
        account_input.send_keys(PCHOME_ACCOUNT)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginPwd"]')
        password_input.send_keys(PCHOME_PASSWORD)

        login_btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        login_btn.click()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    def wait_page_by_check_xpath(self, xpath, cart = 0):
        i = 0
        while True:
            if self.check_exists_by_xpath(xpath):
                break
            if i > 4 and cart == 1:
                self.driver.get('https://24h.pchome.com.tw/cart.php')
            print('wait page...')
            sleep(0.3)
    
    def check_time(self):
        while True:
            now = datetime.now()
            [_, H, M, S] = now.strftime("%Y/%m/%d:%H:%M:%S").split(':')
            if int(H) == START_HOUR and M == START_MIN:
                break
            print(H,':',M, ':', S)
            sleep(self.wait_time(M, S))

    
    def wait_time(self, M, S):
        return 1

    
    def safe_find_by_xpath(self, xpath):
        buy_btn = None
        while True:
            try:
                buy_btn = self.driver.find_element_by_xpath(xpath) #//*[@id="ButtonContainer"]/button
                break
            except:
                print('find error')
        return buy_btn
    
    def safe_click(self, btn):
        while True:
            try:
                btn.click()
                break
            except:
                r = random.randint(0, 4)/10
                print('btn not work. sleep ', r)
                sleep(r)
            


if __name__ == "__main__":
    bot = pchomebot()
    bot.start()