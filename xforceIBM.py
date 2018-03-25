import requests
from requests.auth import HTTPBasicAuth

import json

def myXForceChecker(url):

    # User: 473284ee-2c45-4719-a201-5e6c81c0253a
    # Password: 8acd0774-7238-4ad7-bc09-a2003ca6e80f

    # Auth first
    print ''
    print '[.] IBM X-Force Result'

    # e.g. url = "https://exchange.xforce.ibmcloud.com/ip//114.200.4.207"
    # IP Report
    myResult1 = requests.get(url, auth=HTTPBasicAuth('473284ee-2c45-4719-a201-5e6c81c0253a',
                                                     '8acd0774-7238-4ad7-bc09-a2003ca6e80f'))
    c1 = myResult1.content
    myJson1 = json.loads(c1)

    # >>>>>>>>>>>  IP/Domain Report Check <<<<<<<<<<<<<
    # ...........
    '''
    # indent = 2
    # json.dumps() change data to python dictionary
    # sortedData = json.dumps(myJson1, sort_keys=True, indent=2)
    # print sortedData
    '''

    #----------These three keys are for IP checker----------
    # [Print] Geo information
    if "geo" in myJson1:
        for key, value in myJson1["geo"].items():
            geo = "Country" + ": " + str(value)
            print geo
            # Only print country
            # (Ingore country code)
            break
    # [Print] Overrall Risk Score
    if "score" in myJson1:
        if myJson1["score"] == 1:
            print "Risk Score: " + str(myJson1["score"]) + " (low)"
        else:
            print "Risk Score: " + str(myJson1["score"])
    # [Print] Categorization:
    if "cats" in myJson1:
        if myJson1["cats"]:
            for key, value in myJson1["cats"].items():
                cat = str(key) + " (" + str(value) + "%)"
                print "Categorization: " + cat
        else:
            print "Categorization: Unsuspicious"


    # ----------These keys are for Domain checker----------
    if "result" in myJson1:
        myJsonResult = myJson1["result"]
        if myJsonResult["score"] == 1:
            print "Risk Score: " + str(myJsonResult["score"]) + " (low)"
        else:
            print "Risk Score: " + str(myJsonResult["score"])

        if myJsonResult["categoryDescriptions"]:
            for key, value in myJsonResult["categoryDescriptions"].items():
                cat = "<" + str(key).replace(" / ", "|") + ">: " + str(value)
                print cat
