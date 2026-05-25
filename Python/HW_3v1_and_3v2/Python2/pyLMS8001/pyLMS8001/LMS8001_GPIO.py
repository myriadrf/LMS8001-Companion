
class LMS8001_GPIO(object):
    def __init__(self, chip, n):
        if n not in range(0,9):
            raise ValueError("GPIO n must be in range 0 - 8")
        self.chip = chip    # reference to chip instance
        self.n = n          # GPIO number
        
    #
    # GPIOn output value
    #

    @property
    def OUT(self):
        """
        Get the value written to GPIOn
        """
        val = self.chip["GPIOOutData"]["GPIO_OUT_SPI<8:0>"]
        if val & (1<<self.n)>0:
            return 1
        return 0

    @OUT.setter
    def OUT(self, value):
        """
        Write the value to GPIOn
        """
        tmp = self.chip["GPIOOutData"]["GPIO_OUT_SPI<8:0>"]
        mask = 1<<self.n
        tmp &= (0xFFFF ^ mask)
        if value > 0:
            tmp |= mask
        self.chip["GPIOOutData"]["GPIO_OUT_SPI<8:0>"] = tmp

    #
    # GPIOn output value
    #

    @property
    def IN(self):
        """
        Get the value of GPIOn pin
        """
        val = self.chip["GPIOInData"]["GPIO_IN<8:0>"]
        if val & (1<<self.n)>0:
            return 1
        return 0

    #
    # GPIO selector
    #
    
    @property
    def SEL(self):
        """
        Get the value of GPIOn_SEL<2:0>
        """
        if self.n<5:
            regName = "GPIOOUT_SEL0"
        else:
            regName = "GPIOOUT_SEL1"
        fieldName = "GPIO"+str(self.n)+"_SEL<2:0>"
        return self.chip[regName][fieldName]
        
    @SEL.setter
    def SEL(self, value):
        """
        Set the value of GPIOn_SEL<2:0>
        """
        if value not in [0,1,2,3,4,"SPI","PLL_LOCK","VTUNE_LOW","VTUNE_HIGH","FAST_LOCK"]:
            raise ValueError('GPIO_SEL must have value of 0,1,2,3,4,"SPI","PLL_LOCK","VTUNE_LOW","VTUNE_HIGH","FAST_LOCK"')
        if value==0 or value=="SPI":
            tmp = 0
        elif value==1 or value=="PLL_LOCK":
            tmp = 1
        elif value==2 or value=="VTUNE_LOW":
            tmp = 2
        elif value==3 or value=="VTUNE_HIGH":
            tmp = 3
        else:
            tmp = 4

        if self.n<5:
            regName = "GPIOOUT_SEL0"
        else:
            regName = "GPIOOUT_SEL1"

        fieldName = "GPIO"+str(self.n)+"_SEL<2:0>"
        self.chip[regName][fieldName] = tmp
        
    #
    # GPIO_PEn output value
    #

    @property
    def PE(self):
        """
        Get the value of GPIO_PEn
        """
        val = self.chip["GPIOConfig_PE"]["GPIO_PE<8:0>"]
        if val & (1<<self.n)>0:
            return 1
        return 0

    @PE.setter
    def PE(self, value):
        """
        Write the value to GPIO_PEn
        """
        tmp = self.chip["GPIOConfig_PE"]["GPIO_PE<8:0>"]
        mask = 1<<self.n
        tmp &= (0xFFFF ^ mask)
        if value > 0:
            tmp |= mask
        self.chip["GPIOConfig_PE"]["GPIO_PE<8:0>"] = tmp        

    #
    # GPIO_DSn output value
    #

    @property
    def DS(self):
        """
        Get the value of GPIO_DSn
        """
        val = self.chip["GPIOConfig_DS"]["GPIO_DS<8:0>"]
        if val & (1<<self.n)>0:
            return 1
        return 0

    @DS.setter
    def DS(self, value):
        """
        Write the value to GPIO_DSn
        """
        tmp = self.chip["GPIOConfig_DS"]["GPIO_DS<8:0>"]
        mask = 1<<self.n
        tmp &= (0xFFFF ^ mask)
        if value > 0:
            tmp |= mask
        self.chip["GPIOConfig_DS"]["GPIO_DS<8:0>"] = tmp             
        
    #
    # GPIO_InOn output value
    #

    @property
    def InO(self):
        """
        Get the value of GPIO_InOn
        """
        val = self.chip["GPIOConfig_IO"]["GPIO_InO<8:0>"]
        if val & (1<<self.n)>0:
            return 1
        return 0

    @InO.setter
    def InO(self, value):
        """
        Write the value to GPIO_InOn
        """
        tmp = self.chip["GPIOConfig_IO"]["GPIO_InO<8:0>"]
        mask = 1<<self.n
        tmp &= (0xFFFF ^ mask)
        if value > 0:
            tmp |= mask
        self.chip["GPIOConfig_IO"]["GPIO_InO<8:0>"] = tmp             


        
    
