
class LMS8001_BIAS(object):
    
    def __init__(self, chip):
        self.chip = chip

    #
    # Read bias settings
    #

    def __getattr__(self, name):
        if name not in ['PD_CALIB_COMP',
                        'RP_CALIB_COMP',
                        'RP_CALIB_BIAS',
                        'PD_FRP_BIAS',
                        'PD_F_BIAS',
                        'PD_PTRP_BIAS',
                        'PD_PT_BIAS',
                        'PD_BIAS']:
            raise ValueError("Invalid field name "+str(name))
        if name=='RP_CALIB_BIAS':
            name+='<4:0>'
        return self.chip['BiasConfig'][name]

    #
    # Write bias settings
    #

    def __setattr__(self, name, value):
        if name == "chip":
            self.__dict__["chip"] = value
            return
        if name not in ['PD_CALIB_COMP',
                        'RP_CALIB_COMP',
                        'RP_CALIB_BIAS',
                        'PD_FRP_BIAS',
                        'PD_F_BIAS',
                        'PD_PTRP_BIAS',
                        'PD_PT_BIAS',
                        'PD_BIAS']:
            raise ValueError("Invalid field name "+str(name))
        if name=='RP_CALIB_BIAS':
            name+='<4:0>'
        self.chip['BiasConfig'][name] = value
            

