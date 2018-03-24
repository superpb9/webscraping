from bs4 import BeautifulSoup
import requests

def sansChecker(url):

    # URL = "https://isc.sans.edu/api/ip/x.x.x.x"
    # HTTP Query
    myResult = requests.get(url)

    c = myResult.content
    soup = BeautifulSoup(c, "lxml")
    mySoup = soup.find('error')
    print '[.] SANS Result'

    # If the input IP has a correct format
    if mySoup is None:
        c = myResult.content
        soup = BeautifulSoup(c, "lxml")

        try:
            reportedTimes = soup.find('count')
            if reportedTimes.text != '':
                print 'Report Times: ' + str(reportedTimes)
            else:
                print 'Report Times: 0'
        except Exception:
            print 'Report Times: 0'

        try:
            targets = soup.find('attacks')
            if targets.text != '':
                print 'Total Targets: ' + str(targets)
            else:print 'Total Targets: 0'
        except Exception:
            print 'Total Targets: 0'

        try:
            firstReported = soup.find('mindate')
            if firstReported.text != '':
                print 'First Reported: ' + str(firstReported)
            else:
                print 'First Reported: 0'
        except Exception:
            print 'First Reported: 0'

        try:
            latestReported = soup.find('updated')
            if latestReported.text != '':
                print 'Recent Report: ' + str(latestReported)
            else:
                print 'Recent Report: 0'
        except Exception:
            print 'Recent Report: 0'

        print "\n"

    # Elif the input IP is wrong
    elif mySoup.text == 'bad IP address':
        print 'We expected a valid IP address.'
        exit()