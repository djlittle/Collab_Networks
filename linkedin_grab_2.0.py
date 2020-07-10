# -------------------------------------------------------------------------------
# Name: linkedin_grab.py
# Purpose: Web scrape from LinkedIn for the Collaboration Networks Project
#
# Author(s):    David Little
#
# Created:      06/08/2020
# Updated:
# Update Comment(s):
#
# TO DO:
#
# -------------------------------------------------------------------------------

import requests
import time
from bs4 import BeautifulSoup
from linkedin_scraper import Person, actions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import pandas as pd
import numpy as np
import random
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

email = 'linkedin.shell.acct@gmail.com'
password = '$ituationNormal'

#person = Person('https://www.linkedin.com/in/michael-simeone-366760a9/', driver=driver,close_on_complete=False)
#person2 = Person("https://www.linkedin.com/in/david-j-little/", driver=driver,close_on_complete=False)

linkedin_urls = pd.read_csv('urls_no_name_filter_sub.csv', error_bad_lines=False,)
linkedin_urls.fillna(-1, inplace=True)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/login")
element = WebDriverWait(driver, 720).until(EC.presence_of_element_located((By.ID, "username")))

email_elem = driver.find_element_by_id("username")
email_elem.send_keys(email)

password_elem = driver.find_element_by_id("password")
password_elem.send_keys(password)
driver.find_element_by_tag_name("button").click()

element = WebDriverWait(driver, 720).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))

linkedin_urls_back = linkedin_urls
#test = linkedin_urls.iloc[449:]
#linkedin_urls = linkedin_urls.iloc[449:]
#name, url = linkedin_urls.loc[26]
#person_back = person
skills = []
#name, url = linkedin_urls.loc[5]
for name, url in linkedin_urls.itertuples(index=False):
    #print(name, url)
    if not(url == -1):
        driver.get(url)
        time.sleep(2)
        for i in range(0,40):
            driver.execute_script("window.scrollBy(0, 100);")
            time.sleep(random.randint(0,1))
        for i in range(0,3):
            driver.execute_script("window.scrollBy(0, -1000);")
            #time.sleep(random.randint(0,1))
        #driver.find_elements_by_xpath('//*[@data-control-name="skill_details"]')[0].click()
        try:
            driver.find_elements_by_xpath('//*[@data-control-name="skill_details"]')[0].click()
            #skill_det = driver.find_elements_by_xpath('//*[@data-control-name="skill_details"]')#[0].click()
            #skill_det.location_once_scrolled_into_view
        except:
            print(name + ' was skipped')
            continue
        find = driver.find_elements_by_xpath(
            "//*[@class='pv-skill-categories-section__expanded']")
        txt = find[0].text.split('\n')
        for s in txt:
            check = any(map(str.isdigit, s))
            if not(check):
                skills.append([name, s])
    time.sleep(3)
skills_df = pd.DataFrame(data=skills, columns=['Name', 'Skill'])
skills_df.to_csv('skills_edgelist_sub_test.csv', index=False)

#len(skills_df['Name'].unique())
#len(skills_df['Skill'].unique())
#len(linkedin_urls['URL'].unique())

#np.logical_not()
#name = 'Michael Simeone'
#txt = find[0].text.split('\n')

#aria = driver.find_element_by_name("aria-expanded")
#driver.find_element_by_tag_name("aria-expanded")
    #getElementById(id2).setAttribute('aria-expanded', 'true')


sub = pd.read_csv('urls_no_name_filter_sub.csv', error_bad_lines=False)
len(sub['Name'].unique())
len(sub['URL'].unique())

sub_e = pd.read_csv('skills_edgelist_sub.csv', error_bad_lines=False)
len(sub_e['Name'].unique())
len(sub_e['Skill'].unique())





#----------------------------------------------------------------------------------------------------


edgelist = pd.read_csv('skills_edgelist_full.csv', error_bad_lines=False)


len(edgelist['Name'].unique())
len(edgelist['Skill'].unique())
