import sys
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import random
from account import PCHOME_ACCOUNT, PCHOME_PASSWORD
# from .. import account

# test
PRODUT_WEBSITE = 'https://24h.pchome.com.tw/prod/DGBJCW-1900AJVIQ'  # switch

LOGIN_WITH_PAGE= 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=' + PRODUT_WEBSITE

START_HOUR = 22
START_MIN  = '41'
random.seed(datetime.now())


class pchomebot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self):

        self.driver.get(LOGIN_WITH_PAGE)
        sleep(1)

        while self.driver.current_url == LOGIN_WITH_PAGE:
            self.login()
            sleep(7)
        print('login finished.')

        while True:
            buy_btn = self.safe_find_by_xpath('//*[@id="ButtonContainer"]/button') 
            t = buy_btn.text
            if t == '加入24h購物車':
                print('Add it to the cart !!!!!')
                break
            r = random.randint(50, 120)
            print('sold out, sleep ', r)
            sleep(r)
            self.driver.refresh()
        
        sleep(2)
        self.safe_click(buy_btn)

        self.check_is_in_cart()

        self.purchase()

        # confirm to buy ~
        buy_btn = self.driver.find_element_by_xpath('//*[@id="btnSubmit"]') # //*[@id="btnSubmit"]
        print('go !!!')
        # buy_btn.click()
        # self.safe_click(buy_btn)
        print('done. You did it!!!!!')
        # sleep(2)
    
    def purchase(self):
        
        # go to the cart
        self.driver.get('https://24h.pchome.com.tw/cart.php')
        print('going to the cart..')

        self.wait_page_by_check_xpath('//*[@id="li_24hMarket"]/label')
        
        # choose 7-11
        seven_checkbox = self.safe_find_by_xpath('//*[@id="li_24hMarket"]/label') # //*[@id="li_24hMarket"]/label
        # seven_checkbox.send_keys(Keys.SPACE)
        self.safe_click(seven_checkbox)


        # choose 7-11 location
        seven_location = self.safe_find_by_xpath('//*[@id="btn_use711"]') # //*[@id="btn_use711"]
        # seven_location.click()
        self.safe_click(seven_location)

        print('choosed 7-11...')


        self.wait_page_by_check_xpath('//*[@id="warning_btn_confirm"]')

        print('find confirm btn')

        continue_btn = self.safe_find_by_xpath('//*[@id="warning_btn_confirm"]') # //*[@id="warning_btn_confirm"]
        # continue_btn.click()
        self.safe_click(continue_btn)

        print('go to the last page')

        # wait page
        self.wait_page_by_check_xpath('//*[@id="btnSubmit"]')

        print('find the last page')


    def check_is_in_cart(self):
        while True:
            price = self.safe_find_by_xpath('//*[@id="CarInfo"]/a/span[1]').text
            print('price=', price)
            if price == None:
                continue
            if price != '$0':
                break
            print('wait..... response')
            sleep(0.1)
        # self.purchase()
    
    def login(self):
        print('login ...')
        self.wait_page_by_check_xpath('//*[@id="loginAcc"]')

        account_input = self.driver.find_element_by_xpath('//*[@id="loginAcc"]')
        account_input.send_keys(PCHOME_ACCOUNT)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginPwd"]')
        password_input.send_keys(PCHOME_PASSWORD)

        sleep(1)

        login_btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        login_btn.click()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    def wait_page_by_check_xpath(self, xpath):
        while True:
            if self.check_exists_by_xpath(xpath):
                break
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