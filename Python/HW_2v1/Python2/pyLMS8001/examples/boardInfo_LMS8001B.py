from pyLMS8001 import *

boards = LMS8001_EVB.findLMS8001()
lms8001_evb = LMS8001_EVB(boards[0])
print("*"*80)
lms8001_evb.printInfo()
print("*"*80)
lms8001 = lms8001_evb.LMS8001
lms8001.printChipInfo()
print("*"*80)
lms8001.infoLDO()
for channel in ['A','B','C','D']:
    lms8001.infoHLMIX(channel)
    print("*"*80)


