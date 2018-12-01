import subprocess
import re
import time
import os

counter = 0
sent = []

with open('TLD.dictionary', 'r') as f:
    for line in f:
        fields = line.split()
        if fields[1] not in sent:
            counter += 1
            sent.append(fields[1])
            print(counter, fields[0], fields[1])
            for i in range(0, 500):
                 print (i)
                # os.system ("dig %s any @%s +recurse +bufsize=65535 +dnssec +aaonly +retry=0 +time=10 >> temp/task3-1.temp.%03d &"
                 print(fields[0])
                 print(fields[1])
                 os.system(
                     "dig %s any @8.8.8.8 +recurse +bufsize=65535 +dnssec +retry=0 +time=10 >> temp/task3-1.temp.%03d &"
                     % (fields[0], i))
                #os.system(
                #    "dig %s any @8.8.8.8 +recurse +bufsize=65535 +dnssec +retry=0 +time=10 >> temp/task3-1.temp.%03d &"
                #    % (fields[0], i))
            time.sleep(1.5)

    '''
    for line in f:
        fields = line.split(" ")
        #p = subprocess.Popen(["dig", fields[1].rstrip(), "+dnssec"], stdout=subprocess.PIPE)
        #p = subprocess.Popen(["dig", "+noall", "+answer", "-x", fields[1].rstrip(), "+dnssec"], stdout=subprocess.PIPE) # your original query
        auth_NS_IP = "@" + fields[1].rstrip()
        p = subprocess.Popen(["dig", fields[0].rstrip(), auth_NS_IP, "ANY", "+dnssec"], stdout=subprocess.PIPE)
        resultString = p.communicate()[0].decode('UTF-8')
        print(resultString)
        domainName = resultString.split(" ")
#        print(domainName[1])
    '''
# run The above with wireshark opened

# run the following commands againts the pcap
#tshark -r input.cap -q -z conv,udp > output.txt


