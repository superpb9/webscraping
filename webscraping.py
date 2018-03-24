#!/usr/bin/python
import sys
import re
import abuseipdb, sans, myIPwhois, xforceIBM

def webscraping():
    if len(sys.argv) != 2:
        print('>>>>> Welcome to my WebScraping Tool <<<<<')
        print('     Usage: python webscraping.py [x.x.x.x | domain]')
    else:
        print('>>>>> Welcome to WebScraping Tool <<<<<')

        # regular expression for IP
        re_ip = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

        print("Now checking " + sys.argv[1] + " ...")
        print ''

        # If the IP format is valid:
        if re_ip.match(sys.argv[1]):
            # Call myIPwhois.py
            myIPwhois.IPWhoisChecker("https://www.abuseipdb.com/whois/" + sys.argv[1])

            # Call sans.py
            sans.sansChecker("https://isc.sans.edu/api/ip/" + sys.argv[1])

            # Call abuseipdb.py
            abuseipdb.abuseipdbChecker("https://www.abuseipdb.com/check/" + sys.argv[1])

            # Call xforceIBM.py
            xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/ipr/" + sys.argv[1])


        # If the input is a domain or other strings, let the website validate then ...
        #else:
            # Call myIPwhois.py
            #myIPwhois.IPWhoisChecker("https://www.abuseipdb.com/whois/" + sys.argv[1])

            # Call sans.py
            #sans.sansChecker("https://isc.sans.edu/api/ip/" + sys.argv[1])

            # Call abuseipdb.py
            #abuseipdb.abuseipdbChecker("https://www.abuseipdb.com/check/" + sys.argv[1])

            # Call xforceIBM.py
            #xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/ipr/" + sys.argv[1])

if __name__ == '__main__':
    webscraping()

