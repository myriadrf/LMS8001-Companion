#
# LMS8001_EVB
#

import serial
from serial.tools import *
from serial.tools.list_ports import *
from copy import copy
from LMS8001 import *
from ADF4002 import *

class LMS8001_EVB(object):

    def __init__(self, portName='/dev/ttyACM0', verbose=0):
        """
        Initialize communication with LMS8001_EVB
        """
        self.ser=serial.Serial(port=portName)
        self.verbose = verbose
        if not self.ser.isOpen():
            self.ser = None
            raise IOError("Could not open port "+portName+"\nPlease ensure that the port exists and that the permissions are set correctly.\nOn Linux systems permissions can be set by sudo chmod a+rw /dev/portName")
        if verbose>0:
            self.printInfo()
        
        self.LMS8001 = LMS8001(SPIwriteFn=self.LMS8001_Write, SPIreadFn=self.LMS8001_Read, verbose=verbose)
        self.ADF4002 = ADF4002(self.ADF4002Program)
        
    def __del__(self):
        """
        Close communication with LMS8001_EVB
        """
        if self.ser:
            self.ser.close()

    def log(self, logMsg):
        print logMsg

    @staticmethod
    def findLMS8001():
        res = []
        for port in serial.tools.list_ports.comports():
            if port.vid==1155 and port.pid==22336:
                try:
                    portName = port.device
                    ser=serial.Serial(port=portName)
                    bytes = [0]*64
                    s = ""
                    for i in range(0,len(bytes)):
                        s += chr(bytes[i])                
                    ser.write(s)
                    tmp = ser.read(size=64)
                    bytes = [0]*int(len(tmp))
                    for i in range(0, len(tmp)):
                        bytes[i] = ord(tmp[i])  
                    if len(bytes)<64:
                        ser.close()
                        continue
                    rxData = bytes[8:]
                    if rxData[1]==1:
                        res.append(portName)
                    ser.close()
                except:
                    pass
        return res         
        
    def getCommandNumber(self, cmdName):
        if cmdName == "CMD_GET_INFO":
            return 0
        elif cmdName == "CMD_LMS_RST":
            return 0x20
        elif cmdName == "LMS_RST_DEACTIVATE":
            return 0
        elif cmdName == "LMS_RST_ACTIVATE":
            return 1
        elif cmdName == "LMS_RST_PULSE":
            return 2
        elif cmdName == "CMD_LMS8001_WR":
            return 0x25
        elif cmdName == "CMD_LMS8001_RD":
            return 0x26
        elif cmdName == "CMD_ADF4002_WR":
            return 0x31            
        else:
            raise ValueError("Unknown command "+cmdName)

    def getLMS8001(self):
        return self.LMS8001        
            
    #
    # Low level communication
    #
    
    @staticmethod
    def bytes2string(bytes):
        """
        Convert the byte array to string.
        Used for serial communication.
        """
        s = ""
        for i in range(0,len(bytes)):
            s += chr(bytes[i])
        return s

    @staticmethod
    def string2bytes(string):
        """
        Convert the string to byte array.
        Used for serial communication.
        """
        bytes = [0]*int(len(string))
        for i in range(0, len(string)):
            bytes[i] = ord(string[i])
        return bytes

    def sendCommand(self, command, nDataBlocks=0, periphID=0, data=[]):
        """
        Send the command to LMS8001_EVB.
        Function returns (status, data)
        """
        tmp = [0]*64
        tmp[0] = command
        tmp[1] = 0
        tmp[2] = nDataBlocks
        tmp[3] = periphID
        nData = len(data)
        if nData>56:
            raise ValueError("Length of data must be less than 56, "+str(nData)+" bytes given")
        for i in range(0, nData):
            tmp[8+i] = data[i]
        if self.verbose>2:
            self.log("sendCommand:Write    : "+str(tmp))
        self.ser.write(self.bytes2string(tmp))
        tmp = self.string2bytes(self.ser.read(size=64))
        if len(tmp)<64:
            raise IOError("Lenght of received data "+len(tmp)+"<64 bytes")
        if self.verbose>2:
            self.log("sendCommand:Response : "+str(tmp))
        rxStatus = tmp[1]
        rxData = tmp[8:]
        return (rxStatus, rxData)

    #
    # Utility functions
    #

    def getInfo(self):
        """
        Get the information about LMS8001_EVB.
        Function returns 
        (FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD)
        """
        command = self.getCommandNumber("CMD_GET_INFO")
        status, rxData = self.sendCommand(command)
        if status != 1:
            raise IOError("Command returned with status "+str(status))
        FW_VER = rxData[0]
        DEV_TYPE = rxData[1]
        LMS_PROTOCOL_VER = rxData[2]
        HW_VER = rxData[3]
        EXP_BOARD = rxData[4]
        return (FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD)
   
    def printInfo(self):
        """
        Print info about LMS8001_EVB
        """
        FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD = self.getInfo()
        self.log("FW_VER           : "+str(FW_VER))
        self.log("DEV_TYPE         : "+str(DEV_TYPE))
        self.log("LMS_PROTOCOL_VER : " + str(LMS_PROTOCOL_VER))
        self.log("HW_VER           : " + str(HW_VER))
        self.log("EXP_BOARD        : " + str(EXP_BOARD))
        
    def LMS8001_Reset(self, rstType="pulse"):
        """
        Reset LMS8001.
        rstType specifies the type of reset:
            pulse - activate and deactivate reset
            activate - activate reset
            deactivate - deactivate reset
        """
        command = self.getCommandNumber("CMD_LMS_RST")
        if rstType=="pulse":
            data = [self.getCommandNumber("LMS_RST_PULSE")]
        elif rstType=="activate":
            data = [self.getCommandNumber("LMS_RST_ACTIVATE")]        
        elif rstType=="deactivate":
            data = [self.getCommandNumber("LMS_RST_DEACTIVATE")]        
        else:
            raise ValueError("Invalid reset type "+str(rstType))
        rxStatus, rxData = self.sendCommand(command, data=data)
        if rxStatus != 1:
            raise IOError("Command returned with status "+str(status))

    def LMS8001_Write(self, regList, packetSize=14):
        """
        Write the data to LMS8001 via SPI interface.
        regList is a list of registers to write in the format:
        [ (regAddr, regData), (regAddr, regData), ...]
        packetSize controls the number of register writes in a single USB transfer
        """
        command = self.getCommandNumber("CMD_LMS8001_WR")
        nDataBlocks = len(regList)

        toSend = copy(regList)
       
        while len(toSend)>0:
            nPackets = 0
            data = []
            while nPackets<packetSize and len(toSend)>0:
                regAddr, regData = toSend[0]
                toSend.pop(0)
                regAddrH = regAddr >> 8
                regAddrL = regAddr % 256
                regDataH = regData >> 8
                regDataL = regData % 256
                data += [regAddrH, regAddrL, regDataH, regDataL]
                nPackets += 1
            rxStatus, rxData = self.sendCommand(command, nDataBlocks = nPackets, data=data)
            if rxStatus != 1:
                raise IOError("Command returned with status "+str(status))

    def LMS8001_Read(self, regList, packetSize=14):
        """
        Read the data from LMS8001 via SPI interface.
        regList is a list of registers to read in the format:
        [ regAddr, regAddr, ...]
        packetSize controls the number of register writes in a single USB transfer
        """
        command = self.getCommandNumber("CMD_LMS8001_RD")
        nDataBlocks = len(regList)

        toRead = copy(regList)
        regData = []
       
        while len(toRead)>0:
            nPackets = 0
            data = []
            while nPackets<packetSize and len(toRead)>0:
                regAddr = toRead[0]
                toRead.pop(0)
                regAddrH = regAddr >> 8
                regAddrL = regAddr % 256
                data += [regAddrH, regAddrL]
                nPackets += 1
            rxStatus, rxData = self.sendCommand(command, nDataBlocks = nPackets, data=data)
            if rxStatus != 1:
                raise IOError("Command returned with status "+str(rxStatus))
            for i in range(0, nPackets):
                regDataH = rxData[i*4+2]
                regDataL = rxData[i*4+3]
                regData.append( (regDataH << 8) + regDataL)
        return regData
    
    #
    # ADF4002 program
    #                

    def ADF4002Program(self, regValues):
        """
        Program ADF4002 with given regValues.
        regValues = [reg1, reg2, reg3, reg4]
        where reg1-4 are integers containing the values of ADF4002 registers (24 bit).
        """
        if len(regValues)!=4:
            raise ValueError("Expected four 24-bit values, got "+str(len(regValues)))
        data = []
        for reg in regValues:
            bits23_16 = (reg >> 16) & 0xFF
            bits15_8 = (reg >> 8) & 0xFF
            bits7_0 = reg & 0xFF
            data += [bits23_16, bits15_8, bits7_0]
        command = self.getCommandNumber("CMD_ADF4002_WR")
        rxStatus, rxData = self.sendCommand(command, nDataBlocks=4, data=data)
        if rxStatus != 1:
            raise IOError("Command returned with status "+str(rxStatus))


