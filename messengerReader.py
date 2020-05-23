from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from time import sleep
import platform
'''
logs into the user's Messenger account
'''
def messengerLogin(driver, email, password):
    driver.get('https://www.messenger.com/')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

'''
goes to conversation conversationName and searches for parts of the conversation containing searchKey
'''
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
        driver.save_screenshot("Results//search"+str(i+1)+".png")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/span[1]/button').click()
        sleep(1)
    
'''
makes chrome headless and calls messengerLogin() and messengerConvo()

where to detech for debugging
'''
def messengerStart(email, password, conversationName, searchkey):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome('chromedriver.exe', chrome_options = chrome_options)
    
    searchkey = urllib.parse.quote(searchkey, safe='')

    messengerLogin(driver, email, password)
    messengerConvo(driver, conversationName, searchkey)

