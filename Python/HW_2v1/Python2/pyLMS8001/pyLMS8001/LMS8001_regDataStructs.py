import math
from copy import copy

regDataStructsVer = "1.6"

class RegBank(object):
    def __init__(self, name, specifier):
        self.name = name
        self.specifier = specifier
        self.registers = []
        
        # Find don't care positions
        pos = 0
        while (specifier[len(specifier)-(pos+1)]) == "X":
            pos = pos+1
        
        if pos==0:
            if "X" not in specifier:
                raise ValueError("Bank specifier "+specifier+" is a fixed address!")
            else:
                raise ValueError("Bank specifier can only have X for lowest bits. Specifier "+specifier+" violates this constraint.")
        
        if "X" in specifier[0:-pos]:
            raise ValueError("Bank specifier can only have X for lowest bits. Specifier "+specifier+" violates this constraint.")
        
        strLow = specifier[0:-pos] + "0"*int(pos)
        if "0x" in specifier:
            # Hexadecimal notation
            strHigh = specifier[0:-pos] + "F"*int(pos)
            self.addrL = int(strLow, 16)
            self.addrH = int(strHigh, 16)
        elif "0b" in specifier:
            # Binary notation
            strHigh = specifier[0:-pos] + "1"*int(pos)
            self.addrL = int(strLow, 2)
            self.addrH = int(strHigh, 2)
        else:
            raise ValueError("Invalid bank specifier : "+specifier)

    def __repr__(self):
        retVal = "REGBANK "+self.getName()+" "+self.getSpecifier()+"\n"
        return retVal

    def __str__(self):
        retVal="Register bank : " + self.name + " " + self.specifier + " ("+hex(self.getAddrH())+","+hex(self.getAddrL())+")\n"
        regs = ""
        for reg in self.registers:
            if regs != "":
                regs = regs + ", " + reg.name
            else:
                regs = reg.name
        retVal=retVal+"Registers=["+regs+"]"
        return retVal

    def getName(self):
        return self.name

    def getSpecifier(self):
        return self.specifier
    
    def getAddrL(self):
        # Returns the lowest address in bank
        return self.addrL

    def getAddrH(self):
        # Returns the highest address in bank
        return self.addrH

    def isInBank(self, addr):
        # Check if address is in this bank range
        if (addr >= self.addrL) and (addr <= self.addrH):
            return True
        return False

    def addRegister(self, register):
        # Check if register is in register bank address range
        if not self.isInBank(register.addr):
            raise ValueError("Register with address "+hex(register.addr)+" cannot be added to bank "+self.name+" ("+hex(self.getAddrH())+","+hex(self.getAddrL())+")")

        # Check if register collides with existing one
        for reg in self.registers:
            if reg.addr == register.addr:
                raise ValueError("Register "+reg.name+" is assigned to the address taken by "+register.name)
        self.registers.append(register)

    def getRegister(self, regName):
        # Get register by name
        for reg in self.registers:
            if (regName == reg.name):
                return reg
        raise ValueError("Register "+regName+" does not exist in bank "+self.name)

    def hasRegister(self, regName):
        # Check if register exists in a register bank
        for reg in self.registers:
            if (regName == reg.name):
                return True
        return False

    def getRegs(self):
        # Get all registers in a bank
        return self.registers

    def getSpecNBits(self):
        addrH = self.getAddrH()
        addrL = self.getAddrL()
        regAddrSpace = addrH-addrL+1 # Size of register address space in register bank
        nBitsRegAddrSpace = int(math.log(regAddrSpace)/math.log(2))
        return int(15-nBitsRegAddrSpace)

    def getSpecBits(self):
        nBits = self.getSpecNBits()
        bits = bin(self.getAddrL()) # bits contain 0b prefix
        bits = bits[2:] # get rid of 0b
        # Make sure that bits has 15 digits
        while len(bits)<15:
            bits = "0"+bits
        return bits[0:nBits]
        

