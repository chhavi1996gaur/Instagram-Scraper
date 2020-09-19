# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from urllib.parse import urlparse
import os
import time
import requests
#from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://www.instagram.com/accounts/login/')
#WebDriverWait(driver,5)
time.sleep(2)
driver.find_element_by_name("username").send_keys('chhavi1996gaur@gmail.com')
time.sleep(2)
driver.find_element_by_name("password").send_keys("Chhavi1996#")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("therock")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]').click()
time.sleep(2)
#driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
post_xpath = "//a[contains(@href, '/p/')]"
post_links = driver.find_elements_by_xpath(post_xpath)
post_link = None
if len(post_links)>0:
    post_link = post_links[0]
if post_link != None:
    post_href = post_link.get_attribute("href")
    driver.get(post_href)

video_el = driver.find_elements_by_xpath("//video")
image_el = driver.find_elements_by_xpath("//img")
base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir,"images")
os.makedirs(img_dir,exist_ok=True)
def scrap_save(elements):
    for el in elements:
        #print(img.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(img_dir, filename)
        if os.path.exists(filepath):
            continue
        with requests.get(url, stream = True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content():
                    if chunk:
                        f.write(chunk)


scrap_save(video_el)
scrap_save(image_el)