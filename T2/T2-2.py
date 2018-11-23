import re


topAF = [5]
afDict = {}

with open('/Users/erwinerwinn/Desktop/MSSD/Computer Networks/CNProjects/T2/T2-Analysis.txt', 'r') as f:
    for line in f:
        fields = line.split()
        port = re.search('(?<=:).*$', fields[2]).group(0)
        srcIP = fields[0]
        dstIP = fields[2]
        requestSize = int(fields[6])
        responseSize = int(fields[4])

        if ( port == "53"):
            if(dstIP not in afDict.keys()):
                try:
                    amplificationFactor = responseSize / requestSize
                except:
                    amplificationFactor = 0
                afDict[dstIP] = [amplificationFactor, responseSize, requestSize]

    print("Top 10 dst with Highest Amplification Factor")
    for k, v in sorted(afDict.items(), key=lambda kv: kv[1], reverse= True)[:10]:
        print("Destination IP: ", k, "has amplification factor of: ", v[0], " Request sent: ",v[2], " response received: ", v[1])