class Register(object):
    @staticmethod
    def intToHex(val, upperCase=True):
        hexVal = hex(val)[2:]
        while len(hexVal)<4:
            hexVal = "0"+hexVal
        if upperCase:
            hexVal = hexVal.upper()
        hexVal = "0x"+hexVal
        return hexVal

    # Instance methods
    def __init__(self, regName, regAddr, chip=None):
        if " " in regName:
            raise ValueError("Invalid register name: "+regName+" (name contains space)")
        self.regAddr = regAddr
        self.name = regName
        if "0x" in regAddr:
            addr = int(regAddr,16)
        elif "0b" in regAddr:
            addr = int(regAddr, 2)
        else:
            raise ValueError("Invalid register address "+str(regAddr))
        
        self.addr = addr
        self.comment = []
        self.bitFields = []
        self.shadowReg = None   # Register which shadows the current register
        self.shadowedRegs = []  # Registers which are shadowed by current register
        self._chip = chip

    @property
    def chip(self):
        return self._chip

    @chip.setter
    def chip(self, val):
        self._chip = val

    @property
    def SPIwriteFn(self):
        return self.chip.SPIwriteFn

    @property
    def SPIreadFn(self):
        return self.chip.SPIreadFn

    @property
    def SPIImmediate(self):
        return self.getImmediateMode()
    
    def getImmediateMode(self):
        return self.chip.SPIImmediate


    def __repr__(self):
        return self.__str__()

    def __REPR__(self):
        register = self
        regName = self.name
        regAddr = self.regAddr
        hexAddr = self.intToHex(self.addr)
        # Print register
        retVal  = "REGISTER    "+regName+"    "+hexAddr+"\n"
        if register.isShadowed():
            retVal += "    SHADOW=" + self.getShadowReg() + "\n"
        for bitField in register.getBitFields():
            retVal += bitField.__repr__()
        retVal += "ENDREGISTER\n"
        return retVal

    def help(self):
        print self.__REPR__()

    def __str__(self,maxFieldNameWidth=20):
        self.refresh()
        hexAddr = self.intToHex(self.addr)
        retVal = "Register : " + self.name + " "+hexAddr+"\n"
        if self.isShadowed():
            retVal = retVal + "Shadowed by : " + self.getShadowReg() + "\n"
        if self.isShadowing():
            retVal = retVal + "Shadows registers : "
            for sreg in self.getShadowedRegs():
                retVal = retVal+sreg+" "
            retVal = retVal+"\n"
        flds = ""
        bitRepr = ""
        bitReprAll = ["0"]*16
        
        # Determine max bitfield width
        for field in self.bitFields:
            if maxFieldNameWidth<len(field.name):
                maxFieldNameWidth = len(field.name)+1
        
        for field in self.bitFields:
            bRep = field.evaluateBinRepr()
            bitRepr = bitRepr + field.name + " "*int(maxFieldNameWidth-len(field.name)) + bRep + "\t(" + self.intToHex(int("0b"+bRep.strip(),2)) + " << "+str(field.getPosL())+")\t("+str(int("0b"+bRep.strip(),2)) + " << "+str(field.getPosL())+")\n"
            for i in range(0,16):
                if bRep[i]!=" ":
                    bitReprAll[i] = bRep[i]
            if flds!="":
                flds = flds+", "+field.name
            else:
                flds = field.name
        #retVal = retVal+"Fields=["+flds+"]\n"
        retVal = retVal + bitRepr
        bRep = ""
        for i in range(0,16):
            if bitReprAll[i]=="0":
                bRep = bRep + "0"
            else:
                bRep = bRep + "1"
        retVal = retVal +  "Register value " + " "*int(maxFieldNameWidth-len("Register value "))+ bRep + "\t("+self.intToHex(int("0b"+bRep,2))+")\n"
        for comment in self.getComments():
            retVal=retVal+"#! " + comment.rstrip()+"\n"
        return retVal

    def getScriptRepr(self):
        self.refresh()
        retVal = self.name + " "
        for field in self.bitFields:
            retVal += field.getName() + "=0b"+field.evaluateBinRepr().strip() + " "
        retVal.strip()
        return retVal            

    def addBitField(self, bitField):
        # Check if bitfield collides with existing ones
        for field in self.bitFields:
            if field.isInField(bitField.getPosH()) or field.isInField(bitField.getPosL()):
                raise ValueError("Bit field "+bitField.name+" position "+bitField.position+" collides with "+field.name+" position "+field.position)

        # All OK, add bitfield to register            
        self.bitFields.append(bitField)
        
    def getBitFieldByName(self, bitFieldName):
        for field in self.bitFields:
            if (bitFieldName == field.name):
                return field
        raise ValueError("Bit field "+bitFieldName+" does not exist in register "+self.name)
    
    def getBitFields(self):
        return self.bitFields
  
    def getName(self):
        return self.name
    
    def addComment(self, commentLine):
        self.comment.append(commentLine)
    
    def getComments(self):
        return self.comment

    def getAddrBits(self):
        bits = bin(self.addr)
        bits = bits[2:] # get rid of 0b
        # Make sure that bits has 15 digits
        while len(bits)<15:
            bits = "0"+bits
        return bits
    
    def getAddress(self):
        return self.addr

    def getValue(self, noUpdate=False):
        # Evaluate bitfields
        if not noUpdate:
            self.refresh()
        val = 0
        for field in self.getBitFields():
            val = val | field.evaluate()
        return val

    def setValue(self, val, noUpdate=False):
        # Write value to bitfields
        for field in self.getBitFields():
            field.setValueFromReg(val)
        if not noUpdate:
            self.immediateWrite()
            
    def refresh(self):
        # Read the value from chip if immediate mode is enabled
        if self.getImmediateMode():
            if self.SPIreadFn==None:
                raise AttributeError("SPIreadFn must be set to use immediate mode")
            else:
                addr = self.getAddress()
                val = self.SPIreadFn([addr])[0]
                self.setValue(val, noUpdate=True)

    def immediateWrite(self):
        # Check if immediate mode is enabled
        if self.getImmediateMode():
            # Immediate mode is enabled, write the new value
            if self.SPIwriteFn==None:
                raise AttributeError("SPIwriteFn must be set to use immediate mode")
            else:
                addr = self.getAddress()
                val = self.getValue(noUpdate=True)
                self.SPIwriteFn([(addr, val)])
    
    
    def getValueBin(self):
        val = self.getValue()
        valB = bin(val)
        valB = valB[2:]
        while len(valB) < 16:
            valB = "0"+valB
        return valB

    def getReadValue(self):
        # Ignore write-only fields
        val = 0
        for field in self.getBitFields():
            if (field.mode == "R") or (field.mode == "RI") or (field.mode == "RW") or (field.mode == "RWI"):
                val = val | field.evaluate()
        return val

    def getReadValueBin(self):
        val = self.getReadValue()
        valB = bin(val)
        valB = valB[2:]
        while len(valB) < 16:
            valB = "0"+valB
        return valB

    def getShadowReg(self):
        # Return the shadow register
        return self.shadowReg
    
    def getShadowedRegs(self):
        # Return the list of shadowed registers
        return self.shadowedRegs
        
    def addShadowedReg(self, regName):
        self.shadowedRegs.append(regName)

    def clearShadowedRegs(self):
        self.shadowedRegs = []

    def isShadowed(self):
        # Determine if this register is shadowed by other register
        if self.shadowReg == None:
            return False
        return True

    def isShadowing(self):
        # Determine if this register shadows other registers
        if len(self.shadowedRegs) == 0:
            return False
        return True

    def __len__(self):
        # Return the number of bitfields
        return len(self.bitFields)

    def __getitem__(self, key):
        self.refresh()
        # Get the bitfield value
        bitField = self.getBitFieldByName(key)
        return bitField.getValue()
        
    def __setitem__(self, key, value):
        # Set the bitfield value
        if key=="":
            self.setValue(value)
        else:
            bitField = self.getBitFieldByName(key)
            if isinstance(value, int):
                val = value
            elif "0b" in value:
                val = int(value,2)
            elif "0x" in value:
                val = int(value,16)
            else:
                raise ValueError("Unknown radix in value "+str(value))
            bitField.setValue(val)
            self.immediateWrite()
    
