
class LMS8001_CHANNEL_PD(object):
    
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
        if name not in ['PA_R50_EN',
                        'PA_BYPASS',
                        'PA_PD',
                        'MIXB_LOBUFF_PD',
                        'MIXA_LOBUFF_PD',
                        'LNA_PD']:
            raise ValueError("Invalid field name "+str(name))
        return self.chip['CH'+channel+'_PD'+str(cfgNo)]['CH'+channel+'_'+name+str(cfgNo)]

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
        if name not in ['PA_R50_EN',
                        'PA_BYPASS',
                        'PA_PD',
                        'MIXB_LOBUFF_PD',
                        'MIXA_LOBUFF_PD',
                        'LNA_PD']:
            raise ValueError("Invalid field name "+str(name))
        self.chip['CH'+channel+'_PD'+str(cfgNo)]['CH'+channel+'_'+name+str(cfgNo)] = value
            


