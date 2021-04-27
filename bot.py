from time import sleep
import secrets
from selenium import webdriver

class giveawaybot:
    def __init__(self, link): 
        self.browser = webdriver.Chrome()
        self.link = 'https://instagram.com/'
        giveawaybot.goinsta(self)

    def goinsta(self):
        giveawaybot.login(self)
        sleep(2)
        self.browser.get(self.link)
        self.browser.maximize_window()
        usernamee = input('Write ID of page. >> ')
        sleep(3)
        self.browser.get(self.link+usernamee)
        giveawaybot.findthepost(self)
        sleep(2)
        commentcount = input('How many comments gonna send ? MAX 6 >> ')
        if int(commentcount) > 6:
            print("You gonna get blocked.")
        elif int(commentcount) < 0:
            print("You can't send negative numbers.")
        else:
            for i in range(int(commentcount)):
                giveawaybot.comment(self)
                sleep(5)

        sleep(1000)
        
    def login(self):
        self.browser.get(self.link)
        sleep(3)
        pageusername = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pagepassword = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pagelogin = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        pageusername.send_keys(secrets.username)
        sleep(2)
        pagepassword.send_keys(secrets.password)
        sleep(1)
        pagelogin.click()
        sleep(3)
        self.browser.get(self.link+secrets.username)

    def findthepost(self):
        findpost = input('Paste the instagram post link without https://  .')
        sleep(1)
        self.browser.get('https://'+findpost)
        sleep(2)

    def comment(self):
        commentwrite = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        commentshare = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')
        sayac=0
        commentwrite.send_keys(secrets.tagged)
        sleep(2)
        commentshare.click()

    
giveawaybot(link="https://instagram.com/")