class BitField(object):
    def __init__(self, name, position, defValue, mode):
        self.name = name
        self.position = position
        self.defValue = defValue
        self.mode = mode.upper()
        self.comment = []
        self.stickyBit = False
        self.readBack = ""
        
        if mode=="RB":
            self.readBack = defValue
            self.defValue = "0"*int(self.getLenFromName())
        
        if mode=="STICKYBIT":
            if self.defValue != '0':
                raise ValueError("Bitfield "+name+" declared as sticky bit, but default value is not '0'")
            if self.getLenFromName() > 1:
                raise ValueError("Bitfield "+name+" declared as sticky bit, but bitfield length > 1")
            self.stickyBit = True
            self.mode = "RW"
        
        # Do some checks
        self.checkPosition()
        if self.getLen() != self.getLenFromName():
            raise ValueError("Bitfield "+self.name+" length is "+str(self.getLenFromName())+" bits, while position "+self.position+" specifies a length of "+str(self.getLen())+" bits" )
        if self.getLen() != len(self.defValue):
            raise ValueError("Invalid default value. Expected "+str(self.getLen())+" bits, got "+str(len(self.defValue))+" ("+self.defValue+")")

        if self.mode not in ["R", "RI", "RB", "W", "WI", "RW", "RWI", "RWE"]:
            raise ValueError("Invalid mode "+mode+" specified for bitfield "+self.name)

    def __repr__(self):
        bitField = self
        # Print bitField definition
        retVal  = "    BITFIELD   "+bitField.getName()+"\n"
        retVal += "        POSITION="+bitField.getPosition()+"\n"
        if self.mode=="RB":
            retVal += "        DEFAULT="+bitField.getReadBackValue()+"\n"        
        else:
            retVal += "        DEFAULT="+bitField.getDefaultValue()+"\n"
        if not self.isSticky():
            retVal += "        MODE="+bitField.getMode()+"\n"
        else:
            retVal += "        MODE=STICKYBIT\n"
        comments = bitField.getComments()
        for comment in comments:
            retVal += "        #! "+comment+"\n"
        retVal += "    ENDBITFIELD\n"
        return retVal    

    def __str__(self):
        if not self.isSticky():
            retVal="Bitfield : " + self.name + " POSITION="+ self.position + " DEFAULT="+self.defValue+" MODE="+self.mode+"\n"
        else:
            retVal="Bitfield : " + self.name + " POSITION="+ self.position + " DEFAULT="+self.defValue+" MODE=STICKYBIT\n"
        bitRepr = self.getBitRepr()
        retVal = retVal + "Bitfield position : " + bitRepr + "\n"
        for comment in self.getComments():
            retVal=retVal+"#! "+comment.rstrip()+"\n"
        return retVal

    def getReadBackValue(self):
        return self.readBack

    def isSticky(self):
        return self.stickyBit
        
    def getBitRepr(self):
        return ("-"*int(15-self.getPosH())) + ("#"*int(self.getPosH()-self.getPosL()+1)) + ("-"*int(self.getPosL()))

    def getName(self):
        return self.name

    def getOnlyName(self):
        if "<" in self.name:
            # Vector
            return (self.name.split("<"))[0]
        else:
            return self.name

    def getPosition(self):
        return self.position
        
    def getDefaultValue(self):
        return self.defValue
        
    def getMode(self):
        return self.mode
        
    def getComments(self):
        return self.comment                   
        
    def checkPosition(self):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            if low<0:
                raise ValueError("Invalid bit field position " + self.position)
            if high>15:
                raise ValueError("Invalid bit field position " + self.position)
        else:
            # Single bit
            pos = int(self.position)
            if pos<0:
                raise ValueError("Invalid bit field position " + self.position)
            if pos>15:
                raise ValueError("Invalid bit field position " + self.position)
        return True

    def getPosH(self):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return high
        else:
            # Single bit
            pos = int(self.position)
            return pos

    def getPosHFromName(self):
        if "<" in self.name:
            # Vector
            if ">" not in self.name:
                raise ValueError("Invalid bit field position " + self.name)
            tmp = self.name.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return high
        else:
            # Single bit
            pos = -1
            return pos

    def getPosL(self):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return low
        else:
            # Single bit
            pos = int(self.position)
            return pos

    def getPosLFromName(self):
        if "<" in self.name:
            # Vector
            if ">" not in self.name:
                raise ValueError("Invalid bit field position " + self.name)
            tmp = self.name.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return low
        else:
            # Single bit
            pos = -1
            return pos

    def getLen(self):
        # Returns the length of bitfield
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return high-low+1
        else:
            # Single bit
            return 1

    def getLenFromName(self):
        # Returns the length of bitfield from name
        if "<" in self.name:
            # Vector
            if ">" not in self.name:
                raise ValueError("Invalid bit field name " + self.name)
            tmp = self.name.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return high-low+1
        else:
            # Single bit
            return 1
       
    def isInField(self, bitPos):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            if (bitPos >= low) and (bitPos <= high):
                return True
            else:
                return False
        else:
            # Single bit
            pos = int(self.position)
            if bitPos == pos:
                return True
            else:
                return False

    def setValue(self, valueInt):
        binValue = bin(valueInt)[2:]
        while len(binValue)<self.getLen():
            binValue = "0"+binValue
        self.defValue = binValue

    def setValueBin(self, valueBin):
        if len(valueBin) != self.getLen():
            raise ValueError("Wrong number of bits given. Bitfield width is "+str(self.getLen())+", while "+len(val)+" bits given.")
        self.defValue = valueBin

    def setValueFromReg(self, regValue):
        # Set bitfield value from register value
        val = regValue >> self.getPosL()
        mask = int("0b" + "1"*self.getLen(), 2)
        val = val & mask
        self.setValue(val)

    def getValueBin(self):
        # Return binary representation of bitfield
        return self.getDefalutValue()

    def getValue(self):
        # Return integer value of bitfield
        return int("0b"+self.getDefaultValue(),2)


    def evaluate(self, bitFieldVal=None):
        # Evaluate bitfield value. Shift to correct position.
        if bitFieldVal==None:
            val = self.defValue
        else:
    	    val = bitFieldVal
        if len(val) != self.getLen():
            raise ValueError("Wrong number of bits given. Bitfield width is "+str(self.getLen())+", while "+len(val)+" bits given.")
        valInt = int("0b"+val, 2)
        valInt = int( valInt * (2**self.getPosL()) )
        return valInt

    def evaluateBin(self, bitFieldVal=None):
        if bitFieldVal==None:
            val = self.defValue
        valInt = self.evaluate(val)
        valB = bin(valInt)
        valB = valB[2:] # get rid of 0b
        while len(valB)<16:
            valB = "0"+valB
        return valB

    def evaluateBinRepr(self):
        binVal = self.evaluateBin()
        retVal = (" "*int(15-self.getPosH())) + (binVal[16-(self.getPosH()+1):16-self.getPosL()]) + (" "*int(self.getPosL()))
        return retVal      

    def addComment(self, commentLine):
        self.comment.append(commentLine)
           
    def getComments(self):
        return self.comment

