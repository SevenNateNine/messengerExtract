from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from time import sleep
import platform

def messengerLogin(driver, email, password):
    driver.get('https://www.messenger.com/')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

def messengerConvo(driver, conversationName, searchkey):
    driver.find_element_by_xpath('//*[contains(text(), "' + conversationName + '")]').click()
    sleep(1)
    driver.get(driver.current_url + "?q=" + searchkey)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/span[1]/button').click()
    sleep(1)
    t = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]').text
    resultNum = int(t.split()[2])
    for i in range(0, resultNum):
        driver.save_screenshot("Results//search"+str(i+1)+".jpg")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/span[1]/button').click()
        sleep(1)
    

def messengerStart(email, password, conversationName, searchkey):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome('chromedriver.exe', chrome_options = chrome_options)

    messengerLogin(driver, email, password)
    messengerConvo(driver, conversationName, searchkey)

