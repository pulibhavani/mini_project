from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as pt
from selenium.webdriver.common.keys import Keys
from credentials import username, password, pagename

# Intialize drivers and set the path
ser = Service("C:/webdriver/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


# Automatic Login
def login():
    # opening instagram in chrome using instagram link
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(1)  # the time idle being to run the next command
    driver.maximize_window()  # to maximize the Chrome window
    # To find username column and enter the username using sendkeys
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    sleep(2)
    # To find password column and enter the password using sendkeys
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    sleep(2)
    # To find login button and click on it
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    sleep(8)
    # To click on not now
    driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    sleep(1)
    # To click not now
    driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
    sleep(3)

# Automatic Follow
def follow():
    # To find search bar
    search_1 = driver.find_element(By.XPATH, '//span[text()="Search"]')
    search_1.click()  # to click on search bar
    sleep(2)
    # To send text to search in search bar
    search_2 = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
    search_2.send_keys(pagename)
    sleep(3)
    # To go down to click using keyboard actions
    search_2.send_keys(Keys.ARROW_DOWN)
    sleep(2)
    # To click on the page using keyboard actions
    search_2.send_keys(Keys.ENTER)
    sleep(3)
    # To Follow
    # If not followed
    try:
        ref_pos = pt.locateOnScreen('image.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 130
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(2)
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_DOWN)
    # if it is followed it will be skipped
    except:
        sleep(2)
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_DOWN)
def like():
    # To Find the first post in the page
    media_element = driver.find_element(By.XPATH, '//div[@class="_aagw"]')
    media_element.click()
    sleep(2)
    # Like the post
def like_save():
    #Like and Save
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 2
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 3
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    #Like and Save - 4
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 5
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 6
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 7
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 8
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 9
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 10
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 11
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
    except:
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.ARROW_RIGHT)
        sleep(4)
    # Like and Save - 12
    try:
        ref_pos = pt.locateOnScreen('like.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
        sleep(1)
    except:
        pass
    # Save The Post
    try:
        ref_pos = pt.locateOnScreen('save.png', confidence=0.5)
        x = ref_pos[0]
        y = ref_pos[1]
        a = x + 13
        b = y + 20
        pt.moveTo(a, b, duration=.05)
        pt.click()
    except:
        pass




login()
follow()
like()
like_save()