class Macro(object):
    def __init__(self, name, templateName):
        self.name = name
        self.templateName = templateName
        self.parameters = {}    # Dictionary of template parameters
        self.comment = []

    def __repr__(self):
        macro = self
        macroName = self.name
        macroTemplate = self.templateName
        # Print macro
        retVal  = "MACRO    "+macroName+"    "+macroTemplate+"\n"
        for comment in macro.getComments():
            retVal += "\t#! "+comment+"\n"
        for parameter in macro.getParameters():
            retVal += "\t"+parameter+"="+macro.getParameterValue(parameter)+"\n"
        retVal += "ENDMACRO\n"
        return retVal

    def __str__(self):
        return self.__repr__()    

    def getName(self):
        return self.name
        
    def getTemplateName(self):
        return self.templateName
        
    def addParameter(self, paramName, paramValue):
        if self.parameters.has_key(paramName):
            raise ValueError("Attempt to overwrite parameter "+paramName)
        self.parameters.update( {paramName:paramValue} )
        
    def getParameters(self):
        # Returns a list of all parameter names
        return self.parameters.keys()
        
    def getParameterValue(self, paramName):
        if not self.parameters.has_key(paramName):
            raise ValueError("Parameter "+paramName+" does not exist in macro "+self.name+" (template "+self.templateName+")")
        return self.parameters[paramName]

    def addComment(self, commentLine):
        self.comment.append(commentLine)
           
    def getComments(self):
        return self.comment    

