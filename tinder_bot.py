from selenium import webdriver
from time import sleep

import random
from secrets import username, password
from pickuplines import english_pickup_lines

chromedriver = "/Users/dimsum/Documents/Code/chromedriver"

class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver)

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)

        try:
            loginbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            loginbtn.click()
        except:
            more_option_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_option_btn.click()
            loginbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
            loginbtn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(5.5)

        allow_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_btn.click()

        accept_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_btn.click()

        sleep(2)
        enable_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_btn.click()

        sleep(3)
        nothanks_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        nothanks_btn.click()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()
        
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div[1]/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                sleep(1)
                try:
                    self.close_match()
                except Exception:
                    self.close_tinderhome()
    
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_tinderhome(self):
        tinderhome = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        tinderhome.click()

    def send_pickup_line(self,x):
  
        for i in range(2,x+2):
            current = "//*[@id=\"matchListNoMessages\"]/div[1]/div[2]/a/div[1]"
            profile = self.driver.find_element_by_xpath(current)
            profile.click()
            sleep(2)
            msg = random.choice(english_pickup_lines)
            email_in = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            email_in.send_keys(msg)
            sleep(1)
            send = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button/span')
            send.click()
            sleep(1)
            returnM = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            returnM.click()
            sleep(1)

bot = TinderBot()
bot.login()


# //*[@id="matchListNoMessages"]/div[1]/div[2]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[3]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[4]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[5]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[6]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[7]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[8]/a/div[1]
# //*[@id="matchListNoMessages"]/div[1]/div[9]/a/div[1]
# //*[@id="matchListNoMessages"]/div[2]/div[1]/a/div[1]
# //*[@id="matchListNoMessages"]/div[2]/div[2]/a/div[1]

