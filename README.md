#### Webscraping Tool
Author: Patrick Dong

Modules Developed: abuseipdb.py, ipvoid.py, myIPWhois.py, sans.py, xforceIBM.py

#### Requirement
Python 2.7 and BeautifulSoup, requests, pandas


#### Usage
```
[kali-linux]$ python webscraping.py <IP|Domain>

>>>>> Welcome to WebScraping Tool <<<<<
Now checking 183.63.206.116 ...

[.] IP Whois Result
% [whois.apnic.net]
% Whois data copyright terms    http://www.apnic.net/db/dbcopyright.html

% Information related to '183.0.0.0 - 183.63.255.255'

% Abuse contact for '183.0.0.0 - 183.63.255.255' is '[email protected]'

inetnum:        183.0.0.0 - 183.63.255.255
netname:        CHINANET-GD
descr:          CHINANET Guangdong province network
descr:          Data Communication Division
descr:          China Telecom
country:        CN
admin-c:        IC83-AP
tech-c:         IC83-AP
status:         ALLOCATED PORTABLE
remarks:        service provider
remarks:        --------------------------------------------------------
remarks:        To report network abuse, please contact mnt-irt
remarks:        For troubleshooting, please contact tech-c and admin-c
remarks:        Report invalid contact via www.apnic.net/invalidcontact
remarks:        --------------------------------------------------------
mnt-by:         APNIC-HM
mnt-lower:      MAINT-CHINANET-GD
last-modified:  2016-05-04T00:19:59Z
source:         APNIC
mnt-irt:        IRT-CHINANET-CN

irt:            IRT-CHINANET-CN
address:        No.31 ,jingrong street,beijing
address:        100032
e-mail:         [email protected]
abuse-mailbox:  [email protected]
admin-c:        CH93-AP
tech-c:         CH93-AP
auth:           # Filtered
mnt-by:         MAINT-CHINANET
last-modified:  2010-11-15T00:31:55Z
source:         APNIC

person:         IPMASTER CHINANET-GD
nic-hdl:        IC83-AP
e-mail:         [email protected]
address:        NO.18,RO. ZHONGSHANER,YUEXIU DISTRIC,GUANGZHOU
phone:          +86-20-87189274
fax-no:         +86-20-87189274
country:        CN
mnt-by:         MAINT-CHINANET-GD
remarks:        IPMASTER is not for spam complaint,please send spam complaint to [email protected]
abuse-mailbox:  [email protected]
last-modified:  2014-09-22T04:41:26Z
source:         APNIC

% This query was served by the APNIC Whois Service version 1.88.15-43 (WHOIS-US4)



[.] IPVoid Result:
                    ITEM                                              DATA
0          Analysis Date                               2018-04-01 23:23:23
1           Elapsed Time                                         1 seconds
2       Blacklist Status                                  BLACKLISTED 6/96
3             IP Address                                    183.63.206.116
4            Reverse DNS                                           Unknown
5                    ASN                                          AS134772
6              ASN Owner  CHINANET Guangdong province Dongguan MAN network
7                    ISP                           China Telecom Guangdong
8              Continent                                              Asia
9           Country Code                                        (CN) China
10  Latitude / Longitude                                  23.1167 / 113.25
11                  City                                         Guangzhou
12                Region                                        Guangdong  


[.] SANS Result
Report Times: 119
Total Targets: 45
First Reported: 2017-11-02
Recent Report: 2018-03-30 14:14:27


[.] AbuseIPDB Result
Reported 8 times
             Date            Reporter                            Category
0   1 minute ago        greensnow.co                       | Port Scan | 
1    29 Mar 2018        greensnow.co                       | Port Scan | 
2    18 Mar 2018        greensnow.co                       | Port Scan | 
3    24 Feb 2018        greensnow.co                       | Port Scan | 
4    05 Nov 2017            Anonymous                      | Port Scan | 
5    18 Oct 2017    danielmellum.com                       | Port Scan | 
6    21 Nov 2016            Anonymous   | DDoS Attack | Exploited Host | 
7    22 Nov 2015        greensnow.co                         | Hacking |  

[.] IBM X-Force Result
Country: China
Risk Score: 1 (low)
Categorization: Unsuspicious
```
