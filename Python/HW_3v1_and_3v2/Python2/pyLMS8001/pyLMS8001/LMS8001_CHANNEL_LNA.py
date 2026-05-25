
class LMS8001_CHANNEL_LNA(object):
    
    def __init__(self, chip, channel, cfgNo):
        self.chip = chip
        self.channel = channel
        self.cfgNo = cfgNo

    #
    # Read channel PD
    #

    def __getattr__(self, name):
        channel = self.__dict__["channel"]
        cfgNo = self.__dict__["cfgNo"]
        if name not in ['ICT_LIN',
                        'ICT_MAIN',
                        'CGSCTRL',
                        'GCTRL']:
            raise ValueError("Invalid field name "+str(name))
        if name=='ICT_LIN':
            return self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_ICT_LIN'+str(cfgNo)+'<4:0>']
        if name=='ICT_MAIN':
            return self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_ICT_MAIN'+str(cfgNo)+'<4:0>']
        if name=='CGSCTRL':
            return self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_CGSCTRL'+str(cfgNo)+'<1:0>']
        if name=='GCTRL':
            return self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_GCTRL'+str(cfgNo)+'<3:0>']        
        

    #
    # Write channel PD
    #

    def __setattr__(self, name, value):
        if name == "chip":
            self.__dict__["chip"] = value
            return
        if name == "channel":
            self.__dict__["channel"] = value
            return
        if name == "cfgNo":
            self.__dict__["cfgNo"] = value
            return
        channel = self.__dict__["channel"]
        cfgNo = self.__dict__["cfgNo"]
        if name not in ['ICT_LIN',
                        'ICT_MAIN',
                        'CGSCTRL',
                        'GCTRL']:
            raise ValueError("Invalid field name "+str(name))
        if name=='ICT_LIN':
            self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_ICT_LIN'+str(cfgNo)+'<4:0>'] = value
        if name=='ICT_MAIN':
            self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_ICT_MAIN'+str(cfgNo)+'<4:0>'] = value
        if name=='CGSCTRL':
            self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_CGSCTRL'+str(cfgNo)+'<1:0>'] = value
        if name=='GCTRL':
            self.chip['CH'+channel+'_LNA_CTRL'+str(cfgNo)]['CH'+channel+'_LNA_GCTRL'+str(cfgNo)+'<3:0>'] = value
            


