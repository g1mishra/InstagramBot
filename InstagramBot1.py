from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from returnPassword import getPassword

delay = 10

def loginAndSeacrh():
    # driver = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://instagram.com")

    time.sleep(5)

    username = driver.find_element_by_css_selector("form#loginForm input[type='text']")
    username.send_keys("usernam")
    password = driver.find_element_by_css_selector("form#loginForm input[type='password']")
    password.send_keys(getPassword()) # getPasseord() : return "password"

    # hit enter to login
    password.send_keys(Keys.ENTER)
    time.sleep(5)

    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type]")))
    driver.find_elements_by_css_selector("button[type]")[-1].click()

    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[tabindex]")))
    driver.find_elements_by_css_selector("button[tabindex]")[-1].click()

    search = driver.find_element_by_css_selector('input[placeholder]')
    search.send_keys("#pythonprogramming")

    time.sleep(5)
    search.send_keys(Keys.ENTER)
    search.send_keys(Keys.ENTER)
    #like and comment post
    likeAndCommentPosts(driver)

def likeAndCommentPosts(driver):
    time.sleep(5)
    driver.find_elements_by_css_selector("article > div > div >div >div > div")[0].click()
    while True :
        time.sleep(2)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='button'] img[srcset]")))
        post = driver.find_element_by_css_selector("div[role='button'] img[srcset]")
        actionChains = ActionChains(driver)
        actionChains.double_click(post).perform()
        # select comment input
        driver.find_element_by_css_selector(".Ypffh").click()
        comment = driver.find_element_by_css_selector(".Ypffh")
        comment.send_keys("Hey! Nice Post")
        time.sleep(0.5)
        comment.send_keys(Keys.ENTER)
        time.sleep(2)
        #next post 
        driver.find_element_by_css_selector("._65Bje").click()


if __name__ == "__main__":
    loginAndSeacrh()
