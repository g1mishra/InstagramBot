from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from returnPassword import getPassword

def loginAndSeacrh():
    driver = webdriver.Firefox()
    driver.get("https://instagram.com")
    time.sleep(3)

    username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
    username.send_keys("yourusername")
    password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    password.send_keys(getPassword()) # getPasseord() : return "password"

    # hit enter to login
    password.send_keys(Keys.ENTER)

    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()

    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys("#pythonprogramming")

    time.sleep(5)
    search.send_keys(Keys.ENTER)
    search.send_keys(Keys.ENTER)
    #like and comment post
    likeAndCommentPosts(driver)

def likeAndCommentPosts(driver):
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()
    while True :
        time.sleep(2)
        post = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]")
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