class regDescParser(object):
    def __init__(self, regDefList, chip=None):
        """
        Read register definitions from a given file        
        """
       
        # Init locals
        self.regBanks = []   # Register banks specified in description
        self.registers = []  # registers
        self.voltages = []   # voltages
        self.currents = []   # currents
        self.vectors = []    # vectors
        self.sigClass = []   # signal classes
        self.comments = []   # comments
        self.macros = []     # macros
        self.inputPorts = []    # Defined input ports
        self.outputPorts = []    # Defined output ports
        self.internalRegs = []   # Internal regs
        self.internalWires = []  # Internal wires
        
        self.regDefList = regDefList
        self.nLine = 0
        self.chip = chip
        
        # Read and parse the input file
        line = " "
        getLine = self.getLine
        try:
            while self.nLine<len(regDefList):
                line = getLine()
                if line == "":
                    continue
                
                line = line.strip()
                line = (line.split("##")[0]).rstrip()  # Throw away comments
                
                if line == "":
                    line = " "
                    continue
                keyword = line.split()[0]    
                if "#!" in keyword:
                    # Documentation comment
                    comment = line.split("#!")[1]
                    self.comments.append(comment)
                    continue
                if "REGISTER" in keyword:
                    # Register definition. Bitfields are parsed within register parser
                    reg = self.parseRegister(line)
                    reg.chip = self.chip
                    self.registers.append(reg)
                    continue
                if "REGBANK" in keyword:
                    # Register bank definition
                    bank = self.parseRegBank(line)
                    self.regBanks.append(bank)
                    continue
                if "SIGNALCLASS" in keyword:
                    # Not implemented
                    continue
                if "VECTOR" in keyword:
                    # Not implemented
                    continue
                if "VOLTAGE" in keyword:
                    # Not implemented
                    continue
                if "CURRENT" in keyword:
                    # Not implemented
                    continue
                if "MACRO" in keyword:
                    macro = self.parseMacro(line)
                    self.macros.append(macro)
                    continue
                if "INPUT_PORT" in keyword:
                    port = line.split()[1]
                    port.strip()
                    self.inputPorts.append(port)
                    continue
                if "OUTPUT_PORT" in keyword:
                    port = line.split()[1]
                    port.strip()
                    self.outputPorts.append(port)
                    continue
                if "INTERNAL_REG" in keyword:
                    sigName = line.split()[1]
                    sigName.strip()
                    self.internalRegs.append(sigName)
                    continue
                if "INTERNAL_WIRE" in keyword:
                    sigName = line.split()[1]
                    sigName.strip()
                    self.internalWires.append(sigName)
                    continue
                # If we get here, we have encountered an unknown construct.
                # Signal error and exit
                raise ValueError( "Unknown construct : " + line  )
                return
        except Exception,error:
            retVal="("+str(self.nLine) + ") ERROR: "+str(error)
            raise ValueError(retVal)

        # Put registers to banks
        for reg in self.registers:
            regAssigned = False
            for bank in self.regBanks:
                if bank.isInBank(reg.addr):
                    bank.addRegister(reg)
                    regAssigned = True
                    break
            if not regAssigned:
                retVal = "ERROR : Register " + reg.name + " does not belong to any register bank"
                raise ValueError(retVal)

        RegisterDefinition.performChecks(self.regBanks)
        return
                   
    def getLine(self):
        line = self.regDefList[self.nLine]
        self.nLine = self.nLine + 1   # Keep track of lines
        return line

    def parseRegBank(self, firstLine):
        # Register bank parsing
        args = firstLine.split()
        # We expect that first argument is REGBANK
        if args[0].strip() != "REGBANK":
            raise ValueError("Missing REGBANK keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing register bank name")
        specifier = args[2].strip()
        return RegBank(name, specifier)

    def parseMacro(self, firstLine):
        # Macro parsing
        args = firstLine.split()
        # We expect that first argument is MACRO
        if args[0].strip() != "MACRO":
            raise ValueError("Missing MACRO keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing macro instance name")
        templateName = args[2].strip()
        if len(templateName) == 0:
            raise ValueError("Missing macro template name")
        
        macro = Macro(name, templateName)
        
        line = " "
        endMacro = False
        while line:
            line = self.getLine()
            if line == "":
                continue
            line = line.strip()
            line = (line.split("##")[0]).strip()  # Throw away comments
            if line == "":
                line = " "
                continue            
            keyword = (line.split()[0]).strip()
            if "#!" in keyword:
                # Documentation comment
                comment = line.split("#!")[1]
                macro.addComment(comment)
                line = line.split("#!")[0]
                line = line.strip()
                if line == "":
                    continue
            if "ENDMACRO" in keyword:
                # Finished parsing macro
                endMacro = True
                break
            # Parameter definition
            paramName, paramValue = line.split("=")
            paramName.strip()
            paramValue.strip()
            macro.addParameter(paramName, paramValue)
        if endMacro:
            return macro
        else:
            raise ValueError("Unexpected end of file while parsing macro "+name)
    

    def parseRegister(self, firstLine):
        # Register parsing
        args = firstLine.split()
        # We expect that first argument is REGISTER
        if args[0].strip() != "REGISTER":
            raise ValueError("Missing REGISTER keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing register name")
        addr = args[2].strip()
        reg = Register(name, addr) # Create register
        line = " "
        endRegister = False
        reg.shadowReg = None
        while line:
            line = self.getLine()
            if line == "":
                continue
            line = line.strip()
            line = (line.split("##")[0]).strip()  # Throw away comments
            if line == "":
                line = " "
                continue            
            keyword = (line.split()[0]).strip()
            if "#!" in keyword:
                # Documentation comment
                comment = line.split("#!")[1]
                reg.addComment(comment)
                continue
            if "BITFIELD" in keyword:
                # Bitfiels definition
                bf = self.parseBitField(line)
                reg.addBitField(bf)
                continue
            if "SHADOW" in keyword:
                # Shadow register definition
                args = line.split("=")
                reg.shadowReg = (args[1]).strip()
                continue
            if "ENDREGISTER" in keyword:
                # Finished parsing register
                endRegister = True
                break
            # Parser has encountered an unknown keyword
            raise ValueError("Unknown construct in register definition : "+line)

        if endRegister:
            return reg
        else:
            raise ValueError("Unexpected end of file while parsing register "+name)
        
    def parseBitField(self, firstLine):
        # Bitfield parsing
        args = firstLine.split()
        # We expect that first argument is BITFIELD
        if args[0].strip() != "BITFIELD":
            raise ValueError("Missing BITFIELD keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing bitfield name")
        position = None
        defaultValue = None
        mode = None
        comments = []
        line = " "
        endBitField = False
        while line:
            line = self.getLine()
            if line == "":
                continue
            line = line.strip()
            line = (line.split("##")[0]).strip()  # Throw away comments
            if line == "":
                line = " "
                continue            
            keyword = (line.split()[0]).strip()
            if "#!" in keyword:
                # Documentation comment
                comment = line.split("#!")[1]
                comments.append(comment)
                continue
            if "POSITION" in keyword:
                # Get position
                args = line.split("=")
                position = (args[1]).strip()
                continue
            if "DEFAULT" in keyword:
                # Get default value
                args = line.split("=")
                defaultValue = (args[1]).strip()
                continue
            if "MODE" in keyword:
                # Get mode
                args = line.split("=")
                mode = (args[1]).strip()
                continue
            if "ENDBITFIELD" in keyword:
                # Finished parsing bitfield
                endBitField = True
                break
            # Parser has encountered an unknown keyword
            raise ValueError("Unknown construct in bitfield definition : "+line)

        if endBitField:
            if (not position):
                raise ValueError("Bit position is missing.")
                return None
            if (not defaultValue):
                raise ValueError("Default value is missing.")
                return None
            if (not mode):
                raise ValueError("Mode is missing.")
                return None           
            bf = BitField(name, position, defaultValue, mode)
            # Add comments to bitfield
            for comment in comments:
                bf.addComment(comment)
            return bf
        else:
            raise ValueError("Unexpected end of file while parsing bitfield "+name)
                    
    def findReg(self, regName):
        for reg in self.registers:
            if reg.name == regName:
                return reg
        raise ValueError("Register "+regName+" does not exist in register bank!")
        
    def getRegisterDefinition(self):
        regDef = RegisterDefinition("# Register definition")

        for regBank in self.regBanks:
            regDef.addRegBank(regBank)
        for voltage in self.voltages:
            regDef.addVoltage(voltage)
        for current in self.currents:
            regDef.addCurrent(current)
        for vector in self.vectors:
            regDef.addVectors(vector)
        for sigClass in self.sigClass:
            regDef.addSigClass(sigClass)
        for comment in self.comments:
            regDef.addComment(comment)
        for macro in self.macros:
            regDef.addMacro(macro)
        for port in self.inputPorts:
            regDef.addInputPort(port)
        for port in self.outputPorts:
            regDef.addOutputPort(port)
        for intReg in self.internalRegs:
            regDef.addInternalReg(intReg)
        for intWire in self.internalWires:
            regDef.addInternalWire(intWire)
        regDef.makeDictionaries()
        return regDef

