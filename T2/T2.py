import subprocess
import re

counter = 0

with open('TLD.dictionary', 'r') as f:
    for line in f:
        fields = line.split(" ")
        print(fields[1])

        p = subprocess.Popen(["dig", fields[1], "NS"], stdout=subprocess.PIPE)
        resultString = p.communicate()[0].decode('UTF-8')



# run The above with wireshark opened

# run the following commands againts the pcap
#tshark -r input.cap -q -z conv,udp > output.txt
