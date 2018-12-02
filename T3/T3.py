import subprocess
import datetime
from time import sleep
import os

counter = 0
time = datetime.datetime.now()
timestamp = time.strftime("%Y-%m-%d-%H:%M")
output_filename = "output." + timestamp +".txt"
output_file = open(output_filename, "w")
sent = []

with open('TLD.dictionary', 'r') as f:
    for line in f:
        fields = line.split(" ")
        if fields[1].rstrip() not in sent:
            sent.append(fields[1].rstrip())
            for i in range(500):
                print(i + 1)
                output_file.write("Packet %s" % (i + 1))
                query_str = "dig %s @%s ANY +recurse +dnssec +bufsize=65535 +recurse +retry=0 +time=3 +notcp" % (
                fields[0].rstrip(), fields[1].rstrip())
                proc = subprocess.Popen(query_str, shell=True,
                                        stdin=None, stdout=None, stderr=None, close_fds=True)

# run The above with wireshark opened

# run the following commands againts the pcap
#tshark -r input.cap -q -z conv,udp > output.txt