class RegisterDefinition(object):
    # Container class for the chip register definition
    def __init__(self, name):
        self.name = name
        self.regBanks = []   # Register banks
        self.voltages = []   # voltages
        self.currents = []   # currents
        self.vectors = []    # vectors
        self.sigClass = []   # signal classes
        self.comments = []   # comments        
        self.macros = []     # macros
        self.inputPorts = []    # Defined input ports
        self.outputPorts = []    # Defined output ports
        self.internalRegs = []
        self.internalWires = []

    def makeDictionaries(self):
        self.regNameDict = {}
        self.regAddrDict = {}
        self.regFldDict = {}
        for regBank in self.regBanks:
            for reg in regBank.getRegs():
                regName = reg.getName()
                regAddr = reg.getAddress()
                self.regNameDict.update( {regName:reg} )
                self.regAddrDict.update( {regAddr:reg} )
                for fld in reg.getBitFields():
                    self.regFldDict.update( {fld.getName():reg} )

    def addInternalReg(self, intReg):
        self.internalRegs.append(intReg)

    def getInternalRegs(self):
        return self.internalRegs

    def addInternalWire(self, intWire):
        self.internalWires.append(intWire)

    def getInternalWires(self):
        return self.internalWires
        
    def addInputPort(self, port):
        self.inputPorts.append(port)
        
    def getInputPorts(self):
        return self.inputPorts
        
    def addOutputPort(self, port):
        self.outputPorts.append(port)
        
    def getOutputPorts(self):
        return self.outputPorts
    
    def getName(self):
        return self.name
    
    def addRegBank(self, regBank):
        self.regBanks.append(regBank)
    
    def getRegBanks(self):
        return self.regBanks
        
    def addVoltage(self, voltage):
        self.voltages.append(voltage)
    
    def getVoltages(self):
        return self.voltages
        
    def addCurrent(self, current):
        self.currents.append(current)
    
    def getCurrents(self):
        return self.currents
        
    def addVector(self, vector):
        self.vectors.append(vector)
        
    def getVectors(self):
        return self.vectors
        
    def addSigClass(self, sigClass):
        self.sigClass.append(sigClass)
        
    def getSigClasses(self):
        return self.sigClass
        
    def addComment(self, comment):
        self.comments.append(comment)
    
    def getComments(self):
        return self.comments

    def addMacro(self, macro):
        self.macros.append(macro)
    
    def getMacros(self):
        return self.macros

    def getRegisterByName(self, regName):
