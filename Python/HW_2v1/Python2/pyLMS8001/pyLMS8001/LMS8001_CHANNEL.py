
from LMS8001_CHANNEL_PD import *
from LMS8001_CHANNEL_LNA import *
from LMS8001_CHANNEL_PA import *

class LMS8001_CHANNEL(object):
    def __init__(self, chip, channel):
        if channel not in ['A','B','C','D']:
            raise ValueError("Channel must be ['A','B','C','D']")
        self.chip = chip
        self.channel = channel
        self.PD = { 0 : LMS8001_CHANNEL_PD(chip, channel, 0),
                    1 : LMS8001_CHANNEL_PD(chip, channel, 1),
                    2 : LMS8001_CHANNEL_PD(chip, channel, 2),
                    3 : LMS8001_CHANNEL_PD(chip, channel, 3)}

        self.LNA_CTRL = { 0 : LMS8001_CHANNEL_LNA(chip, channel, 0),
                          1 : LMS8001_CHANNEL_LNA(chip, channel, 1),
                          2 : LMS8001_CHANNEL_LNA(chip, channel, 2),
                          3 : LMS8001_CHANNEL_LNA(chip, channel, 3)}

        self.PA_CTRL = { 0 : LMS8001_CHANNEL_PA(chip, channel, 0),
                         1 : LMS8001_CHANNEL_PA(chip, channel, 1),
                         2 : LMS8001_CHANNEL_PA(chip, channel, 2),
                         3 : LMS8001_CHANNEL_PA(chip, channel, 3)}


     
    #
    # Channel settings select signals from CHx_PD_SEL1
    #

    @property
    def PD_SEL1_INTERNAL(self):
        """
        Get the value written to PD_SEL1_INTERNAL
        """
        return self.chip["CH"+self.channel+"_PD_SEL1"]["CH"+self.channel+"_PD_SEL1_INTERNAL"]

    @PD_SEL1_INTERNAL.setter
    def PD_SEL1_INTERNAL(self, value):
        """
        Write the value to PD_SEL1_INTERNAL
        """
        self.chip["CH"+self.channel+"_PD_SEL1"]["CH"+self.channel+"_PD_SEL1_INTERNAL"] = value
        

    @property
    def PD_SEL1_INVERT(self):
        """
        Get the value written to PD_SEL1_INVERT
        """
        return self.chip["CH"+self.channel+"_PD_SEL1"]["CH"+self.channel+"_PD_SEL1_INVERT"]

    @PD_SEL1_INVERT.setter
    def PD_SEL1_INVERT(self, value):
        """
        Write the value to PD_SEL1_INVERT
        """
        self.chip["CH"+self.channel+"_PD_SEL1"]["CH"+self.channel+"_PD_SEL1_INVERT"] = value

    @property
    def PD_SEL1_MASK(self):
        """
        Get the value written to PD_SEL1_MASK
        """
        return self.chip["CH"+self.channel+"_PD_SEL1"]["CH"+self.channel+"_PD_SEL1_MASK<8:0>"]

    @PD_SEL1_MASK.setter
    def PD_SEL1_MASK(self, value):
        """
        Write the value to PD_SEL1_MASK
        """
        self.chip["CH"+self.channel+"_PD_SEL1"]["CH"+self.channel+"_PD_SEL1_MASK<8:0>"] = value

    #
    # Channel settings select signals from CHx_PD_SEL0
    #

    @property
    def PD_SEL0_INTERNAL(self):
        """
        Get the value written to PD_SEL0_INTERNAL
        """
        return self.chip["CH"+self.channel+"_PD_SEL0"]["CH"+self.channel+"_PD_SEL0_INTERNAL"]

    @PD_SEL0_INTERNAL.setter
    def PD_SEL0_INTERNAL(self, value):
        """
        Write the value to PD_SEL0_INTERNAL
        """
        self.chip["CH"+self.channel+"_PD_SEL0"]["CH"+self.channel+"_PD_SEL0_INTERNAL"] = value
        

    @property
    def PD_SEL0_INVERT(self):
        """
        Get the value written to PD_SEL0_INVERT
        """
        return self.chip["CH"+self.channel+"_PD_SEL0"]["CH"+self.channel+"_PD_SEL0_INVERT"]

    @PD_SEL0_INVERT.setter
    def PD_SEL0_INVERT(self, value):
        """
        Write the value to PD_SEL0_INVERT
        """
        self.chip["CH"+self.channel+"_PD_SEL0"]["CH"+self.channel+"_PD_SEL0_INVERT"] = value

    @property
    def PD_SEL0_MASK(self):
        """
        Get the value written to PD_SEL0_MASK
        """
        return self.chip["CH"+self.channel+"_PD_SEL0"]["CH"+self.channel+"_PD_SEL0_MASK<8:0>"]

    @PD_SEL0_MASK.setter
    def PD_SEL0_MASK(self, value):
        """
        Write the value to PD_SEL0_MASK
        """
        self.chip["CH"+self.channel+"_PD_SEL0"]["CH"+self.channel+"_PD_SEL0_MASK<8:0>"] = value
    

    #
    # Channel settings select signals from CHx_LNA_SEL0
    #

    @property
    def LNA_SEL0_INTERNAL(self):
        """
        Get the value written to LNA_SEL0_INTERNAL
        """
        return self.chip["CH"+self.channel+"_LNA_SEL0"]["CH"+self.channel+"_LNA_SEL0_INTERNAL"]

    @LNA_SEL0_INTERNAL.setter
    def LNA_SEL0_INTERNAL(self, value):
        """
        Write the value to LNA_SEL0_INTERNAL
        """
        self.chip["CH"+self.channel+"_LNA_SEL0"]["CH"+self.channel+"_LNA_SEL0_INTERNAL"] = value
        

    @property
    def LNA_SEL0_INVERT(self):
        """
        Get the value written to LNA_SEL0_INVERT
        """
        return self.chip["CH"+self.channel+"_LNA_SEL0"]["CH"+self.channel+"_LNA_SEL0_INVERT"]

    @LNA_SEL0_INVERT.setter
    def LNA_SEL0_INVERT(self, value):
        """
        Write the value to LNA_SEL0_INVERT
        """
        self.chip["CH"+self.channel+"_LNA_SEL0"]["CH"+self.channel+"_LNA_SEL0_INVERT"] = value

    @property
    def LNA_SEL0_MASK(self):
        """
        Get the value written to LNA_SEL0_MASK
        """
        return self.chip["CH"+self.channel+"_LNA_SEL0"]["CH"+self.channel+"_LNA_SEL0_MASK<8:0>"]

    @LNA_SEL0_MASK.setter
    def LNA_SEL0_MASK(self, value):
        """
        Write the value to LNA_SEL0_MASK
        """
        self.chip["CH"+self.channel+"_LNA_SEL0"]["CH"+self.channel+"_LNA_SEL0_MASK<8:0>"] = value


    #
    # Channel settings select signals from CHx_LNA_SEL1
    #

    @property
    def LNA_SEL1_INTERNAL(self):
        """
        Get the value written to LNA_SEL1_INTERNAL
        """
        return self.chip["CH"+self.channel+"_LNA_SEL1"]["CH"+self.channel+"_LNA_SEL1_INTERNAL"]

    @LNA_SEL1_INTERNAL.setter
    def LNA_SEL1_INTERNAL(self, value):
        """
        Write the value to LNA_SEL1_INTERNAL
        """
        self.chip["CH"+self.channel+"_LNA_SEL1"]["CH"+self.channel+"_LNA_SEL1_INTERNAL"] = value
        

    @property
    def LNA_SEL1_INVERT(self):
        """
        Get the value written to LNA_SEL1_INVERT
        """
        return self.chip["CH"+self.channel+"_LNA_SEL1"]["CH"+self.channel+"_LNA_SEL1_INVERT"]

    @LNA_SEL1_INVERT.setter
    def LNA_SEL1_INVERT(self, value):
        """
        Write the value to LNA_SEL1_INVERT
        """
        self.chip["CH"+self.channel+"_LNA_SEL1"]["CH"+self.channel+"_LNA_SEL1_INVERT"] = value

    @property
    def LNA_SEL1_MASK(self):
        """
        Get the value written to LNA_SEL1_MASK
        """
        return self.chip["CH"+self.channel+"_LNA_SEL1"]["CH"+self.channel+"_LNA_SEL1_MASK<8:0>"]

    @LNA_SEL1_MASK.setter
    def LNA_SEL1_MASK(self, value):
        """
        Write the value to LNA_SEL1_MASK
        """
        self.chip["CH"+self.channel+"_LNA_SEL1"]["CH"+self.channel+"_LNA_SEL1_MASK<8:0>"] = value


    #
    # Channel settings select signals from CHx_PA_SEL0
    #

    @property
    def PA_SEL0_INTERNAL(self):
        """
        Get the value written to PA_SEL0_INTERNAL
        """
        return self.chip["CH"+self.channel+"_PA_SEL0"]["CH"+self.channel+"_PA_SEL0_INTERNAL"]

    @PA_SEL0_INTERNAL.setter
    def PA_SEL0_INTERNAL(self, value):
        """
        Write the value to PA_SEL0_INTERNAL
        """
        self.chip["CH"+self.channel+"_PA_SEL0"]["CH"+self.channel+"_PA_SEL0_INTERNAL"] = value
        

    @property
    def PA_SEL0_INVERT(self):
        """
        Get the value written to PA_SEL0_INVERT
        """
        return self.chip["CH"+self.channel+"_PA_SEL0"]["CH"+self.channel+"_PA_SEL0_INVERT"]

    @PA_SEL0_INVERT.setter
    def PA_SEL0_INVERT(self, value):
        """
        Write the value to PA_SEL0_INVERT
        """
        self.chip["CH"+self.channel+"_PA_SEL0"]["CH"+self.channel+"_PA_SEL0_INVERT"] = value

    @property
    def PA_SEL0_MASK(self):
        """
        Get the value written to PA_SEL0_MASK
        """
        return self.chip["CH"+self.channel+"_PA_SEL0"]["CH"+self.channel+"_PA_SEL0_MASK<8:0>"]

    @PA_SEL0_MASK.setter
    def PA_SEL0_MASK(self, value):
        """
        Write the value to PA_SEL0_MASK
        """
        self.chip["CH"+self.channel+"_PA_SEL0"]["CH"+self.channel+"_PA_SEL0_MASK<8:0>"] = value

    #
    # Channel settings select signals from CHx_PA_SEL1
    #

    @property
    def PA_SEL1_INTERNAL(self):
        """
        Get the value written to PA_SEL1_INTERNAL
        """
        return self.chip["CH"+self.channel+"_PA_SEL1"]["CH"+self.channel+"_PA_SEL1_INTERNAL"]

    @PA_SEL1_INTERNAL.setter
    def PA_SEL1_INTERNAL(self, value):
        """
        Write the value to PA_SEL1_INTERNAL
        """
        self.chip["CH"+self.channel+"_PA_SEL1"]["CH"+self.channel+"_PA_SEL1_INTERNAL"] = value
        

    @property
    def PA_SEL1_INVERT(self):
        """
        Get the value written to PA_SEL1_INVERT
        """
        return self.chip["CH"+self.channel+"_PA_SEL1"]["CH"+self.channel+"_PA_SEL1_INVERT"]

    @PA_SEL1_INVERT.setter
    def PA_SEL1_INVERT(self, value):
        """
        Write the value to PA_SEL1_INVERT
        """
        self.chip["CH"+self.channel+"_PA_SEL1"]["CH"+self.channel+"_PA_SEL1_INVERT"] = value

    @property
    def PA_SEL1_MASK(self):
        """
        Get the value written to PA_SEL1_MASK
        """
        return self.chip["CH"+self.channel+"_PA_SEL1"]["CH"+self.channel+"_PA_SEL1_MASK<8:0>"]

    @PA_SEL1_MASK.setter
    def PA_SEL1_MASK(self, value):
        """
        Write the value to PA_SEL1_MASK
        """
        self.chip["CH"+self.channel+"_PA_SEL1"]["CH"+self.channel+"_PA_SEL1_MASK<8:0>"] = value

    #
    # CHx_INT_SEL
    #

    @property
    def PA_INT_SEL(self):
        """
        Get the value written to PA_INT_SEL
        """
        return self.chip["CH"+self.channel+"_INT_SEL"]["CH"+self.channel+"_PA_INT_SEL<1:0>"]

    @PA_INT_SEL.setter
    def PA_INT_SEL(self, value):
        """
        Write the value to PA_INT_SEL
        """
        self.chip["CH"+self.channel+"_INT_SEL"]["CH"+self.channel+"_PA_INT_SEL<1:0>"] = value

    @property
    def LNA_INT_SEL(self):
        """
        Get the value written to LNA_INT_SEL
        """
        return self.chip["CH"+self.channel+"_INT_SEL"]["CH"+self.channel+"_LNA_INT_SEL<1:0>"]

    @LNA_INT_SEL.setter
    def LNA_INT_SEL(self, value):
        """
        Write the value to LNA_INT_SEL
        """
        self.chip["CH"+self.channel+"_INT_SEL"]["CH"+self.channel+"_LNA_INT_SEL<1:0>"] = value

    @property
    def PD_INT_SEL(self):
        """
        Get the value written to PD_INT_SEL
        """
        return self.chip["CH"+self.channel+"_INT_SEL"]["CH"+self.channel+"_PD_INT_SEL<1:0>"]

    @PD_INT_SEL.setter
    def PD_INT_SEL(self, value):
        """
        Write the value to PD_INT_SEL
        """
        self.chip["CH"+self.channel+"_INT_SEL"]["CH"+self.channel+"_PD_INT_SEL<1:0>"] = value
    
    #
    # PA_ILIN2X
    #

    @property
    def PA_ILIN2X(self):
        """
        Get the value written to PA_ILIN2X
        """
        return self.chip["CH"+self.channel+"_HFPAD_ICT"]["CH"+self.channel+"_PA_ILIN2X"]

    @PA_ILIN2X.setter
    def PA_ILIN2X(self, value):
        """
        Write the value to PA_ILIN2X
        """
        self.chip["CH"+self.channel+"_HFPAD_ICT"]["CH"+self.channel+"_PA_ILIN2X"] = value
        
    #
    # PA_ICT_LIN
    #

    @property
    def PA_ICT_LIN(self):
        """
        Get the value written to PA_ICT_LIN
        """
        return self.chip["CH"+self.channel+"_HFPAD_ICT"]["CH"+self.channel+"_PA_ICT_LIN<4:0>"]

    @PA_ICT_LIN.setter
    def PA_ICT_LIN(self, value):
        """
        Write the value to PA_ICT_LIN
        """
        self.chip["CH"+self.channel+"_HFPAD_ICT"]["CH"+self.channel+"_PA_ICT_LIN<4:0>"] = value

    #
    # PA_ICT_MAIN
    #

    @property
    def PA_ICT_MAIN(self):
        """
        Get the value written to PA_ICT_MAIN
        """
        return self.chip["CH"+self.channel+"_HFPAD_ICT"]["CH"+self.channel+"_PA_ICT_MAIN<4:0>"]

    @PA_ICT_MAIN.setter
    def PA_ICT_MAIN(self, value):
        """
        Write the value to PA_ICT_MAIN
        """
        self.chip["CH"+self.channel+"_HFPAD_ICT"]["CH"+self.channel+"_PA_ICT_MAIN<4:0>"] = value

    #
    # Readback values
    #

    @property
    def PA_R50_EN(self):
        return self.chip["CH"+self.channel+"_PD_RB"]["CH"+self.channel+"_PA_R50_EN_RB"]

    @property
    def PA_BYPASS(self):
        return self.chip["CH"+self.channel+"_PD_RB"]["CH"+self.channel+"_PA_BYPASS_RB"]

    @property
    def PA_PD(self):
        return self.chip["CH"+self.channel+"_PD_RB"]["CH"+self.channel+"_PA_PD_RB"]

    @property
    def MIXB_LOBUFF_PD(self):
        return self.chip["CH"+self.channel+"_PD_RB"]["CH"+self.channel+"_MIXB_LOBUFF_PD_RB"]

    @property
    def MIXA_LOBUFF_PD(self):
        return self.chip["CH"+self.channel+"_PD_RB"]["CH"+self.channel+"_MIXA_LOBUFF_PD_RB"]

    @property
    def LNA_PD(self):
        return self.chip["CH"+self.channel+"_PD_RB"]["CH"+self.channel+"_LNA_PD_RB"]

    @property
    def LNA_ICT_LIN(self):
        return self.chip["CH"+self.channel+"_LNA_CTRL_RB"]["CH"+self.channel+"_LNA_ICT_LIN_RB<4:0>"]

    @property
    def LNA_ICT_MAIN(self):
        return self.chip["CH"+self.channel+"_LNA_CTRL_RB"]["CH"+self.channel+"_LNA_ICT_MAIN_RB<4:0>"]

    @property
    def LNA_CGSCTRL(self):
        return self.chip["CH"+self.channel+"_LNA_CTRL_RB"]["CH"+self.channel+"_LNA_CGSCTRL_RB<1:0>"]

    @property
    def LNA_GCTRL(self):
        return self.chip["CH"+self.channel+"_LNA_CTRL_RB"]["CH"+self.channel+"_LNA_GCTRL_RB<3:0>"]

    @property
    def PA_LIN_LOSS(self):
        return self.chip["CH"+self.channel+"_PA_CTRL_RB"]["CH"+self.channel+"_PA_LIN_LOSS_RB<3:0>"]

    @property
    def PA_MAIN_LOSS(self):
        return self.chip["CH"+self.channel+"_PA_CTRL_RB"]["CH"+self.channel+"_PA_MAIN_LOSS_RB<3:0>"]


