
class LMS8001_HLMIX_CFG(object):
    
    def __init__(self, chip, channel, cfgNo):
        self.chip = chip
        self.channel = channel
        self.cfgNo = cfgNo

    #
    # Read HLMIX settings
    #

    def __getattr__(self, name):
        channel = self.__dict__["channel"]
        cfgNo = self.__dict__["cfgNo"]
        if name not in ['VGCAS',
                        'ICT_BIAS',
                        'BIAS_PD',
                        'LOBUF_PD',
                        'MIXLOSS']:
            raise ValueError("Invalid field name "+str(name))
        if name=='VGCAS':
            return self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_VGCAS'+str(cfgNo)+'<6:0>']
        if name=='ICT_BIAS':
            return self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_ICT_BIAS'+str(cfgNo)+'<4:0>']
        if name=='BIAS_PD':
            return self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_BIAS_PD'+str(cfgNo)]
        if name=='LOBUF_PD':
            return self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_LOBUF_PD'+str(cfgNo)]
        if name=='MIXLOSS':
            return self.chip['HLMIX'+channel+'_LOSS'+str(cfgNo)]['HLMIX'+channel+'_MIXLOSS'+str(cfgNo)+'<3:0>']
            

    #
    # Write HLMIX setting
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
        if name not in ['VGCAS',
                        'ICT_BIAS',
                        'BIAS_PD',
                        'LOBUF_PD',
                        'MIXLOSS']:
            raise ValueError("Invalid field name "+str(name))
        if name=='VGCAS':
            self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_VGCAS'+str(cfgNo)+'<6:0>'] = value
        if name=='ICT_BIAS':
            self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_ICT_BIAS'+str(cfgNo)+'<4:0>'] = value
        if name=='BIAS_PD':
            self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_BIAS_PD'+str(cfgNo)] = value
        if name=='LOBUF_PD':
            self.chip['HLMIX'+channel+'_CONFIG'+str(cfgNo)]['HLMIX'+channel+'_LOBUF_PD'+str(cfgNo)] = value
        if name=='MIXLOSS':
            self.chip['HLMIX'+channel+'_LOSS'+str(cfgNo)]['HLMIX'+channel+'_MIXLOSS'+str(cfgNo)+'<3:0>'] = value
            