#        for regBank in self.regBanks:
#            for reg in regBank.registers:
#                if reg.getName()==regName:
#                    return reg
#        raise ValueError("Register "+regName+" not found")
        if self.regNameDict.has_key(regName):
            return self.regNameDict[regName]
        else:
            raise ValueError("Register "+regName+" not found")

    def getRegisterByAddress(self, regAddr):
#        for regBank in self.regBanks:
#            for reg in regBank.registers:
#                if reg.getAddress()==regAddr:
#                    return reg
#        raise ValueError("Register on address "+str(regAddr)+" not found")
        if self.regAddrDict.has_key(regAddr):
            return self.regAddrDict[regAddr]
        else:
            raise ValueError("Register on address "+str(regAddr)+" not found")

    def getRegistersByName(self, regList="ALL"):
#        regs = []
#        for regBank in self.regBanks:
#            for reg in regBank.registers:
#                if regList == "ALL":
#                    regs.append(reg)
#                else:
#                    if reg.getName() in regList:
#                        regs.append(reg)
#        return regs
        if regList=="ALL":
            regs = copy(self.regNameDict.values())
        else:
            regs = []
            for regName in regList:
                regs.append( self.getRegisterByName(regName) )
        return regs
        

    def getRegisterAddresesByName(self, regList="ALL"):
