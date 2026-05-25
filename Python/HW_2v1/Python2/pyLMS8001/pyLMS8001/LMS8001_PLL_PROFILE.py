from math import ceil, floor

class LMS8001_PLL_PROFILE(object):
    def __init__(self, chip, cfgNo):
        self.chip = chip
        self.cfgNo = cfgNo

    def _readReg(self, reg, field):
        return self.chip[reg][field]
        
    def _writeReg(self, reg, field,val):
        self.chip[reg][field] = val

    # PLL_LODIST_EN_BIAS
    @property 
    def PLL_LODIST_EN_BIAS(self):
        """
        Get the value of PLL_LODIST_EN_BIAS
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_LODIST_EN_BIAS_'+str(self.cfgNo))

    @PLL_LODIST_EN_BIAS.setter
    def PLL_LODIST_EN_BIAS(self, value):
        """
        Set the value of PLL_LODIST_EN_BIAS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_LODIST_EN_BIAS_'+str(self.cfgNo), value)

    # PLL_LODIST_EN_DIV2IQ
    @property 
    def PLL_LODIST_EN_DIV2IQ(self):
        """
        Get the value of PLL_LODIST_EN_DIV2IQ
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_LODIST_EN_DIV2IQ_'+str(self.cfgNo))

    @PLL_LODIST_EN_DIV2IQ.setter
    def PLL_LODIST_EN_DIV2IQ(self, value):
        """
        Set the value of PLL_LODIST_EN_DIV2IQ
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_LODIST_EN_DIV2IQ_'+str(self.cfgNo), value)

    # PLL_EN_VTUNE_COMP
    @property 
    def PLL_EN_VTUNE_COMP(self):
        """
        Get the value of PLL_EN_VTUNE_COMP
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_VTUNE_COMP_'+str(self.cfgNo))

    @PLL_EN_VTUNE_COMP.setter
    def PLL_EN_VTUNE_COMP(self, value):
        """
        Set the value of PLL_EN_VTUNE_COMP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_VTUNE_COMP_'+str(self.cfgNo), value)

    # PLL_EN_LD
    @property 
    def PLL_EN_LD(self):
        """
        Get the value of PLL_EN_LD
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_LD_'+str(self.cfgNo))

    @PLL_EN_LD.setter
    def PLL_EN_LD(self, value):
        """
        Set the value of PLL_EN_LD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_LD_'+str(self.cfgNo), value)

    # PLL_EN_PFD
    @property 
    def PLL_EN_PFD(self):
        """
        Get the value of PLL_EN_PFD
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_PFD_'+str(self.cfgNo))

    @PLL_EN_PFD.setter
    def PLL_EN_PFD(self, value):
        """
        Set the value of PLL_EN_PFD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_PFD_'+str(self.cfgNo), value)

    # PLL_EN_CP
    @property 
    def PLL_EN_CP(self):
        """
        Get the value of PLL_EN_CP
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_CP_'+str(self.cfgNo))

    @PLL_EN_CP.setter
    def PLL_EN_CP(self, value):
        """
        Set the value of PLL_EN_CP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_CP_'+str(self.cfgNo), value)

    # PLL_EN_CPOFS
    @property 
    def PLL_EN_CPOFS(self):
        """
        Get the value of PLL_EN_CPOFS
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_CPOFS_'+str(self.cfgNo))

    @PLL_EN_CPOFS.setter
    def PLL_EN_CPOFS(self, value):
        """
        Set the value of PLL_EN_CPOFS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_CPOFS_'+str(self.cfgNo), value)

    # PLL_EN_VCO
    @property 
    def PLL_EN_VCO(self):
        """
        Get the value of PLL_EN_VCO
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_VCO_'+str(self.cfgNo))

    @PLL_EN_VCO.setter
    def PLL_EN_VCO(self, value):
        """
        Set the value of PLL_EN_VCO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_VCO_'+str(self.cfgNo), value)

    # PLL_EN_FFDIV
    @property 
    def PLL_EN_FFDIV(self):
        """
        Get the value of PLL_EN_FFDIV
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FFDIV_'+str(self.cfgNo))

    @PLL_EN_FFDIV.setter
    def PLL_EN_FFDIV(self, value):
        """
        Set the value of PLL_EN_FFDIV
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FFDIV_'+str(self.cfgNo), value)

    # PLL_EN_FB_PDIV2
    @property 
    def PLL_EN_FB_PDIV2(self):
        """
        Get the value of PLL_EN_FB_PDIV2
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FB_PDIV2_'+str(self.cfgNo))

    @PLL_EN_FB_PDIV2.setter
    def PLL_EN_FB_PDIV2(self, value):
        """
        Set the value of PLL_EN_FB_PDIV2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FB_PDIV2_'+str(self.cfgNo), value)

    # PLL_EN_FFCORE
    @property 
    def PLL_EN_FFCORE(self):
        """
        Get the value of PLL_EN_FFCORE
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FFCORE_'+str(self.cfgNo))

    @PLL_EN_FFCORE.setter
    def PLL_EN_FFCORE(self, value):
        """
        Set the value of PLL_EN_FFCORE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FFCORE_'+str(self.cfgNo), value)

    # PLL_EN_FBDIV
    @property 
    def PLL_EN_FBDIV(self):
        """
        Get the value of PLL_EN_FBDIV
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FBDIV_'+str(self.cfgNo))

    @PLL_EN_FBDIV.setter
    def PLL_EN_FBDIV(self, value):
        """
        Set the value of PLL_EN_FBDIV
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_EN_FBDIV_'+str(self.cfgNo), value)

    # PLL_SDM_CLK_EN
    @property 
    def PLL_SDM_CLK_EN(self):
        """
        Get the value of PLL_SDM_CLK_EN
        """
        return self._readReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_SDM_CLK_EN_'+str(self.cfgNo))

    @PLL_SDM_CLK_EN.setter
    def PLL_SDM_CLK_EN(self, value):
        """
        Set the value of PLL_SDM_CLK_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_ENABLE_'+str(self.cfgNo), 'PLL_SDM_CLK_EN_'+str(self.cfgNo), value)

    # R3<3:0>
    @property 
    def R3(self):
        """
        Get the value of R3<3:0>
        """
        return self._readReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'R3_'+str(self.cfgNo)+'<3:0>')

    @R3.setter
    def R3(self, value):
        """
        Set the value of R3<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'R3_'+str(self.cfgNo)+'<3:0>', value)

    # R2<3:0>
    @property 
    def R2(self):
        """
        Get the value of R2<3:0>
        """
        return self._readReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'R2_'+str(self.cfgNo)+'<3:0>')

    @R2.setter
    def R2(self, value):
        """
        Set the value of R2<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'R2_'+str(self.cfgNo)+'<3:0>', value)

    # C2<3:0>
    @property 
    def C2(self):
        """
        Get the value of C2<3:0>
        """
        return self._readReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'C2_'+str(self.cfgNo)+'<3:0>')

    @C2.setter
    def C2(self, value):
        """
        Set the value of C2<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'C2_'+str(self.cfgNo)+'<3:0>', value)

    # C1<3:0>
    @property 
    def C1(self):
        """
        Get the value of C1<3:0>
        """
        return self._readReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'C1_'+str(self.cfgNo)+'<3:0>')

    @C1.setter
    def C1(self, value):
        """
        Set the value of C1<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_LPF_CFG1_'+str(self.cfgNo), 'C1_'+str(self.cfgNo)+'<3:0>', value)

    # VTUNE_VCT<1:0>
    @property 
    def VTUNE_VCT(self):
        """
        Get the value of VTUNE_VCT<1:0>
        """
        return self._readReg('PLL_LPF_CFG2_'+str(self.cfgNo), 'VTUNE_VCT_'+str(self.cfgNo)+'<1:0>')

    @VTUNE_VCT.setter
    def VTUNE_VCT(self, value):
        """
        Set the value of VTUNE_VCT<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_LPF_CFG2_'+str(self.cfgNo), 'VTUNE_VCT_'+str(self.cfgNo)+'<1:0>', value)

    # LPFSW
    @property 
    def LPFSW(self):
        """
        Get the value of LPFSW
        """
        return self._readReg('PLL_LPF_CFG2_'+str(self.cfgNo), 'LPFSW_'+str(self.cfgNo))

    @LPFSW.setter
    def LPFSW(self, value):
        """
        Set the value of LPFSW
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_LPF_CFG2_'+str(self.cfgNo), 'LPFSW_'+str(self.cfgNo), value)

    # C3<3:0>
    @property 
    def C3(self):
        """
        Get the value of C3<3:0>
        """
        return self._readReg('PLL_LPF_CFG2_'+str(self.cfgNo), 'C3_'+str(self.cfgNo)+'<3:0>')

    @C3.setter
    def C3(self, value):
        """
        Set the value of C3<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_LPF_CFG2_'+str(self.cfgNo), 'C3_'+str(self.cfgNo)+'<3:0>', value)

    # FLIP
    @property 
    def FLIP(self):
        """
        Get the value of FLIP
        """
        return self._readReg('PLL_CP_CFG0_'+str(self.cfgNo), 'FLIP_'+str(self.cfgNo))

    @FLIP.setter
    def FLIP(self, value):
        """
        Set the value of FLIP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_CP_CFG0_'+str(self.cfgNo), 'FLIP_'+str(self.cfgNo), value)

    # DEL<1:0>
    @property 
    def DEL(self):
        """
        Get the value of DEL<1:0>
        """
        return self._readReg('PLL_CP_CFG0_'+str(self.cfgNo), 'DEL_'+str(self.cfgNo)+'<1:0>')

    @DEL.setter
    def DEL(self, value):
        """
        Set the value of DEL<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_CP_CFG0_'+str(self.cfgNo), 'DEL_'+str(self.cfgNo)+'<1:0>', value)

    # PULSE<5:0>
    @property 
    def PULSE(self):
        """
        Get the value of PULSE<5:0>
        """
        return self._readReg('PLL_CP_CFG0_'+str(self.cfgNo), 'PULSE_'+str(self.cfgNo)+'<5:0>')

    @PULSE.setter
    def PULSE(self, value):
        """
        Set the value of PULSE<5:0>
        """
        if not(0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PLL_CP_CFG0_'+str(self.cfgNo), 'PULSE_'+str(self.cfgNo)+'<5:0>', value)

    # OFS<5:0>
    @property 
    def OFS(self):
        """
        Get the value of OFS<5:0>
        """
        return self._readReg('PLL_CP_CFG0_'+str(self.cfgNo), 'OFS_'+str(self.cfgNo)+'<5:0>')

    @OFS.setter
    def OFS(self, value):
        """
        Set the value of OFS<5:0>
        """
        if not(0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PLL_CP_CFG0_'+str(self.cfgNo), 'OFS_'+str(self.cfgNo)+'<5:0>', value)

    # LD_VCT<1:0>
    @property 
    def LD_VCT(self):
        """
        Get the value of LD_VCT<1:0>
        """
        return self._readReg('PLL_CP_CFG1_'+str(self.cfgNo), 'LD_VCT_'+str(self.cfgNo)+'<1:0>')

    @LD_VCT.setter
    def LD_VCT(self, value):
        """
        Set the value of LD_VCT<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_CP_CFG1_'+str(self.cfgNo), 'LD_VCT_'+str(self.cfgNo)+'<1:0>', value)

    # ICT_CP<4:0>
    @property 
    def ICT_CP(self):
        """
        Get the value of ICT_CP<4:0>
        """
        return self._readReg('PLL_CP_CFG1_'+str(self.cfgNo), 'ICT_CP_'+str(self.cfgNo)+'<4:0>')

    @ICT_CP.setter
    def ICT_CP(self, value):
        """
        Set the value of ICT_CP<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PLL_CP_CFG1_'+str(self.cfgNo), 'ICT_CP_'+str(self.cfgNo)+'<4:0>', value)

    # VCO_FREQ<7:0>
    @property 
    def VCO_FREQ(self):
        """
        Get the value of VCO_FREQ<7:0>
        """
        return self._readReg('PLL_VCO_FREQ_'+str(self.cfgNo), 'VCO_FREQ_'+str(self.cfgNo)+'<7:0>')

    @VCO_FREQ.setter
    def VCO_FREQ(self, value):
        """
        Set the value of VCO_FREQ<7:0>
        """
        if not(0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PLL_VCO_FREQ_'+str(self.cfgNo), 'VCO_FREQ_'+str(self.cfgNo)+'<7:0>', value)


    # SPDUP_VCO
    @property 
    def SPDUP_VCO(self):
        """
        Get the value of SPDUP_VCO
        """
        return self._readReg('PLL_VCO_CFG_'+str(self.cfgNo), 'SPDUP_VCO_'+str(self.cfgNo))

    @SPDUP_VCO.setter
    def SPDUP_VCO(self, value):
        """
        Set the value of SPDUP_VCO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_VCO_CFG_'+str(self.cfgNo), 'SPDUP_VCO_'+str(self.cfgNo), value)

    # VCO_AAC_EN
    @property 
    def VCO_AAC_EN(self):
        """
        Get the value of VCO_AAC_EN
        """
        return self._readReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VCO_AAC_EN_'+str(self.cfgNo))

    @VCO_AAC_EN.setter
    def VCO_AAC_EN(self, value):
        """
        Set the value of VCO_AAC_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VCO_AAC_EN_'+str(self.cfgNo), value)

    # VDIV_SWVDD<1:0>
    @property 
    def VDIV_SWVDD(self):
        """
        Get the value of VDIV_SWVDD<1:0>
        """
        return self._readReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VDIV_SWVDD_'+str(self.cfgNo)+'<1:0>')

    @VDIV_SWVDD.setter
    def VDIV_SWVDD(self, value):
        """
        Set the value of VDIV_SWVDD<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VDIV_SWVDD_'+str(self.cfgNo)+'<1:0>', value)

    # VCO_SEL<1:0>
    @property 
    def VCO_SEL(self):
        """
        Get the value of VCO_SEL<1:0>
        """
        return self._readReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VCO_SEL_'+str(self.cfgNo)+'<1:0>')

    @VCO_SEL.setter
    def VCO_SEL(self, value):
        """
        Set the value of VCO_SEL<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VCO_SEL_'+str(self.cfgNo)+'<1:0>', value)

    # VCO_AMP<6:0>
    @property 
    def VCO_AMP(self):
        """
        Get the value of VCO_AMP<6:0>
        """
        return self._readReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VCO_AMP_'+str(self.cfgNo)+'<6:0>')

    @VCO_AMP.setter
    def VCO_AMP(self, value):
        """
        Set the value of VCO_AMP<6:0>
        """
        if not(0 <= value <= 127):
            raise ValueError("Value must be [0..127]")
        self._writeReg('PLL_VCO_CFG_'+str(self.cfgNo), 'VCO_AMP_'+str(self.cfgNo)+'<6:0>', value)

    # FFDIV_SEL
    @property 
    def FFDIV_SEL(self):
        """
        Get the value of FFDIV_SEL
        """
        return self._readReg('PLL_FF_CFG_'+str(self.cfgNo), 'FFDIV_SEL_'+str(self.cfgNo))

    @FFDIV_SEL.setter
    def FFDIV_SEL(self, value):
        """
        Set the value of FFDIV_SEL
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_FF_CFG_'+str(self.cfgNo), 'FFDIV_SEL_'+str(self.cfgNo), value)

    # FFCORE_MOD<1:0>
    @property 
    def FFCORE_MOD(self):
        """
        Get the value of FFCORE_MOD<1:0>
        """
        return self._readReg('PLL_FF_CFG_'+str(self.cfgNo), 'FFCORE_MOD_'+str(self.cfgNo)+'<1:0>')

    @FFCORE_MOD.setter
    def FFCORE_MOD(self, value):
        """
        Set the value of FFCORE_MOD<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('PLL_FF_CFG_'+str(self.cfgNo), 'FFCORE_MOD_'+str(self.cfgNo)+'<1:0>', value)
        # added by pavlej, FFCORE_MOD and FF_MOD should always be the same
        self._writeReg('PLL_FF_CFG_'+str(self.cfgNo), 'FF_MOD_'+str(self.cfgNo)+'<1:0>', value)

    # FF_MOD<1:0>
    @property 
    def FF_MOD(self):
        """
        Get the value of FF_MOD<1:0>
        """
        return self._readReg('PLL_FF_CFG_'+str(self.cfgNo), 'FF_MOD_'+str(self.cfgNo)+'<1:0>')
        
        

    @FF_MOD.setter
    def FF_MOD(self, value):
        """
        Set the value of FF_MOD<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        # added by pavlej, FFCORE_MOD and FF_MOD should always be the same
        self._writeReg('PLL_FF_CFG_'+str(self.cfgNo), 'FFCORE_MOD_'+str(self.cfgNo)+'<1:0>', value)
        self._writeReg('PLL_FF_CFG_'+str(self.cfgNo), 'FF_MOD_'+str(self.cfgNo)+'<1:0>', value)

    # INTMOD_EN
    @property 
    def INTMOD_EN(self):
        """
        Get the value of INTMOD_EN
        """
        return self._readReg('PLL_SDM_CFG_'+str(self.cfgNo), 'INTMOD_EN_'+str(self.cfgNo))

    @INTMOD_EN.setter
    def INTMOD_EN(self, value):
        """
        Set the value of INTMOD_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_CFG_'+str(self.cfgNo), 'INTMOD_EN_'+str(self.cfgNo), value)

    # DITHER_EN
    @property 
    def DITHER_EN(self):
        """
        Get the value of DITHER_EN
        """
        return self._readReg('PLL_SDM_CFG_'+str(self.cfgNo), 'DITHER_EN_'+str(self.cfgNo))

    @DITHER_EN.setter
    def DITHER_EN(self, value):
        """
        Set the value of DITHER_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_CFG_'+str(self.cfgNo), 'DITHER_EN_'+str(self.cfgNo), value)

    # SEL_SDMCLK
    @property 
    def SEL_SDMCLK(self):
        """
        Get the value of SEL_SDMCLK
        """
        return self._readReg('PLL_SDM_CFG_'+str(self.cfgNo), 'SEL_SDMCLK_'+str(self.cfgNo))

    @SEL_SDMCLK.setter
    def SEL_SDMCLK(self, value):
        """
        Set the value of SEL_SDMCLK
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_CFG_'+str(self.cfgNo), 'SEL_SDMCLK_'+str(self.cfgNo), value)

    # REV_SDMCLK
    @property 
    def REV_SDMCLK(self):
        """
        Get the value of REV_SDMCLK
        """
        return self._readReg('PLL_SDM_CFG_'+str(self.cfgNo), 'REV_SDMCLK_'+str(self.cfgNo))

    @REV_SDMCLK.setter
    def REV_SDMCLK(self, value):
        """
        Set the value of REV_SDMCLK
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_SDM_CFG_'+str(self.cfgNo), 'REV_SDMCLK_'+str(self.cfgNo), value)

    # INTMOD<9:0>
    @property 
    def INTMOD(self):
        """
        Get the value of INTMOD<9:0>
        """
        return self._readReg('PLL_SDM_CFG_'+str(self.cfgNo), 'INTMOD_'+str(self.cfgNo)+'<9:0>')

    @INTMOD.setter
    def INTMOD(self, value):
        """
        Set the value of INTMOD<9:0>
        """
        if not(0 <= value <= 1023):
            raise ValueError("Value must be [0..1023]")
        self._writeReg('PLL_SDM_CFG_'+str(self.cfgNo), 'INTMOD_'+str(self.cfgNo)+'<9:0>', value)

    # FRACMODL<15:0>
    @property 
    def FRACMODL(self):
        """
        Get the value of FRACMODL<15:0>
        """
        return self._readReg('PLL_FRACMODL_'+str(self.cfgNo), 'FRACMODL_'+str(self.cfgNo)+'<15:0>')

    @FRACMODL.setter
    def FRACMODL(self, value):
        """
        Set the value of FRACMODL<15:0>
        """
        if not(0 <= value <= 65535):
            raise ValueError("Value must be [0..65535]")
        self._writeReg('PLL_FRACMODL_'+str(self.cfgNo), 'FRACMODL_'+str(self.cfgNo)+'<15:0>', value)


    # FRACMODH<3:0>
    @property 
    def FRACMODH(self):
        """
        Get the value of FRACMODH<3:0>
        """
        return self._readReg('PLL_FRACMODH_'+str(self.cfgNo), 'FRACMODH_'+str(self.cfgNo)+'<3:0>')

    @FRACMODH.setter
    def FRACMODH(self, value):
        """
        Set the value of FRACMODH<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FRACMODH_'+str(self.cfgNo), 'FRACMODH_'+str(self.cfgNo)+'<3:0>', value)

    # PLL_LODIST_EN_OUT<3:0>
    @property 
    def PLL_LODIST_EN_OUT(self):
        """
        Get the value of PLL_LODIST_EN_OUT<3:0>
        """
        return self._readReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_EN_OUT_'+str(self.cfgNo)+'<3:0>')

    @PLL_LODIST_EN_OUT.setter
    def PLL_LODIST_EN_OUT(self, value):
        """
        Set the value of PLL_LODIST_EN_OUT<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_EN_OUT_'+str(self.cfgNo)+'<3:0>', value)

    # PLL_LODIST_FSP_OUT3<2:0>
    @property 
    def PLL_LODIST_FSP_OUT3(self):
        """
        Get the value of PLL_LODIST_FSP_OUT3<2:0>
        """
        return self._readReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT3_'+str(self.cfgNo)+'<2:0>')

    @PLL_LODIST_FSP_OUT3.setter
    def PLL_LODIST_FSP_OUT3(self, value):
        """
        Set the value of PLL_LODIST_FSP_OUT3<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT3_'+str(self.cfgNo)+'<2:0>', value)

    # PLL_LODIST_FSP_OUT2<2:0>
    @property 
    def PLL_LODIST_FSP_OUT2(self):
        """
        Get the value of PLL_LODIST_FSP_OUT2<2:0>
        """
        return self._readReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT2_'+str(self.cfgNo)+'<2:0>')

    @PLL_LODIST_FSP_OUT2.setter
    def PLL_LODIST_FSP_OUT2(self, value):
        """
        Set the value of PLL_LODIST_FSP_OUT2<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT2_'+str(self.cfgNo)+'<2:0>', value)

    # PLL_LODIST_FSP_OUT1<2:0>
    @property 
    def PLL_LODIST_FSP_OUT1(self):
        """
        Get the value of PLL_LODIST_FSP_OUT1<2:0>
        """
        return self._readReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT1_'+str(self.cfgNo)+'<2:0>')

    @PLL_LODIST_FSP_OUT1.setter
    def PLL_LODIST_FSP_OUT1(self, value):
        """
        Set the value of PLL_LODIST_FSP_OUT1<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT1_'+str(self.cfgNo)+'<2:0>', value)

    # PLL_LODIST_FSP_OUT0<2:0>
    @property 
    def PLL_LODIST_FSP_OUT0(self):
        """
        Get the value of PLL_LODIST_FSP_OUT0<2:0>
        """
        return self._readReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT0_'+str(self.cfgNo)+'<2:0>')

    @PLL_LODIST_FSP_OUT0.setter
    def PLL_LODIST_FSP_OUT0(self, value):
        """
        Set the value of PLL_LODIST_FSP_OUT0<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('PLL_LODIST_CFG_'+str(self.cfgNo), 'PLL_LODIST_FSP_OUT0_'+str(self.cfgNo)+'<2:0>', value)

    # FLOCK_R3<3:0>
    @property 
    def FLOCK_R3(self):
        """
        Get the value of FLOCK_R3<3:0>
        """
        return self._readReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_R3_'+str(self.cfgNo)+'<3:0>')

    @FLOCK_R3.setter
    def FLOCK_R3(self, value):
        """
        Set the value of FLOCK_R3<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_R3_'+str(self.cfgNo)+'<3:0>', value)

    # FLOCK_R2<3:0>
    @property 
    def FLOCK_R2(self):
        """
        Get the value of FLOCK_R2<3:0>
        """
        return self._readReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_R2_'+str(self.cfgNo)+'<3:0>')

    @FLOCK_R2.setter
    def FLOCK_R2(self, value):
        """
        Set the value of FLOCK_R2<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_R2_'+str(self.cfgNo)+'<3:0>', value)

    # FLOCK_C2<3:0>
    @property 
    def FLOCK_C2(self):
        """
        Get the value of FLOCK_C2<3:0>
        """
        return self._readReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_C2_'+str(self.cfgNo)+'<3:0>')

    @FLOCK_C2.setter
    def FLOCK_C2(self, value):
        """
        Set the value of FLOCK_C2<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_C2_'+str(self.cfgNo)+'<3:0>', value)

    # FLOCK_C1<3:0>
    @property 
    def FLOCK_C1(self):
        """
        Get the value of FLOCK_C1<3:0>
        """
        return self._readReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_C1_'+str(self.cfgNo)+'<3:0>')

    @FLOCK_C1.setter
    def FLOCK_C1(self, value):
        """
        Set the value of FLOCK_C1<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FLOCK_CFG1_'+str(self.cfgNo), 'FLOCK_C1_'+str(self.cfgNo)+'<3:0>', value)

    # FLOCK_C3<3:0>
    @property 
    def FLOCK_C3(self):
        """
        Get the value of FLOCK_C3<3:0>
        """
        return self._readReg('PLL_FLOCK_CFG2_'+str(self.cfgNo), 'FLOCK_C3_'+str(self.cfgNo)+'<3:0>')

    @FLOCK_C3.setter
    def FLOCK_C3(self, value):
        """
        Set the value of FLOCK_C3<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FLOCK_CFG2_'+str(self.cfgNo), 'FLOCK_C3_'+str(self.cfgNo)+'<3:0>', value)

    # FLOCK_PULSE<5:0>
    @property 
    def FLOCK_PULSE(self):
        """
        Get the value of FLOCK_PULSE<5:0>
        """
        return self._readReg('PLL_FLOCK_CFG2_'+str(self.cfgNo), 'FLOCK_PULSE_'+str(self.cfgNo)+'<5:0>')

    @FLOCK_PULSE.setter
    def FLOCK_PULSE(self, value):
        """
        Set the value of FLOCK_PULSE<5:0>
        """
        if not(0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PLL_FLOCK_CFG2_'+str(self.cfgNo), 'FLOCK_PULSE_'+str(self.cfgNo)+'<5:0>', value)

    # FLOCK_OFS<5:0>
    @property 
    def FLOCK_OFS(self):
        """
        Get the value of FLOCK_OFS<5:0>
        """
        return self._readReg('PLL_FLOCK_CFG2_'+str(self.cfgNo), 'FLOCK_OFS_'+str(self.cfgNo)+'<5:0>')

    @FLOCK_OFS.setter
    def FLOCK_OFS(self, value):
        """
        Set the value of FLOCK_OFS<5:0>
        """
        if not(0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PLL_FLOCK_CFG2_'+str(self.cfgNo), 'FLOCK_OFS_'+str(self.cfgNo)+'<5:0>', value)

    # FLOCK_LODIST_EN_OUT<3:0>
    @property 
    def FLOCK_LODIST_EN_OUT(self):
        """
        Get the value of FLOCK_LODIST_EN_OUT<3:0>
        """
        return self._readReg('PLL_FLOCK_CFG3_'+str(self.cfgNo), 'FLOCK_LODIST_EN_OUT_'+str(self.cfgNo)+'<3:0>')

    @FLOCK_LODIST_EN_OUT.setter
    def FLOCK_LODIST_EN_OUT(self, value):
        """
        Set the value of FLOCK_LODIST_EN_OUT<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('PLL_FLOCK_CFG3_'+str(self.cfgNo), 'FLOCK_LODIST_EN_OUT_'+str(self.cfgNo)+'<3:0>', value)

    # FLOCK_VCO_SPDUP
    @property 
    def FLOCK_VCO_SPDUP(self):
        """
        Get the value of FLOCK_VCO_SPDUP
        """
        return self._readReg('PLL_FLOCK_CFG3_'+str(self.cfgNo), 'FLOCK_VCO_SPDUP_'+str(self.cfgNo))

    @FLOCK_VCO_SPDUP.setter
    def FLOCK_VCO_SPDUP(self, value):
        """
        Set the value of FLOCK_VCO_SPDUP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('PLL_FLOCK_CFG3_'+str(self.cfgNo), 'FLOCK_VCO_SPDUP_'+str(self.cfgNo), value)

    # FLOCK_N<9:0>
    @property 
    def FLOCK_N(self):
        """
        Get the value of FLOCK_N<9:0>
        """
        return self._readReg('PLL_FLOCK_CFG3_'+str(self.cfgNo), 'FLOCK_N_'+str(self.cfgNo)+'<9:0>')

    @FLOCK_N.setter
    def FLOCK_N(self, value):
        """
        Set the value of FLOCK_N<9:0>
        """
        if not(0 <= value <= 1023):
            raise ValueError("Value must be [0..1023]")
        self._writeReg('PLL_FLOCK_CFG3_'+str(self.cfgNo), 'FLOCK_N_'+str(self.cfgNo)+'<9:0>', value)
    
    # added by pavlej

    @property
    def EN_LO_A(self):
        """
        Get value of the PLL_LODIST_EN_OUT[0]
        """
        return self.PLL_LODIST_EN_OUT&1

    @EN_LO_A.setter
    def EN_LO_A(self, value):
        """
        Set value of the PLL_LODIST_EN_OUT[0]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="A", EN=value, EN_FLOCK=self.FLOCK_LODIST_EN_OUT&1, IQ=1-(self.PLL_LODIST_FSP_OUT0&4)>>2, phase=self.PLL_LODIST_FSP_OUT0&3, PROFILE=self.cfgNo)

    @property
    def EN_LO_FLOCK_A(self):
        """
        Get value of the FLOCK_LODIST_EN_OUT[0]
        """
        return self.FLOCK_LODIST_EN_OUT&1

    @EN_LO_FLOCK_A.setter
    def EN_LO_FLOCK_A(self, value):
        """
        Set value of the FLOCK_LODIST_EN_OUT[0]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="A", EN=self.PLL_LODIST_EN_OUT&1, EN_FLOCK=value, IQ=1-(self.PLL_LODIST_FSP_OUT0&4)>>2, phase=self.PLL_LODIST_FSP_OUT0&3, PROFILE=self.cfgNo)

    @property
    def IQ_LO_A(self):
        """
        Get value of the PLL_LODIST_FSP_OUT0[2]
        """
        return 1-(self.PLL_LODIST_FSP_OUT0&4)>>2

    @IQ_LO_A.setter
    def IQ_LO_A(self, value):
        """
        Set value of the PLL_LODIST_FSP_OUT0[2]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="A", EN=(self.PLL_LODIST_EN_OUT&1)>>0, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&1)>>0, IQ=value, phase=self.PLL_LODIST_FSP_OUT0&3, PROFILE=self.cfgNo)

    @property
    def PHASE_LO_A(self):
        """
        Get value of the LO phase in degrees for channel A
        """
        if (self.IQ_LO_A==1):
            return (self.PLL_LODIST_FSP_OUT0&3)*90
        else:
            return ((self.PLL_LODIST_FSP_OUT0&2)>>1)*180
    
    @PHASE_LO_A.setter
    def PHASE_LO_A(self, value):
        """
        Set value of the LO phase in degrees for channel A
        """
        if (self.IQ_LO_A==1):
            if not (value in [0, 90, 180, 270]):
                raise ValueError("Value must be [0,90,180 or 270], Divide By 2 in LO-DIST selected for channel A output.")
        else:
            if not (value in [0,180]):
                raise ValueError("Value must be [0,180], Divide By 1 in LO-DIST selected for channel A output.")
        
        self.PLL.PLL_METHODS.setLODIST(channel="A", EN=(self.PLL_LODIST_EN_OUT&1)>>0, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&1)>>0, IQ=1-(self.PLL_LODIST_FSP_OUT0&4)>>2, phase=value, PROFILE=self.cfgNo)

    @property
    def EN_LO_B(self):
        """
        Get value of the PLL_LODIST_EN_OUT[1]
        """
        return (self.PLL_LODIST_EN_OUT&2)>>1

    @EN_LO_B.setter
    def EN_LO_B(self, value):
        """
        Set value of the PLL_LODIST_EN_OUT[1]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="B", EN=value, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&2)>>1, IQ=1-(self.PLL_LODIST_FSP_OUT1&4)>>2, phase=self.PLL_LODIST_FSP_OUT1&3, PROFILE=self.cfgNo)

    @property
    def EN_LO_FLOCK_B(self):
        """
        Get value of the FLOCK_LODIST_EN_OUT[1]
        """
        return (self.FLOCK_LODIST_EN_OUT&2)>>1

    @EN_LO_FLOCK_B.setter
    def EN_LO_FLOCK_B(self, value):
        """
        Set value of the FLOCK_LODIST_EN_OUT[1]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="B", EN=(self.PLL_LODIST_EN_OUT&2)>>1, EN_FLOCK=value, IQ=1-(self.PLL_LODIST_FSP_OUT1&4)>>2, phase=self.PLL_LODIST_FSP_OUT1&3, PROFILE=self.cfgNo)
    
    @property
    def IQ_LO_B(self):
        """
        Get value of the PLL_LODIST_FSP_OUT1[2]
        """
        return 1-(self.PLL_LODIST_FSP_OUT1&4)>>2

    @IQ_LO_B.setter
    def IQ_LO_B(self, value):
        """
        Set value of the PLL_LODIST_FSP_OUT1[2]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="B", EN=(self.PLL_LODIST_EN_OUT&2)>>1, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&2)>>1, IQ=value, phase=self.PLL_LODIST_FSP_OUT1&3, PROFILE=self.cfgNo)

    @property
    def PHASE_LO_B(self):
        """
        Get value of the LO phase in degrees for channel B
        """
        if (self.IQ_LO_B==1):
            return (self.PLL_LODIST_FSP_OUT1&3)*90
        else:
            return ((self.PLL_LODIST_FSP_OUT1&2)>>1)*180
    
    @PHASE_LO_B.setter
    def PHASE_LO_B(self, value):
        """
        Set value of the LO phase in degrees for channel B
        """
        if (self.IQ_LO_B==1):
            if not (value in [0, 90, 180, 270]):
                raise ValueError("Value must be [0,90,180 or 270], Divide By 2 in LO-DIST selected for channel B output.")
        else:
            if not (value in [0,180]):
                raise ValueError("Value must be [0,180], Divide By 1 in LO-DIST selected for channel B output.")
        
        self.PLL.PLL_METHODS.setLODIST(channel="B", EN=(self.PLL_LODIST_EN_OUT&2)>>1, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&2)>>1, IQ=1-(self.PLL_LODIST_FSP_OUT1&4)>>2, phase=value, PROFILE=self.cfgNo)

    @property
    def EN_LO_C(self):
        """
        Get value of the PLL_LODIST_EN_OUT[2]
        """
        return (self.PLL_LODIST_EN_OUT&4)>>2

    @EN_LO_C.setter
    def EN_LO_C(self, value):
        """
        Set value of the PLL_LODIST_EN_OUT[2]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="C", EN=value, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&4)>>2, IQ=1-(self.PLL_LODIST_FSP_OUT2&4)>>2, phase=self.PLL_LODIST_FSP_OUT2&3, PROFILE=self.cfgNo)

    @property
    def EN_LO_FLOCK_C(self):
        """
        Get value of the FLOCK_LODIST_EN_OUT[2]
        """
        return (self.FLOCK_LODIST_EN_OUT&4)>>2

    @EN_LO_FLOCK_C.setter
    def EN_LO_FLOCK_C(self, value):
        """
        Set value of the FLOCK_LODIST_EN_OUT[2]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="C", EN=(self.PLL_LODIST_EN_OUT&4)>>2, EN_FLOCK=value, IQ=1-(self.PLL_LODIST_FSP_OUT2&4)>>2, phase=self.PLL_LODIST_FSP_OUT2&3, PROFILE=self.cfgNo)

    @property
    def IQ_LO_C(self):
        """
        Get value of the PLL_LODIST_FSP_OUT2[2]
        """
        return 1-(self.PLL_LODIST_FSP_OUT2&4)>>2

    @IQ_LO_C.setter
    def IQ_LO_C(self, value):
        """
        Set value of the PLL_LODIST_FSP_OUT2[2]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="C", EN=(self.PLL_LODIST_EN_OUT&4)>>2, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&4)>>2, IQ=value, phase=self.PLL_LODIST_FSP_OUT2&3, PROFILE=self.cfgNo)

    @property
    def PHASE_LO_C(self):
        """
        Get value of the LO phase in degrees for channel C
        """
        if (self.IQ_LO_C==1):
            return (self.PLL_LODIST_FSP_OUT2&3)*90
        else:
            return ((self.PLL_LODIST_FSP_OUT2&2)>>1)*180
    
    @PHASE_LO_C.setter
    def PHASE_LO_C(self, value):
        """
        Set value of the LO phase in degrees for channel C
        """
        if (self.IQ_LO_C==1):
            if not (value in [0, 90, 180, 270]):
                raise ValueError("Value must be [0,90,180 or 270], Divide By 2 in LO-DIST selected for channel C output.")
        else:
            if not (value in [0,180]):
                raise ValueError("Value must be [0,180], Divide By 1 in LO-DIST selected for channel C output.")
        
        self.PLL.PLL_METHODS.setLODIST(channel="C", EN=(self.PLL_LODIST_EN_OUT&4)>>2, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&4)>>2, IQ=1-(self.PLL_LODIST_FSP_OUT2&4)>>2, phase=value, PROFILE=self.cfgNo)

    @property
    def EN_LO_D(self):
        """
        Get value of the PLL_LODIST_EN_OUT[3]
        """
        return (self.PLL_LODIST_EN_OUT&8)>>3

    @EN_LO_D.setter
    def EN_LO_D(self, value):
        """
        Set value of the PLL_LODIST_EN_OUT[3]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="D", EN=value, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&8)>>3, IQ=1-(self.PLL_LODIST_FSP_OUT3&4)>>2, phase=self.PLL_LODIST_FSP_OUT3&3, PROFILE=self.cfgNo)

    @property
    def EN_LO_FLOCK_D(self):
        """
        Get value of the FLOCK_LODIST_EN_OUT[3]
        """
        return (self.FLOCK_LODIST_EN_OUT&8)>>3

    @EN_LO_FLOCK_D.setter
    def EN_LO_FLOCK_D(self, value):
        """
        Set value of the FLOCK_LODIST_EN_OUT[3]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="D", EN=(self.PLL_LODIST_EN_OUT&8)>>3, EN_FLOCK=value, IQ=1-(self.PLL_LODIST_FSP_OUT3&4)>>2, phase=self.PLL_LODIST_FSP_OUT3&3, PROFILE=self.cfgNo)
    
    @property
    def IQ_LO_D(self):
        """
        Get value of the PLL_LODIST_FSP_OUT3[2]
        """
        return 1-(self.PLL_LODIST_FSP_OUT3&8)>>3

    @IQ_LO_D.setter
    def IQ_LO_D(self, value):
        """
        Set value of the PLL_LODIST_FSP_OUT3[2]
        """
        if not(0 <= value <= 1):
            raise ValueError("Value must be [0..1]")
        self.PLL.PLL_METHODS.setLODIST(channel="D", EN=(self.PLL_LODIST_EN_OUT&8)>>3, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&8)>>3, IQ=1-(self.PLL_LODIST_FSP_OUT3&4)>>2, phase=value, PROFILE=self.cfgNo)

    @property
    def PHASE_LO_D(self):
        """
        Get value of the LO phase in degrees for channel D
        """
        if (self.IQ_LO_D==1):
            return (self.PLL_LODIST_FSP_OUT3&3)*90
        else:
            return ((self.PLL_LODIST_FSP_OUT3&2)>>1)*180
    
    @PHASE_LO_D.setter
    def PHASE_LO_D(self, value):
        """
        Set value of the LO phase in degrees for channel D
        """
        if (self.IQ_LO_D==1):
            if not (value in [0, 90, 180, 270]):
                raise ValueError("Value must be [0,90,180 or 270], Divide By 2 in LO-DIST selected for channel D output.")
        else:
            if not (value in [0,180]):
                raise ValueError("Value must be [0,180], Divide By 1 in LO-DIST selected for channel D output.")
        self.PLL.PLL_METHODS.setLODIST(channel="D", EN=(self.PLL_LODIST_EN_OUT&8)>>3, EN_FLOCK=(self.FLOCK_LODIST_EN_OUT&8)>>3, IQ=value, phase=self.PLL_LODIST_FSP_OUT3&3, PROFILE=self.cfgNo)


    @property
    def N_FBDIV(self):
        return self.INTMOD+(2**16*self.FRACMODH+self.FRACMODL)*1.0/2**20*(1-self.INTMOD_EN)

    @N_FBDIV.setter
    def N_FBDIV(self, value):
        self.INTMOD=int(floor(value))
        FRACMOD=int(ceil(value-int(floor(value)))*2**20)
        FRACMODH=int(FRACMOD/2**16)
        FRACMODL=FRACMOD-FRACMODH
        self.FRACMODL=FRACMODL
        self.FRACMODH=FRACMODH

    @property
    def N_FFDIV(self):
        if (self.FFDIV_SEL==0):
            return 1
        else:
            return int(2**self.FF_MOD)

    @N_FFDIV.setter
    def N_FFDIV(self, value):
        self.FF_MOD=value
        if (self.FF_MOD>0):
            self.FFDIV_SEL=1
        else:
            self.FFDIV_SEL=0
      

    # Info functions

    def infoLPFConfig(self, printInfo=True):
        """ Get info about Loop-Filter configuration."""
        nChars = int(55)
        nChars_field=int(11)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("LoopFLT configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" C1 ",nChars_field-2) + "|" + self.chip.fixLen(" C2 ", nChars_field-1) +"|" + self.chip.fixLen(" C3 ", nChars_field-1) +"|" + self.chip.fixLen(" R2 ", nChars_field-1) +"|" +  self.chip.fixLen(" R3 ", nChars_field-1) +"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" %d " %(self.C1), nChars_field-2) + "|" + self.chip.fixLen(" %d " %(self.C2), nChars_field-1) +"|" + self.chip.fixLen(" %d " %(self.C3), nChars_field-1) +"|" + self.chip.fixLen(" %d " %(self.R2), nChars_field-1) +"|" +  self.chip.fixLen(" %d " %(self.R3), nChars_field-1) +"|\n"
        res += "|"+ self.chip.fixLen(" %.1fpF " %(self.C1*1.2), nChars_field-2) + "|" + self.chip.fixLen(" %.1fpF " %(self.C2*10+150), nChars_field-1) +"|" + self.chip.fixLen(" %.1fpF " %(self.C3*1.2+5), nChars_field-1) +"|" + self.chip.fixLen("Inf." if self.R2==0 else " %.1fkOhm " %(24.6/self.R2), nChars_field-1) +"|" +  self.chip.fixLen("Inf." if self.R3==0 else" %.1fkOhm " %(14.9/self.R3), nChars_field-1) +"|\n"

        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoVTUNEGENConfig(self, printInfo=True):
        """ Get info about VTUNE-Gen configuration."""

        nChars = int(39)
        nChars_field=int(13)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" VTUNE-Gen. configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("VTUNE_VCT", nChars_field-2) + "|" + self.chip.fixLen(" LPFSW ", 2*nChars_field-1) +"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" %d " %(self.VTUNE_VCT), nChars_field-2) + "|" + self.chip.fixLen(" %d " %(self.LPFSW), 2*nChars_field-1) +"|\n"
        VTUNE_VCT_CODE=self.VTUNE_VCT
        if (VTUNE_VCT_CODE==0):
            VTUNE_VCT_mV=300
        elif (VTUNE_VCT_CODE==1):
            VTUNE_VCT_mV=600
        elif (VTUNE_VCT_CODE==2):
            VTUNE_VCT_mV=750
        else:
            VTUNE_VCT_mV=900    
                
        res += "|"+self.chip.fixLen(" %dmV " %(VTUNE_VCT_mV), nChars_field-2) + "|" + self.chip.fixLen("PLL Loop Opened" if (self.LPFSW) else "PLL Loop Closed", 2*nChars_field-1) +"|\n"

        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoPFDCPConfig(self, printInfo=True):
        """ Get info about VTUNE-Gen configuration."""

        nChars = int(54)
        nChars_field=int(9)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" PFD-CP configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" FLIP ", nChars_field-2) + "|" + self.chip.fixLen(" DEL ", nChars_field-1) + "|" + self.chip.fixLen(" LD_VCT ", nChars_field-1) + "|" + self.chip.fixLen(" ICT_CP ", nChars_field-1) + "|" + self.chip.fixLen(" PULSE ", nChars_field-1) + "|" + self.chip.fixLen(" OFS ", nChars_field-1) +"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" %d " %(self.FLIP), nChars_field-2) + "|" + self.chip.fixLen(" %d " %(self.DEL), nChars_field-1) +"|" + self.chip.fixLen(" %d " %(self.LD_VCT), nChars_field-1) + "|"+ self.chip.fixLen(" %d " %(self.ICT_CP), nChars_field-1) + "|"+ self.chip.fixLen(" %d " %(self.PULSE), nChars_field-1) + "|"+ self.chip.fixLen(" %d " %(self.OFS), nChars_field-1) + "|\n"

        res += "|"+self.chip.fixLen("ON" if self.FLIP else "OFF", nChars_field-2) + "|" + self.chip.fixLen("%dps" %(440+50*self.DEL), nChars_field-1)+ "|" + self.chip.fixLen("%dmV" %(600+100*self.LD_VCT), nChars_field-1) + "|" + self.chip.fixLen("%.2fuA" %(self.ICT_CP*1.0/16*25), nChars_field-1) + "|" + self.chip.fixLen("%.2fuA" %(self.ICT_CP*1.0/16*25*self.PULSE), nChars_field-1) + "|" + self.chip.fixLen("%.2fuA" %(self.ICT_CP*1.0/16*25*self.OFS/4.0), nChars_field-1) +"|\n"
        
  
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoVCOConfig(self, printInfo=True):
        """ Get info about VCO configuration."""
        nChars = int(84)
        nChars_field=int(14)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" VCO configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"

        F_VCO=2**self.PLL_EN_FB_PDIV2*self.N_FBDIV*self.chip.fRef
        
        res += "|"+self.chip.fixLen("VDIV_SWVDD", nChars_field-2) + "|"+self.chip.fixLen("SPDUP_VCO", nChars_field-1) + "|"+self.chip.fixLen("VCO_AAC_EN", nChars_field-1) + "|"+self.chip.fixLen("VCO_AMP", nChars_field-1) + "|"+self.chip.fixLen("VCO_SEL", nChars_field-1) + "|"+self.chip.fixLen("VCO_FREQ", nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("%d" %(self.VDIV_SWVDD), nChars_field-2) + "|"+self.chip.fixLen("%d" %(self.SPDUP_VCO), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.VCO_AAC_EN), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.VCO_AMP), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.VCO_SEL), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.VCO_FREQ), nChars_field-1) + "|\n"
        VCO_SEL=self.VCO_SEL
        if (VCO_SEL==1):
            VCO_SEL_TXT="4.1-5.8GHz"
        elif (VCO_SEL==2):
            VCO_SEL_TXT="5.7-7.6GHz"
        elif (VCO_SEL==3):
            VCO_SEL_TXT="7.6-9.1GHz"
        else:
            VCO_SEL_TXT="EXT-LO"

        res += "|"+self.chip.fixLen("%dmV" %(self.VDIV_SWVDD*200+600), nChars_field-2) + "|"+self.chip.fixLen("ON" if (self.SPDUP_VCO) else "OFF", nChars_field-1) + "|"+self.chip.fixLen("ON" if (self.VCO_AAC_EN) else "OFF", nChars_field-1) + "|"+self.chip.fixLen("-", nChars_field-1) + "|"+self.chip.fixLen(VCO_SEL_TXT, nChars_field-1) + "|"+self.chip.fixLen("%.5fMHz" %(F_VCO/1.0e6), nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoFFDIVConfig(self, printInfo=True):
        """Get info about FFDIV configuration."""
        nChars=int(40)
        nChars_field=int(20)
        
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" FFDIV configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"

        res += "|"+self.chip.fixLen("FFDIV_SEL", nChars_field-2) + "|"+self.chip.fixLen("FF_MOD", nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("%d" %(self.FFDIV_SEL), nChars_field-2) + "|"+self.chip.fixLen("%d" %(self.FF_MOD), nChars_field-1) + "|\n"
        res += "|"+self.chip.fixLen("No Division" if (self.FFDIV_SEL==0) else "Input Freq. Divided", nChars_field-2) + "|"+self.chip.fixLen("Div. By 1" if (self.FFDIV_SEL==0 or self.FF_MOD==0) else "Div. By %d" %(int(2**self.FF_MOD)), nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        F_VCO=2**self.PLL_EN_FB_PDIV2*self.N_FBDIV*self.chip.fRef
        res += "|"+self.chip.fixLen("FIN=%.5fMHz, FOUT=%.5fMHz" %(F_VCO/1.0e6, F_VCO/self.N_FFDIV/1.0e6), 2*nChars_field-2) + "|\n"
        res += "-"*nChars+"\n"
        if printInfo:
            self.chip.log(res)
        else:
            return res
    

    def infoFBDIVConfig(self, printInfo=True):
        """Get info about FBDIV configuration."""
        nChars=int(80)
        nChars_field=int(20)
        
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" FBDIV configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"

        res += "|"+self.chip.fixLen("INTMOD_EN", nChars_field-2) + "|"+self.chip.fixLen("DITHER_EN", nChars_field-1) + "|"+self.chip.fixLen("SEL_SDMCLK", nChars_field-1) + "|"+self.chip.fixLen("REV_SDMCLK", nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("%d" %(self.INTMOD_EN), nChars_field-2) + "|"+self.chip.fixLen("%d" %(self.DITHER_EN), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.SEL_SDMCLK), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.REV_SDMCLK), nChars_field-1) + "|\n"
        res += "|"+self.chip.fixLen("Int-N Mode" if (self.INTMOD_EN==1) else "Frac-N Mode", nChars_field-2) + "|"+self.chip.fixLen("ON" if (self.DITHER_EN==1) else "OFF", nChars_field-1) + "|"+self.chip.fixLen("SDM CLK = FBDIV OUT" if (self.SEL_SDMCLK==0) else "SDMCLK = REF", nChars_field-1) + "|"+self.chip.fixLen("Normal" if (self.REV_SDMCLK==0) else "Reversed", nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        res+="|"+self.chip.fixLen("INTMOD", nChars_field-2) + "|"+self.chip.fixLen("FRACMODH", nChars_field-1) + "|"+self.chip.fixLen("FRACMODL", nChars_field-1) + "|"+self.chip.fixLen("N_FBDIV", nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        res+="|"+self.chip.fixLen("%d" %(self.INTMOD), nChars_field-2) + "|"+self.chip.fixLen("%d" %(self.FRACMODH), nChars_field-1) + "|"+self.chip.fixLen("%d" %(self.FRACMODL), nChars_field-1) + "|"+self.chip.fixLen("-", nChars_field-1) + "|\n"
        res+="|"+self.chip.fixLen("%d" %(self.INTMOD), nChars_field-2) + "|"+self.chip.fixLen("FRACMOD=2^16xFRACMODH+FRACMOD=%d" %(int(2**16*self.FRACMODH+self.FRACMODL)), 2*nChars_field-1) + "|"+self.chip.fixLen("%.8f" %(self.INTMOD+(2**16*self.FRACMODH+self.FRACMODL)*1.0/2**20*(1-self.INTMOD_EN)), nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoFLOCKConfig(self, printInfo=True):
        """ Get info about Fast-Lock Mode configuration."""

        LO_EN_OUT=self.FLOCK_LODIST_EN_OUT
        LO_EN_LIST=[]
        if (LO_EN_OUT&1):
            LO_EN_LIST.append("A")
        if ((LO_EN_OUT&2)>>1):
            LO_EN_LIST.append("B")
        if ((LO_EN_OUT&4)>>2):
            LO_EN_LIST.append("C")
        if ((LO_EN_OUT&8)>>2):
            LO_EN_LIST.append("D")

        nChars = int(100)
        nChars_field=int(20)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("Fast-Lock configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" FLOCK_C1 ",nChars_field-2) + "|" + self.chip.fixLen(" FLOCK_C2 ", nChars_field-1) +"|" + self.chip.fixLen(" FLOCK_C3 ", nChars_field-1) +"|" + self.chip.fixLen(" FLOCK_R2 ", nChars_field-1) +"|" +  self.chip.fixLen(" FLOCK_R3 ", nChars_field-1) +"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen(" %d " %(self.FLOCK_C1), nChars_field-2) + "|" + self.chip.fixLen(" %d " %(self.FLOCK_C2), nChars_field-1) +"|" + self.chip.fixLen(" %d " %(self.FLOCK_C3), nChars_field-1) +"|" + self.chip.fixLen(" %d " %(self.FLOCK_R2), nChars_field-1) +"|" +  self.chip.fixLen(" %d " %(self.FLOCK_R3), nChars_field-1) +"|\n" 

             
        
        
        res += "|"+self.chip.fixLen(" %.1fpF " %(self.FLOCK_C1*1.2), nChars_field-2) + "|" + self.chip.fixLen(" %.1fpF " %(self.FLOCK_C2*10+150), nChars_field-1) +"|" + self.chip.fixLen(" %.1fpF " %(self.FLOCK_C3*1.2+5), nChars_field-1) +"|" + self.chip.fixLen("Inf." if self.FLOCK_R2==0 else " %.1fkOhm " %(24.6/self.FLOCK_R2), nChars_field-1) +"|" +  self.chip.fixLen("Inf." if self.FLOCK_R3==0 else" %.1fkOhm " %(14.9/self.FLOCK_R3), nChars_field-1) + "|\n" 

        res += "-"*nChars+"\n"
        res+="|" + self.chip.fixLen(" FLOCK_PULSE ", nChars_field-2) +"|" + self.chip.fixLen(" FLOCK_OFS ", nChars_field-1) +"|" + self.chip.fixLen(" FLOCK_VCO_SPDUP ", nChars_field-1) +"|" + self.chip.fixLen(" FLOCK_N ", nChars_field-1) +"|" + self.chip.fixLen("FLOCK_LODIST_EN_OUT", nChars_field-1) +"|\n" 
        res += "-"*nChars+"\n"
        res+="|" + self.chip.fixLen(" %d " %(self.FLOCK_PULSE), nChars_field-2) +"|" +  self.chip.fixLen(" %d " %(self.FLOCK_OFS), nChars_field-1) +"|" +  self.chip.fixLen(" %d " %(self.FLOCK_VCO_SPDUP), nChars_field-1) +"|" + self.chip.fixLen("%d ref. cycles" %(self.FLOCK_N), nChars_field-1) +"|" + self.chip.fixLen(" %d " %(self.FLOCK_LODIST_EN_OUT), nChars_field-1) +"|\n"
        res+="|" + self.chip.fixLen("%.2fuA" %(self.ICT_CP*1.0/16*25*self.FLOCK_PULSE), nChars_field-2) + "|" + self.chip.fixLen("%.2fuA" %(self.ICT_CP*1.0/16*25*self.FLOCK_OFS/4.0), nChars_field-1) + "|" + self.chip.fixLen("ON" if (self.FLOCK_VCO_SPDUP) else "OFF", nChars_field-1) + "|"+ self.chip.fixLen("%.2fus" %(self.FLOCK_N*1.0e6/self.chip._fRef), nChars_field-1) + "|" + self.chip.fixLen("Enabled LOs: %s" %(', '.join(LO_EN_LIST)), nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        
        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoLODISTConfig(self, printInfo=True):
        """ Get info about LO-DIST configuration."""
        LODIST_EN_OUT=self.PLL_LODIST_EN_OUT
        FSP_OUT0=self.PLL_LODIST_FSP_OUT0
        FSP_OUT1=self.PLL_LODIST_FSP_OUT1
        FSP_OUT2=self.PLL_LODIST_FSP_OUT2
        FSP_OUT3=self.PLL_LODIST_FSP_OUT3
        
       

        F_VCO=2**self.PLL_EN_FB_PDIV2*self.N_FBDIV*self.chip.fRef
        
        EN_A=(LODIST_EN_OUT&1)>>0
        EN_B=(LODIST_EN_OUT&2)>>1
        EN_C=(LODIST_EN_OUT&4)>>2
        EN_D=(LODIST_EN_OUT&8)>>3

        N_DIV_A=2.0**(1-((FSP_OUT0&4)>>2))
        N_DIV_B=2.0**(1-((FSP_OUT1&4)>>2))
        N_DIV_C=2.0**(1-((FSP_OUT2&4)>>2))
        N_DIV_D=2.0**(1-((FSP_OUT3&4)>>2))
        
        F_LO_A=(F_VCO/self.N_FFDIV)/N_DIV_A
        F_LO_B=(F_VCO/self.N_FFDIV)/N_DIV_B
        F_LO_C=(F_VCO/self.N_FFDIV)/N_DIV_C
        F_LO_D=(F_VCO/self.N_FFDIV)/N_DIV_D

        
 
        nChars = int(110)
        nChars_field=int(11)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("LO-DIST configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("Channel", nChars_field-2) + "|" + self.chip.fixLen("Enable", nChars_field-1) + "|" + self.chip.fixLen("Div.Ratio", nChars_field-1) + "|" + self.chip.fixLen("Phase", nChars_field-1) + "|" + self.chip.fixLen("Freq.[MHz]", nChars_field-1) + "|" + self.chip.fixLen("Bit Fields", 5*nChars_field-1) + "|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("A", nChars_field-2) + "|" + self.chip.fixLen("%d" %(EN_A), nChars_field-1) + "|" + self.chip.fixLen("%d" %(N_DIV_A), nChars_field-1) + "|" + self.chip.fixLen("%d deg." %(90*(FSP_OUT0&3) if int(N_DIV_A)==2 else (0 if (FSP_OUT0&3)<=1 else 180)), nChars_field-1) + "|" + self.chip.fixLen("%.5f" %(F_LO_A/1.0e6) if (EN_A) else "-", nChars_field-1) + "|" + self.chip.fixLen("PLL_LO_DIST_EN_OUT[0]=%d, PLL_LO_DIST_FSP_OUT0=%d" %((LODIST_EN_OUT&1)>>0, FSP_OUT0), 5*nChars_field-1) + "|\n"
        res += "|"+self.chip.fixLen("B", nChars_field-2) + "|" + self.chip.fixLen("%d" %(EN_B), nChars_field-1) + "|" + self.chip.fixLen("%d" %(N_DIV_B), nChars_field-1) + "|" + self.chip.fixLen("%d deg." %(90*(FSP_OUT1&3) if int(N_DIV_B)==2 else (0 if (FSP_OUT1&3)<=1 else 180)), nChars_field-1) + "|" + self.chip.fixLen("%.5f" %(F_LO_B/1.0e6) if (EN_B) else "-", nChars_field-1) + "|"+  self.chip.fixLen("PLL_LO_DIST_EN_OUT[1]=%d, PLL_LO_DIST_FSP_OUT1=%d" %((LODIST_EN_OUT&2)>>1, FSP_OUT1), 5*nChars_field-1) + "|\n"
        res += "|"+self.chip.fixLen("C", nChars_field-2) + "|" + self.chip.fixLen("%d" %(EN_C), nChars_field-1) + "|" + self.chip.fixLen("%d" %(N_DIV_C), nChars_field-1) + "|" + self.chip.fixLen("%d deg." %(90*(FSP_OUT2&3) if int(N_DIV_C)==2 else (0 if (FSP_OUT2&3)<=1 else 180)), nChars_field-1) + "|" + self.chip.fixLen("%.5f" %(F_LO_C/1.0e6) if (EN_C) else "-", nChars_field-1) + "|"+ self.chip.fixLen("PLL_LO_DIST_EN_OUT[2]=%d, PLL_LO_DIST_FSP_OUT2=%d" %((LODIST_EN_OUT&4)>>2, FSP_OUT2), 5*nChars_field-1) + "|\n"
        res += "|"+self.chip.fixLen("D", nChars_field-2) + "|" + self.chip.fixLen("%d" %(EN_D), nChars_field-1) + "|" + self.chip.fixLen("%d" %(N_DIV_D), nChars_field-1) + "|" + self.chip.fixLen("%d deg." %(90*(FSP_OUT3&3) if int(N_DIV_D)==2 else (0 if (FSP_OUT3&3)<=1 else 180)), nChars_field-1) + "|" + self.chip.fixLen("%.5f" %(F_LO_D/1.0e6) if (EN_D) else "-", nChars_field-1) + "|" + self.chip.fixLen("PLL_LO_DIST_EN_OUT[3]=%d, PLL_LO_DIST_FSP_OUT3=%d" %((LODIST_EN_OUT&4)>>3, FSP_OUT3), 5*nChars_field-1) + "|\n"
        
        res += "-"*nChars+"\n"

        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoENABLEConfig(self, printInfo=True):
        """ Get info about PLL_ENABLE configuration."""
        nChars = int(40)
        nChars_field=int(10)
        res = "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("PLL_ENABLE configuration", nChars-2)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("Bitfield", 3*nChars_field-2)+"|"+self.chip.fixLen("Value", nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        res += "|"+self.chip.fixLen("PLL_LODIST_EN_BIAS", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_LODIST_EN_BIAS), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_LODIST_EN_DIV2IQ", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_LODIST_EN_DIV2IQ), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_VTUNE_COMP", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_VTUNE_COMP), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_LD", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_LD), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_PFD", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_PFD), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_CP", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_CP), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_CPOFS", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_CPOFS), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_VCO", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_VCO), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_FFDIV", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_FFDIV), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_FB_PDIV2", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_FB_PDIV2), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_FFCORE", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_FFCORE), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_EN_FBDIV", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_EN_FBDIV), nChars_field-1)+"|\n"
        res += "|"+self.chip.fixLen("PLL_SDM_CLK_EN", 3*nChars_field-2)+"|"+self.chip.fixLen("%d" %(self.PLL_SDM_CLK_EN), nChars_field-1)+"|\n"
        res += "-"*nChars+"\n"
        
        if printInfo:
            self.chip.log(res)
        else:
            return res

    def infoConfig(self, printInfo=True):
        nChars = int(110)
        if (printInfo):
            self.chip.log(self.chip.fixLen("PLL Profile %d Configuration" %(self.cfgNo), nChars))
            self.chip.log("*"*nChars)
            self.infoENABLEConfig(printInfo=printInfo)
            self.infoPFDCPConfig(printInfo=printInfo)
            self.infoLPFConfig(printInfo=printInfo)
            self.infoFLOCKConfig(printInfo=printInfo)
            self.infoFBDIVConfig(printInfo=printInfo)
            self.infoVCOConfig(printInfo=printInfo)
            self.infoFFDIVConfig(printInfo=printInfo)
            self.infoLODISTConfig(printInfo=printInfo)
            self.chip.log("*"*nChars)
        else:
            res=self.chip.fixLen("PLL Profile %d Configuration" %(self.cfgNo), nChars)+"\n"
            res+=("*"*nChars+"\n")
            res+=self.infoENABLEConfig(printInfo=printInfo)
            res+=self.infoPFDCPConfig(printInfo=printInfo)
            res+=self.infoLPFConfig(printInfo=printInfo)
            res+=self.infoFLOCKConfig(printInfo=printInfo)
            res+=self.infoFBDIVConfig(printInfo=printInfo)
            res+=self.infoVCOConfig(printInfo=printInfo)
            res+=self.infoFFDIVConfig(printInfo=printInfo)
            res+=self.infoLODISTConfig(printInfo=printInfo)
            res+=("*"*nChars+"\n")
            return res
