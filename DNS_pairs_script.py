from subprocess import call
import os
import sys

with open ("./root.zone.txt") as f:

	count = 0
	alt_count = 0
	TLD_Dict = {}

	for line in f:

		# print (line)
		fields = line.split()
		if (fields[3] == 'NS') :
			if fields[0] not in TLD_Dict : 
				TLD_Dict[fields[0]] = []
				count += 1
			TLD_Dict[fields[0]].append(fields[4])
			alt_count += 1
	


	print ("TLD Count = ", count)
	print ("Alt NS = ", alt_count)

	# sys.exit (0)

	
	f.seek (0)
	a_count = 0
	for line in f:
		fields = line.split()
		if (fields[3] == 'A') :
			for TLD in TLD_Dict :
				for i,NS in enumerate(TLD_Dict[TLD]) :
					if (NS == fields[0]) :
						# print (TLD, NS, fields[0], fields[4])
						TLD_Dict[TLD][i] = fields[4]
						# TLD_Dict[TLD] = fields[4]
						a_count += 1
	

	print ("Address Count = ", a_count)

	# sys.exit (0)

	pair = 0
	import ipaddress
	fout = open ("TLD.dictionary", "w")
	for TLD in sorted(TLD_Dict) :
		for A in TLD_Dict[TLD] :
			try:
				IPv4 = ipaddress.ip_address (A)
				fout.write (str(TLD) + " " + str(A) +"\n")
				pair += 1
			except ValueError :
				print (TLD + " => " + A)
	fout.close ()

	print ("Size of Dictionary = ", len(TLD_Dict))
	print ("Number of TLD-IPv4 pairs = ", pair)
	f.close ()

# End of Program ...
