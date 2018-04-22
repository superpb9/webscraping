#!/usr/bin/python
from __future__ import print_function
import sys
import re
import abuseipdb, ipvoid, sans, myIPwhois, xforceIBM

def webscraping():
    myIPvoidPrint1 = ''
    mySansPrint2 = ''
    myAbuseIPDBPrint3 = ''
    myXForcePrint4 = ''

    if len(sys.argv) != 2:
        print('>>>>> Welcome to my WebScraping Tool <<<<<')
        print('     Usage: python webscraping.py [x.x.x.x | domain]')
    else:
        print('>>>>> Welcome to WebScraping Tool <<<<<')

        # regular expression for IP
        re_ip = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

        print("Now checking " + sys.argv[1] + " ...")
        print("")

        # If the IP format is valid:
        if re_ip.match(sys.argv[1]):
            # Call myIPwhois.py
            myIPwhois.IPWhoisChecker("https://www.abuseipdb.com/whois/" + sys.argv[1])

            # Call ipvoid.py
            myIPvoidPrint1 = ipvoid.ipvoidChecker(sys.argv[1])

            # Call sans.py
            mySansPrint2 = sans.sansChecker(sys.argv[1])

            # Call abuseipdb.py
            myAbuseIPDBPrint3 = abuseipdb.abuseipdbChecker("https://www.abuseipdb.com/check/" + sys.argv[1])

            # Call xforceIBM.py
            myXForcePrint4 = xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/ipr/" + sys.argv[1])


        # If the input is a domain or other strings, let the website validate then ...
        else:
            #Call myIPwhois.py
            myIPwhois.IPWhoisChecker("https://www.abuseipdb.com/whois/" + sys.argv[1])

            # Call sans.py
            # sans.sansChecker("https://isc.sans.edu/api/ip/" + sys.argv[1])
            sans.sansChecker(sys.argv[1])

            # Call abuseipdb.py
            abuseipdb.abuseipdbChecker("https://www.abuseipdb.com/check/" + sys.argv[1])

            # Call xforceIBM.py
            # Check the domain
            xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/url/" + sys.argv[1])

    print ("")
    print ("[.] IPVoid Result: " + myIPvoidPrint1)
    print ("[.] SANS Result: " + ' | '.join(mySansPrint2))
    print ("[.] AbuseIPDB Result: " + myAbuseIPDBPrint3)
    print ("[.] XForce Result:  " + ' | '.join(myXForcePrint4))

if __name__ == '__main__':
    webscraping()

