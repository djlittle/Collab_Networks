# -------------------------------------------------------------------------------
# Name: scopus_grab.py
# Purpose: Web scrape from Scopus for the Collaboration Networks Project
#
# Author(s):    David Little
#
# Created:      06/25/2020
# Updated:
# Update Comment(s):
#
# TO DO:
#
# -------------------------------------------------------------------------------

#import elsapy

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor
from elsapy.elssearch import ElsSearch
import pandas as pd

names_csv = 'sustainability-persons_no_sir_sub.csv'
df = pd.read_csv(names_csv, error_bad_lines=False)

API_KEY = 'd54807cb12735c3d461f169c0ae75a2e'

## Initialize client
client = ElsClient(API_KEY)

query = 'AUTHFIRST(%s) AND AUTHLASTNAME(%s)'# AND AF-ID(60003892)'

#name_list = df["Name"][86].split()
#first,last = name_list[0],name_list[len(name_list)-1]
name = df["Name"].iloc[26]

profile_urls = []
for name in df["Name"]:
    name_list = name.split()
    first, last = name_list[0], name_list[len(name_list) - 1]
    auth_srch = ElsSearch(query%(first,last),'author')
    auth_srch.execute(client)
    #print ("auth_srch has", len(auth_srch.results), "results.")
    try:
        url = auth_srch.results[0]['prism:url']
        print(name, url)
        profile_urls.append([name,url])
    except:
        print('Author: '+name+' not found.')
        profile_urls.append([name,''])
scopus_urls = pd.DataFrame(data=profile_urls, columns=['Name', 'URL'])

scopus_urls.to_csv('scopus_urls_no_affil_full.csv', index=False)
len(scopus_urls['Name'].unique())
len(scopus_urls['URL'].unique())

# scopus_urls_back = scopus_urls
#scopus_urls_back.to_csv('scopus_urls.csv', index=False)


# ---------------------------------- author subjects ------------------------------

urls_filepath = 'scopus_urls_no_affil_sub.csv'
scopus_urls = pd.read_csv(urls_filepath, error_bad_lines=False)
scopus_urls.fillna(-1, inplace=True)

#url = scopus_urls['URL'][0]
subjects = []
for url in scopus_urls['URL']:
    if not(url == -1):
        my_auth = ElsAuthor(uri=url)
        if my_auth.read(client):
            print("Retrieving ", my_auth.full_name)
        else:
            print("Read author failed.")
        try:
            for item in my_auth.data['subject-areas']['subject-area']:
                subjects.append([my_auth.full_name, item['$']])
            print(my_auth.full_name+': Subjects pulled successfully')
        except:
            print(my_auth.full_name+': No subjects identified')

subjects_edgelist = pd.DataFrame(data=subjects, columns=['Name', 'Subject'])
#subjects_edgelist.to_csv('subjects_edgelist_no_affil_full.csv', index=False)

len(subjects_edgelist['Name'].unique())
len(subjects_edgelist['Subject'].unique())


sub = pd.read_csv(urls_filepath, error_bad_lines=False)
len(sub['Name'].unique())
len(sub['URL'].unique())

sub_e = pd.read_csv('subjects_edgelist_no_affil_sub.csv', error_bad_lines=False)
len(sub_e['Name'].unique())
len(sub_e['Subject'].unique())
