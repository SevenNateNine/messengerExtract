from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import platform

username = ''
password = ''

def messengerLogin():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.messenger.com/')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

print("logging in to messenger")
messengerLogin()
print("action complete")
