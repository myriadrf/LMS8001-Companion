
class LMS8001_CHANNEL_PA(object):
    
    def __init__(self, chip, channel, cfgNo):
        self.chip = chip
        self.channel = channel
        self.cfgNo = cfgNo

    #
    # Read channel settings
    #

    def __getattr__(self, name):
        channel = self.__dict__["channel"]
        cfgNo = self.__dict__["cfgNo"]
        if name not in ['LIN_LOSS',
                        'MAIN_LOSS']:
            raise ValueError("Invalid field name "+str(name))
        if name=='LIN_LOSS':
            return self.chip['CH'+channel+'_PA_CTRL'+str(cfgNo)]['CH'+channel+'_PA_LIN_LOSS'+str(cfgNo)+'<3:0>']
        if name=='MAIN_LOSS':
            return self.chip['CH'+channel+'_PA_CTRL'+str(cfgNo)]['CH'+channel+'_PA_MAIN_LOSS'+str(cfgNo)+'<3:0>']

    #
    # Write channel setting
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
        if name not in ['LIN_LOSS',
                        'MAIN_LOSS']:
            raise ValueError("Invalid field name "+str(name))
        if name=='LIN_LOSS':
            self.chip['CH'+channel+'_PA_CTRL'+str(cfgNo)]['CH'+channel+'_PA_LIN_LOSS'+str(cfgNo)+'<3:0>'] = value
        if name=='MAIN_LOSS':
            self.chip['CH'+channel+'_PA_CTRL'+str(cfgNo)]['CH'+channel+'_PA_MAIN_LOSS'+str(cfgNo)+'<3:0>'] = value
            

