from pyLMS8001 import *


boards = LMS8001_EVB.findLMS8001()
lms8001_evb = LMS8001_EVB(boards[0])
lms8001_evb.LMS8001_Reset()
print("*"*80)
lms8001_evb.printInfo()
print("*"*80)
lms8001 = lms8001_evb.LMS8001
lms8001.printChipInfo()


# The purpose of this example is to explain basic functions for manipulating and configuring 
# the PLL and LO-Distribution subsystems inside the LMS8001-IC
#####################################################################################
# First define LO channels which will be used
lms8001.PLL.setLODIST(channel="A", EN=1, IQ=False, phase=0)
lms8001.PLL.setLODIST(channel="C", EN=1, IQ=False, phase=180)

# Tune the PLL to desired frequency [Hz]
lms8001.PLL.frequency=6.0e9

# User can also setup PLL loop dynamics by using setLoopBW method 
# Arguments are desired PLL 3dB close loop bandwidth [Hz] and phase margin [deg]
lms8001.PLL.setLoopBW(LoopBW=340e3, PM=55)

# Use setFastLockLoopBW method to explicitly define PLL loop dynamics during fast-lock mode
lms8001.PLL.setFastLockLoopBW(LoopBW=500.0e3, PM=50, FLOCK_N=450)
#####################################################################################


# Previous functions were all used for currently active PLL profile configuration
# By defaults it is PLL Profile 0 (zero)
#####################################################################################
# User should manualy change active PLL profile in order to configure another PLL profile
lms8001.PLL.ACTIVE_PROFILE=3


# First define LO channels which will be used
lms8001.PLL.setLODIST(channel="B", EN=1, IQ=True, phase=90)
lms8001.PLL.setLODIST(channel="D", EN=1, IQ=True, phase=270)

# Tune the PLL to desired frequency [Hz]
# When user wants to have quadrature phases at LO-DIST output
# PLL should be tuned to the 2x  of the value of desired LO-DIST output frequency
lms8001.PLL.frequency=4.1511e9*2


# User can also setup PLL loop dynamics by using setLoopBW method 
# Arguments are desired PLL 3dB close loop bandwidth [Hz] and phase margin [deg]
lms8001.PLL.setLoopBW(LoopBW=300e3, PM=55)

# Use setFastLockBWEF method to define PLL loop dynamics during fast-lock mode
# BWEF - ratio of loopBW in fast-lock and normal operation mode
# This is simpler method for Fast-Lock mode definition
lms8001.PLL.setFastLockBWEF(BWEF=2.0, FLOCK_N=300)
#####################################################################################

# Use the infoConfig() method of PLL class object to print the LMS8001-PLL configuration
# for active PLL profile
lms8001.PLL.infoConfig(printInfo=True)
#####################################################################################

# Use the infoConfig() method for PLL Profile class object to print the LMS8001-PLL configuration
# which is defined in the PLL profile which is not currently active
lms8001.PLL.PROFILES[0].infoConfig(printInfo=True)
#####################################################################################
