from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from time import sleep
import platform

username = ''
password = ''
friend = '' # account for nicknames
searchkey = ''

def messengerLogin(driver):
    driver.get('https://www.messenger.com/')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

def messengerConvo(driver):
    driver.find_element_by_xpath('//*[contains(text(), "' + friend + '")]').click()
    sleep(1)
    driver.get(driver.current_url + "?q=" + searchkey)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/span[1]/button').click()
    sleep(1)
    t = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]').text
    resultNum = int(t.split()[2])
    for i in range(0, resultNum):
        driver.save_screenshot("search"+str(i)+".jpg")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/span[1]/button').click()
        sleep(1)
    

def messengerMain():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome('chromedriver.exe', chrome_options = chrome_options)

    print("logging in to messenger")
    messengerLogin(driver)
    print("action complete")
    print("going to conversation message")
    messengerConvo(driver)
    print("action complete")

messengerMain()
