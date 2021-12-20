from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.digikala.com")
email = "cabelucamelia@gmail.com"
password = "Camelia2323"
expected="Camelia Cabelo"

def TestLogin():
        driver.find_element_by_xpath("/html/body/header/div/div/div[2]/div[1]/div/a").click()
        sleep(2)
        email_phone = driver.find_element_by_name('login[email_phone]')
        email_phone.send_keys(email)
        driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()
        sleep(3)
        driver.find_element_by_name("login[password]").send_keys(password)
        driver.find_element_by_xpath('//*[@id="authForm"]/button').click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/header/div/div/div[2]/div[1]/div/a").click()
        driver.find_element_by_xpath("/html/body/header/div/div/div[2]/div[1]/div/div/div[1]/a").click()
        actual =driver.find_element_by_xpath("/html/body/main/div[2]/div/section/div[1]/section[1]/div/div/div[1]/div/div[2]/div[1]")
        assert actual.text==expected


TestLogin()
