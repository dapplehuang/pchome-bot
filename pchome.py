from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import random

# test
PRODUT_WEBSITE = 'https://24h.pchome.com.tw/prod/DAAN8E-A900AIH6O?fq=/A/144454'

# switch
# PRODUT_WEBSITE = 'https://24h.pchome.com.tw/cdn/prod/DGBJCW-1900AJVIQ-000?fq=/S/DGBJDE'

LOGIN_WITH_PAGE= 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=' + PRODUT_WEBSITE

PCHOME_ACCOUNT = '1038790@gmail.com'
PCHOME_PASSWORD= ''

START_HOUR = 22
START_MIN  = '41'
random.seed(datetime.now())


class pchomebot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self):

        self.driver.get(LOGIN_WITH_PAGE)

        while self.driver.current_url == LOGIN_WITH_PAGE:
            self.login()
            sleep(3)
        print('login finished.')

        print('start check time...')
        self.check_time()

        self.driver.refresh()

        


        # choose gift
        # gift_checkbox = self.driver.find_element_by_xpath('//*[@id="DGBJCW-A900A9YOA"]/div/ul/li[1]/label')
        # gift_checkbox.send_keys(Keys.SPACE)
        self.wait_page_by_check_xpath('//*[@id="ButtonContainer"]/button')

        # add to cart
        # buy_btn = self.driver.find_element_by_xpath('//*[@id="ButtonContainer"]/button') #//*[@id="ButtonContainer"]/button
        # buy_btn.click()
        buy_btn = self.safe_find_by_xpath('//*[@id="ButtonContainer"]/button')
        self.safe_click(buy_btn)

        
        # go to the cart
        cart_btn = self.driver.find_element_by_xpath('//*[@id="ServiceContainer"]/li[1]/a') # //*[@id="ServiceContainer"]/li[1]/a
        # # cart_btn.click()
        self.safe_click(cart_btn)
        print('going to the cart..')
        

        self.wait_page_by_check_xpath('//*[@id="li_24hMarket"]/label', cart = 1)
        
        # choose 7-11
        seven_checkbox = self.driver.find_element_by_xpath('//*[@id="li_24hMarket"]/label') # //*[@id="li_24hMarket"]/label
        # seven_checkbox.send_keys(Keys.SPACE)
        self.safe_click(seven_checkbox)


        # choose 7-11 location
        seven_location = self.driver.find_element_by_xpath('//*[@id="btn_use711"]') # //*[@id="btn_use711"]
        # seven_location.click()
        self.safe_click(seven_location)

        print('choosed 7-11...')


        self.wait_page_by_check_xpath('//*[@id="warning_btn_confirm"]')

        print('find confirm btn')

        continue_btn = self.driver.find_element_by_xpath('//*[@id="warning_btn_confirm"]') # //*[@id="warning_btn_confirm"]
        # continue_btn.click()
        self.safe_click(continue_btn)

        print('going to the last page')

        # wait page
        self.wait_page_by_check_xpath('//*[@id="btnSubmit"]')

        print('find the last page')

        # confirm to buy ~
        buy_btn = self.driver.find_element_by_xpath('//*[@id="btnSubmit"]') # //*[@id="btnSubmit"]
        print('hi')
        # buy_btn.click()
        # self.safe_click(buy_btn)
        print('done. You did it!!!!!')
        # sleep(2)

        

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