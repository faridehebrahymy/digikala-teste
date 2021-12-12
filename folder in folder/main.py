from selenium import webdriver
from selenium.webdriver.common.keys import keys
from time import sleep
import random
driver = webdriver.Firefox("C:\Users\Parseh\datin_project\my_venv\geckodriver.exe")

driver.get("https://www.digikala.com")
email = "cabelucamelia@gmail.com"
password = "qwerty997wertR"

def TestLogin():
        driver.find_element_by_xpath("/html/body/header/div/div/div[2]/div[1]/div/a").click()
        sleep(2)
        email_phone = driver.find_element_by_name('login[email_phone]')    
        email_phone.send_keys(email)
        driver.find_element_by_xpath("//*[@id="loginForm"]/button").click()
        sleep(3)
        driver.find_element_by_name('login[password]').send_keys(password)
        driver.find_element_by_xpath("//*[@id="authForm"]/button").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/header/div/div/div[2]/div[1]/div/a").click()


TestLogin()
