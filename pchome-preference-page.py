from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import random
from account import PCHOME_ACCOUNT, PCHOME_PASSWORD
# preference
PRE_WEBSITE = 'https://ecvip.pchome.com.tw/?0xbd4e346710df1d2def8ec7173f512bff6256cf55a33e2af66dee8e04adcd755d048ad1706961f2c54ab83701f9e653fc'

LOGIN_WITH_PAGE= 'https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=' + PRE_WEBSITE


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
        # self.check_time()

        self.driver.refresh()


        while True:
            self.wait_page_by_check_xpath('//*[@id="add_DRAF07-A900AL12Z-000"]')

            # check start saling
            switch_btn = self.safe_find_by_xpath(SWITCH_ID)
            classes = switch_btn.get_attribute('class')
            if 'add24hCart' in classes:
                print('go!!!!!')
                break
            print('not yet....')
            self.driver.refresh()

        # add to cart
        buy_btn = self.safe_find_by_xpath(SWITCH_ID)
        self.safe_click(buy_btn)
        print('add to the cart')

        while True:
            price = self.safe_find_by_xpath('/html/body/div[5]/a/span[1]/span').text
            print('price=', price)
            if price == None:
                continue
            if price != '$0':
                break
            print('wait..... response')
            sleep(0.1)
        self.purchase()

        # confirm to buy ~
        buy_btn = self.safe_find_by_xpath('//*[@id="btnSubmit"]') # //*[@id="btnSubmit"]
        print('hi')
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

        print('going to the last page')

        # wait page
        self.wait_page_by_check_xpath('//*[@id="btnSubmit"]')

        print('find the last page')

    def login(self):
        print('login ...')
        self.wait_page_by_check_xpath('//*[@id="loginAcc"]')

        account_input = self.safe_find_by_xpath('//*[@id="loginAcc"]')
        account_input.send_keys(PCHOME_ACCOUNT)

        password_input = self.safe_find_by_xpath('//*[@id="loginPwd"]')
        password_input.send_keys(PCHOME_PASSWORD)

        login_btn = self.safe_find_by_xpath('//*[@id="btnLogin"]')
        self.safe_click(login_btn)
        # login_btn.click()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    def wait_page_by_check_xpath(self, xpath, cart = 0):
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
                print('find not safely...')
                r = random.randint(0, 4)/10
                sleep(r)
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