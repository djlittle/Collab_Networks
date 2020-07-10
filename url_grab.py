# -------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author(s):    David Little
#
# Created:      06/23/2020
# Updated:
# Update Comment(s):
#
# TO DO:
#
# -------------------------------------------------------------------------------

import requests
import bs4
import pandas as pd

names_csv = 'sustainability-persons.csv'
BASE_URL = 'https://www.google.com/search?q=site:linkedin.com/in+\"Arizona+State+University\"+AND+\"%s\"'

df = pd.read_csv(names_csv, error_bad_lines=False)

import requests
from bs4 import BeautifulSoup

# profile_urls = []
#
# name = df['Name'][5]
#
# for name in df['Name']:
#     response = requests.get(BASE_URL % name)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     for anchor in soup.find_all('a'):
#         url = anchor["href"]
#         if 'https://www.linkedin.com/' in url:
#             url = url[7:url.find('&')]
#             profile_urls.append([url])
#             print(url)

#---------------------- NOTES -----------------------------------------------------------
#https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A620%22%5D&firstName=%2B&lastName=Abbaszadegan&origin=SEO_PSERP

#https://www.google.com/search?q=site:linkedin.com/in+AND+%22Morteza%20Abbaszadegan%22

first = 'Joni'
last = 'Adamson'

linked_link = 'https://www.linkedin.com/search/results/people/' \
                   '?facetGeoRegion=%5B%22us%3A620%22%5D&firstName=' + first +\
                    '&lastName='+ last + '&origin=SEO_PSERP'

req = requests.get(linked_link )

soup = BeautifulSoup(req.text, 'html.parser')
anchors = soup.find_all('a')

anchors['href']
finded = soup.find('href')
#<div class="search-result__info pt3 pb4 ph0">
#<a data-control-id="YfQDOUCvRrqNn+pzCyOOyg==" data-control-name="search_srp_result" href="/in/joni-adamson-b2004496/" id="ember65" class="search-result__result-link ember-view">      <h3 id="ember66" class="actor-name-with-distance search-result__title single-line-truncate ember-view">  <span class="name-and-icon"><span class="name-and-distance">
anchors[0]

