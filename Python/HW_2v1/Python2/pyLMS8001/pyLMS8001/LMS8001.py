
# Add power

from LMS8001_REGDESC import *
from LMS8001_regDataStructs import *
# added by pavlej
from LMS8001_PLL_METHODS import *

from LMS8001_GPIO import *
from LMS8001_CHIP import *
from LMS8001_BIAS import *
from LMS8001_LDO import *
from LMS8001_CHANNEL import *
from LMS8001_HLMIX import *
from LMS8001_PLL import *

class LMS8001(object):

    def __init__(self, SPIwriteFn=None, SPIreadFn=None, verbose=0):
        self._fRef = 40e6
        self._SPIwriteFn = SPIwriteFn
        self._SPIreadFn = SPIreadFn
        self._SPIImmediate = True
        self.verbose = verbose
        regDefList = LMS8001_REGDESC.split('\n')
        regParser = regDescParser(regDefList, self)
        self.regDesc = regParser.getRegisterDefinition()
        
        # GPIO
        self.GPIO = [0]*9
        for i in range(0,9):
            self.GPIO[i] = LMS8001_GPIO(self, i)

        # Chip config
        self.CHIP = LMS8001_CHIP(self)
        
        # Bias
        self.BIAS = LMS8001_BIAS(self)

        # On-chip LDOs
        self.LDOofs = 0.86
        self.LDOcoef = 3.92e-3
        self.LDOlist = ['LOBUFA', 'LOBUFB', 'LOBUFC', 'LOBUFD', 'HFLNAA', 'HFLNAB', 'HFLNAC', 'HFLNAD', 'CLK_BUF', 'PLL_DIV', 'PLL_CP', 'DIG_CORE']

        self.LDO = {}
        for LDOname in self.LDOlist:
            self.LDO.update({LDOname:LMS8001_LDO(self,LDOname)})
        
        # RF channels of LMS8001A
        self.CHANNEL = { 'A' : LMS8001_CHANNEL(self, 'A'),
                         'B' : LMS8001_CHANNEL(self, 'B'),
                         'C' : LMS8001_CHANNEL(self, 'C'),
                         'D' : LMS8001_CHANNEL(self, 'D')}

        # HLMIX channels of LMS8001B
        self.HLMIX = { 'A' : LMS8001_HLMIX(self, 'A'),
                       'B' : LMS8001_HLMIX(self, 'B'),
                       'C' : LMS8001_HLMIX(self, 'C'),
                       'D' : LMS8001_HLMIX(self, 'D')}
        
        # PLL
        self.PLL = LMS8001_PLL(self, self._fRef)
        
        # Temperature sensor coefficients
        self.T0 = -105.45
        self.T1 = 1.2646
        self.T2 = -0.000548
        
        # Block power
        # LNA
        self.LNAMainICC = [20e-3]*15
        self.LNALinICC = [20e-6]*15
        self.LNAVDD = 1.8
        
        # PA
        self.PAMainICC = [20e-3]*15
        self.PALinICC = [20e-6]*15
        self.PAVDD = 1.3
        
        # MIXA
        self.MIXAICC = [25e-3]
        self.MIXAVDD = 1.3

        # MIXB
        self.MIXBICC = [25e-3]
        self.MIXBVDD = 1.3
        
        # HLMIX
        self.HLMIXVDD = 1.3
        self.HLMIXBIASICC = [25e-3]
        self.HLMIXLOICC = [25e-3]
        self.HLMIXIbNom = 20e-6        
        

    @property
    def fRef(self):
        return self._fRef
        
    @fRef.setter
    def fRef(self, f):
        self._fRef = f
        self.PLL.fRef = f

    @property
    def SPIImmediate(self):
        return self.getImmediateMode()

    def getImmediateMode(self):
        return self._SPIImmediate

    @SPIImmediate.setter
    def SPIImmediate(self, val):
        self.setImmediateMode(val)

    def setImmediateMode(self, immediateMode):
        self._SPIImmediate=immediateMode

    @property
    def SPIwriteFn(self):
        return self.getSPIwriteFn()
        
    def getSPIwriteFn(self):
        return self._SPIwriteFn

    @property 
    def SPIreadFn(self):
        return self.getSPIreadFn()
    
    def getSPIreadFn(self):
        return self._SPIreadFn
                
    def enableInteractiveMode(self):
        if self.verbose>1:
            self.log("Enabling interactive mode")
        self.setImmediateMode(True)
    
    def disableInteractiveMode(self):
        if self.verbose>1:
            self.log("Disabling interactive mode")
        self.setImmediateMode(False)
        
    def isInteractive(self):
        return self.getImmediateMode()
        
    def getRegisterByName(self, regName):
        reg = self.regDesc.getRegisterByName(regName)
        return reg
        
    def getRegisterByAddress(self, regAddr):
        reg = self.regDesc.getRegisterByAddress(regAddr)
        return reg

    def log(self, msg):
        print msg

    #
    # Auxiliary functions
    #

    @staticmethod
    def intToHex(val, upperCase=True):
        hexVal = hex(val)[2:]
        while len(hexVal)<4:
            hexVal = "0"+hexVal
        if upperCase:
            hexVal = hexVal.upper()
        hexVal = "0x"+hexVal
        return hexVal

    @staticmethod
    def fixLen(string, length, center=True):
        res = string
        if not center:
            while len(res)<length:
                res += " "
        else:
            nSpaces = length-len(string)
            if nSpaces>0:
                if nSpaces%2==1:
                    nLeft = nSpaces//2+1
                    nRight = nSpaces//2
                else:
                    nLeft = nSpaces//2
                    nRight = nSpaces//2
                res = " "*nLeft + res + " "*nRight
        return res
        
    #
    # Register reading/writing functions
    #
        
    def readRegisters(self, regAddrs="ALL"):
        """
        Read registers from LMS8001 at given addresses.
        regAddrs = [ regAddr, regAddr, ...]
        If regAddrs = "ALL" all registers are read.
        
        Read values are written to registers and returned as a list.
        """
        if self.SPIreadFn==None:
            self.log("SPIreadFn not set, skipping")
            return []
        if regAddrs == "ALL":
            addrList = self.regDesc.getRegisterAddresesByName("ALL")
        else:
            addrList = regAddrs
        regValues = self.SPIreadFn(addrList)
        for i in range(0,len(addrList)):
            addr = addrList[i]
            reg = self.getRegisterByAddress(addr)
            reg.setValue(regValues[i], noUpdate=True)
        return regValues

    def readRegistersByName(self, regNames="ALL"):
        """
        Read registers from LMS8001 by names.
        regNames = [ regName, regName, ...]
        If regNames = "ALL" all registers are read.
        
        Read values are written to registers and returned as a list.
        """
        if self.SPIreadFn==None:
            self.log("SPIreadFn not set, skipping reading from SPI")
            return []
        addrList = self.regDesc.getRegisterAddresesByName(regNames)
        regValues = self.SPIreadFn(addrList)
        for i in range(0,len(addrList)):
            addr = addrList[i]
            reg = self.getRegisterByAddress(addr)
            reg.setValue(regValues[i], noUpdate=True)
        return regValues

    def writeRegisters(self, regAddrs="ALL"):
        """
        Write registers to LMS8001 at given addresses.
        regAddrs = [ regAddr, regAddr, ... ]
        If regAddrs = "ALL" all registers are written.
        Values to be written are taken from memory.
        """
        if self.SPIwriteFn==None:
            self.log("SPIwriteFn not set, skipping  writing to SPI")
            return
        if regAddrs == "ALL":
            addrList = self.regDesc.getRegisterAddresesByName("ALL")
        else:
            addrList = regAddrs
        toWriteList = []
        for i in range(0, len(addrList)):
            addr = addrList[i]
            reg = self.getRegisterByAddress(addr)
            val = reg.getValue(noUpdate=True)
            toWriteList += [ (addr, val) ]
        self.SPIwriteFn( toWriteList )

    def writeRegistersByName(self, regNames="ALL"):
        """
        Write registers to LMS8001.
        regNames = [ "regName", "regName", ... ]
        If regNames = "ALL" all registers are written.
        Values to be written are taken from memory.
        """
        if self.SPIwriteFn==None:
            self.log("SPIwriteFn not set, skipping writing to SPI")
            return
        addrList = self.regDesc.getRegisterAddresesByName(regNames)
        toWriteList = []
        for i in range(0, len(addrList)):
            addr = addrList[i]
            reg = self.getRegisterByAddress(addr)
            val = reg.getValue(noUpdate=True)
            toWriteList += [ (addr, val) ]
        self.SPIwriteFn( toWriteList )
    
    #
    # Ini file input/output functions
    #
    
    def readIniFile(self, fileName, ignoreErrors=True):
        """
        Read register values from ini file
        """
        f = open(fileName, 'r')
        section = ""
        for line in f:
            tmp = line.strip()
            if tmp=="":
                continue
            if tmp=="[file_info]":
                section="file_info"
                continue
            elif tmp=="[lms8001_registers]":
                section="registers"
                continue
            elif tmp=="[temp_sens_coeff]":
                section="temp_sens_coeff"
                continue
            elif tmp=="[reference_clock]":
                section="reference_clock"
                continue                
            else:
                if "[" in tmp:
                    if ignoreErrors:
                        continue
                    else:
                        raise ValueError("Unknown section "+line)
            if section=="file_info":
                continue
            elif section=="registers":
                addrStr, valStr = tmp.split("=")
                addr = int(addrStr, 16)
                val = int(valStr, 16)
                if ignoreErrors:
                    try:
                        reg = self.getRegisterByAddress(addr)
                        reg.setValue(val, noUpdate=True)
                    except:
                        continue
                else:
                    reg = self.getRegisterByAddress(addr)
                    reg.setValue(val, noUpdate=True)
            elif section=="temp_sens_coeff":
                name, valStr = tmp.split("=")
                if name=="T0":
                    self.T0 = float(valStr)
                else:
                    if ignoreErrors:
                        continue
                    else:
                        raise ValueError("Unknown coefficient "+name)
            elif section=="reference_clock":
                name, valStr = tmp.split("=")
                if name=="ref_clk_mhz":
                    self.ref_clk_mhz = float(valStr)
                else:
                    if ignoreErrors:
                        continue
                    else:
                        raise ValueError("Unknown coefficient "+name)                        
        self.writeRegisters()                        

    def writeIniFile(self, fileName, readRegisters=True):
        if readRegisters:
            self.readRegisters()
        f = open(fileName, 'w')
        f.write("[file_info]\n")
        f.write("type=lms8001_minimal_config\n")
        f.write("version=1\n")
        f.write("[lms8001_registers]\n")
        addrList = self.regDesc.getRegisterAddresesByName("ALL")
        addrList.sort()
        for addr in addrList:
            reg = self.getRegisterByAddress(addr)
            val = reg.getValue(noUpdate=True)
            strToWrite = self.intToHex(addr)+"="+self.intToHex(val)+"\n"
            f.write(strToWrite)
        f.write("[temp_sens_coeff]\n")
        f.write("T0="+str(self.T0))
        f.close()

    #
    # Operator overloading
    #        

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.getRegisterByAddress(key)
        else:
            return self.getRegisterByName(key)
   
    def __setitem__(self, key, val):
        if isinstance(key, int):
            reg = self.getRegisterByAddress(key)
        else:
            reg = self.getRegisterByName(key)
        reg.setValue(val)

    #
    #
    #

    def chipInfo(self):
        reg = self.getRegisterByName('ChipInfo')
        chipVer = reg['VER<4:0>']
        chipRev = reg['REV<4:0>']
        chipMask = reg['MASK<5:0>']
        if self.verbose>0:
            self.log("Chip version  : "+str(chipVer))
            self.log("Chip revision : "+str(chipRev))
            self.log("Chip mask     : "+str(chipMask))
        return (chipVer, chipRev, chipMask)

    def printChipInfo(self):
        reg = self.getRegisterByName('ChipInfo')
        chipVer = reg['VER<4:0>']
        chipRev = reg['REV<4:0>']
        chipMask = reg['MASK<5:0>']
        self.log("Chip version  : "+str(chipVer))
        self.log("Chip revision : "+str(chipRev))
        self.log("Chip mask     : "+str(chipMask))
    
    def chipTemperature(self):
        immMode = self.isInteractive()
        self.enableInteractiveMode()
        regXBuf = self.getRegisterByName('PLL_CFG_XBUF')
        xbufState = regXBuf['PLL_XBUF_EN']
        if xbufState==0:
            if self.verbose>1:
                self.log("Enabling PLL XBUF")
            regXBuf['PLL_XBUF_EN'] = 1
        reg = self.getRegisterByName('TEMP_SENS')        
        reg['TEMP_SENS_EN'] = 1
        reg['TEMP_SENS_CLKEN'] = 1
        reg['TEMP_START_CONV'] = 1
        while reg['TEMP_START_CONV']==1:
            continue
        tempRead = reg['TEMP_READ<7:0>']
        reg['TEMP_SENS_EN'] = 0
        reg['TEMP_SENS_CLKEN'] = 0
        if xbufState==0:
            if self.verbose>1:
                self.log("Disabling PLL XBUF")
            regXBuf['PLL_XBUF_EN'] = 0
        if not immMode:
            self.disableInteractiveMode()
        temperature = self.T0 + self.T1 * tempRead + self.T2 * tempRead*tempRead
        return temperature

    #
    # Bias
    #
    
    def calibrateBias(self):
        pass

    #
    # LDO related
    #
    
    def getLDOconfig(self, ldoName):
        """
        Get the LDO configuration
        """
        regName = ldoName+"_LDO_Config"
        reg = self.getRegisterByName(regName)
        enLoadImp = reg['EN_LOADIMP_LDO_'+ldoName]
        spDup = reg['SPDUP_LDO_'+ldoName]
        if ldoName=="DIG_CORE":
            enabled = 1-reg['PD_LDO_DIG_CORE']
        else:
            enabled = reg['EN_LDO_'+ldoName]
        rdiv = reg['RDIV_'+ldoName+'<7:0>']
        vout = self.LDOofs + rdiv * self.LDOcoef
        return (enLoadImp, spDup, enabled, vout)
        
    def infoLDO(self, ldoList="ALL", printInfo=True):
        """
        Print info about LDOs
        """
        if ldoList=="ALL":
            ldos = self.LDOlist
        else:
            ldos = ldoList
        res = "-"*47+"\n"
        res += "| "+self.fixLen("LDO Name", 10, center=False) +"|"
        res += self.fixLen("EN", 8)+"|"
        res += self.fixLen("VOUT", 6)+"|"
        res += self.fixLen("SPDUP", 7)+"|"
        res += self.fixLen("LOADIMP", 9)+"|"
        res += "\n"
        res += "-"*47+"\n"
        for ldo in ldos:
            enLoadImp, spDup, enabled, vout = self.getLDOconfig(ldo)
            res += "| "+self.fixLen(ldo, 10, center=False)+"|"
            if enabled==1:
                res += self.fixLen("ON", 8)+"|"
            else:
                res += self.fixLen("OFF", 8)+"|"
            res += self.fixLen(str(vout)[0:4], 6)+"|"
            if spDup==1:
                res += self.fixLen("ON", 7)+"|"
            else:
                res += self.fixLen("OFF", 7)+"|"
            if enLoadImp==1:
                res += self.fixLen("ON", 9)+"|"
            else:
                res += self.fixLen("OFF", 9)+"|"
            res += "\n"
        res += "-"*47
        if printInfo:
            self.log(res)
        else:
            return res

    #
    # MUXSEL
    #
    
    def evalMUXSELbit(self, mxName, bitNo, nBits=2):
        mxRegName = mxName+"_SEL"+str(bitNo)
        mxReg = self.getRegisterByName(mxRegName)
        internal = mxReg[ mxName+"_SEL"+str(bitNo)+"_INTERNAL" ]
        invert = mxReg[ mxName+"_SEL"+str(bitNo)+"_INVERT" ]
        mask = mxReg[ mxName+"_SEL"+str(bitNo)+"_MASK<8:0>" ]
        if internal==0:
            gpioInReg = self.getRegisterByName("GPIOInData")
            gpioInData = gpioInReg["GPIO_IN<8:0>"]
            if (gpioInData & mask) > 0:
                gpioVal = 1
            else:
                gpioVal = 0
            if invert==0:
                val = gpioVal
            else:
                val = 1-gpioVal
        else:
            intValReg = self.regDesc.getRegisterByBitField(mxName+"_INT_SEL<"+str(nBits-1)+":0>")
            intVal = intValReg[mxName+"_INT_SEL<"+str(nBits-1)+":0>"]
            if ((1<<bitNo) & intVal)>0:
                intBit = 1
            else:
                intBit = 0
            if invert==0:
                val = intBit
            else:
                val = 1-intBit
        return val
        
    def evalMUXSEL(self, mxName, nBits=2):
        val = 0
        mult = 1
        for i in range(0, nBits):
            bit = self.evalMUXSELbit(mxName, i, nBits)
            val += bit*mult
            mult *= 2
        return val


    #
    # CHx
    #

    def getChannelPowerConfig(self, channel, config=None):
        """
        getChannelPowerConfig(channel, config=None)
        Get the channel power configuration if config is specified, otherwise return active configuration.
        Returns: (lnaPd, mixaPd, mixbPd, paPd, paByp, r50En)
        """
        if config==None:
            nConfig = self.evalMUXSEL("CH"+channel+"_PD")   # Active configuration
        else:
            nConfig=config
        reg = self.getRegisterByName("CH"+channel+"_PD"+str(nConfig))
        lnaPd = reg["CH"+channel+"_LNA_PD"+str(nConfig)]
        mixaPd = reg["CH"+channel+"_MIXA_LOBUFF_PD"+str(nConfig)]
        mixbPd = reg["CH"+channel+"_MIXB_LOBUFF_PD"+str(nConfig)]
        paPd = reg["CH"+channel+"_PA_PD"+str(nConfig)]
        paByp = reg["CH"+channel+"_PA_BYPASS"+str(nConfig)]
        r50En = reg["CH"+channel+"_PA_R50_EN"+str(nConfig)]
        return (lnaPd, mixaPd, mixbPd, paPd, paByp, r50En)
    
    def infoChannelPowerConfig(self, channel, printInfo=True):
        """
        Get info about power configuration of channel.
        """
        res = "-"*40+"\n"
        res += "|"+self.fixLen("Channel "+channel+" PD configuration", 38)+"|\n"
        res += "-"*40+"\n"
        res += "| N |"
        res += self.fixLen("LNA", 5) + "|"
        res += self.fixLen("MIXA", 7)+"|"
        res += self.fixLen("MIXB", 7)+"|"
        res += self.fixLen("R50", 5)+"|"
        res += self.fixLen("PA", 6)+"|\n"
        res += "-"*40+"\n"
        warnings = []        
        muxselVal = self.evalMUXSEL("CH"+channel+"_PD")
        for i in range(0,4):
            lnaPd, mixaPd, mixbPd, paPd, paByp, r50En = self.getChannelPowerConfig(channel, i)

            if lnaPd==0:
                lnaState = "ON"
            else:
                lnaState = "OFF"
            if mixaPd==0:
                mixaState = "ON"
            else:
                mixaState = "OFF"
            if mixbPd==0:
                mixbState = "ON"
            else:
                mixbState = "OFF"
            if (paPd==0) and (paByp==0):
                paState = "ON"
            elif (paPd==1) and (paByp==0):
                paState = "OFF"
            elif (paPd==1) and (paByp==1):
                paState = "BYP"
            else:
                paState = "WRN"
            if r50En==0:
                r50State = "ON"
            else:
                r50State = "OFF"
            res += "| "+str(i)+" |"
            res += self.fixLen(lnaState, 5) + "|"
            res += self.fixLen(mixaState, 7)+"|"
            res += self.fixLen(mixbState, 7)+"|"
            res += self.fixLen(r50State, 5)+"|"
            res += self.fixLen(paState, 6)+"|"
            if i==muxselVal:
                res += " <- Active"
            res += "\n"
            if paState=="WRN":
                warnings.append("Configuration "+str(i)+" : PA is both bypassed and turned on.")
            if (mixaPd==0) and (mixbPd==0):
                warnings.append("Configuration "+str(i)+" : Both mixers are turned on.")
        res += "-"*40+"\n"
         
        for warn in warnings:
            res += "WARNING: "+warn+"\n"   

        if printInfo:
            self.log(res)
        else:
            return res

    def getPAict(self, channel):
        """
        Get the PA biasing current scaling.
        Returns (paMainIct, paLinIct)
        """
        reg = self.getRegisterByName("CH"+channel+"_HFPAD_ICT")
        paLin2x = 1.0+reg["CH"+channel+"_PA_ILIN2X"]*1.0
        paLinIct = paLin2x*reg["CH"+channel+"_PA_ICT_LIN<4:0>"]/16.0
        paMainIct = reg["CH"+channel+"_PA_ICT_LIN<4:0>"]*1.0/16.0
        return (paMainIct, paLinIct)

    def getPALoss(self, channel, config=None):
        """
        getPALoss(channel, config=None)
        Get the channel PA loss if config is specified, otherwise return active configuration.
        Returns: (mainLoss, linLoss)
        """
        if config==None:
            nConfig = self.evalMUXSEL("CH"+channel+"_PA")   # Active configuration
        else:
            nConfig=config
        reg = self.getRegisterByName("CH"+channel+"_PA_CTRL"+str(nConfig))
        linLoss = reg["CH"+channel+"_PA_LIN_LOSS"+str(nConfig)+"<3:0>"]
        mainLoss = reg["CH"+channel+"_PA_MAIN_LOSS"+str(nConfig)+"<3:0>"]
        return (mainLoss, linLoss)

    def getLNAConfig(self, channel, config=None):
        """
        getLNAConfig(channel, config=None)
        Get the channel LNA parameters if config is specified, otherwise return active configuration.
        Returns: (LNAictLin, LNAictMain, LNAcgsctrl, LNAgctrl)
        """
        if config==None:
            nConfig = self.evalMUXSEL("CH"+channel+"_LNA")   # Active configuration
        else:
            nConfig=config
        reg = self.getRegisterByName("CH"+channel+"_LNA_CTRL"+str(nConfig))
        lnagctrl = reg["CH"+channel+"_LNA_GCTRL"+str(nConfig)+"<3:0>"]
        lnacgsctrl = reg["CH"+channel+"_LNA_CGSCTRL"+str(nConfig)+"<1:0>"]
        lnaictmain = reg["CH"+channel+"_LNA_ICT_MAIN"+str(nConfig)+"<4:0>"]*1.0/16.0
        lnaictlin = reg["CH"+channel+"_LNA_ICT_LIN"+str(nConfig)+"<4:0>"]*1.0/16.0        
        return (lnaictlin, lnaictmain, lnacgsctrl, lnagctrl)
    
    def infoChannelLNAConfig(self, channel, printInfo=True):
        """
        Get info about channel configuration.
        """
        paMainIct, paLinIct = self.getPAict(channel)
        
        nChars = int(39)
        res = "-"*nChars+"\n"
        res += "|"+self.fixLen("Channel "+channel+" LNA configurations", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "| N |"
        res += self.fixLen(" GAIN ", 6) + "|" + self.fixLen(" CGS ", 5) +"|"+ self.fixLen(" ICT_MAIN ", 10) +"|"+ self.fixLen(" ICT_LIN ", 9) +"|\n"
        res += "-"*nChars+"\n"
        
        warnings = []        
        muxselVal = self.evalMUXSEL("CH"+channel+"_LNA")
        for i in range(0,4):
            reg = self.getRegisterByName("CH"+channel+"_LNA_CTRL"+str(i))
            lnagctrl = reg["CH"+channel+"_LNA_GCTRL"+str(i)+"<3:0>"]
            lnacgsctrl = reg["CH"+channel+"_LNA_CGSCTRL"+str(i)+"<1:0>"]
            lnaictmain = reg["CH"+channel+"_LNA_ICT_MAIN"+str(i)+"<4:0>"]
            lnaictlin = reg["CH"+channel+"_LNA_ICT_LIN"+str(i)+"<4:0>"]

            reg = self.getRegisterByName("CH"+channel+"_PA_CTRL"+str(i))
            paLinLoss = reg["CH"+channel+"_PA_LIN_LOSS"+str(i)+"<3:0>"]
            paMainLoss = reg["CH"+channel+"_PA_MAIN_LOSS"+str(i)+"<3:0>"]

            lnaGain = str(lnagctrl)
            lnaCgs = str(lnacgsctrl)
            lnaICTMain = str(lnaictmain)
            lnaICTLin = str(lnaictlin)

            res += "| "+str(i)+" |"
            res += self.fixLen(lnaGain, 6) + "|" + self.fixLen(lnaCgs, 5) + "|" + self.fixLen(lnaICTMain, 10) + "|" + self.fixLen(lnaICTLin, 9) + "|"
            if i==muxselVal:
                res += " <- Active"
            res += "\n"
        res += "-"*nChars+"\n"
         
        for warn in warnings:
            res += "WARNING: "+warn+"\n"   

        if printInfo:
            self.log(res)
        else:
            return res    

    def infoChannelPAConfig(self, channel, printInfo=True):
        """
        Get info about channel PA configuration.
        """
        nChars = int(39)
        res = "-"*nChars+"\n"
        res += "|"+self.fixLen("Channel "+channel+" PA configurations", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "| N |"
        res += self.fixLen(" MAIN ", 6) + "|" + self.fixLen(" LIN ", 5) +"|"+ self.fixLen(" ICT_MAIN ", 10) +"|"+ self.fixLen(" ICT_LIN ", 9) +"|\n"
        res += "-"*nChars+"\n"
        
        warnings = []        
        muxselVal = self.evalMUXSEL("CH"+channel+"_PA")
        for i in range(0,4):
            reg = self.getRegisterByName("CH"+channel+"_PA_CTRL"+str(i))
            paLinLoss = reg["CH"+channel+"_PA_LIN_LOSS"+str(i)+"<3:0>"]
            paMainLoss = reg["CH"+channel+"_PA_MAIN_LOSS"+str(i)+"<3:0>"]

            reg = self.getRegisterByName("CH"+channel+"_HFPAD_ICT")
            paLin2x = 1+reg["CH"+channel+"_PA_ILIN2X"]
            paLinIct = paLin2x*reg["CH"+channel+"_PA_ICT_LIN<4:0>"]
            paMainIct = reg["CH"+channel+"_PA_ICT_LIN<4:0>"]

            paMain = str(paMainLoss)
            paLin = str(paLinLoss)
            paICTMain = str(paMainIct)
            if paLin2x>1:
                paICTLin = "2*"+str(paLinIct)
            else:
                paICTLin = str(paLinIct)            
            res += "| "+str(i)+" |"
            res += self.fixLen(paMain, 6)+"|"+self.fixLen(paLin, 5)+"|"+self.fixLen(paICTMain, 10)+"|"+self.fixLen(paICTLin, 9)+"|"
            if i==muxselVal:
                res += " <- Active"
            res += "\n"
        res += "-"*nChars+"\n"
         
        for warn in warnings:
            res += "WARNING: "+warn+"\n"   

        if printInfo:
            self.log(res)
        else:
            return res    
    
    def getPAICC(self, channel):
        config = self.evalMUXSEL("CH"+channel+"_PD")   # Active configuration
        lnaPd, mixaPd, mixbPd, paPd, paByp, r50En = self.getChannelPowerConfig(channel, config)
        config = self.evalMUXSEL("CH"+channel+"_PA")   # Active configuration
        mainLoss, linLoss = self.getPALoss(channel, config)
        mainICT, linICT = self.getPAict(channel)
        mainICC = mainICT * self.PAMainICC[mainLoss]
        linICC = linICT * self.PALinICC[linLoss]
        icc = (1.0-paPd)*(mainICC+linICC)
        return icc 

    def getLNAICC(self, channel):
        config = self.evalMUXSEL("CH"+channel+"_PD")   # Active configuration
        lnaPd, mixaPd, mixbPd, paPd, paByp, r50En = self.getChannelPowerConfig(channel, config)
        config = self.evalMUXSEL("CH"+channel+"_LNA")   # Active configuration
        lnaictlin, lnaictmain, lnacgsctrl, lnagctrl = self.getLNAConfig(channel, config)
        mainICC = lnaictmain * self.LNAMainICC[lnagctrl]
        linICC = lnaictlin * self.LNALinICC[lnagctrl]
        icc = (1.0-lnaPd)*(mainICC+linICC)
        return icc

    def getMIXAICC(self, channel):
        config = self.evalMUXSEL("CH"+channel+"_PD")   # Active configuration
        lnaPd, mixaPd, mixbPd, paPd, paByp, r50En = self.getChannelPowerConfig(channel, config)        
        icc = (1.0-mixaPd)*(self.MIXAICC[0])
        return icc
    
    def getMIXBICC(self, channel):
        config = self.evalMUXSEL("CH"+channel+"_PD")   # Active configuration
        lnaPd, mixaPd, mixbPd, paPd, paByp, r50En = self.getChannelPowerConfig(channel, config)        
        icc = (1.0-mixbPd)*(self.MIXBICC[0])
        return icc

    def getChannelPower(self, channel):
        paICC = self.getPAICC(channel)
        lnaICC = self.getLNAICC(channel)
        mixaICC = self.getMIXAICC(channel)
        mixbICC = self.getMIXAICC(channel)
        power = paICC * self.PAVDD + lnaICC * self.LNAVDD + self.MIXAVDD*mixaICC+ self.MIXBVDD*mixbICC
        return power

    def infoChannel(self, channel, printInfo=True):
        # Read all registers to get chip state which could have been changed by GPIO
        self.readRegisters()    
        interactive = self.isInteractive()
        self.disableInteractiveMode()
        res = self.infoChannelPowerConfig(channel, printInfo=False) + "\n"
        res += self.infoChannelLNAConfig(channel, printInfo=False) + "\n"
        res += self.infoChannelPAConfig(channel, printInfo=False) + "\n"
        res += "ICC(LNA)  = " + self.fixLen(str(self.getLNAICC(channel)/1e-3),4,center=False)[0:4] + " mA\n"
        res += "ICC(MIXA) = " + self.fixLen(str(self.getMIXAICC(channel)/1e-3),4,center=False)[0:4] + " mA\n"
        res += "ICC(MIXB) = " + self.fixLen(str(self.getMIXBICC(channel)/1e-3),4,center=False)[0:4] + " mA\n"
        res += "ICC(PA)   = " + self.fixLen(str(self.getPAICC(channel)/1e-3),4,center=False)[0:4] + " mA\n"        
        res += "Channel "+channel+" power "+str(self.getChannelPower(channel)/1e-3) + " mW"
        if interactive:
            self.enableInteractiveMode()
        if printInfo:
            self.log(res)
        else:
            return res

    #
    # HLMIX
    #
    
    def getHLMIXConfig(self, channel, config=None):
        if config==None:
            nConfig = self.evalMUXSEL("HLMIX"+channel+"_CONF")   # Active configuration
        else:
            nConfig=config        
        reg = self.getRegisterByName("HLMIX"+channel+"_CONFIG"+str(nConfig))
        VGCAS = reg["HLMIX"+channel+"_VGCAS"+str(nConfig)+"<6:0>"]
        ICT = reg["HLMIX"+channel+"_ICT_BIAS"+str(nConfig)+"<4:0>"]
        biasPD = reg["HLMIX"+channel+"_BIAS_PD"+str(nConfig)]
        lobufPD = reg["HLMIX"+channel+"_LOBUF_PD"+str(nConfig)]
        
        if ( (VGCAS//(1<<4))==0 ):
            rb = 20e3
        elif ( (VGCAS//(1<<4))<2 ):
            rb = 15e3
        else:
            rb = 10e3
        
        ib = (VGCAS & 31)*1.0/16.0 * self.HLMIXIbNom
        
        vgcas = self.HLMIXVDD - rb * ib
        ict = ICT*1.0/16.0
        return (vgcas, ict, biasPD, lobufPD)

    def getHLMIXLoss(self, channel, config=None):
        if config==None:
            nConfig = self.evalMUXSEL("HLMIX"+channel+"_LOSS")   # Active configuration
        else:
            nConfig=config        
        reg = self.getRegisterByName("HLMIX"+channel+"_LOSS"+str(nConfig))
        loss = reg["HLMIX"+channel+"_MIXLOSS"+str(nConfig)+"<3:0>"]
        return loss

    def getHLMIXICC(self, channel):
        biasicc = self.HLMIXBIASICC[0]
        loicc = self.HLMIXLOICC[0]
        vgcas, ict, biasPD, lobufPD = self.getHLMIXConfig(channel)
        icc = biasicc*(1-biasPD)+loicc*(1-lobufPD)
        return icc        

    def getHLMIXPower(self, channel):
        icc = self.getHLMIXICC(channel)
        vdd = self.HLMIXVDD
        return icc*vdd

    def infoHLMIXConfig(self, channel, printInfo=True):
        """
        Get info about HLMIX configuration.
        """
        nChar = 38
        res = "-"*nChar+"\n"
        res += "|"+self.fixLen("HLMIX "+channel+" configuration", nChar-2)+"|\n"
        res += "-"*nChar+"\n"
        res += "| N |"
        res += self.fixLen("VGCAS", 7) + "|"
        res += self.fixLen("BIAS ICT", 9)+"|"
        res += self.fixLen("BIAS", 6)+"|"
        res += self.fixLen("LOBUF", 7)+"|\n"

        res += "-"*nChar+"\n"
        warnings = []        
        muxselVal = self.evalMUXSEL("HLMIX"+channel+"_CONF")
        for i in range(0,4):
            vgcas, ict, biasPd, lobufPd = self.getHLMIXConfig(channel, i)

            vgcasStr = str(vgcas)[0:4]
            ictStr = str(int(ict*16))

            if biasPd==0:
                biasState = "ON"
            else:
                biasState = "OFF"
            if lobufPd==0:
                lobufState = "ON"
            else:
                lobufState = "OFF"


            res += "| "+str(i)+" |"
            res += self.fixLen(vgcasStr, 7) + "|"
            res += self.fixLen(ictStr, 9)+"|"
            res += self.fixLen(biasState, 6)+"|"
            res += self.fixLen(lobufState, 7)+"|"
            if i==muxselVal:
                res += " <- Active"
            res += "\n"
        res += "-"*nChar+"\n"
         
        for warn in warnings:
            res += "WARNING: "+warn+"\n"   

        if printInfo:
            self.log(res)
        else:
            return res

    def infoHLMIXLoss(self, channel, printInfo=True):
        """
        Get info about HLMIX loss.
        """
        nChar = 12
        res = "-"*nChar+"\n"
        res += "|"+self.fixLen("HLMIX "+channel, nChar-2)+"|\n"
        res += "-"*nChar+"\n"
        res += "| N |"
        res += self.fixLen("LOSS", 6) + "|\n"

        res += "-"*nChar+"\n"
        warnings = []        
        muxselVal = self.evalMUXSEL("HLMIX"+channel+"_LOSS")
        for i in range(0,4):
            loss = self.getHLMIXLoss(channel, i)

            res += "| "+str(i)+" |"
            res += self.fixLen(str(loss), 6) + "|"
            if i==muxselVal:
                res += " <- Active"
            res += "\n"
        res += "-"*nChar+"\n"
         
        for warn in warnings:
            res += "WARNING: "+warn+"\n"   

        if printInfo:
            self.log(res)
        else:
            return res

    def infoHLMIX(self, channel, printInfo=True):
        # Read all registers to get chip state which could have been changed by GPIO
        self.readRegisters()    
        interactive = self.isInteractive()
        self.disableInteractiveMode()
        res = self.infoHLMIXConfig(channel, printInfo=False) + "\n"
        res += self.infoHLMIXLoss(channel, printInfo=False) + "\n"
        res += "ICC(HLMIX)  = " + self.fixLen(str(self.getHLMIXICC(channel)/1e-3),4,center=False)[0:4] + " mA\n"
        res += "HLMIX "+channel+" power "+str(self.getHLMIXPower(channel)/1e-3) + " mW"
        if interactive:
            self.enableInteractiveMode()
        if printInfo:
            self.log(res)
        else:
            return res        

        
            
    
    
