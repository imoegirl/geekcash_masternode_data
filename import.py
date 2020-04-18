import json
import os

def import_address(address, index):
	command = 'geekcash-cli -datadir=d:/geekcash importaddress %s watch_%d false' % (address, index)
	sl = os.popen(command).read()
	print("import address: ", address, "index: ", index, "output: ", sl)


with open("d:/mn2_address.txt", 'r') as f:
	json_data = json.load(f)
	index = 904
	for x in json_data:
		#import_address(x, index)
		#index += 1
		print(x)

# command = 'geekcash-cli -datadir=d:/geekcash listtransactions'

# sl = os.popen(command).read()

# print(sl)