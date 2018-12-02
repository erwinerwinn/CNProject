import subprocess
import datetime
import time
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
        if sent.__contains__(fields[1].rstrip()):
            # skip this ip address
            continue
        else:
            sent.append(fields[1].rstrip())
            success = 0  # for counting the number of successful queries
            for i in range(500):
                print(i + 1)
                output_file.write("Packet %s" % (i + 1))
                auth_NS_IP = "@" + fields[1].rstrip()
                p = subprocess.Popen(
                    ["dig", fields[0].rstrip(), auth_NS_IP, "+dnssec", "+retry=0", "+recurse", "+time=10",
                     "+bufsize=65535"], stdout=subprocess.PIPE)
                # p = subprocess.Popen(["dig", "edu.sg", "ANY", "@8.8.8.1", "+dnssec", "+retry=0", "+recurse", "+time=1"], stdout=subprocess.PIPE)
                resultString: str = p.communicate()[0].decode('UTF-8')

                if resultString.__contains__("connection timed out"):  # check whether there is a response was received
                    ...
                else:
                    success += 1

                print(resultString)  # print to console
                output_file.write(resultString)  # write to output file

            print("Number of successful packets: %s out of 500 packets" % (success))
            output_file.write("\n========================================================================\n")
            output_file.write("Statistics: \t| Source \t| Destination \t| Sent \t| Received \t| Success(%)\n")
            output_file.write("Statistics: \t| %s \t| %s \t| 500 \t| %s \t| %s\n" % (
            fields[0].rstrip(), fields[1].rstrip(), success, str(success / 500 * 100)))
            # output_file.write("Number of successful packets: %s out of 500 packets" % (success))
            output_file.write("========================================================================\n\n")

# run The above with wireshark opened

# run the following commands againts the pcap
#tshark -r input.cap -q -z conv,udp > output.txt
