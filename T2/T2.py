import subprocess
import re

counter = 0

with open('TLD.dictionary', 'r') as f:
    for line in f:
        fields = line.split(" ")
        #p = subprocess.Popen(["dig", fields[1].rstrip(), "+dnssec"], stdout=subprocess.PIPE)
        p = subprocess.Popen(["dig", "+noall", "+answer", "-x", fields[1].rstrip(), "+dnssec"], stdout=subprocess.PIPE)
        resultString = p.communicate()[0].decode('UTF-8')
        print(resultString)
        domainName = resultString.split(" ")
        print(domainName[1])

# run The above with wireshark opened

# run the following commands againts the pcap
#tshark -r input.cap -q -z conv,udp > output.txt
