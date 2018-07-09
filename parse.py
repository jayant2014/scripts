#!/usr/bin/python

import re

in_file = open("test.txt", "r") 
list = in_file.readlines() 
in_file.close()

patterns = {}
patterns["abc"] = []
startcnt = 0
endcnt = 0
tag = None

#deepmodel = []
for line in list:
	line = line.rstrip().lstrip()
	#model = []
	if re.match(r".*:<",line):
		tag = line.split(':')[0]
		startcnt += 1
		#if startcnt == 1:
			#patterns[tag] = []
	elif re.match(r">;",line):
		endcnt += 1
		if startcnt == endcnt:
			break
	else:
		if re.match(r".*=.*;",line):
			deepmodel = []
			attr, val = line.split('=')
			if startcnt == 1:
				mode = {}
				mode[attr] = val
				patterns["abc"].append(mode)
			else:
				mode = {}
				mode[attr] = val
				deepmodel.append(mode)
				print("=============")
				print(deepmodel)
				#model.append(deepmodel)
			print(deepmodel)
			patterns["abc"].append(deepmodel)
	#elif re.match(r".*=.*;",line):
	#	if startcnt == 1:
	#		attr, val = line.split('=')
	#		print(attr)
	#		patterns[tag][attr] = val
	#	elif startcnt == 2:
	#		attr, val = line.split('=')
	#		patterns[tag][attr] = val
	#elif re.match(r">;",line):
	#	endcnt += 1
	#	print("============")
	#	print(startcnt)
	#	print(endcnt)
	#	if startcnt == endcnt:
	#		break
	#	else:
	#		continue
	#print(cnt)

print(patterns)
