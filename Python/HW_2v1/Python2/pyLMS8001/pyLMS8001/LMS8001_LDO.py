
class LMS8001_LDO(object):
    
    def __init__(self, chip, LDOname):
        self.chip = chip
        self.LDOname = LDOname
        self.__dict__.update({'set_vout':self.set_vout})

    #
    # Read LDO settings
    #

    def __getattr__(self, name):
        LDOname = self.__dict__["LDOname"]
        if name not in ['EN_LOADIMP_LDO',
                        'SPDUP_LDO',
                        'EN_LDO',
                        'RDIV']:
            raise ValueError("Invalid field name "+str(name))
        if name=='RDIV':
            return self.chip[self.LDOname+'_LDO_Config'][name+"_"+LDOname+'<7:0>']
        else:
            return self.chip[self.LDOname+'_LDO_Config'][name+"_"+LDOname]

    #
    # Write LDO settings
    #

    def __setattr__(self, name, value):
        if name == "chip":
            self.__dict__["chip"] = value
            return
        if name == "LDOname":
            self.__dict__["LDOname"] = value
            return
        LDOname = self.__dict__["LDOname"]
        if name not in ['EN_LOADIMP_LDO',
                        'SPDUP_LDO',
                        'EN_LDO',
                        'RDIV',
                        'vout']:
            raise ValueError("Invalid field name "+str(name))
        if name=='vout':
            self.__dict__['set_vout'](value)
        elif name=='RDIV':
            self.chip[self.LDOname+'_LDO_Config'][name+"_"+LDOname+'<7:0>'] = value
        else:
            self.chip[self.LDOname+'_LDO_Config'][name+"_"+LDOname] = value
            

    @property
    def vout(self):
        rdiv = self.RDIV
        chip = self.chip
        LDOofs = chip.LDOofs
        LDOcoef = chip.LDOcoef
        vout = LDOofs + rdiv * LDOcoef
        return vout

    def set_vout(self, value):
        chip = self.chip
        LDOofs = chip.LDOofs
        LDOcoef = chip.LDOcoef
        if value<LDOofs:
            raise ValueError("Output voltage too low")
        elif value>1.8:
            raise ValueError("Output voltage too high")
        rdiv = int((value-LDOofs)/LDOcoef)
        self.RDIV = rdiv
        
        
        