#        regAddrs = []
#        for regBank in self.regBanks:
#            for reg in regBank.registers:
#                if regList == "ALL":
#                    regAddrs.append(reg.getAddress())
#                else:
#                    if reg.getName() in regList:
#                        regAddrs.append(reg.getAddress())
#        return regAddrs
        if regList=="ALL":
            regAddrs = copy(self.regAddrDict.keys())
        else:
            regAddrs = []
            for regName in regList:
                regAddrs.append( self.getRegisterByName(regName).getAddress() )
        return regAddrs

    def getRegisterByBitField(self, bitFieldName):
        return self.regFldDict[bitFieldName]

    def __repr__(self):
        # Dump the whole register bank
        retVal  = self.name + "\n"
        for comment in self.getComments():
            retVal += comment + "\n"
        
        for regBank in self.regBanks:
            retVal += regBank.__repr__()
            
        for regBank in self.regBanks:
            for reg in regBank.getRegs():
                retVal += reg.__repr__() + "\n"

        for macro in self.macros:
            retVal += macro.__repr__() + "\n"

        for port in self.inputPorts:
            retVal += "INPUT_PORT\t"+port+"\n"

        for port in self.outputPorts:
            retVal += "OUTPUT_PORT\t"+port+"\n"

        for intReg in self.internalRegs:
            retVal += "INTERNAL_REG\t"+intReg+"\n"

        for intWire in self.internalWires:
            retVal += "INTERNAL_WIRE\t"+intWire+"\n"

        return retVal                

    def check(self):
        self.performChecks(self.getRegBanks())

    @staticmethod
    def performChecks(regBanks):
        # Perform various checks on a set of register banks
        # Connect shadowed and shadowing registers

        # Check if register bank names are unique
        allRegBanks = {}
        for bank in regBanks:
            if allRegBanks.has_key(bank.name):
                retVal = "ERROR: Bank name " + bank.name + " is not unique."
                raise ValueError(retVal)
            allRegBanks.update({bank.name : None})
        
        # Check if register and field names are unique
        allRegs = {}
        allFields = {}
        for bank in regBanks:
            for reg in bank.getRegs():
                if allRegs.has_key(reg.name):
                    retVal = "ERROR: Register name " + reg.name + " is not unique."
                    raise ValueError(retVal)
                allRegs.update({reg.name : None})
                for field in reg.getBitFields():
                    if allFields.has_key(field.name):
                        retVal = "ERROR: Field name " + field.name + " is not unique."
                        raise ValueError(retVal)
                    allFields.update({field.name : None})
        
        # Check if register banks are overlapping
        for bank1 in regBanks:
            for bank2 in regBanks:
                if bank1==bank2:
                    continue
                lowAddr = bank1.getAddrL()
                highAddr = bank1.getAddrH()
                if bank2.isInBank(lowAddr) or bank2.isInBank(highAddr):
                    raise ValueError("ERROR: Banks "+bank1.getName()+" and "+bank2.getName()+" are overlapping")
        
        # Now work on shadow registers
        for bank in regBanks:
            for reg in bank.getRegs():
                reg.clearShadowedRegs()
        
        for bank in regBanks:
            for reg in bank.getRegs():
                if not reg.isShadowed():
                    # Register is not shadowed
                    continue
                # Register is shadowed, assign it to its shadowing register
                shadowName = reg.getShadowReg()
                if bank.hasRegister(shadowName):
                    shadowReg = bank.getRegister(shadowName)
                else:
                    retVal = "Shadowing register "+shadowName+", used to shadow "+reg.getName()+" does not exist in register bank "+bank.getName+"\n"
                    retVal += "Ensure that both registers are in the same register bank"
                    raise ValueError(retVal)
                shadowReg.addShadowedReg(reg.name)
                
                # Check if shadowed register has sticky bit
                for field in reg.getBitFields():
                    if field.isSticky():
                        raise ValueError("ERROR : ("+field.getName()+") Sticky bit cannot be assigned to shadowed register.")

        # Check for circular shadow references and multiple shadowing
        for bank in regBanks:
            for reg in bank.getRegs():
                if not reg.isShadowing():
                    continue
                # Register shadows other registers
                # Ensure that all shadowed registers are not shadowing other registers
                for sregName in reg.getShadowedRegs():
                    sreg = bank.getRegister(sregName)
                    if sreg.isShadowing():
                        raise ValueError("Register " + sregName + " is shadowed by "+reg.name+" but shadows other registers.")        
            
