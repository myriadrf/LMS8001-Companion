
from LMS8001_HLMIX_CFG import *

class LMS8001_HLMIX(object):
    def __init__(self, chip, channel):
        if channel not in ['A','B','C','D']:
            raise ValueError("Channel must be ['A','B','C','D']")
        self.chip = chip
        self.channel = channel
        self.CFG = { 0 : LMS8001_HLMIX_CFG(chip, channel, 0),
                     1 : LMS8001_HLMIX_CFG(chip, channel, 1),
                     2 : LMS8001_HLMIX_CFG(chip, channel, 2),
                     3 : LMS8001_HLMIX_CFG(chip, channel, 3)}

    #
    # Channel settings select signals from CHx_CONF_SEL0
    #

    @property
    def CONF_SEL0_INTERNAL(self):
        """
        Get the value written to CONF_SEL0_INTERNAL
        """
        return self.chip["HLMIX"+self.channel+"_CONF_SEL0"]["HLMIX"+self.channel+"_CONF_SEL0_INTERNAL"]

    @CONF_SEL0_INTERNAL.setter
    def CONF_SEL0_INTERNAL(self, value):
        """
        Write the value to CONF_SEL0_INTERNAL
        """
        self.chip["HLMIX"+self.channel+"_CONF_SEL0"]["HLMIX"+self.channel+"_CONF_SEL0_INTERNAL"] = value

    @property
    def CONF_SEL0_INVERT(self):
        """
        Get the value written to CONF_SEL0_INVERT
        """
        return self.chip["HLMIX"+self.channel+"_CONF_SEL0"]["HLMIX"+self.channel+"_CONF_SEL0_INVERT"]

    @CONF_SEL0_INVERT.setter
    def CONF_SEL0_INVERT(self, value):
        """
        Write the value to CONF_SEL0_INVERT
        """
        self.chip["HLMIX"+self.channel+"_CONF_SEL0"]["HLMIX"+self.channel+"_CONF_SEL0_INVERT"] = value

    @property
    def CONF_SEL0_MASK(self):
        """
        Get the value written to CONF_SEL0_MASK
        """
        return self.chip["HLMIX"+self.channel+"_CONF_SEL0"]["HLMIX"+self.channel+"_CONF_SEL0_MASK<8:0>"]

    @CONF_SEL0_MASK.setter
    def CONF_SEL0_MASK(self, value):
        """
        Write the value to CONF_SEL0_MASK
        """
        self.chip["HLMIX"+self.channel+"_CONF_SEL0"]["HLMIX"+self.channel+"_CONF_SEL0_MASK<8:0>"] = value
    

    #
    # Channel settings select signals from CHx_CONF_SEL1
    #

    @property
    def CONF_SEL1_INTERNAL(self):
        """
        Get the value written to CONF_SEL1_INTERNAL
        """
        return self.chip["HLMIX"+self.channel+"_CONF_SEL1"]["HLMIX"+self.channel+"_CONF_SEL1_INTERNAL"]

    @CONF_SEL1_INTERNAL.setter
    def CONF_SEL1_INTERNAL(self, value):
        """
        Write the value to CONF_SEL1_INTERNAL
        """
        self.chip["HLMIX"+self.channel+"_CONF_SEL1"]["HLMIX"+self.channel+"_CONF_SEL1_INTERNAL"] = value

    @property
    def CONF_SEL1_INVERT(self):
        """
        Get the value written to CONF_SEL1_INVERT
        """
        return self.chip["HLMIX"+self.channel+"_CONF_SEL1"]["HLMIX"+self.channel+"_CONF_SEL1_INVERT"]

    @CONF_SEL1_INVERT.setter
    def CONF_SEL1_INVERT(self, value):
        """
        Write the value to CONF_SEL1_INVERT
        """
        self.chip["HLMIX"+self.channel+"_CONF_SEL1"]["HLMIX"+self.channel+"_CONF_SEL1_INVERT"] = value

    @property
    def CONF_SEL1_MASK(self):
        """
        Get the value written to CONF_SEL1_MASK
        """
        return self.chip["HLMIX"+self.channel+"_CONF_SEL1"]["HLMIX"+self.channel+"_CONF_SEL1_MASK<8:0>"]

    @CONF_SEL1_MASK.setter
    def CONF_SEL1_MASK(self, value):
        """
        Write the value to CONF_SEL1_MASK
        """
        self.chip["HLMIX"+self.channel+"_CONF_SEL1"]["HLMIX"+self.channel+"_CONF_SEL1_MASK<8:0>"] = value

    #
    # Channel settings select signals from CHx_LOSS_SEL0
    #

    @property
    def LOSS_SEL0_INTERNAL(self):
        """
        Get the value written to LOSS_SEL0_INTERNAL
        """
        return self.chip["HLMIX"+self.channel+"_LOSS_SEL0"]["HLMIX"+self.channel+"_LOSS_SEL0_INTERNAL"]

    @LOSS_SEL0_INTERNAL.setter
    def LOSS_SEL0_INTERNAL(self, value):
        """
        Write the value to LOSS_SEL0_INTERNAL
        """
        self.chip["HLMIX"+self.channel+"_LOSS_SEL0"]["HLMIX"+self.channel+"_LOSS_SEL0_INTERNAL"] = value

    @property
    def LOSS_SEL0_INVERT(self):
        """
        Get the value written to LOSS_SEL0_INVERT
        """
        return self.chip["HLMIX"+self.channel+"_LOSS_SEL0"]["HLMIX"+self.channel+"_LOSS_SEL0_INVERT"]

    @LOSS_SEL0_INVERT.setter
    def LOSS_SEL0_INVERT(self, value):
        """
        Write the value to LOSS_SEL0_INVERT
        """
        self.chip["HLMIX"+self.channel+"_LOSS_SEL0"]["HLMIX"+self.channel+"_LOSS_SEL0_INVERT"] = value

    @property
    def LOSS_SEL0_MASK(self):
        """
        Get the value written to LOSS_SEL0_MASK
        """
        return self.chip["HLMIX"+self.channel+"_LOSS_SEL0"]["HLMIX"+self.channel+"_LOSS_SEL0_MASK<8:0>"]

    @LOSS_SEL0_MASK.setter
    def LOSS_SEL0_MASK(self, value):
        """
        Write the value to LOSS_SEL0_MASK
        """
        self.chip["HLMIX"+self.channel+"_LOSS_SEL0"]["HLMIX"+self.channel+"_LOSS_SEL0_MASK<8:0>"] = value

    #
    # Channel settings select signals from CHx_LOSS_SEL1
    #

    @property
    def LOSS_SEL1_INTERNAL(self):
        """
        Get the value written to LOSS_SEL1_INTERNAL
        """
        return self.chip["HLMIX"+self.channel+"_LOSS_SEL1"]["HLMIX"+self.channel+"_LOSS_SEL1_INTERNAL"]

    @LOSS_SEL1_INTERNAL.setter
    def LOSS_SEL1_INTERNAL(self, value):
        """
        Write the value to LOSS_SEL1_INTERNAL
        """
        self.chip["HLMIX"+self.channel+"_LOSS_SEL1"]["HLMIX"+self.channel+"_LOSS_SEL1_INTERNAL"] = value

    @property
    def LOSS_SEL1_INVERT(self):
        """
        Get the value written to LOSS_SEL1_INVERT
        """
        return self.chip["HLMIX"+self.channel+"_LOSS_SEL1"]["HLMIX"+self.channel+"_LOSS_SEL1_INVERT"]

    @LOSS_SEL1_INVERT.setter
    def LOSS_SEL1_INVERT(self, value):
        """
        Write the value to LOSS_SEL1_INVERT
        """
        self.chip["HLMIX"+self.channel+"_LOSS_SEL1"]["HLMIX"+self.channel+"_LOSS_SEL1_INVERT"] = value

    @property
    def LOSS_SEL1_MASK(self):
        """
        Get the value written to LOSS_SEL1_MASK
        """
        return self.chip["HLMIX"+self.channel+"_LOSS_SEL1"]["HLMIX"+self.channel+"_LOSS_SEL1_MASK<8:0>"]

    @LOSS_SEL1_MASK.setter
    def LOSS_SEL1_MASK(self, value):
        """
        Write the value to LOSS_SEL1_MASK
        """
        self.chip["HLMIX"+self.channel+"_LOSS_SEL1"]["HLMIX"+self.channel+"_LOSS_SEL1_MASK<8:0>"] = value        

    #
    # HLMIXx_INT_SEL
    #

    @property
    def LOSS_INT_SEL(self):
        """
        Get the value written to LOSS_INT_SEL
        """
        return self.chip["HLMIX"+self.channel+"_INT_SEL"]["HLMIX"+self.channel+"_LOSS_INT_SEL<1:0>"]

    @LOSS_INT_SEL.setter
    def LOSS_INT_SEL(self, value):
        """
        Write the value to LOSS_INT_SEL
        """
        self.chip["HLMIX"+self.channel+"_INT_SEL"]["HLMIX"+self.channel+"_LOSS_INT_SEL<1:0>"] = value

    @property
    def CONF_INT_SEL(self):
        """
        Get the value written to CONF_INT_SEL
        """
        return self.chip["HLMIX"+self.channel+"_INT_SEL"]["HLMIX"+self.channel+"_CONF_INT_SEL<1:0>"]

    @CONF_INT_SEL.setter
    def CONF_INT_SEL(self, value):
        """
        Write the value to CONF_INT_SEL
        """
        self.chip["HLMIX"+self.channel+"_INT_SEL"]["HLMIX"+self.channel+"_CONF_INT_SEL<1:0>"] = value


    #
    # Readback values
    #

    @property
    def VGCAS(self):
        return self.chip["HLMIX"+self.channel+"_CONFIG_RB"]["HLMIX"+self.channel+"_VGCAS_RB<6:0>"]

    @property
    def ICT_BIAS(self):
        return self.chip["HLMIX"+self.channel+"_CONFIG_RB"]["HLMIX"+self.channel+"_ICT_BIAS_RB<4:0>"]

    @property
    def BIAS_PD(self):
        return self.chip["HLMIX"+self.channel+"_CONFIG_RB"]["HLMIX"+self.channel+"_BIAS_PD_RB"]

    @property
    def LOBUF_PD(self):
        return self.chip["HLMIX"+self.channel+"_CONFIG_RB"]["HLMIX"+self.channel+"_LOBUF_PD_RB"]

    @property
    def MIXLOSS(self):
        return self.chip["HLMIX"+self.channel+"_LOSS_RB"]["HLMIX"+self.channel+"_MIXLOSS_RB<3:0>"]



