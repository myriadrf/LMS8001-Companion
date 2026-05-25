
from LMS8001_PLL_METHODS import *
from LMS8001_PLL_PROFILE import *

class LMS8001_PLL(object):
    def __init__(self, chip, fRef):
        self.chip = chip
        self.fRef = fRef
        self._freq = 0
        self.PLLmethods = PLL_METHODS(chip, fRef)
        self.PROFILES = []
        # Add PLL profiles
        for i in range(0,8):
            self.PROFILES.append(LMS8001_PLL_PROFILE(chip, i))

        # Auto-Config for XBUF, VREG
        self.autoConfXBUF=True
        self.autoConfVREG=True


    def _readReg(self, reg, field):
        return self.chip[reg][field]
        
    def _writeReg(self, reg, field,val):
        self.chip[reg][field] = val

    #
    # PLL frequency
    #

    @property
    def frequency(self):
        return self._freq
    

    @frequency.setter
    def frequency(self, f):
        """
        Tunes VCO and sets division rations in feedback and feedforward paths to synthesize desired frequency at the output of FF-DIV (input of LO-DIST Network)
        """
        status=self.PLLmethods.configPLL(f, PROFILE=self.ACTIVE_PROFILE, IQ=False, autoConfXBUF=self.autoConfXBUF, autoConfVREG=self.autoConfVREG, SKIP_STEPS=[2,3,4])
        if (status):
            self._freq = f
        else:
            self.chip.log("PLL: Frequency tuning to %.6f MHz FAILED!" %(f/1.0e6))
    #
    # PLL Loop Dynamics
    # 

    def setLoopBW(self, LoopBW=340.0e3, PM=55.0):
        """
        Calculates and sets PFD-CP and Loop Filter parameters to achieve targeted performance
        """
        if (self.PLL_LOCK==1):
            status=self.PLLmethods.configPLL(F_LO=self.frequency, PROFILE=self.ACTIVE_PROFILE, LoopBW=LoopBW, PM=PM, SKIP_STEPS=[1,4])
            if (not status):
                self.chip.log("PLL: Setting LoopBW=%.2f kHz and Ph.Margin=%.2f deg. FAILED!" %(LoopBW/1.0e3, PM))
        else:
            self.chip.log("PLL: PLL is not locked. Before defining the loop dynamics, tune PLL to the desired frequency.")


    #
    # PLL Fast-Lock Mode
    # 

    def setFastLockBWEF(self, BWEF=2.0, FLOCK_N=400):
        """
        Calculates and sets PFD-CP and Loop-Filter parameters to achieve desired performance during fast-lock mode.
        BWEF - Bandwidth Extension Factor - during fast-lock mode compared to normal operation mode
        FLOCK_N - time expressed as number of reference clock cycles during which PLL will operate with fast-lock settings at the beginning of freq. settling process
        """
        if (self.PLL_LOCK==1):
            status=self.PLLmethods.configPLL(F_LO=self.frequency, PROFILE=self.ACTIVE_PROFILE, BWEF=BWEF, FLOCK_N=FLOCK_N, SKIP_STEPS=[1,2,3])
            if (not status):
                self.chip.log("PLL: Setting Fast-Lock Mode Configuration FAILED!")
        else:
            self.chip.log("PLL: PLL is not locked. Before defining the fast-lock mode configurations, tune PLL to the desired frequency.")

    def setFastLockLoopBW(self, LoopBW=500.0e3, PM=55, FLOCK_N=400):
        """
        Calculates and sets PFD-CP and Loop-Filter parameters to achieve desired performance during fast-lock mode.
        LoopBW, PM - 3dB close-loop bandwidth and phase-margin of PLL during fast-lock operation mode
        FLOCK_N - time expressed as number of reference clock cycles during which PLL will operate with fast-lock settings at the beginning of freq. settling process
        """
        if (self.PLL_LOCK==1):
            status=self.PLLmethods.setFLOCK(BWEF=1.0, LoopBW=LoopBW, PM=PM, FLOCK_N=FLOCK_N, METHOD="SMART", FIT_KVCO=True, FLOCK_VCO_SPDUP=1, PROFILE=self.ACTIVE_PROFILE)
            if (not status):
                self.chip.log("PLL: Setting Fast-Lock Mode Configuration FAILED!")
        else:
            self.chip.log("PLL: PLL is not locked. Before defining the fast-lock mode configurations, tune PLL to the desired frequency.")

    #
    # LO Distribution Settings
    # 

    def setLODIST(self, channel, EN=True, EN_FLOCK=False, IQ=True, phase=0):
        """
        More readable way to define various settings for LO channel(s)
        """
        self.PLLmethods.setLODIST(channel=channel, EN=EN, EN_FLOCK=EN_FLOCK, IQ=IQ, phase=phase, PROFILE=self.ACTIVE_PROFILE)

    # EN_VCOBIAS
    @property 
    def EN_VCOBIAS(self):
        """
        Get the value of EN_VCOBIAS
        """
        return self._readReg('PLL_VREG', 'EN_VCOBIAS')

    @EN_VCOBIAS.setter
    def EN_VCOBIAS(self, value):
        """
        Set the value of EN_VCOBIAS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_VREG', 'EN_VCOBIAS', value)

    # BYP_VCOREG
    @property 
    def BYP_VCOREG(self):
        """
        Get the value of BYP_VCOREG
        """
        return self._readReg('PLL_VREG', 'BYP_VCOREG')

    @BYP_VCOREG.setter
    def BYP_VCOREG(self, value):
        """
        Set the value of BYP_VCOREG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_VREG', 'BYP_VCOREG', value)

    # CURLIM_VCOREG
    @property 
    def CURLIM_VCOREG(self):
        """
        Get the value of CURLIM_VCOREG
        """
        return self._readReg('PLL_VREG', 'CURLIM_VCOREG')

    @CURLIM_VCOREG.setter
    def CURLIM_VCOREG(self, value):
        """
        Set the value of CURLIM_VCOREG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_VREG', 'CURLIM_VCOREG', value)

    # SPDUP_VCOREG
    @property 
    def SPDUP_VCOREG(self):
        """
        Get the value of SPDUP_VCOREG
        """
        return self._readReg('PLL_VREG', 'SPDUP_VCOREG')

    @SPDUP_VCOREG.setter
    def SPDUP_VCOREG(self, value):
        """
        Set the value of SPDUP_VCOREG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_VREG', 'SPDUP_VCOREG', value)

    # VDIV_VCOREG<7:0>
    @property 
    def VDIV_VCOREG(self):
        """
        Get the value of VDIV_VCOREG<7:0>
        """
        return self._readReg('PLL_VREG', 'VDIV_VCOREG<7:0>')

    @VDIV_VCOREG.setter
    def VDIV_VCOREG(self, value):
        """
        Set the value of VDIV_VCOREG<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_VREG', 'VDIV_VCOREG<7:0>', value)

    # PLL_XBUF_SLFBEN
    @property 
    def PLL_XBUF_SLFBEN(self):
        """
        Get the value of PLL_XBUF_SLFBEN
        """
        return self._readReg('PLL_CFG_XBUF', 'PLL_XBUF_SLFBEN')

    @PLL_XBUF_SLFBEN.setter
    def PLL_XBUF_SLFBEN(self, value):
        """
        Set the value of PLL_XBUF_SLFBEN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_XBUF', 'PLL_XBUF_SLFBEN', value)

    # PLL_XBUF_BYPEN
    @property 
    def PLL_XBUF_BYPEN(self):
        """
        Get the value of PLL_XBUF_BYPEN
        """
        return self._readReg('PLL_CFG_XBUF', 'PLL_XBUF_BYPEN')

    @PLL_XBUF_BYPEN.setter
    def PLL_XBUF_BYPEN(self, value):
        """
        Set the value of PLL_XBUF_BYPEN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_XBUF', 'PLL_XBUF_BYPEN', value)

    # PLL_XBUF_EN
    @property 
    def PLL_XBUF_EN(self):
        """
        Get the value of PLL_XBUF_EN
        """
        return self._readReg('PLL_CFG_XBUF', 'PLL_XBUF_EN')

    @PLL_XBUF_EN.setter
    def PLL_XBUF_EN(self, value):
        """
        Set the value of PLL_XBUF_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_XBUF', 'PLL_XBUF_EN', value)

    # FCAL_START
    @property 
    def FCAL_START(self):
        """
        Get the value of FCAL_START
        """
        return self._readReg('PLL_CAL_AUTO0', 'FCAL_START')

    @FCAL_START.setter
    def FCAL_START(self, value):
        """
        Set the value of FCAL_START
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CAL_AUTO0', 'FCAL_START', value)

    # VCO_SEL_FINAL_VAL
    @property 
    def VCO_SEL_FINAL_VAL(self):
        """
        Get the value of VCO_SEL_FINAL_VAL
        """
        return self._readReg('PLL_CAL_AUTO0', 'VCO_SEL_FINAL_VAL')

    # VCO_SEL_FINAL<1:0>
    @property 
    def VCO_SEL_FINAL(self):
        """
        Get the value of VCO_SEL_FINAL<1:0>
        """
        return self._readReg('PLL_CAL_AUTO0', 'VCO_SEL_FINAL<1:0>')

    # FREQ_FINAL_VAL
    @property 
    def FREQ_FINAL_VAL(self):
        """
        Get the value of FREQ_FINAL_VAL
        """
        return self._readReg('PLL_CAL_AUTO0', 'FREQ_FINAL_VAL')

    # FREQ_FINAL<7:0>
    @property 
    def FREQ_FINAL(self):
        """
        Get the value of FREQ_FINAL<7:0>
        """
        return self._readReg('PLL_CAL_AUTO0', 'FREQ_FINAL<7:0>')


    # VCO_SEL_FORCE
    @property 
    def VCO_SEL_FORCE(self):
        """
        Get the value of VCO_SEL_FORCE
        """
        return self._readReg('PLL_CAL_AUTO1', 'VCO_SEL_FORCE')

    @VCO_SEL_FORCE.setter
    def VCO_SEL_FORCE(self, value):
        """
        Set the value of VCO_SEL_FORCE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CAL_AUTO1', 'VCO_SEL_FORCE', value)

    # VCO_SEL_INIT<1:0>
    @property 
    def VCO_SEL_INIT(self):
        """
        Get the value of VCO_SEL_INIT<1:0>
        """
        return self._readReg('PLL_CAL_AUTO1', 'VCO_SEL_INIT<1:0>')

    @VCO_SEL_INIT.setter
    def VCO_SEL_INIT(self, value):
        """
        Set the value of VCO_SEL_INIT<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_CAL_AUTO1', 'VCO_SEL_INIT<1:0>', value)

    # FREQ_INIT_POS<2:0>
    @property 
    def FREQ_INIT_POS(self):
        """
        Get the value of FREQ_INIT_POS<2:0>
        """
        return self._readReg('PLL_CAL_AUTO1', 'FREQ_INIT_POS<2:0>')

    @FREQ_INIT_POS.setter
    def FREQ_INIT_POS(self, value):
        """
        Set the value of FREQ_INIT_POS<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('PLL_CAL_AUTO1', 'FREQ_INIT_POS<2:0>', value)

    # FREQ_INIT<7:0>
    @property 
    def FREQ_INIT(self):
        """
        Get the value of FREQ_INIT<7:0>
        """
        return self._readReg('PLL_CAL_AUTO1', 'FREQ_INIT<7:0>')

    @FREQ_INIT.setter
    def FREQ_INIT(self, value):
        """
        Set the value of FREQ_INIT<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_CAL_AUTO1', 'FREQ_INIT<7:0>', value)

    # FREQ_SETTLING_N<3:0>
    @property 
    def FREQ_SETTLING_N(self):
        """
        Get the value of FREQ_SETTLING_N<3:0>
        """
        return self._readReg('PLL_CAL_AUTO2', 'FREQ_SETTLING_N<3:0>')

    @FREQ_SETTLING_N.setter
    def FREQ_SETTLING_N(self, value):
        """
        Set the value of FREQ_SETTLING_N<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_CAL_AUTO2', 'FREQ_SETTLING_N<3:0>', value)

    # VTUNE_WAIT_N<7:0>
    @property 
    def VTUNE_WAIT_N(self):
        """
        Get the value of VTUNE_WAIT_N<7:0>
        """
        return self._readReg('PLL_CAL_AUTO2', 'VTUNE_WAIT_N<7:0>')

    @VTUNE_WAIT_N.setter
    def VTUNE_WAIT_N(self, value):
        """
        Set the value of VTUNE_WAIT_N<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_CAL_AUTO2', 'VTUNE_WAIT_N<7:0>', value)

    # VCO_SEL_FREQ_MAX<7:0>
    @property 
    def VCO_SEL_FREQ_MAX(self):
        """
        Get the value of VCO_SEL_FREQ_MAX<7:0>
        """
        return self._readReg('PLL_CAL_AUTO3', 'VCO_SEL_FREQ_MAX<7:0>')

    @VCO_SEL_FREQ_MAX.setter
    def VCO_SEL_FREQ_MAX(self, value):
        """
        Set the value of VCO_SEL_FREQ_MAX<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_CAL_AUTO3', 'VCO_SEL_FREQ_MAX<7:0>', value)

    # VCO_SEL_FREQ_MIN<7:0>
    @property 
    def VCO_SEL_FREQ_MIN(self):
        """
        Get the value of VCO_SEL_FREQ_MIN<7:0>
        """
        return self._readReg('PLL_CAL_AUTO3', 'VCO_SEL_FREQ_MIN<7:0>')

    @VCO_SEL_FREQ_MIN.setter
    def VCO_SEL_FREQ_MIN(self, value):
        """
        Set the value of VCO_SEL_FREQ_MIN<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_CAL_AUTO3', 'VCO_SEL_FREQ_MIN<7:0>', value)

    # VCO_FREQ_MAN<7:0>
    @property 
    def VCO_FREQ_MAN(self):
        """
        Get the value of VCO_FREQ_MAN<7:0>
        """
        return self._readReg('PLL_CAL_MAN', 'VCO_FREQ_MAN<7:0>')

    @VCO_FREQ_MAN.setter
    def VCO_FREQ_MAN(self, value):
        """
        Set the value of VCO_FREQ_MAN<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_CAL_MAN', 'VCO_FREQ_MAN<7:0>', value)

    # VCO_SEL_MAN<1:0>
    @property 
    def VCO_SEL_MAN(self):
        """
        Get the value of VCO_SEL_MAN<1:0>
        """
        return self._readReg('PLL_CAL_MAN', 'VCO_SEL_MAN<1:0>')

    @VCO_SEL_MAN.setter
    def VCO_SEL_MAN(self, value):
        """
        Set the value of VCO_SEL_MAN<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_CAL_MAN', 'VCO_SEL_MAN<1:0>', value)

    # FREQ_HIGH
    @property 
    def FREQ_HIGH(self):
        """
        Get the value of FREQ_HIGH
        """
        return self._readReg('PLL_CAL_MAN', 'FREQ_HIGH')

    # FREQ_EQUAL
    @property 
    def FREQ_EQUAL(self):
        """
        Get the value of FREQ_EQUAL
        """
        return self._readReg('PLL_CAL_MAN', 'FREQ_EQUAL')

    # FREQ_LOW
    @property 
    def FREQ_LOW(self):
        """
        Get the value of FREQ_LOW
        """
        return self._readReg('PLL_CAL_MAN', 'FREQ_LOW')

    # CTUNE_STEP_DONE
    @property 
    def CTUNE_STEP_DONE(self):
        """
        Get the value of CTUNE_STEP_DONE
        """
        return self._readReg('PLL_CAL_MAN', 'CTUNE_STEP_DONE')

    # CTUNE_START
    @property 
    def CTUNE_START(self):
        """
        Get the value of CTUNE_START
        """
        return self._readReg('PLL_CAL_MAN', 'CTUNE_START')

    @CTUNE_START.setter
    def CTUNE_START(self, value):
        """
        Set the value of CTUNE_START
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CAL_MAN', 'CTUNE_START', value)

    # CTUNE_EN
    @property 
    def CTUNE_EN(self):
        """
        Get the value of CTUNE_EN
        """
        return self._readReg('PLL_CAL_MAN', 'CTUNE_EN')

    @CTUNE_EN.setter
    def CTUNE_EN(self, value):
        """
        Set the value of CTUNE_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CAL_MAN', 'CTUNE_EN', value)

    # PLL_CFG_SEL0_INTERNAL
    @property 
    def PLL_CFG_SEL0_INTERNAL(self):
        """
        Get the value of PLL_CFG_SEL0_INTERNAL
        """
        return self._readReg('PLL_CFG_SEL0', 'PLL_CFG_SEL0_INTERNAL')

    @PLL_CFG_SEL0_INTERNAL.setter
    def PLL_CFG_SEL0_INTERNAL(self, value):
        """
        Set the value of PLL_CFG_SEL0_INTERNAL
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_SEL0', 'PLL_CFG_SEL0_INTERNAL', value)

    # PLL_CFG_SEL0_INVERT
    @property 
    def PLL_CFG_SEL0_INVERT(self):
        """
        Get the value of PLL_CFG_SEL0_INVERT
        """
        return self._readReg('PLL_CFG_SEL0', 'PLL_CFG_SEL0_INVERT')

    @PLL_CFG_SEL0_INVERT.setter
    def PLL_CFG_SEL0_INVERT(self, value):
        """
        Set the value of PLL_CFG_SEL0_INVERT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_SEL0', 'PLL_CFG_SEL0_INVERT', value)

    # PLL_CFG_SEL0_MASK<8:0>
    @property 
    def PLL_CFG_SEL0_MASK(self):
        """
        Get the value of PLL_CFG_SEL0_MASK<8:0>
        """
        return self._readReg('PLL_CFG_SEL0', 'PLL_CFG_SEL0_MASK<8:0>')

    @PLL_CFG_SEL0_MASK.setter
    def PLL_CFG_SEL0_MASK(self, value):
        """
        Set the value of PLL_CFG_SEL0_MASK<8:0>
        """
        if not(0<= value <=511):
            raise ValueError("Value must be [0..511]")
        self._writeReg('PLL_CFG_SEL0', 'PLL_CFG_SEL0_MASK<8:0>', value)

    # PLL_CFG_SEL1_INTERNAL
    @property 
    def PLL_CFG_SEL1_INTERNAL(self):
        """
        Get the value of PLL_CFG_SEL1_INTERNAL
        """
        return self._readReg('PLL_CFG_SEL1', 'PLL_CFG_SEL1_INTERNAL')

    @PLL_CFG_SEL1_INTERNAL.setter
    def PLL_CFG_SEL1_INTERNAL(self, value):
        """
        Set the value of PLL_CFG_SEL1_INTERNAL
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_SEL1', 'PLL_CFG_SEL1_INTERNAL', value)

    # PLL_CFG_SEL1_INVERT
    @property 
    def PLL_CFG_SEL1_INVERT(self):
        """
        Get the value of PLL_CFG_SEL1_INVERT
        """
        return self._readReg('PLL_CFG_SEL1', 'PLL_CFG_SEL1_INVERT')

    @PLL_CFG_SEL1_INVERT.setter
    def PLL_CFG_SEL1_INVERT(self, value):
        """
        Set the value of PLL_CFG_SEL1_INVERT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_SEL1', 'PLL_CFG_SEL1_INVERT', value)

    # PLL_CFG_SEL1_MASK<8:0>
    @property 
    def PLL_CFG_SEL1_MASK(self):
        """
        Get the value of PLL_CFG_SEL1_MASK<8:0>
        """
        return self._readReg('PLL_CFG_SEL1', 'PLL_CFG_SEL1_MASK<8:0>')

    @PLL_CFG_SEL1_MASK.setter
    def PLL_CFG_SEL1_MASK(self, value):
        """
        Set the value of PLL_CFG_SEL1_MASK<8:0>
        """
        if not(0<= value <=511):
            raise ValueError("Value must be [0..511]")
        self._writeReg('PLL_CFG_SEL1', 'PLL_CFG_SEL1_MASK<8:0>', value)

    # PLL_CFG_SEL2_INTERNAL
    @property 
    def PLL_CFG_SEL2_INTERNAL(self):
        """
        Get the value of PLL_CFG_SEL2_INTERNAL
        """
        return self._readReg('PLL_CFG_SEL2', 'PLL_CFG_SEL2_INTERNAL')

    @PLL_CFG_SEL2_INTERNAL.setter
    def PLL_CFG_SEL2_INTERNAL(self, value):
        """
        Set the value of PLL_CFG_SEL2_INTERNAL
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_SEL2', 'PLL_CFG_SEL2_INTERNAL', value)

    # PLL_CFG_SEL2_INVERT
    @property 
    def PLL_CFG_SEL2_INVERT(self):
        """
        Get the value of PLL_CFG_SEL2_INVERT
        """
        return self._readReg('PLL_CFG_SEL2', 'PLL_CFG_SEL2_INVERT')

    @PLL_CFG_SEL2_INVERT.setter
    def PLL_CFG_SEL2_INVERT(self, value):
        """
        Set the value of PLL_CFG_SEL2_INVERT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG_SEL2', 'PLL_CFG_SEL2_INVERT', value)

    # PLL_CFG_SEL2_MASK<8:0>
    @property 
    def PLL_CFG_SEL2_MASK(self):
        """
        Get the value of PLL_CFG_SEL2_MASK<8:0>
        """
        return self._readReg('PLL_CFG_SEL2', 'PLL_CFG_SEL2_MASK<8:0>')

    @PLL_CFG_SEL2_MASK.setter
    def PLL_CFG_SEL2_MASK(self, value):
        """
        Set the value of PLL_CFG_SEL2_MASK<8:0>
        """
        if not(0<= value <=511):
            raise ValueError("Value must be [0..511]")
        self._writeReg('PLL_CFG_SEL2', 'PLL_CFG_SEL2_MASK<8:0>', value)

    # PLL_RSTN
    @property 
    def PLL_RSTN(self):
        """
        Get the value of PLL_RSTN
        """
        return self._readReg('PLL_CFG', 'PLL_RSTN')

    @PLL_RSTN.setter
    def PLL_RSTN(self, value):
        """
        Set the value of PLL_RSTN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG', 'PLL_RSTN', value)

    # CTUNE_RES<1:0>
    @property 
    def CTUNE_RES(self):
        """
        Get the value of CTUNE_RES<1:0>
        """
        return self._readReg('PLL_CFG', 'CTUNE_RES<1:0>')

    @CTUNE_RES.setter
    def CTUNE_RES(self, value):
        """
        Set the value of CTUNE_RES<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_CFG', 'CTUNE_RES<1:0>', value)

    # PLL_CALIBRATION_MODE
    @property 
    def PLL_CALIBRATION_MODE(self):
        """
        Get the value of PLL_CALIBRATION_MODE
        """
        return self._readReg('PLL_CFG', 'PLL_CALIBRATION_MODE')

    @PLL_CALIBRATION_MODE.setter
    def PLL_CALIBRATION_MODE(self, value):
        """
        Set the value of PLL_CALIBRATION_MODE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG', 'PLL_CALIBRATION_MODE', value)

    # PLL_CALIBRATION_EN
    @property 
    def PLL_CALIBRATION_EN(self):
        """
        Get the value of PLL_CALIBRATION_EN
        """
        return self._readReg('PLL_CFG', 'PLL_CALIBRATION_EN')

    @PLL_CALIBRATION_EN.setter
    def PLL_CALIBRATION_EN(self, value):
        """
        Set the value of PLL_CALIBRATION_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG', 'PLL_CALIBRATION_EN', value)

    # PLL_FLOCK_INTERNAL
    @property 
    def PLL_FLOCK_INTERNAL(self):
        """
        Get the value of PLL_FLOCK_INTERNAL
        """
        return self._readReg('PLL_CFG', 'PLL_FLOCK_INTERNAL')

    @PLL_FLOCK_INTERNAL.setter
    def PLL_FLOCK_INTERNAL(self, value):
        """
        Set the value of PLL_FLOCK_INTERNAL
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG', 'PLL_FLOCK_INTERNAL', value)

    # PLL_FLOCK_INTVAL
    @property 
    def PLL_FLOCK_INTVAL(self):
        """
        Get the value of PLL_FLOCK_INTVAL
        """
        return self._readReg('PLL_CFG', 'PLL_FLOCK_INTVAL')

    @PLL_FLOCK_INTVAL.setter
    def PLL_FLOCK_INTVAL(self, value):
        """
        Set the value of PLL_FLOCK_INTVAL
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CFG', 'PLL_FLOCK_INTVAL', value)

    # PLL_CFG_INT_SEL<2:0>
    @property 
    def PLL_CFG_INT_SEL(self):
        """
        Get the value of PLL_CFG_INT_SEL<2:0>
        """
        return self._readReg('PLL_CFG', 'PLL_CFG_INT_SEL<2:0>')

    @PLL_CFG_INT_SEL.setter
    def PLL_CFG_INT_SEL(self, value):
        """
        Set the value of PLL_CFG_INT_SEL<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('PLL_CFG', 'PLL_CFG_INT_SEL<2:0>', value)

    # VTUNE_HIGH
    @property 
    def VTUNE_HIGH(self):
        """
        Get the value of VTUNE_HIGH
        """
        return self._readReg('PLL_CFG_STATUS', 'VTUNE_HIGH')

    # VTUNE_LOW
    @property 
    def VTUNE_LOW(self):
        """
        Get the value of VTUNE_LOW
        """
        return self._readReg('PLL_CFG_STATUS', 'VTUNE_LOW')


    # PLL_LOCK
    @property 
    def PLL_LOCK(self):
        """
        Get the value of PLL_LOCK
        """
        return self._readReg('PLL_CFG_STATUS', 'PLL_LOCK')


    # SEL_BIAS_CORE
    @property 
    def SEL_BIAS_CORE(self):
        """
        Get the value of SEL_BIAS_CORE
        """
        return self._readReg('PLL_LODIST_CFG1', 'SEL_BIAS_CORE')

    @SEL_BIAS_CORE.setter
    def SEL_BIAS_CORE(self, value):
        """
        Set the value of SEL_BIAS_CORE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_LODIST_CFG1', 'SEL_BIAS_CORE', value)

    # PLL_LODIST_ICT_CORE<4:0>
    @property 
    def PLL_LODIST_ICT_CORE(self):
        """
        Get the value of PLL_LODIST_ICT_CORE<4:0>
        """
        return self._readReg('PLL_LODIST_CFG1', 'PLL_LODIST_ICT_CORE<4:0>')

    @PLL_LODIST_ICT_CORE.setter
    def PLL_LODIST_ICT_CORE(self, value):
        """
        Set the value of PLL_LODIST_ICT_CORE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('PLL_LODIST_CFG1', 'PLL_LODIST_ICT_CORE<4:0>', value)

    # PLL_LODIST_ICT_BUF<4:0>
    @property 
    def PLL_LODIST_ICT_BUF(self):
        """
        Get the value of PLL_LODIST_ICT_BUF<4:0>
        """
        return self._readReg('PLL_LODIST_CFG1', 'PLL_LODIST_ICT_BUF<4:0>')

    @PLL_LODIST_ICT_BUF.setter
    def PLL_LODIST_ICT_BUF(self, value):
        """
        Set the value of PLL_LODIST_ICT_BUF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('PLL_LODIST_CFG1', 'PLL_LODIST_ICT_BUF<4:0>', value)

    # PLL_ICT_OUT3<1:0>
    @property 
    def PLL_ICT_OUT3(self):
        """
        Get the value of PLL_ICT_OUT3<1:0>
        """
        return self._readReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT3<1:0>')

    @PLL_ICT_OUT3.setter
    def PLL_ICT_OUT3(self, value):
        """
        Set the value of PLL_ICT_OUT3<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT3<1:0>', value)

    # PLL_ICT_OUT2<1:0>
    @property 
    def PLL_ICT_OUT2(self):
        """
        Get the value of PLL_ICT_OUT2<1:0>
        """
        return self._readReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT2<1:0>')

    @PLL_ICT_OUT2.setter
    def PLL_ICT_OUT2(self, value):
        """
        Set the value of PLL_ICT_OUT2<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT2<1:0>', value)

    # PLL_ICT_OUT1<1:0>
    @property 
    def PLL_ICT_OUT1(self):
        """
        Get the value of PLL_ICT_OUT1<1:0>
        """
        return self._readReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT1<1:0>')

    @PLL_ICT_OUT1.setter
    def PLL_ICT_OUT1(self, value):
        """
        Set the value of PLL_ICT_OUT1<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT1<1:0>', value)

    # PLL_ICT_OUT0<1:0>
    @property 
    def PLL_ICT_OUT0(self):
        """
        Get the value of PLL_ICT_OUT0<1:0>
        """
        return self._readReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT0<1:0>')

    @PLL_ICT_OUT0.setter
    def PLL_ICT_OUT0(self, value):
        """
        Set the value of PLL_ICT_OUT0<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_LODIST_CFG2', 'PLL_ICT_OUT0<1:0>', value)

    # BSIGL<6:0>
    @property 
    def BSIGL(self):
        """
        Get the value of BSIGL<6:0>
        """
        return self._readReg('PLL_SDM_BIST1', 'BSIGL<6:0>')

    # BSTATE
    @property 
    def BSTATE(self):
        """
        Get the value of BSTATE
        """
        return self._readReg('PLL_SDM_BIST1', 'BSTATE')

    # EN_SDM_TSTO
    @property 
    def EN_SDM_TSTO(self):
        """
        Get the value of EN_SDM_TSTO
        """
        return self._readReg('PLL_SDM_BIST1', 'EN_SDM_TSTO')

    @EN_SDM_TSTO.setter
    def EN_SDM_TSTO(self, value):
        """
        Set the value of EN_SDM_TSTO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_BIST1', 'EN_SDM_TSTO', value)

    # BEN
    @property 
    def BEN(self):
        """
        Get the value of BEN
        """
        return self._readReg('PLL_SDM_BIST1', 'BEN')

    @BEN.setter
    def BEN(self, value):
        """
        Set the value of BEN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_BIST1', 'BEN', value)

    # BSTART
    @property 
    def BSTART(self):
        """
        Get the value of BSTART
        """
        return self._readReg('PLL_SDM_BIST1', 'BSTART')

    @BSTART.setter
    def BSTART(self, value):
        """
        Set the value of BSTART
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_BIST1', 'BSTART', value)

    # BSIGH
    @property 
    def BSIGH(self):
        """
        Get the value of BSIGH
        """
        return self._readReg('PLL_SDM_BIST2', 'BSIGH')


    # Active PLL_PROFILE
    @property 
    def ACTIVE_PROFILE(self):
        """
        Get the value of active PLL Profile configuration
        """
        # Check first if the control of active PLL profile is completely internal
        pll_cfg_sel0=self.chip.getRegisterByName('PLL_CFG_SEL0')
        pll_cfg_sel1=self.chip.getRegisterByName('PLL_CFG_SEL1')
        pll_cfg_sel2=self.chip.getRegisterByName('PLL_CFG_SEL2')
        if (pll_cfg_sel0["PLL_CFG_SEL0_INTERNAL"]==1 and pll_cfg_sel1["PLL_CFG_SEL1_INTERNAL"]==1 and pll_cfg_sel2["PLL_CFG_SEL2_INTERNAL"]==1):
            INT_SEL=self.PLL_CFG_INT_SEL
            return INT_SEL ^ (4*pll_cfg_sel2["PLL_CFG_SEL2_INVERT"]+2*pll_cfg_sel1["PLL_CFG_SEL1_INVERT"]+pll_cfg_sel0["PLL_CFG_SEL0_INVERT"])
        else:
            # if it's not internal
            # this takes longer time to getactive PLL profile
            return self.chip.evalMUXSEL("PLL_CFG", nBits=3)

    @ACTIVE_PROFILE.setter
    def ACTIVE_PROFILE(self, value):
        if (self.PLL_CFG_SEL0_INTERNAL==1 and self.PLL_CFG_SEL1_INTERNAL==1 and self.PLL_CFG_SEL2_INTERNAL==1):
            self.PLL_CFG_INT_SEL=value
            return True
        else:
            self.chip.log("PLL Profile Selection controled by GPIO inputs. Failed to change ACTIVE_PLL Profile!!!")
            self.chip.log(" ")
            self.info_PLL_SEL()

    
    def infoVREGConfig(self, printInfo=True):
        """ Get info about VCO_VREG configuration."""
        nChars = int(80)
        nChars_field=int(16)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("VCO_VREG configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("EN_VCOBIAS", nChars_field-2)+"|"+self.chip.fixLen("BYP_VCOREG", nChars_field-1)+"|"+self.chip.fixLen("CURLIM_VCOREG", nChars_field-1)+"|"+self.chip.fixLen("SPDUP_VCOREG", nChars_field-1)+"|"+self.chip.fixLen("VDIV_VCOREG", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("%d" %(self.EN_VCOBIAS), nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.BYP_VCOREG), nChars_field-1)+"|"+self.chip.fixLen("%d" %(self.CURLIM_VCOREG), nChars_field-1)+"|"+self.chip.fixLen("%d" %(self.SPDUP_VCOREG), nChars_field-1)+"|"+self.chip.fixLen("%d" %(self.VDIV_VCOREG), nChars_field-1)+"|\n"
        res +="|"+self.chip.fixLen("Enabled" if (self.EN_VCOBIAS) else "Powered down", nChars_field-2)+"|"+self.chip.fixLen("LDO Active" if (self.BYP_VCOREG==0) else "LDO bypassed", nChars_field-1)+"|"+self.chip.fixLen("Curr.Limir ON" if (self.CURLIM_VCOREG) else "Curr.Limir OFF", nChars_field-1)+"|"+self.chip.fixLen("Speed-Up ON" if (self.SPDUP_VCOREG) else "Speed-Up OFF", nChars_field-1)+"|"+self.chip.fixLen("VOUT=%.3fV" %(1.8*(257-self.VDIV_VCOREG)/(265-self.VDIV_VCOREG)), nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoXBUFConfig(self, printInfo=True):
        """ Get info about PLL_CFG_XBUF configuration."""
        nChars = int(60)
        nChars_field=int(20)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("PLL_XBUF configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("PLL_XBUF_SLFBEN", nChars_field-2)+"|"+self.chip.fixLen("PLL_XBUF_BYPEN", nChars_field-1)+"|"+self.chip.fixLen("PLL_XBUF_EN", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("%d" %(self.PLL_XBUF_SLFBEN), nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_XBUF_BYPEN), nChars_field-1)+"|"+self.chip.fixLen("%d" %(self.PLL_XBUF_EN), nChars_field-1)+"|\n"
        res +="|"+self.chip.fixLen("Self-Bias Enabled" if (self.PLL_XBUF_SLFBEN) else "Self-Bias Disabled", nChars_field-2)+"|"+self.chip.fixLen("Bypass Active" if (self.PLL_XBUF_BYPEN) else "Bypass not active", nChars_field-1)+"|"+self.chip.fixLen("Enabled" if (self.PLL_XBUF_EN) else "Powered down", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoLOCK(self, printInfo=True):
        """ Get info about PLL Lock status."""

        VTUNE_HIGH=self.VTUNE_HIGH
        VTUNE_LOW=self.VTUNE_LOW
        PLL_LOCK=self.PLL_LOCK

        nChars = int(66)
        nChars_field=int(22)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("PLL Lock Status", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("VTUNE_HIGH", nChars_field-2)+"|"+self.chip.fixLen("VTUNE_LOW", nChars_field-1)+"|"+self.chip.fixLen("PLL_LOCK", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("%d" %(VTUNE_HIGH), nChars_field-2)+"|"+self.chip.fixLen("%d" %(VTUNE_LOW), nChars_field-1)+"|"+self.chip.fixLen("%d" %(PLL_LOCK), nChars_field-1)+"|\n"

        if (VTUNE_HIGH and not VTUNE_LOW):
             VTUNE_TXT="VTUNE Too High"
        elif (VTUNE_LOW and not VTUNE_HIGH):
             VTUNE_TXT="VTUNE Too Low"
        elif (not VTUNE_HIGH and not VTUNE_LOW):
            VTUNE_TXT="VTUNE In Normal Range"
        else:
            VTUNE_TXT="PLL Reset Active or VTUNE Monitor Disabled"       

        res +="|"+self.chip.fixLen("%s" %(VTUNE_TXT), 2*nChars_field-2)+"|"+self.chip.fixLen("PLL Locked" if (PLL_LOCK) else "PLL Not Locked", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def info_PLL_SEL(self, printInfo=True):
        """ Get info about PLL Profile Selection Logic configuration."""

        gpioInReg = self.chip.getRegisterByName("GPIOInData")
        GPIO_IN = gpioInReg["GPIO_IN<8:0>"]
        
        GPIO_IN_bin='0'*(9-len(bin(GPIO_IN)[2:]))+bin(GPIO_IN)[2:]

        SEL0_INTERNAL=self.PLL_CFG_SEL0_INTERNAL
        SEL1_INTERNAL=self.PLL_CFG_SEL1_INTERNAL
        SEL2_INTERNAL=self.PLL_CFG_SEL2_INTERNAL
        
        SEL0_INVERT=self.PLL_CFG_SEL0_INVERT
        SEL1_INVERT=self.PLL_CFG_SEL1_INVERT
        SEL2_INVERT=self.PLL_CFG_SEL2_INVERT

        SEL0_MASK=self.PLL_CFG_SEL0_MASK
        SEL1_MASK=self.PLL_CFG_SEL1_MASK
        SEL2_MASK=self.PLL_CFG_SEL2_MASK
        SEL0_MASK_bin='0'*(9-len(bin(SEL0_MASK)[2:]))+bin(SEL0_MASK)[2:]
        SEL1_MASK_bin='0'*(9-len(bin(SEL1_MASK)[2:]))+bin(SEL1_MASK)[2:]
        SEL2_MASK_bin='0'*(9-len(bin(SEL2_MASK)[2:]))+bin(SEL2_MASK)[2:]

        INT_SEL=self.PLL_CFG_INT_SEL
        
        ACTIVE_PROFILE=self.ACTIVE_PROFILE

        nChars = int(100)
        nChars_field=int(20)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("PLL Profile Multiplexer logic configuration, PLL_CFG and PLL_CFG_SEL0,1,2 Registers", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("INT_SEL<2:0>", nChars_field-2)+"|"+self.chip.fixLen("SEL0_INTERNAL", nChars_field-1)+"|"+self.chip.fixLen("SEL0_INVERT", nChars_field-1)+"|"+self.chip.fixLen("SEL0_MASK", nChars_field-1)+"|"+self.chip.fixLen("SEL1_INTERNAL", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        res +="|"+self.chip.fixLen("%d" %(INT_SEL), nChars_field-2)+"|"+self.chip.fixLen("%d" %(SEL0_INTERNAL), nChars_field-1)+"|"+self.chip.fixLen("%d" %(SEL0_INVERT), nChars_field-1)+"|"+self.chip.fixLen("0b%s(%d)" %(SEL0_MASK_bin, SEL0_MASK), nChars_field-1)+"|"+self.chip.fixLen("%d" %(SEL1_INTERNAL), nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"

        res+="|" + self.chip.fixLen("SEL1_INVERT", nChars_field-2)+"|"+self.chip.fixLen("SEL1_MASK", nChars_field-1)+"|"+self.chip.fixLen("SEL2_INTERNAL", nChars_field-1)+"|"+self.chip.fixLen("SEL2_INVERT", nChars_field-1)+"|"+self.chip.fixLen("SEL2_MASK", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        res+="|"+self.chip.fixLen("%d" %(SEL1_INVERT), nChars_field-2)+"|"+self.chip.fixLen("0b%s(%d)" %(SEL1_MASK_bin, SEL1_MASK), nChars_field-1)+"|"+self.chip.fixLen("%d" %(SEL2_INTERNAL), nChars_field-1)+"|"+self.chip.fixLen("%d" %(SEL2_INVERT), nChars_field-1)+"|"+self.chip.fixLen("0b%s(%d)" %(SEL2_MASK_bin, SEL2_MASK), nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        if (SEL0_INTERNAL==1 and SEL1_INTERNAL==1 and SEL2_INTERNAL==1):
            res +="|" + self.chip.fixLen("Active PLL Profile IS completely determined by internal SPI values PLL_CFG_INT_SEL<2:0>", nChars-2) +"|\n"
        else:
            res +="|" + self.chip.fixLen("Active PLL Profile is NOT completely determined by internal SPI values.", nChars-2) +"|\n"
            res +="|" + self.chip.fixLen("Bits with SEL0,1,2_INTERNAL=0 are controled via GPIO inputs.", nChars-2) +"|\n"
            res +="|" + self.chip.fixLen("GPIO_IN=0b%s(%d)." %(GPIO_IN_bin, GPIO_IN), nChars-2) +"|\n"
            res +="|" + self.chip.fixLen("Check documentation for more info.", nChars-2) +"|\n"
        res += "-"*nChars+"\n"
        res +="|" + self.chip.fixLen("Active PLL Profile=%d" %(ACTIVE_PROFILE), nChars-2) +"|\n" 
        res += "-"*nChars+"\n"
        if printInfo:
            self.chip.log(res)
        else:
            return res


    def infoConfig(self, printInfo=True):
        nChars = int(110)
        if (printInfo):
            self.chip.log(self.chip.fixLen("PLL Configuration, Active Profile No. %d" %(self.ACTIVE_PROFILE), nChars))
            self.chip.log("*"*nChars)
            self.infoXBUFConfig(printInfo=printInfo)
            self.infoVREGConfig(printInfo=printInfo)
            self.chip.log("*"*nChars)
            self.PROFILES[self.ACTIVE_PROFILE].infoConfig(printInfo=printInfo)
            self.infoLOCK(printInfo=printInfo)
            self.chip.log("*"*nChars)
        else:
            res=self.chip.fixLen("PLL Configuration, Active Profile No. %d" %(self.ACTIVE_PROFILE), nChars)+"\n"
            res+="*"*nChar+"\n"
            res+=self.infoXBUFConfig(printInfo=printInfo)
            res+=self.infoVREGConfig(printInfo=printInfo)
            res+="*"*nChars+"\n"
            res+=self.PROFILES[self.ACTIVE_PROFILE].infoConfig(printInfo=printInfo)
            res+=self.infoLOCK(printInfo=printInfo)
            res+="*"*nChars+"\n"
            return res
