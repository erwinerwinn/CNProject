import subprocess
import csv
import re

contain = 0
notContain = 0

raYes = 0
raNo = 0

messageSize=''

keyWords = ['dnssec', 'secdns']

with open('/Users/erwinerwinn/Desktop/MSSD/Computer Networks/CNProjects/top-120-sites copy.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        site = row['Site']
        # dig sutd.edu.sg +short +dnssec
        # dig DNSKEY cloudflare.com +short
        # dig +multi +noall +answer dnskey google.com  +short
        p = subprocess.Popen(["dig", site, "+dnssec"], stdout=subprocess.PIPE)
        resultString = p.communicate()[0].decode('UTF-8')

        # Check for DNSSEC indicators
        # if any(re.findall('|'.join(keyWords), resultString)):
        #     print(site + " Contains DNSSEC")
        #     contain += 1
        # else:
        #     print(site + " does not contain DNSSEC")
        #     notContain += 1

        # search for RA flag
        # regex for msg size:  [\q\d\s]*MSG SIZE  rcvd:[0-9 ]+

        flagCapture = re.search('[\w\d\s]*flags:[a-z ]+;', resultString).group(0)
        print(flagCapture)
        if 'ra' in flagCapture:
            print(site+" is recursively available")
            raYes += 1
        if 'ad' in flagCapture:
            print(site + " is DNSSec")
            contain += 1
        # else:
        #     print(site + " is not recursively available")
        #     raNo += 1

        # Message Size
        message = re.search('[\w\d\s]*MSG SIZE  rcvd:[0-9 ]+', resultString).group(0)
        messageSize = int(re.search('[\d][0-9 ]',message).group(0))
        print("msg size for {} is {}".format(site, messageSize))
        print()

print("============== Runtime Report ======================")
print("Contain DNSSec: ", +contain)
# print("Does not Contain DNSSec: ", +notContain)
print("no of sites that is recursive available: ", +raYes)
# print("No of sites that does not use recursive query: ", +raNo)

