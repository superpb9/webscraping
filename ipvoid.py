from bs4 import BeautifulSoup
import requests

import pandas as pd
from pandas import Series, DataFrame

def ipvoidChecker(ip):

    url = "http://www.ipvoid.com/ip-blacklist-check/"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Referer":"http://www.ipvoid.com/ip-blacklist-check/",}
    payload = {'ip':ip}
    # Note: Using 'data' instead of 'params'
    r = requests.post(url, headers=headers, data=payload)
    returnData = r.content
    soup = BeautifulSoup(returnData, "lxml")

    #mySoup = soup.find('div', {'class': 'responsive'})
    tables = soup.find_all(class_="table table-striped table-bordered")

    column1 = []
    column2 = []

    if tables !=[]:
        rows = tables[0].findAll('tr')
        for tr in rows:
            cols = tr.findAll('td')
            column1.append(cols[0].text)
            column2.append(cols[1].text.
                           replace(" Find Sites | IP Whois","").
                           replace(" Google Map",""))
    # Panda Series
    column1 = Series(column1)
    column2 = Series(column2)

    # Concatenate into a DataFrame
    legislative_df = pd.concat([column1, column2], axis=1)

    # Set up the columns
    legislative_df.columns = ['ITEM', 'DATA']

    # Show the finished DataFrame
    print '[.] IPVoid Result:'
    print legislative_df,'\n\n'