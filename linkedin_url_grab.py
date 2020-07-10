# -------------------------------------------------------------------------------
# Name: linkedin_grab.py
# Purpose: Web scrape from LinkedIn for the Collaboration Networks Project
#
# Author(s):    David Little
#
# Created:      07/10/2020
# Updated:
# Update Comment(s):
#
# TO DO: Comment code
# Modularize components
#
# -------------------------------------------------------------------------------

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

names_csv = 'sustainability-persons_no_sir_sub.csv'

df = pd.read_csv(names_csv, error_bad_lines=False)

email = 'linkedin.shell.acct@gmail.com'
password = '$ituationNormal'

#df_sample = df.sample(10) # For testing

# -------------------------------- CREATING DRIVER ------------------------------------------------------

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/login")
element = WebDriverWait(driver, 720).until(EC.presence_of_element_located((By.ID, "username")))

email_elem = driver.find_element_by_id("username")
email_elem.send_keys(email)

password_elem = driver.find_element_by_id("password")
password_elem.send_keys(password)
driver.find_element_by_tag_name("button").click()

element = WebDriverWait(driver, 720).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))

#-------------------------------------------------------------------------------

profile_urls = []
for name in df["Name"]:
    print(name)
    search_bar = driver.find_elements_by_id('global-nav-typeahead')
    text_box = driver.find_element_by_tag_name('input')

    time.sleep(1)
    search_bar[0].click()
    time.sleep(1)
    text_box.clear()
    time.sleep(1)
    text_box.send_keys(name)
    time.sleep(1)
    text_box.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(1)

    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    anchors = soup.find_all('a')
    anc_urls = []
    for anc in anchors:
        try:
            url = anc['href']
        #    print(anc["class"][0])
            if anc['class'][0] == "search-result__result-link":
                if "/in/" in anc['href']:
                    #if anc.text.strip() == name:
                    url_ext = "https://www.linkedin.com" + url
                    anc_urls.append(url_ext)
                    print(url_ext)
        except:
            continue
    if len(anc_urls)>0:
        profile_urls.append([name, anc_urls[0]])
    else:
        profile_urls.append([name, ''])
    time.sleep(random.randint(3, 5))


linkedin_urls = pd.DataFrame(data=profile_urls, columns=['Name', 'URL'])

linkedin_urls.to_csv("urls_no_name_filter_sub.csv", index=False)

