import os,sys
from time import sleep
from fac_def import *
from variables import *

tc_num = os.path.basename(__file__).split('.')[0]
path = "C:\\fac_test_dir\\%s"%tc_num

if os.path.isfile(path) == False:
	f = open(path,'w')
	f.write("TC14_12_5_delete test file")
	f.close()
try:
	os.remove("C:\\fac_test_dir\\%s"%tc_num)
except Exception as e:
	print(e)
sleep(1)

if logCheck(tc_num) == policy_status :
	print("true")
	sys.exit(0)
else :
	print("fail")
	sys.exit(-1)

