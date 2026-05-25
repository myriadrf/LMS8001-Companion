import math
from time import sleep
from timeit import default_timer as timer

LMS8001_C1_STEP=1.2e-12
LMS8001_C2_STEP=10.0e-12
LMS8001_C3_STEP=1.2e-12
LMS8001_C2_FIX=150.0e-12
LMS8001_C3_FIX=5.0e-12
LMS8001_R2_0=24.6e3
LMS8001_R3_0=14.9e3
    
class PLL_METHODS(object):

    def __init__(self, chip, fRef):
        self.chip = chip
        self.fRef = fRef

    def estim_KVCO(self, FIT_KVCO=True, PROFILE=0):

        # Check VCO_SEL and VCO_FREQ
        reg_pll_vco_freq=self.chip.getRegisterByName('PLL_VCO_FREQ_'+str(PROFILE))
        reg_pll_vco_cfg=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        vco_sel=reg_pll_vco_cfg['VCO_SEL_'+str(PROFILE)+'<1:0>']
        vco_freq=reg_pll_vco_freq['VCO_FREQ_'+str(PROFILE)+'<7:0>']

        if not (FIT_KVCO):
            # Use Average for KVCO in Calculations
            if (vco_sel==1):
                KVCO_avg=44.404e6
            elif (vco_sel==2):
                KVCO_avg=33.924e6    
            elif (vco_sel==3):
                KVCO_avg=41.455e6
            else:
                self.chip.log('Ext. LO selected in PLL_PROFILE.')
                return None
        else:
            # Use Fitted Values for KVCO in Calculations
            # Changed on 17.05.2017. with new results
            # Following equations fitted for VTUNE=0.7 V
            CBANK=vco_freq
            if (vco_sel==1):
                KVCO_avg=27.296e6 * (2.26895e-10*CBANK**4+4.98467e-9*CBANK**3+9.01884e-6*CBANK**2+3.69804e-3*CBANK**1+1.01283e+00)
            elif (vco_sel==2):
                KVCO_avg=23.277e6 * (8.38795e-11*CBANK**4+2.20202e-08*CBANK**3+3.68009e-06*CBANK**2+3.22264e-03*CBANK**1+1.01093e+00)    
            elif (vco_sel==3):
                KVCO_avg=29.110e6 * (-1.54988e-11*CBANK**4+4.27489e-08*CBANK**3+5.26971e-06*CBANK**2+2.83453e-03*CBANK**1+9.94192e-01)
            else:
                self.chip.log('Ext. LO selected in PLL_PROFILE.')
                return None
                
        return KVCO_avg

    def calc_ideal_LPF(self, fc, PM_deg, Icp, KVCO_HzV, N, gamma=1.045, T31=0.1):

        PM_rad=PM_deg*math.pi/180
        wc=2*math.pi*fc    

        Kphase=Icp/(2*math.pi)
        Kvco=2*math.pi*KVCO_HzV

        # Approx. formula, Dean Banerjee
        T1=(1.0/math.cos(PM_rad)-math.tan(PM_rad))/(wc*(1+T31))

        T3=T1*T31;
        T2=gamma/((wc**2)*(T1+T3));
    
        A0=(Kphase*Kvco)/((wc**2)*N)*math.sqrt((1+(wc**2)*(T2**2))/((1+(wc**2)*(T1**2))*(1+(wc**2)*(T3**2))));
        A2=A0*T1*T3;
        A1=A0*(T1+T3);
    
        C1=A2/(T2**2)*(1+math.sqrt(1+T2/A2*(T2*A0-A1)));
        C3=(-(T2**2)*(C1**2)+T2*A1*C1-A2*A0)/((T2**2)*C1-A2);
        C2=A0-C1-C3;
        R2=T2/C2;
        R3=A2/(C1*C3*T2);

        LPF_vals=dict()
        LPF_vals['C1']=C1
        LPF_vals['C2']=C2
        LPF_vals['C3']=C3
        LPF_vals['R2']=R2
        LPF_vals['R3']=R3
        return LPF_vals
    

    def calc_real_LPF(self, LPF_IDEAL_VALS):
        C1_cond=(LMS8001_C1_STEP<=LPF_IDEAL_VALS['C1']<=15*LMS8001_C1_STEP)
        C2_cond=(LMS8001_C2_FIX<=LPF_IDEAL_VALS['C2']<=LMS8001_C2_FIX+15*LMS8001_C2_STEP)
        C3_cond=(LMS8001_C3_FIX+LMS8001_C3_STEP<=LPF_IDEAL_VALS['C3']<=LMS8001_C3_FIX+15*LMS8001_C3_STEP)
        R2_cond=(LMS8001_R2_0/15.0<=LPF_IDEAL_VALS['R2']<=LMS8001_R2_0)
        R3_cond=(LMS8001_R3_0/15.0<=LPF_IDEAL_VALS['R3']<=LMS8001_R3_0)

        LPFvals_OK=(C1_cond and C2_cond and C3_cond and R2_cond and R3_cond)    
        LPF_REAL_VALS=dict()
        if (LPFvals_OK):

            C1_CODE=int(round(LPF_IDEAL_VALS['C1']/LMS8001_C1_STEP))
            C2_CODE=int(round((LPF_IDEAL_VALS['C2']-LMS8001_C2_FIX)/LMS8001_C2_STEP))
            C3_CODE=int(round((LPF_IDEAL_VALS['C3']-LMS8001_C3_FIX)/LMS8001_C3_STEP))
            C1_CODE=int(min(max(C1_CODE,0),15))
            C2_CODE=int(min(max(C2_CODE,0),15))
            C3_CODE=int(min(max(C3_CODE,0),15))
    
            R2_CODE=int(round(LMS8001_R2_0/LPF_IDEAL_VALS['R2']))
            R3_CODE=int(round(LMS8001_R3_0/LPF_IDEAL_VALS['R3']))
            R2_CODE=min(max(R2_CODE,1),15)
            R3_CODE=min(max(R3_CODE,1),15)
                
            LPF_REAL_VALS['C1_CODE']=C1_CODE
            LPF_REAL_VALS['C2_CODE']=C2_CODE
            LPF_REAL_VALS['C3_CODE']=C3_CODE
            LPF_REAL_VALS['R2_CODE']=R2_CODE
            LPF_REAL_VALS['R3_CODE']=R3_CODE

        return (LPFvals_OK, LPF_REAL_VALS)
            


    def setSDM(self, DITHER_EN=0, SEL_SDMCLK=0, REV_SDMCLK=0, PROFILE=0):
        # Sets Sigma-Delta Modulator Config.
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_PLL_SDM_CFG=self.chip.getRegisterByName('PLL_SDM_CFG_'+str(PROFILE))    
        reg_PLL_SDM_CFG['DITHER_EN_'+str(PROFILE)]=DITHER_EN
        reg_PLL_SDM_CFG['SEL_SDMCLK_'+str(PROFILE)]=SEL_SDMCLK
        reg_PLL_SDM_CFG['REV_SDMCLK_'+str(PROFILE)]=REV_SDMCLK
        
        self.chip.setImmediateMode(Imd_Mode)

    def setVCOBIAS(self, EN=0, BYP_VCOREG=1, CURLIM_VCOREG=1, SPDUP_VCOREG=0, VDIV_VCOREG=32):
        """Sets VCO Bias Parameters"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        regVCOBIAS=self.chip.getRegisterByName('PLL_VREG')
        regVCOBIAS['EN_VCOBIAS']=EN
        regVCOBIAS['BYP_VCOREG']=BYP_VCOREG
        regVCOBIAS['CURLIM_VCOREG']=CURLIM_VCOREG
        regVCOBIAS['SPDUP_VCOREG']=SPDUP_VCOREG
        regVCOBIAS['VDIV_VCOREG<7:0>']=VDIV_VCOREG

        self.chip.setImmediateMode(Imd_Mode)


    def setSPDUP_VCO(self, SPDUP=0, PROFILE=0):
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
        
        reg_VCO_CFG=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        reg_VCO_CFG['SPDUP_VCO_'+str(PROFILE)]=SPDUP

        self.chip.setImmediateMode(Imd_Mode)

    
    def setSPDUP_VCOREG(self, SPDUP=0):
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
        
        regVCOBIAS=self.chip.getRegisterByName('PLL_VREG')
        regVCOBIAS['SPDUP_VCOREG']=SPDUP
        
        self.chip.setImmediateMode(Imd_Mode)
        
    def setXBUF(self, EN=0, BYPEN=0, SLFBEN=1):
        """Sets XBUF Configuration"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
    
        regXBUF=self.chip.getRegisterByName('PLL_CFG_XBUF')
        regXBUF['PLL_XBUF_EN']=EN
        regXBUF['PLL_XBUF_SLFBEN']=SLFBEN
        regXBUF['PLL_XBUF_BYPEN']=BYPEN

        self.chip.setImmediateMode(Imd_Mode)

    def setCP(self, PULSE=4, OFS=0, ICT_CP=16, PROFILE=0):
        """Sets CP Parameters"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
    
        reg_CP_CFG0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        reg_CP_CFG0['PULSE_'+str(PROFILE)+'<5:0>']=PULSE
        reg_CP_CFG0['OFS_'+str(PROFILE)+'<5:0>']=OFS
    
        reg_CP_CFG1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        reg_CP_CFG1['ICT_CP_'+str(PROFILE)+'<4:0>']=ICT_CP

        reg_PLL_ENABLE=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
        if (OFS>0):    
            reg_PLL_ENABLE['PLL_EN_CPOFS_'+str(PROFILE)]=1
        else:
            reg_PLL_ENABLE['PLL_EN_CPOFS_'+str(PROFILE)]=0
        self.chip.setImmediateMode(Imd_Mode)

    def getCP(self, PROFILE=0):
        """Returns CP Parameters"""
        d=dict()
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
    
        reg_CP_CFG0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        d["PULSE"]=reg_CP_CFG0['PULSE_'+str(PROFILE)+'<5:0>']
        d["OFS"]=reg_CP_CFG0['OFS_'+str(PROFILE)+'<5:0>']
    
        reg_CP_CFG1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        d["ICT_CP"]=reg_CP_CFG1['ICT_CP_'+str(PROFILE)+'<4:0>']

        reg_PLL_ENABLE=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
            
        d["EN_CPOFS"]=reg_PLL_ENABLE['PLL_EN_CPOFS_'+str(PROFILE)]
        
        
        self.chip.setImmediateMode(Imd_Mode)
        
        return d

    def setCP_FLOCK(self, PULSE=4, OFS=0, PROFILE=0):
        reg_pll_flock_cfg2=self.chip.getRegisterByName('PLL_FLOCK_CFG2_'+str(PROFILE))
        reg_pll_flock_cfg2['FLOCK_PULSE_'+str(PROFILE)+'<5:0>']=int(PULSE)
        reg_pll_flock_cfg2['FLOCK_OFS_'+str(PROFILE)+'<5:0>']=int(OFS)

    def setLD(self, LD_VCT=2, PROFILE=0):
        """Sets Lock-Detector's Comparator Threashold"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
    
        reg_pll_enable=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
        reg_pll_enable['PLL_EN_LD_'+str(PROFILE)]=1
        reg_pll_cp_cfg1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        reg_pll_cp_cfg1['LD_VCT_'+str(PROFILE)+'<1:0>']=LD_VCT

        self.chip.setImmediateMode(Imd_Mode)

    def setPFD(self, DEL=0, FLIP=0, PROFILE=0):
        """Sets PFD Parameters"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_CP_CFG0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        reg_CP_CFG0['FLIP_'+str(PROFILE)]=FLIP
        reg_CP_CFG0['DEL_'+str(PROFILE)+'<1:0>']=DEL

        self.chip.setImmediateMode(Imd_Mode)
    

    def setVTUNE_VCT(self, VTUNE_VCT, PROFILE=0):
        reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
        reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']=VTUNE_VCT
    
    def openPLL(self, VTUNE_VCT=2, PROFILE=0, dbgMode=False):
        """Breaks the PLL Loop and sets the fixed VCO tuning voltage"""
        
        VTUNE_VCT=int(VTUNE_VCT)
        VTUNE_DICT={0:300, 1:600, 2:750, 3:900}
        if (VTUNE_VCT>3):
            VTUNE_VCT=3
        elif (VTUNE_VCT<0):
            VTUNE_VCT=0


        reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
        reg_pll_lpf_cfg2['LPFSW_'+str(PROFILE)]=1
        reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']=VTUNE_VCT

        if (dbgMode):
            self.chip.log("PLL Loop Broken. VTUNE=%.2f mV" %(VTUNE_DICT[VTUNE_VCT]))
    
    def closePLL(self, PROFILE=0):
        """Closes PLL Loop"""
        reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
        reg_pll_lpf_cfg2['LPFSW_'+str(PROFILE)]=0
        reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)]=2
    

    def setVCO(self, SEL=3, FREQ=128, AMP=1, VCO_AAC_EN=True, VDIV_SWVDD=2, PROFILE=0):
        """Sets VCO Parameters"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_VCO_FREQ=self.chip.getRegisterByName('PLL_VCO_FREQ_'+str(PROFILE))
        reg_VCO_FREQ['VCO_FREQ_'+str(PROFILE)+'<7:0>']=FREQ
    
        reg_VCO_CFG=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        if (VCO_AAC_EN):
            reg_VCO_CFG['VCO_AAC_EN_'+str(PROFILE)]=1
        else:
            reg_VCO_CFG['VCO_AAC_EN_'+str(PROFILE)]=0

        reg_VCO_CFG['VCO_SEL_'+str(PROFILE)+'<1:0>']=SEL
        reg_VCO_CFG['VCO_AMP_'+str(PROFILE)+'<6:0>']=AMP
        reg_VCO_CFG['VDIV_SWVDD_'+str(PROFILE)+'<1:0>']=VDIV_SWVDD
    
        self.chip.setImmediateMode(Imd_Mode)

    def setFFDIV(self, FFMOD=0, PROFILE=0):
        """Sets FF-DIV Modulus"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_PLL_ENABLE=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
        if (FFMOD>0):
            reg_PLL_ENABLE['PLL_EN_FFCORE_'+str(PROFILE)]=1
        else:
            reg_PLL_ENABLE['PLL_EN_FFCORE_'+str(PROFILE)]=0

        reg_FF_CFG=self.chip.getRegisterByName('PLL_FF_CFG_'+str(PROFILE))
        if (FFMOD>0):
            reg_FF_CFG['FFDIV_SEL_'+str(PROFILE)]=1
        else:
            reg_FF_CFG['FFDIV_SEL_'+str(PROFILE)]=0

        reg_FF_CFG['FFCORE_MOD_'+str(PROFILE)+'<1:0>']=FFMOD
        reg_FF_CFG['FF_MOD_'+str(PROFILE)+'<1:0>']=FFMOD

        self.chip.setImmediateMode(Imd_Mode)

    def setFBDIV(self, N_INT, N_FRAC, IntN_Mode=False, PROFILE=0):
        """Sets FB-DIV Parameters"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_SDM_CFG=self.chip.getRegisterByName('PLL_SDM_CFG_'+str(PROFILE))
        if (IntN_Mode):
            reg_SDM_CFG['INTMOD_EN_'+str(PROFILE)]=1
            N_FRAC_H=0
            N_FRAC_L=0
        else:
            reg_SDM_CFG['INTMOD_EN_'+str(PROFILE)]=0
            N_FRAC_H=int(math.floor(N_FRAC/2**16))
            N_FRAC_L=int(N_FRAC-N_FRAC_H*(2**16))

        #if (DITHER_EN):
        #    reg_SDM_CFG['DITHER_EN_'+str(PROFILE)]=1
        #else:
        #    reg_SDM_CFG['DITHER_EN_'+str(PROFILE)]=0

        reg_SDM_CFG['INTMOD_'+str(PROFILE)+'<9:0>']=N_INT
    
    

        reg_FRACMODL=self.chip.getRegisterByName('PLL_FRACMODL_'+str(PROFILE))
        reg_FRACMODL['FRACMODL_'+str(PROFILE)+'<15:0>']=N_FRAC_L
    
        reg_FRACMODH=self.chip.getRegisterByName('PLL_FRACMODH_'+str(PROFILE))
        reg_FRACMODH['FRACMODH_'+str(PROFILE)+'<3:0>']=N_FRAC_H

        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1

        self.chip.setImmediateMode(Imd_Mode)

    def setLPF(self, C1=8, C2=8, R2=1, C3=8, R3=1, PROFILE=0):
        """Sets LPF Element Values"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_PLL_LPF_CFG1=self.chip.getRegisterByName('PLL_LPF_CFG1_'+str(PROFILE))
        reg_PLL_LPF_CFG1['R3_'+str(PROFILE)+'<3:0>']=R3
        reg_PLL_LPF_CFG1['R2_'+str(PROFILE)+'<3:0>']=R2
        reg_PLL_LPF_CFG1['C2_'+str(PROFILE)+'<3:0>']=C2
        reg_PLL_LPF_CFG1['C1_'+str(PROFILE)+'<3:0>']=C1

        reg_PLL_LPF_CFG2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
        reg_PLL_LPF_CFG2['C3_'+str(PROFILE)+'<3:0>']=C3

        self.chip.setImmediateMode(Imd_Mode)

    def setLPF_FLOCK(self, C1=8, C2=8, R2=1, C3=8, R3=1, PROFILE=0):
        reg_pll_flock_cfg1=self.chip.getRegisterByName('PLL_FLOCK_CFG1_'+str(PROFILE))
        reg_pll_flock_cfg1['FLOCK_R3_'+str(PROFILE)+'<3:0>']=int(R3)
        reg_pll_flock_cfg1['FLOCK_R2_'+str(PROFILE)+'<3:0>']=int(R2)
        reg_pll_flock_cfg1['FLOCK_C1_'+str(PROFILE)+'<3:0>']=int(C1)
        reg_pll_flock_cfg1['FLOCK_C2_'+str(PROFILE)+'<3:0>']=int(C2)

        reg_pll_flock_cfg2=self.chip.getRegisterByName('PLL_FLOCK_CFG2_'+str(PROFILE))
        reg_pll_flock_cfg2['FLOCK_C3_'+str(PROFILE)+'<3:0>']=int(C3)

    def setLODIST(self, channel, EN=True, EN_FLOCK=False, IQ=True, phase=0, PROFILE=0):
        """Sets LODIST Configuration"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        channel_dict={'A':0, 'B':1, 'C':2, 'D':3}
        phase_dict={0:0, 90:1, 180:2, 270:3}
    
        if (channel not in channel_dict.keys()):
            self.chip.log("Not valid LO-DIST channel name.")
            return None

        if (phase not in phase_dict.keys()):
            self.chip.log("Not valid LO-DIST phase value.")
            return None
    
        reg_pll_enable=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
        

        reg_lodist_cfg=self.chip.getRegisterByName('PLL_LODIST_CFG_'+str(PROFILE))
        val_old=reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']
        if (EN):
            reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']=val_old|int(2**channel_dict[channel])
            reg_pll_enable['PLL_LODIST_EN_BIAS_'+str(PROFILE)]=1
        else:
            reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']=val_old&(15-int(2**channel_dict[channel]))
        
            # Disable LO DIST Bias if not needed
            if (reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']==0):
                reg_pll_enable['PLL_LODIST_EN_BIAS_'+str(PROFILE)]=0
                reg_pll_enable['PLL_LODIST_EN_DIV2IQ_'+str(PROFILE)]=0
    
        if (IQ==True):
            reg_lodist_cfg['PLL_LODIST_FSP_OUT'+str(channel_dict[channel])+'_'+str(PROFILE)+'<2:0>']=phase_dict[phase]
            reg_pll_enable['PLL_LODIST_EN_DIV2IQ_'+str(PROFILE)]=1
        else:
            reg_lodist_cfg['PLL_LODIST_FSP_OUT'+str(channel_dict[channel])+'_'+str(PROFILE)+'<2:0>']=phase_dict[phase]+4
            A_IQ=reg_lodist_cfg['PLL_LODIST_FSP_OUT0_'+str(PROFILE)+'<2:0>']
            A_EN=reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']&1
            
            B_IQ=reg_lodist_cfg['PLL_LODIST_FSP_OUT1_'+str(PROFILE)+'<2:0>']
            B_EN=reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']&2
            
            C_IQ=reg_lodist_cfg['PLL_LODIST_FSP_OUT2_'+str(PROFILE)+'<2:0>']
            C_EN=reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']&4
            
            D_IQ=reg_lodist_cfg['PLL_LODIST_FSP_OUT3_'+str(PROFILE)+'<2:0>']
            D_EN=reg_lodist_cfg['PLL_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']&8

            # Disable DivBy2 IQ Gen. Core if not needed
            if ((A_IQ>=4 or A_EN==0) and (B_IQ>=4 or B_EN==0) and (C_IQ>=4 or C_EN==0) and (D_IQ>=4 or D_EN==0)):
                reg_pll_enable['PLL_LODIST_EN_DIV2IQ_'+str(PROFILE)]=0

        # Enable Output of desired LO channel during the Fast-Lock Operating Mode of LMS8001-PLL if EN_FLOCK=True
        if (EN_FLOCK):
            if (channel=='A'):
                LO_FLOCK_EN_MASK=1
            elif (channel=='B'):
                LO_FLOCK_EN_MASK=2
            elif (channel=='C'):
                LO_FLOCK_EN_MASK=4
            else:
                LO_FLOCK_EN_MASK=8
        else:
            LO_FLOCK_EN_MASK=0
        
        reg_pll_flock_cfg3=self.chip.getRegisterByName('PLL_FLOCK_CFG3_'+str(PROFILE))
        LO_FLOCK_EN=reg_pll_flock_cfg3['FLOCK_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']
        reg_pll_flock_cfg3['FLOCK_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']=LO_FLOCK_EN | LO_FLOCK_EN_MASK
                    
        # Set Back to initial value of ImmediateMode
        self.chip.setImmediateMode(Imd_Mode)

    def setFLOCK(self, BWEF, LoopBW=600.0e3, PM=50.0, FLOCK_N=200, Ch_EN=[], METHOD='SIMPLE', FIT_KVCO=True, FLOCK_VCO_SPDUP=1, PROFILE=0, dbgMode=False):
        """
        Automatically calculates Fast-Lock Mode parameters from BWEF argument. BWEF-BandWidth Extension Factor
        METHOD='SIMPLE'
            Clips charge pump current settings in Fast-Lock Operating Mode if ICP_NORMAL*BWEF^2 is greater than (ICP)max.
            Only changes the values of LoopFilter resistors during Fast-Lock mode.
            Capacitor values are the same as in NORMAL operating mode.
        METHOD=='SMART'
            Takes the phase-margin argument PM to calculate LoopFilter elements and maximum pulse CP current which will give 
            the PLL loop bandwidth value of LoopBW with desired phase margin PM.
        """
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

    
        LO_OUT_EN=0
        if ('A' in Ch_EN):
            LO_OUT_EN+=1
        if ('B' in Ch_EN):
            LO_OUT_EN+=2
        if ('C' in Ch_EN):
            LO_OUT_EN+=4
        if ('D' in Ch_EN):
            LO_OUT_EN+=8
        
        if (METHOD not in ['SIMPLE', 'SMART']):
            self.chip.log("Bad Fast-Lock Mode Optimization Method. METHOD='SIMPLE' or METHOD='SMART'.")
            return  False

        reg_cp_cfg0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        PULSE=reg_cp_cfg0['PULSE_'+str(PROFILE)+'<5:0>']
        OFS=reg_cp_cfg0['OFS_'+str(PROFILE)+'<5:0>']
        reg_pll_cp_cfg1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        ICT_CP_INIT=reg_pll_cp_cfg1['ICT_CP_'+str(PROFILE)+'<4:0>']

        reg_pll_flock_cfg3=self.chip.getRegisterByName('PLL_FLOCK_CFG3_'+str(PROFILE))
        reg_pll_flock_cfg3['FLOCK_LODIST_EN_OUT_'+str(PROFILE)+'<3:0>']=LO_OUT_EN
        reg_pll_flock_cfg3['FLOCK_VCO_SPDUP_'+str(PROFILE)]=0
        reg_pll_flock_cfg3['FLOCK_N_'+str(PROFILE)+'<9:0>']=min(FLOCK_N, 1023)
        reg_pll_flock_cfg3['FLOCK_VCO_SPDUP_'+str(PROFILE)]=FLOCK_VCO_SPDUP
        
        if (METHOD=='SIMPLE'):
            reg_lpf_cfg1=self.chip.getRegisterByName('PLL_LPF_CFG1_'+str(PROFILE))
            R3=reg_lpf_cfg1['R3_'+str(PROFILE)+'<3:0>']
            R2=reg_lpf_cfg1['R2_'+str(PROFILE)+'<3:0>']
            C1=reg_lpf_cfg1['C1_'+str(PROFILE)+'<3:0>']
            C2=reg_lpf_cfg1['C2_'+str(PROFILE)+'<3:0>']

            reg_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
            C3=reg_lpf_cfg2['C3_'+str(PROFILE)+'<3:0>']

            R3_FLOCK=min(round(R3*BWEF), 15)
            # R3_FLOCK=min(round(R3*math.sqrt(BWEF)), 15)
            R2_FLOCK=min(round(R2*BWEF), 15)
    
            PULSE_FLOCK=min(round(PULSE*BWEF**2), 63)
            #PULSE_FLOCK=min(round(PULSE*BWEF), 63)
            OFS_FLOCK=min(round(OFS*PULSE_FLOCK/PULSE), 63)
            #OFS_FLOCK=OFS
            
            self.setLPF_FLOCK(C1=C1, C2=C2, R2=R2_FLOCK, C3=C3, R3=R3_FLOCK, PROFILE=PROFILE)
            self.setCP_FLOCK(PULSE=PULSE_FLOCK, OFS=OFS_FLOCK, PROFILE=PROFILE)

            
        else:
            fc=LoopBW/1.65
            
            # Sweep CP PULSE values and find the first one that result with implementable LPF values for desired PLL dynamics in Fast-Lock Mode
            cp_pulse_vals=range(PULSE,64)
            cp_pulse_vals.reverse()
    
            # Estimate the value of KVCO for settings in the PLL Profile PROFILE
            KVCO_avg=self.estim_KVCO(FIT_KVCO=FIT_KVCO, PROFILE=PROFILE)

            # Read Feedback-Divider Modulus
            N=self.getNDIV(PROFILE=PROFILE)
    
        
            for cp_pulse in cp_pulse_vals:
                # Calculate CP Current Value
                Icp=ICT_CP_INIT*25.0e-6/16.0*cp_pulse
                
                gamma=1.045 
                T31=0.1
        
                LPF_IDEAL_VALS=self.calc_ideal_LPF(fc=fc, PM_deg=PM, Icp=Icp, KVCO_HzV=KVCO_avg, N=N, gamma=gamma, T31=T31)
                (LPFvals_OK, LPF_REAL_VALS)=self.calc_real_LPF(LPF_IDEAL_VALS)

            
                if (LPFvals_OK):
                    # Set CP Pulse Current to the optimized value
                    self.setCP_FLOCK(PULSE=cp_pulse, OFS=min(round(OFS*cp_pulse/PULSE),63), PROFILE=PROFILE)
                    # self.setCP_FLOCK(PULSE=cp_pulse, OFS=0, PROFILE=PROFILE)
                    # Set LPF Components to the optimized values
                    self.setLPF_FLOCK(C1=LPF_REAL_VALS['C1_CODE'], C2=LPF_REAL_VALS['C2_CODE'], R2=LPF_REAL_VALS['R2_CODE'], C3=LPF_REAL_VALS['C3_CODE'], R3=LPF_REAL_VALS['R3_CODE'], PROFILE=PROFILE)
                    
                
                    if (dbgMode):
                        self.chip.log('PLL LoopBW Optimization finished successfuly.')
                        self.chip.log('-'*45)
                        self.chip.log('\tIcp=%.2f uA' %(Icp/1.0e-6))
                        self.chip.log('\tUsed Value for KVCO=%.2f MHz/V' %(KVCO_avg/1.0e6))
                        self.chip.log('\tNDIV=%.2f' % (N))
                        self.chip.log('-'*45)
                        self.chip.log('')
                        self.chip.log('Ideal LPF Values')
                        self.chip.log('-'*45)
                        self.chip.log('\tC1= %.2f pF' %(LPF_IDEAL_VALS['C1']/1.0e-12))
                        self.chip.log('\tC2= %.2f pF' %(LPF_IDEAL_VALS['C2']/1.0e-12))
                        self.chip.log('\tR2= %.2f kOhm' %(LPF_IDEAL_VALS['R2']/1.0e3))
                        self.chip.log('\tC3= %.2f pF' %(LPF_IDEAL_VALS['C3']/1.0e-12))
                        self.chip.log('\tR3= %.2f kOhm' %(LPF_IDEAL_VALS['R3']/1.0e3))
                        self.chip.log('')
                    return True

        self.chip.setImmediateMode(Imd_Mode)
        return True
        
    def disablePLL(self, PROFILE=0):
        """Disables PLL Blocks, XBUF and VCO Bias"""
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        # Disable VCO-BIAS
        self.setVCOBIAS(EN=0)


        # Disable XBUF
        self.setXBUF(EN=0)

        # Disable PLL core circuits
        reg_pll_enable=self.chip.getRegisterByName("PLL_ENABLE_"+str(PROFILE))
        reg_pll_enable['PLL_EN_VTUNE_COMP_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_LD_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_PFD_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_CP_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_CPOFS_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_VCO_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_FFDIV_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_FBDIV_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]=0
        reg_pll_enable['PLL_SDM_CLK_EN_'+str(PROFILE)]=0

        self.chip.setImmediateMode(Imd_Mode)

    def enablePLL(self, PDIV2=False, IntN_Mode=False, XBUF_SLFBEN=1, PROFILE=0):
        """Enables VCO Bias, XBUF and PLL Blocks"""

        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        # Define PLL Config
        # Enable VCO Biasing Block        
        reg_pll_vreg=self.chip.getRegisterByName("PLL_VREG")
        reg_pll_vreg['EN_VCOBIAS']=1
        

        # Enable XBUF
        # Sets SLFBEN, when TCXO is AC-coupled to LMS8001 IC REFIN
        reg_cfg_xbuf=self.chip.getRegisterByName("PLL_CFG_XBUF")
        reg_cfg_xbuf['PLL_XBUF_EN']=1
        reg_cfg_xbuf['PLL_XBUF_SLFBEN']=XBUF_SLFBEN

        # Define Desired PLL Profile
        # Enable Blocks
        reg_pll_enable=self.chip.getRegisterByName("PLL_ENABLE_"+str(PROFILE))
        reg_pll_enable['PLL_EN_VTUNE_COMP_'+str(PROFILE)]=1
        reg_pll_enable['PLL_EN_LD_'+str(PROFILE)]=1
        reg_pll_enable['PLL_EN_PFD_'+str(PROFILE)]=1
        reg_pll_enable['PLL_EN_CP_'+str(PROFILE)]=1
        reg_pll_enable['PLL_EN_VCO_'+str(PROFILE)]=1
        reg_pll_enable['PLL_EN_FFDIV_'+str(PROFILE)]=1
        reg_pll_enable['PLL_EN_FBDIV_'+str(PROFILE)]=1
    
        if (PDIV2):
            reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]=1
        else:
            reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]=0
        reg_pll_enable['PLL_EN_FBDIV_'+str(PROFILE)]=1

        if (IntN_Mode):
            reg_pll_enable['PLL_SDM_CLK_EN_'+str(PROFILE)]=0
        else:
            reg_pll_enable['PLL_SDM_CLK_EN_'+str(PROFILE)]=1

        self.chip.setImmediateMode(Imd_Mode)

    def calc_fbdiv(self, F_TARGET, IntN_Mode, PDIV2):
        """Calculates Configuration Parameters for FB-DIV for targeted VCO Frequency"""
        if (PDIV2):
            N_FIX=2.0
        else:
            N_FIX=1.0

        # Integer-N or Fractional-N Mode
        if (IntN_Mode):
            N_INT=round(F_TARGET/N_FIX/self.fRef)
            N_FRAC=0

        
        else:
            N_INT=int(math.floor(F_TARGET/N_FIX/self.fRef))
            N_FRAC=int(round(2**20*(F_TARGET/N_FIX/self.fRef-N_INT)))

        return (N_INT, N_FRAC, N_FIX)

    
    def vco_auto_ctune(self, F_TARGET, PROFILE=0, XBUF_SLFBEN=1, IntN_Mode=False, PDIV2=False, VTUNE_VCT=1, VCO_SEL_FORCE=0, VCO_SEL_INIT=2, FREQ_INIT_POS=7, FREQ_INIT=0, FREQ_SETTLING_N=4, VTUNE_WAIT_N=128, VCO_SEL_FREQ_MAX=250, VCO_SEL_FREQ_MIN=5, dbgMode=False):
        """Performs VCO Coarse Frequency Tuning Using On-Chip LMS8001 IC Calibration State-Machine"""
        
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        # Store the current PLL Profile Index before proceeding to the new one for configuration
        PROFILE_OLD=self.chip.PLL.ACTIVE_PROFILE
        if (PROFILE_OLD!=PROFILE):
            self.chip.PLL.ACTIVE_PROFILE=PROFILE
            
        # Determine the FB-DIV configuration for targeted VCO frequency and self.fRef reference frequency
        (N_INT, N_FRAC, N_FIX)=self.calc_fbdiv(F_TARGET, IntN_Mode, PDIV2)

        # The exact value of targetec VCO frequency that will be used in automatic coarse-tune algorithm
        # If IntN-Mode is chosen, VCO will be locked to the closest integer multiple of reference frequency
        FVCO_TARGET=N_FIX*(N_INT+N_FRAC/2.0**20)*self.fRef    

        # Calculate the fractional division words
        N_FRAC_H=int(math.floor(N_FRAC/2**16))
        N_FRAC_L=int(N_FRAC-N_FRAC_H*(2**16))
    

        # Enable PLL
        self.enablePLL(PDIV2, IntN_Mode, XBUF_SLFBEN, PROFILE)

        # Define VCO
        reg_vco_cfg=self.chip.getRegisterByName("PLL_VCO_CFG_"+str(PROFILE))
        
        # Set the VCO tuning voltage value during coarse-tuning
        reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
        reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']=VTUNE_VCT
    
        # Define SDM & FB-DIV Modulus
        reg_sdm_cfg=self.chip.getRegisterByName("PLL_SDM_CFG_"+str(PROFILE))
        if (IntN_Mode or N_FRAC==0):
            reg_sdm_cfg['INTMOD_EN_'+str(PROFILE)]=1
        else:
            reg_sdm_cfg['INTMOD_EN_'+str(PROFILE)]=0
        reg_sdm_cfg['INTMOD_'+str(PROFILE)+'<9:0>']=int(N_INT)
        
        reg_fracmod_l=self.chip.getRegisterByName("PLL_FRACMODL_"+str(PROFILE))
        reg_fracmod_l['FRACMODL_'+str(PROFILE)+'<15:0>']=N_FRAC_L
    
        reg_fracmod_h=self.chip.getRegisterByName("PLL_FRACMODH_"+str(PROFILE))
        reg_fracmod_h['FRACMODH_'+str(PROFILE)+'<3:0>']=N_FRAC_H

        # Reset PLL, Enable Calibration Mode
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1
        reg_pll_cfg['PLL_CALIBRATION_EN']=1
        reg_pll_cfg['CTUNE_RES<1:0>']=3

        # Write VCO AUTO-CAL Registers
        reg_pll_cal_auto1=self.chip.getRegisterByName('PLL_CAL_AUTO1')
        reg_pll_cal_auto1['VCO_SEL_FORCE']=VCO_SEL_FORCE
        reg_pll_cal_auto1['VCO_SEL_INIT<1:0>']=VCO_SEL_INIT
        reg_pll_cal_auto1['FREQ_INIT_POS<2:0>']=FREQ_INIT_POS
        reg_pll_cal_auto1['FREQ_INIT<7:0>']=FREQ_INIT
    
        reg_pll_cal_auto2=self.chip.getRegisterByName('PLL_CAL_AUTO2')
        reg_pll_cal_auto2['FREQ_SETTLING_N<3:0>']=FREQ_SETTLING_N
        reg_pll_cal_auto2['VTUNE_WAIT_N<7:0>']=VTUNE_WAIT_N
    
        reg_pll_cal_auto3=self.chip.getRegisterByName('PLL_CAL_AUTO3')
        reg_pll_cal_auto3['VCO_SEL_FREQ_MAX<7:0>']=VCO_SEL_FREQ_MAX
        reg_pll_cal_auto3['VCO_SEL_FREQ_MIN<7:0>']=VCO_SEL_FREQ_MIN
    
        # Start VCO Auto-Tuning Process
        reg_pll_cal_auto0=self.chip.getRegisterByName('PLL_CAL_AUTO0')
        reg_pll_cal_auto0['FCAL_START']=1

    
        # Wait for VCO Auto-Tuning to Finish
        while(True):
            reg_pll_cal_auto0=self.chip.getRegisterByName('PLL_CAL_AUTO0')
            if (reg_pll_cal_auto0['FCAL_START']==0):
                break

        # Evaluate Calibration Results
        reg_pll_cal_auto0=self.chip.getRegisterByName('PLL_CAL_AUTO0')
        if (reg_pll_cal_auto0['VCO_SEL_FINAL_VAL'] and reg_pll_cal_auto0['FREQ_FINAL_VAL']):
            VCO_SEL_FINAL=reg_pll_cal_auto0['VCO_SEL_FINAL<1:0>']
            VCO_FREQ_FINAL=reg_pll_cal_auto0['FREQ_FINAL<7:0>']
        else:
            self.chip.log("Calibration Failed!!!!")
            return False


        # Disable Calibration
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_CALIBRATION_EN']=0

        # Write Calibration Results to the Dedicated VCO Registers in the Chosen Profile
        reg_vco_freq=self.chip.getRegisterByName('PLL_VCO_FREQ_'+str(PROFILE))
        reg_vco_freq['VCO_FREQ_'+str(PROFILE)+'<7:0>']=VCO_FREQ_FINAL
        reg_vco_cfg=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        reg_vco_cfg['VCO_SEL_'+str(PROFILE)+'<1:0>']=VCO_SEL_FINAL

        if (dbgMode):
            self.chip.log("Calibration Done!!!")
            self.chip.log("Configured PLL Profile=%d" %(PROFILE))
            self.chip.log("Target VCO Frequency [MHz]= %.5f" %(FVCO_TARGET/1.0e6))
            self.chip.log("Frequency Error [Hz]= %.2e" %(abs(FVCO_TARGET-F_TARGET)))
            self.chip.log("VCO_SEL_FINAL= %d" %(VCO_SEL_FINAL))
            self.chip.log("VCO_FREQ_FINAL= %d" %(VCO_FREQ_FINAL))
            self.chip.log('')
            self.chip.log('')
    
        

        if (dbgMode):
            self.chip.PLL.infoLOCK()
        

        # Go back to the initial PLL profile
        if (PROFILE_OLD!=PROFILE):
            self.chip.PLL.ACTIVE_PROFILE=PROFILE_OLD

        self.chip.setImmediateMode(Imd_Mode)

        return True
    
    def vco_manual_cloop_tune(self, F_TARGET, PROFILE=0,  XBUF_SLFBEN=1, IntN_Mode=False, PDIV2=False, dbgMode=False):
            
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)


        # Store the current PLL Profile Index before proceeding to the new one for configuration
        PROFILE_OLD=self.chip.PLL.ACTIVE_PROFILE
        if (PROFILE_OLD!=PROFILE):
            self.chip.PLL.ACTIVE_PROFILE=PROFILE
        
            
        # Determine the FB-DIV configuration for targeted VCO frequency and self.fRef reference frequency
        (N_INT, N_FRAC, N_FIX)=self.calc_fbdiv(F_TARGET, IntN_Mode, PDIV2)

        # The exact value of targetec VCO frequency that will be used in automatic coarse-tune algorithm
        # If IntN-Mode is chosen, VCO will be locked to the closest integer multiple of reference frequency
        FVCO_TARGET=N_FIX*(N_INT+N_FRAC/2.0**20)*self.fRef    

        # Calculate the fractional division words
        N_FRAC_H=int(math.floor(N_FRAC/2**16))
        N_FRAC_L=int(N_FRAC-N_FRAC_H*(2**16))
    

        # Enable PLL
        self.enablePLL(PDIV2, IntN_Mode, XBUF_SLFBEN, PROFILE)

        # Define VCO
        reg_vco_cfg=self.chip.getRegisterByName("PLL_VCO_CFG_"+str(PROFILE))
            
        # Define SDM & FB-DIV Modulus
        reg_sdm_cfg=self.chip.getRegisterByName("PLL_SDM_CFG_"+str(PROFILE))
        if (IntN_Mode or N_FRAC==0):
            reg_sdm_cfg['INTMOD_EN_'+str(PROFILE)]=1
        else:
            reg_sdm_cfg['INTMOD_EN_'+str(PROFILE)]=0
        reg_sdm_cfg['INTMOD_'+str(PROFILE)+'<9:0>']=int(N_INT)
    
        reg_fracmod_l=self.chip.getRegisterByName("PLL_FRACMODL_"+str(PROFILE))
        reg_fracmod_l['FRACMODL_'+str(PROFILE)+'<15:0>']=N_FRAC_L
        
        reg_fracmod_h=self.chip.getRegisterByName("PLL_FRACMODH_"+str(PROFILE))
        reg_fracmod_h['FRACMODH_'+str(PROFILE)+'<3:0>']=N_FRAC_H


        # Reset PLL, Enable Manual Calibration Mode
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1

        

        reg_pll_cfg['PLL_CALIBRATION_EN']=1
        reg_pll_cfg['PLL_CALIBRATION_MODE']=1
    

        reg_pll_cal_man=self.chip.getRegisterByName('PLL_CAL_MAN')
    
        # 1st step is to determine the correct VCO core for targeted frequency
        reg_pll_cal_man['VCO_SEL_MAN<1:0>']=2
        
        reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=15
    
        sleep(0.01) # wait 10ms for PLL loop to settle
    
        reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')
        if (reg_pll_status['VTUNE_LOW']==1):
            reg_pll_cal_man['VCO_SEL_MAN<1:0>']=1
        else:
            reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=240
            sleep(0.01)
            reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')
            if (reg_pll_status['VTUNE_HIGH']==1):
                reg_pll_cal_man['VCO_SEL_MAN<1:0>']=3

    
    
        # 2nd step is to determine optimal cap bank configuration of selected VCO core for the targeted frequency value
        freq_low=0
        freq_high=255
        freq=int((freq_high+freq_low+1)/2)
        
        iter_num=0
        while (freq_low<freq_high and iter_num<=8):
            iter_num+=1
            reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=freq
            sleep(0.01)
            reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')
        
            if (reg_pll_status['VTUNE_HIGH']==1):
                freq_low=freq
                freq=int((freq_high+freq_low+1)/2.0)
            elif (reg_pll_status['VTUNE_LOW']==1):
                freq_high=freq
                freq=int((freq_high+freq_low+1)/2.0)
            else:
                if (reg_pll_status['PLL_LOCK']==1):
                    # Cap. bank configuration for which PLL is locked at the targeted frequency is found
                    # This is the starting point for the next step
                    break
                else:
                    self.chip.log("Calibration Failed.")
                    return False
    
        # Find 1st cap. bank configuration above initial one, for which stands VTUNE_LOW=1
        reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')
        freq_init=freq
        while(reg_pll_status['VTUNE_LOW']==0):
            freq=freq+1
            if (freq>=255):
                break
            reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=freq
            sleep(0.01)
            reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')
        freq_max=freq
    
        # Find 1st cap. bank configuration bellow initial one, for which stands VTUNE_HIGH=1
        freq=freq_init
        reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=freq
        sleep(0.01)
        while(reg_pll_status['VTUNE_HIGH']==0):
            freq=freq-1
            if (freq<=1):
                break
            reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=freq
            sleep(0.01)
            reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')            
            # In some VCO_FREQ<7:0> regions, FVCO vs VCO_FREQ<7:0> is not monotonic
            # Next line detects that condition and exits the loop to prevent false results
            if (reg_pll_status['VTUNE_LOW']==1):
                break
        freq_min=freq
    
        # Optimal cap. bank configuration is between freq_min and freq_max
        # It can be arithmetic or geometric average of boundary values

        #freq_opt=int(math.sqrt(freq_min*freq_max))
        freq_opt=int((freq_min+freq_max)/2.0)
        sel_opt=reg_pll_cal_man['VCO_SEL_MAN<1:0>']

        # Exit the manual calibration mode, enter the normal PLL operation mode
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1

        reg_pll_cfg['PLL_CALIBRATION_EN']=0
        reg_pll_cfg['PLL_CALIBRATION_MODE']=0
    

        # Write the results of calibration to the dedicated registers inside the chosen PLL profile
        reg_vco_freq=self.chip.getRegisterByName('PLL_VCO_FREQ_'+str(PROFILE))
        reg_vco_freq['VCO_FREQ_'+str(PROFILE)+'<7:0>']=freq_opt
        reg_vco_cfg=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        reg_vco_cfg['VCO_SEL_'+str(PROFILE)+'<1:0>']=sel_opt

        if (dbgMode):
            self.chip.log("")
            self.chip.log("Closed-Loop Manual Calibration Done!!!")
            self.chip.log("Configured PLL Profile= %d" %(PROFILE))
            self.chip.log("Target VCO Frequency [MHz]= %.5f" % (FVCO_TARGET/1.0e6))
            self.chip.log("Frequency Error [Hz]= %.2e" %(abs(FVCO_TARGET-F_TARGET)))
            self.chip.log("VCO_SEL_FINAL= %d" %(sel_opt))
            self.chip.log("VCO_FREQ_FINAL= %d" %(freq_opt))
            self.chip.log("VCO_FREQ_INIT= %d" %(freq_init))
            self.chip.log("VCO_FREQ_MIN= %d" %(freq_min))
            self.chip.log("VCO_FREQ_MAX= %d" %(freq_max))
            self.chip.log('')
            self.chip.log('')
    
        if (dbgMode):
            self.chip.PLL.infoLOCK()


        # Go back to the initial PLL profile
        if (PROFILE_OLD!=PROFILE):
            self.chip.PLL.ACTIVE_PROFILE=PROFILE_OLD

        self.chip.setImmediateMode(Imd_Mode)    
    
        return True

    def vco_manual_ctune(self, F_TARGET, XBUF_SLFBEN=1, PROFILE=0, IntN_Mode=False, PDIV2=False, VTUNE_VCT=2, dbgMode=False):
        """Selects the tuning curve where VCO frequency @ VTUNE_VCT is closest to F_TARGET (greater/equal than targeted frequecy)"""
        
            
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        # Store the current PLL Profile Index before proceeding to the new one for configuration
        PROFILE_OLD=self.chip.PLL.ACTIVE_PROFILE
        if (PROFILE_OLD!=PROFILE):
            self.chip.PLL.ACTIVE_PROFILE=PROFILE
                    
        # Determine the FB-DIV configuration for targeted VCO frequency and self.fRef reference frequency
        (N_INT, N_FRAC, N_FIX)=self.calc_fbdiv(F_TARGET, IntN_Mode, PDIV2)
        # The exact value of targetec VCO frequency that will be used in automatic coarse-tune algorithm
        # If IntN-Mode is chosen, VCO will be locked to the closest integer multiple of reference frequency
        FVCO_TARGET=N_FIX*(N_INT+N_FRAC/2.0**20)*self.fRef    

        # Calculate the fractional division words
        N_FRAC_H=int(math.floor(N_FRAC/2**16))
        N_FRAC_L=int(N_FRAC-N_FRAC_H*(2**16))
    

        # Enable PLL
        self.enablePLL(PDIV2, IntN_Mode, XBUF_SLFBEN, PROFILE)

        # Define VCO
        reg_vco_cfg=self.chip.getRegisterByName("PLL_VCO_CFG_"+str(PROFILE))


        # Set the VCO tuning voltage value during coarse-tuning
        reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
        reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']=VTUNE_VCT
    
        # Define SDM & FB-DIV Modulus
        reg_sdm_cfg=self.chip.getRegisterByName("PLL_SDM_CFG_"+str(PROFILE))
        if (IntN_Mode or N_FRAC==0):
            reg_sdm_cfg['INTMOD_EN_'+str(PROFILE)]=1
        else:
            reg_sdm_cfg['INTMOD_EN_'+str(PROFILE)]=0
        reg_sdm_cfg['INTMOD_'+str(PROFILE)+'<9:0>']=int(N_INT)
            
        
        reg_fracmod_l=self.chip.getRegisterByName("PLL_FRACMODL_"+str(PROFILE))
        reg_fracmod_l['FRACMODL_'+str(PROFILE)+'<15:0>']=N_FRAC_L
    
        reg_fracmod_h=self.chip.getRegisterByName("PLL_FRACMODH_"+str(PROFILE))
        reg_fracmod_h['FRACMODH_'+str(PROFILE)+'<3:0>']=N_FRAC_H

        # Reset PLL, Enable Calibration Mode
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1


        reg_pll_cfg['CTUNE_RES<1:0>']=3
        reg_pll_cfg['PLL_CALIBRATION_EN']=1
        reg_pll_cfg['PLL_CALIBRATION_MODE']=1

        # Write to PLL_CAL_MAN Register
        reg_pll_cal_man=self.chip.getRegisterByName('PLL_CAL_MAN')
    
        # Enable Coarse-Tuning Frequency Comparator
        reg_pll_cal_man['CTUNE_EN']=1

        # Initial Value for VCO_SEL
        reg_pll_cal_man['VCO_SEL_MAN<1:0>']=2
    
        
        # Find optimal VCO Core
        # 24.02.2017. - overlap between VCO cores 2 and 3 is quite large, therefore value 240 for upper boundary can be decreased down to 200
        #reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=240
        reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=200
        
        reg_pll_cal_man['CTUNE_START']=1

        
        
        # Start the coarse-tuning step
            
        
        # Wait for CTUNE_STEP_DONE
        #while (reg_pll_cal_man['CTUNE_STEP_DONE']==0):
        #    reg_pll_cal_man=self.chip.getRegisterByName('PLL_CAL_MAN')
    
        
        
        # Read the result of coarse-tuning step
        freq_high=reg_pll_cal_man['FREQ_HIGH']
        freq_equal=reg_pll_cal_man['FREQ_EQUAL']
        freq_low=reg_pll_cal_man['FREQ_LOW']
        
        
        # Reset the frequency comparator
        reg_pll_cal_man['CTUNE_START']=0

        if (freq_low==1):
            reg_pll_cal_man['VCO_SEL_MAN<1:0>']=3
        else:
            #reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=15
            reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=8
            
            # Start the coarse-tuning step
            reg_pll_cal_man['CTUNE_START']=1

            # Wait for CTUNE_STEP_DONE
            #while (reg_pll_cal_man['CTUNE_STEP_DONE']==0):
            #    reg_pll_cal_man=self.chip.getRegisterByName('PLL_CAL_MAN')
    
            # Read the result of coarse-tuning step
            freq_high=reg_pll_cal_man['FREQ_HIGH']
            freq_equal=reg_pll_cal_man['FREQ_EQUAL']
            freq_low=reg_pll_cal_man['FREQ_LOW']

            # Reset the frequency comparator
            reg_pll_cal_man['CTUNE_START']=0
        
            if (freq_high==1):
                reg_pll_cal_man['VCO_SEL_MAN<1:0>']=1

        

        
        # Find the optimal VCO_FREQ value
        bit_pos=7
        bit_mask=0
    
    
        
        freq=0
        while (bit_pos>=0):
            
            freq+=2**bit_pos
            reg_pll_cal_man['VCO_FREQ_MAN<7:0>']=freq

            # Start the coarse-tuning step
            reg_pll_cal_man['CTUNE_START']=1

            # Wait for CTUNE_STEP_DONE
            #while (reg_pll_cal_man['CTUNE_STEP_DONE']==0):
            #    reg_pll_cal_man=self.chip.getRegisterByName('PLL_CAL_MAN')

            # Read the result of coarse-tuning step
            freq_high=reg_pll_cal_man['FREQ_HIGH']
            freq_equal=reg_pll_cal_man['FREQ_EQUAL']
            freq_low=reg_pll_cal_man['FREQ_LOW']

            # Reset the frequency comparator
            reg_pll_cal_man['CTUNE_START']=0

            bit_mask=(2**bit_pos)*(1-freq_low)
            bit_val=(freq&bit_mask)>>bit_pos

            

            if (bit_val==1):
                freq-=2**bit_pos
        
            if (bit_pos==0 and freq_low):
                reg_pll_cal_man['VCO_FREQ_MAN<7:0>']+=1
            
                # In the last pass, set VTUNE_VCT to minimum value of 300 mV
                reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
                reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']=0

                # Start the coarse-tuning step
                reg_pll_cal_man['CTUNE_START']=1

                # Wait for CTUNE_STEP_DONE
                #while (reg_pll_cal_man['CTUNE_STEP_DONE']==0):
                #    reg_pll_cal_man=self.chip.getRegisterByName('PLL_CAL_MAN')

                # Read the result of coarse-tuning step
                freq_high=reg_pll_cal_man['FREQ_HIGH']
                freq_equal=reg_pll_cal_man['FREQ_EQUAL']
                freq_low=reg_pll_cal_man['FREQ_LOW']

                # Reset the frequency comparator
                reg_pll_cal_man['CTUNE_START']=0
                
                # Set-Back the VTUNE_VCT  to the initial value
                reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']=VTUNE_VCT
                
                if (freq_high==1):
                    reg_pll_cal_man['VCO_FREQ_MAN<7:0>']-=1
        
            bit_pos-=1
            
            
    

        sel_opt=reg_pll_cal_man['VCO_SEL_MAN<1:0>']    
        freq_opt=reg_pll_cal_man['VCO_FREQ_MAN<7:0>']

        # Disable Frequency Comparator
        reg_pll_cal_man['CTUNE_EN']=0

        # Exit the manual calibration mode, enter the normal PLL operation mode
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1

        reg_pll_cfg['PLL_CALIBRATION_EN']=0
        reg_pll_cfg['PLL_CALIBRATION_MODE']=0
    

        # Write the results of calibration to the dedicated registers inside the chosen PLL profile
        reg_vco_freq=self.chip.getRegisterByName('PLL_VCO_FREQ_'+str(PROFILE))
        reg_vco_freq['VCO_FREQ_'+str(PROFILE)+'<7:0>']=freq_opt
        reg_vco_cfg=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        reg_vco_cfg['VCO_SEL_'+str(PROFILE)+'<1:0>']=sel_opt
    
        if (dbgMode):
            self.chip.log("Open-Loop Manual Calibration Done!!!")
            self.chip.log("Configured PLL Profile= %d" %(PROFILE))
            self.chip.log("Target VCO Frequency [MHz]= %.5f" %(FVCO_TARGET/1.0e6))
            self.chip.log("Frequency Error [Hz]= %.2e" %(abs(FVCO_TARGET-F_TARGET)))
            self.chip.log("VCO_SEL_FINAL= %d" %(sel_opt))
            self.chip.log("VCO_FREQ_FINAL= %d" %(freq_opt))
            self.chip.log('')
            self.chip.log('')
    
        if (dbgMode):
            self.chip.PLL.infoLOCK()


        # Go back to the initial PLL profile
        if (PROFILE_OLD!=PROFILE):
            self.chip.PLL.ACTIVE_PROFILE=PROFILE_OLD
    
        self.chip.setImmediateMode(Imd_Mode)    

        return True
    

    def optimLPF(self, PM_deg=49.8, fc=80.0e3, PROFILE=0, dbgMode=False):
        PM_rad=PM_deg*math.pi/180
        wc=2*math.pi*fc        

        # Check VCO_SEL
        reg_vco_cfg=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        vco_sel=reg_vco_cfg['VCO_SEL_'+str(PROFILE)+'<1:0>']

        # Use Average for KVCO in Calculations
        if (vco_sel==1):
            KVCO_avg=44.404e6
        elif (vco_sel==2):
            KVCO_avg=33.924e6    
        elif (vco_sel==3):
            KVCO_avg=41.455e6
        else:
            self.chip.log('Ext. LO selected in PLL_PROFILE %d.' % (PROFILE))
            return None

        # Read CP Current Value
        reg_pll_cp_cfg0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        PULSE=reg_pll_cp_cfg0['PULSE_'+str(PROFILE)+'<5:0>']
        reg_pll_cp_cfg1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        ICT_CP=reg_pll_cp_cfg1['ICT_CP_'+str(PROFILE)+'<4:0>']
        Icp=ICT_CP*25.0e-6/16.0*PULSE
        

        # Read Feedback-Divider Modulus
        reg_pll_enable=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
        PDIV2=reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]

        reg_pll_sdm_cfg=self.chip.getRegisterByName('PLL_SDM_CFG_'+str(PROFILE))
        N_INT=reg_pll_sdm_cfg['INTMOD_'+str(PROFILE)+'<9:0>']
        INTMOD_EN=reg_pll_sdm_cfg['INTMOD_EN_'+str(PROFILE)]
        
        reg_pll_fracmodl=self.chip.getRegisterByName('PLL_FRACMODL_'+str(PROFILE))
        N_FRACL=reg_pll_fracmodl['FRACMODL_'+str(PROFILE)+'<15:0>']
        reg_pll_fracmodh=self.chip.getRegisterByName('PLL_FRACMODH_'+str(PROFILE))
        N_FRACH=reg_pll_fracmodh['FRACMODH_'+str(PROFILE)+'<3:0>']
        N_FRAC=N_FRACH*2**16+N_FRACL
        N=N_INT+(1-INTMOD_EN)*N_FRAC*1.0/2.0**20
    

        Kvco=2*math.pi*KVCO_avg
        Kphase=Icp/(2*math.pi)
        
        gamma=1.045 
        T31=0.1
        
        # Approx. formula, Dean Banerjee
        T1=(1.0/math.cos(PM_rad)-math.tan(PM_rad))/(wc*(1+T31))

        T3=T1*T31;
        T2=gamma/((wc**2)*(T1+T3));

        A0=(Kphase*Kvco)/((wc**2)*N)*math.sqrt((1+(wc**2)*(T2**2))/((1+(wc**2)*(T1**2))*(1+(wc**2)*(T3**2))));
        A2=A0*T1*T3;
        A1=A0*(T1+T3);

        C1=A2/(T2**2)*(1+math.sqrt(1+T2/A2*(T2*A0-A1)));
        C3=(-(T2**2)*(C1**2)+T2*A1*C1-A2*A0)/((T2**2)*C1-A2);
        C2=A0-C1-C3;
        R2=T2/C2;
        R3=A2/(C1*C3*T2);

        if (dbgMode):
            self.chip.log('Loop-Filter Optimization')
            self.chip.log('-'*45)
            self.chip.log('Input Parameters')
            self.chip.log('\tIcp=%.2f uA' %(Icp/1.0e-6))
            self.chip.log('\tKVCO=%.2f MHz/V' %(KVCO_avg/1.0e6))
            self.chip.log('\tNDIV=%.2f' % (N))
            self.chip.log('-'*45)
            self.chip.log('Ideal LPF Values')
            self.chip.log('\tC1= %.2f pF' %(C1/1.0e-12))
            self.chip.log('\tC2= %.2f pF' %(C2/1.0e-12))
            self.chip.log('\tR2= %.2f kOhm' %(R2/1.0e3))
            self.chip.log('\tC3= %.2f pF' %(C3/1.0e-12))
            self.chip.log('\tR3= %.2f kOhm' %(R3/1.0e3))
            self.chip.log('')
            self.chip.log('')

        C1_CODE=int(round(C1/1.2e-12))
        C2_CODE=int(round((C2-150.0e-12)/10.0e-12))
        C3_CODE=int(round((C3-5.0e-12)/1.2e-12))
        C1_CODE=int(min(max(C1_CODE,0),15))
        C2_CODE=int(min(max(C2_CODE,0),15))
        C3_CODE=int(min(max(C3_CODE,0),15))

        R2_CODE=int(round(24.6e3/R2))
        R3_CODE=int(round(14.9e3/R3))
        R2_CODE=min(max(R2_CODE,1),15)
        R3_CODE=min(max(R3_CODE,1),15)

        self.setLPF(C1=C1_CODE, C2=C2_CODE, R2=R2_CODE, C3=C3_CODE, R3=R3_CODE, PROFILE=PROFILE)

    def getNDIV(self, PROFILE=0):
        """
        Returns float that represents PLL feedback division ratio for configuration in PLL profile PROFILE.
        """
        # Set Immediate Mode for LMS8001 EVB
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)

        reg_pll_enable=self.chip.getRegisterByName('PLL_ENABLE_'+str(PROFILE))
        PDIV2=reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]

        reg_fracmodl=self.chip.getRegisterByName('PLL_FRACMODL_'+str(PROFILE))
        reg_fracmodh=self.chip.getRegisterByName('PLL_FRACMODH_'+str(PROFILE))
        reg_pll_sdm_cfg=self.chip.getRegisterByName('PLL_SDM_CFG_'+str(PROFILE))

        NINT=reg_pll_sdm_cfg['INTMOD_'+str(PROFILE)+'<9:0>']
        NFRAC=reg_fracmodh['FRACMODH_'+str(PROFILE)+'<3:0>']*2**16+reg_fracmodl['FRACMODL_'+str(PROFILE)+'<15:0>']

        self.chip.setImmediateMode(Imd_Mode)

        return 2**PDIV2*1.0*(NINT*1.0+NFRAC*1.0/2**20)

    def getNFFDIV(self, PROFILE=0):
        """
        Returns float that represents PLL feedforward division ratio for configuration in PLL profile PROFILE.
        """
        # Set Immediate Mode for LMS8001 EVB
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
        
        reg_pll_ff_cfg=self.chip.getRegisterByName('PLL_FF_CFG_'+str(PROFILE))
        if (reg_pll_ff_cfg['FFDIV_SEL_'+str(PROFILE)]==0):
            return 1.0
        else:
            return 2.0**int(reg_pll_ff_cfg['FFMOD_'+str(PROFILE)])
        
        self.chip.setImmediateMode(Imd_Mode)

    def getNIQDIV2(self, channel, PROFILE=0):
        """
        Returns float that represents PLL IQ-DivBy2 division ratio for configuration in PLL profile PROFILE for desired LO channel.
        """

        if (PROFILE>=8):
            self.chip.log('Wrong PLL Profile Number. Valid values 0-7.')
            return None

        # Set Immediate Mode for LMS8001 EVB
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
    

        if (channel=='A' or channel==0):
            reg_pll_lodist_cfg=self.chip.getRegisterByName('PLL_LODIST_CFG_'+str(PROFILE))
            IQ_EXP=(reg_pll_lodist_cfg["PLL_LODIST_FSP_OUT0_"+str(PROFILE)+"<2:0>"]&4)>>2
        elif (channel=='B' or channel==1):
            reg_pll_lodist_cfg=self.chip.getRegisterByName('PLL_LODIST_CFG_'+str(PROFILE))
            IQ_EXP=(reg_pll_lodist_cfg["PLL_LODIST_FSP_OUT1_"+str(PROFILE)+"<2:0>"]&4)>>2
        elif (channel=='C' or channel==2):
            reg_pll_lodist_cfg=self.chip.getRegisterByName('PLL_LODIST_CFG_'+str(PROFILE))
            IQ_EXP=(reg_pll_lodist_cfg["PLL_LODIST_FSP_OUT2_"+str(PROFILE)+"<2:0>"]&4)>>2
        elif (channel=='D' or channel==3):
            reg_pll_lodist_cfg=self.chip.getRegisterByName('PLL_LODIST_CFG_'+str(PROFILE))
            IQ_EXP=(reg_pll_lodist_cfg["PLL_LODIST_FSP_OUT3_"+str(PROFILE)+"<2:0>"]&4)>>2
        else:
            self.chip.log('Wrong LO channel selected. Valid values: "A" or 0, "B" or 1, "C" or 2, "D" or 3.')
            return None
        
        self.chip.setImmediateMode(Imd_Mode)
        
        return 2.0**(1.0-IQ_EXP)
        

    def get_LOfreq(self, channel, PROFILE=0):
        """
        Returns the exact value of LO frequency at chosen LO channel.
        """
        if (PROFILE>=8):
            self.chip.log('Wrong PLL Profile Number. Valid values 0-7.')
            return None

        # Set Immediate Mode for LMS8001 EVB
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
        
        # Get Feedback-Divider Division Modulus
        N_FBDIV=self.getNDIV(PROFILE=PROFILE)
        # Get Feedforward-Divider Division Modulus
        N_FFDIV=self.getNFFDIV(PROFILE=PROFILE)
        # Get IQ-DivBy2 Division Modulus
        N_IQDIV2=self.getNIQDIV2(channel, PROFILE)

        self.chip.setImmediateMode(Imd_Mode)

        return (N_FBDIV)*self.fRef/N_FFDIV/N_IQDIV2
    
    def centerVTUNE(self, PROFILE=0, dbgMode=False):
        """
        This method should be used when coarse tuning algorithm converges to the subband at which PLL locks with VTUNE_HIGH=1 or VTUNE_LOW=1
        If it's possible, this method tweaks different VCO setings in order to get PLL locked at desired frequency with VTUNE_HIGH=VTUNE_LOW=0

        The purpose of this method is same as of centerVTUNE method.
        Algorithm is different.
        """
        
        # Set Immediate Mode for LMS8001 EVB
        Imd_Mode=self.chip.getImmediateMode()
        self.chip.setImmediateMode(True)
        
        # Reset PLL
        reg_pll_cfg=self.chip.getRegisterByName('PLL_CFG')
        reg_pll_cfg['PLL_RSTN']=0
        reg_pll_cfg['PLL_RSTN']=1


        # Here set active PLL profile to the value given by argument PROFILE
        self.chip.PLL.ACTIVE_PROFILE=PROFILE
        
        # Get register with VTUNE_HIGH and VTUNE_LOW Indicators and PLL_LOCK bit
        reg_pll_status=self.chip.getRegisterByName('PLL_CFG_STATUS')

        # Get register with VCO_FREQ_n<7:0> word
        #reg_pll_vco_freq=self.chip.getRegisterByName('PLL_VCO_FREQ_'+str(PROFILE))
    
        # Get register with VDIV_SWVDD_n<1:0> word
        reg_pll_vco_cfg=self.chip.getRegisterByName('PLL_VCO_CFG_'+str(PROFILE))
        
        # Get Initial value for VCO_FREQ<1:0> word
        #freq_init=reg_pll_vco_freq['VCO_FREQ_'+str(PROFILE)+'<7:0>']
        
        # Get Initial value for VDIV_SWVDD<1:0> word
        vdiv_swvdd_init=reg_pll_vco_cfg['VDIV_SWVDD_'+str(PROFILE)+'<1:0>']
        #sel_init=reg_pll_vco_cfg['VCO_SEL_'+str(PROFILE)+'<1:0>']
        
        # Get Initial Value for VCO_AMP<7:0> and VCO_AAC_EN
        amp_init=reg_pll_vco_cfg['VCO_AMP_'+str(PROFILE)+'<6:0>']
        aac_en_init=reg_pll_vco_cfg['VCO_AAC_EN_'+str(PROFILE)]
        
        
        # Get VTUNE_HIGH, VTUNE_LOW, PLL_LOCK bit values
        vtune_high=reg_pll_status['VTUNE_HIGH']
        vtune_low=reg_pll_status['VTUNE_LOW']
        pll_lock=reg_pll_status['PLL_LOCK']


        if (vtune_high==0 and vtune_low==0):
            if (dbgMode):
                self.chip.log('Centering of VTUNE not needed.')
            self.chip.setImmediateMode(Imd_Mode)
            return True

        swvdd_list=range(0,4)
        swvdd_list.reverse()
        
        amp_list=range(0,4)
        amp_list.reverse()
        
        # Try to center VTUNE by changing Bias Voltages of MOS switches in Capacitor Bank and VCO Amp control and reruning VCO Auto-Tuning State-Machine
        reg_pll_vco_cfg['VCO_AAC_EN_'+str(PROFILE)]=1
        for amp in amp_list:
            reg_pll_vco_cfg['VCO_AMP_'+str(PROFILE)+'<6:0>']=amp
            
            for vdiv_swvdd in swvdd_list:
                 if not (amp_init==amp and vdiv_swvdd_init==vdiv_swvdd):
                    reg_pll_vco_cfg['VDIV_SWVDD_'+str(PROFILE)+'<1:0>']=vdiv_swvdd
                    # changed FREQ_INIT_POS to 5
                    # The VCO Auto-Tuning State Machine will not be re-runed again for each amp and swvdd combination
                    # The following two commands can be commented

        
                    #autotune_status=self.vco_auto_ctune(F_TARGET=F_TARGET, PROFILE=0, XBUF_SLFBEN=1, IntN_Mode=INTMOD_EN, PDIV2=PDIV2_EN, VTUNE_VCT=1, VCO_SEL_FORCE=1, VCO_SEL_INIT=sel_init, FREQ_INIT_POS=5, FREQ_INIT=freq_init, dbgMode=dbgMode)
                    #sleep(0.001)
                
                    vtune_high=reg_pll_status['VTUNE_HIGH']
                    vtune_low=reg_pll_status['VTUNE_LOW']
                    pll_lock=reg_pll_status['PLL_LOCK']

                    if (vtune_high==0 and vtune_low==0):
                        if (dbgMode):
                            self.chip.log('VTUNE voltage centered successfuly.')
                            self.chip.log('New VCO control values: VDIV_AMP<6:0>= %d, VCO_AAC_EN=1, VDIV_SWVDD<1:0>= %d' %(amp, vdiv_swvdd))
                            self.chip.log('')
                            self.chip.PLL.infoLOCK()
                        self.chip.setImmediateMode(Imd_Mode)
                        
                        # Set back PLL_CAL_AUTO1 to starting values
                        # Uncomment these lines bellow if autotuning was invoked for each step of centering VTUNE
                        #reg_pll_cal_auto1['VCO_SEL_FORCE']=vco_sel_force_init
                        #reg_pll_cal_auto1['VCO_SEL_INIT<1:0>']=vco_sel_init
                        #reg_pll_cal_auto1['FREQ_INIT_POS<2:0>']=vco_freq_init_pos
                        #reg_pll_cal_auto1['FREQ_INIT<7:0>']=vco_freq_init

                        return True

        
        if (dbgMode):
            self.chip.log("Centering VTUNE failed.")
        
        # Set back VDIV_SWVDD<1:0> and FREQ<7:0> to inital values
        reg_pll_vco_cfg['VDIV_SWVDD_'+str(PROFILE)+'<1:0>']=vdiv_swvdd_init
        #reg_pll_vco_freq['VCO_FREQ_'+str(PROFILE)+'<7:0>']=freq_init
        # Set back VCO amplitude controls to initial values
        reg_pll_vco_cfg['VCO_AMP_'+str(PROFILE)+'<6:0>']=amp_init
        reg_pll_vco_cfg['VCO_AAC_EN_'+str(PROFILE)]=aac_en_init
        # Set back the inital value of Immediate mode for LMS8001 EVB
        self.chip.setImmediateMode(Imd_Mode)
        return False        
        

    def setLOFREQ(self, F_LO, XBUF_SLFBEN=1, IQ=False, IntN_Mode=False, CTUNE_METHOD='OPEN-LOOP', PROFILE=0, dbgMode=False):
        """
        This methods configures PLL-LODIST subsystems of LMS8001 IC to generate desired LO frequency.
        
        Frequency Range Available with Quadrature Divider By 2 enabled:
        260 MHz<=F_LO<=4.55 GHz,
        Frequency Range Available with Quadrature Divider By 2 disabled:,
        520 MHz<=F_LO<=9.11 GHz.
        Frequencies bellow 520 MHz can only be synthesized using IQ generator.
        CTUNE_METHOD='OPEN-LOOP' calls the vco_auto_tune method to tune VCO to the desired frequency
        CTUNE_METHOD='OPEN-LOOP-MANUAL' calls the vco_manual_ctune method to tune VCO to the desired frequency
        CTUNE_METHOD='CLOSE-LOOP' calls the vco_manual_cloop_tune method to tune VCO to the desired frequency
        """
        if (IQ):
            if not (260.0e6<=F_LO<=4.55e9):
                self.chip.log("F_LO should be between 260 MHz and 4.55 GHz, with argument IQ=True. Failed to set LO Freq.")
                return False
            DIV2IQ=1
        else:
            if not (260.0e6<=F_LO<=9.11e9):
                self.chip.log("F_LO should be between 260 MHz and 9.11 GHz. Failed to set LO Freq.")
                return False
            if (260e6<=F_LO<=520e6):
                self.chip.log("F_LO values between 260 MHz and 520 MHz can only be generated with argument IQ=True. Failed to set LO Freq.")
                return False

            DIV2IQ=0

        FFMOD=0
        F_VCO=(2.0**DIV2IQ)*(2.0**FFMOD)*F_LO
        while not (4.1e9<=F_VCO<=9.11e9):
            FFMOD+=1
            F_VCO=(2.0**DIV2IQ)*(2**FFMOD)*F_LO
        
        if (dbgMode):
            self.chip.log('')
            self.chip.log('Setting LO Frequency')
            self.chip.log('-'*60)
            self.chip.log('Required FF-DIV Modulus: %d (%d)' %(2**FFMOD, FFMOD))
            self.chip.log('IQ DIV2 Gen: %s' %(str(IQ)))
            self.chip.log('Targeted VCO Frequency: %.5f GHz' %(F_VCO/1.0e9))
            self.chip.log('IntN-Mode: %s' %(str(IntN_Mode)))
            self.chip.log('-'*60)
            self.chip.log('')
        
        # Set FF-DIV Control Signals
        self.setFFDIV(FFMOD=FFMOD, PROFILE=PROFILE)
        
        
        if (CTUNE_METHOD=='OPEN-LOOP'):
            # Read VCO AUTO-CAL Registers - use user defined values
            reg_pll_cal_auto1=self.chip.getRegisterByName('PLL_CAL_AUTO1')
            VCO_SEL_FORCE=reg_pll_cal_auto1['VCO_SEL_FORCE']
            VCO_SEL_INIT=reg_pll_cal_auto1['VCO_SEL_INIT<1:0>']
            FREQ_INIT_POS=reg_pll_cal_auto1['FREQ_INIT_POS<2:0>']
            FREQ_INIT=reg_pll_cal_auto1['FREQ_INIT<7:0>']
    
            reg_pll_cal_auto2=self.chip.getRegisterByName('PLL_CAL_AUTO2')
            FREQ_SETTLING_N=reg_pll_cal_auto2['FREQ_SETTLING_N<3:0>']
            VTUNE_WAIT_N=reg_pll_cal_auto2['VTUNE_WAIT_N<7:0>']
    
            reg_pll_cal_auto3=self.chip.getRegisterByName('PLL_CAL_AUTO3')
            VCO_SEL_FREQ_MAX=reg_pll_cal_auto3['VCO_SEL_FREQ_MAX<7:0>']
            VCO_SEL_FREQ_MIN=reg_pll_cal_auto3['VCO_SEL_FREQ_MIN<7:0>']

            # Read PLL_EN_FB_PDIV2_n value - use user defined values
            reg_pll_enable=self.chip.getRegisterByName("PLL_ENABLE_"+str(PROFILE))
            PDIV2=reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]
        
            # Read VTUNE_VCT_n value - use user defined values
            reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
            VTUNE_VCT=reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']
                        
            
            ctune_status=self.vco_auto_ctune(F_TARGET=F_VCO,  PROFILE=PROFILE, XBUF_SLFBEN=XBUF_SLFBEN, IntN_Mode=IntN_Mode, PDIV2=PDIV2, VTUNE_VCT=VTUNE_VCT, VCO_SEL_FORCE=VCO_SEL_FORCE, VCO_SEL_INIT=VCO_SEL_INIT, FREQ_INIT_POS=FREQ_INIT_POS, FREQ_INIT=FREQ_INIT, FREQ_SETTLING_N=FREQ_SETTLING_N, VTUNE_WAIT_N=VTUNE_WAIT_N, VCO_SEL_FREQ_MAX=VCO_SEL_FREQ_MAX, VCO_SEL_FREQ_MIN=VCO_SEL_FREQ_MIN, dbgMode=dbgMode)
            
        elif (CTUNE_METHOD=='OPEN-LOOP-MANUAL'):
            # Read PLL_EN_FB_PDIV2_n value - use user defined values
            reg_pll_enable=self.chip.getRegisterByName("PLL_ENABLE_"+str(PROFILE))
            PDIV2=reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]
        
            # Read VTUNE_VCT_n value - use user defined values
            reg_pll_lpf_cfg2=self.chip.getRegisterByName('PLL_LPF_CFG2_'+str(PROFILE))
            VTUNE_VCT=reg_pll_lpf_cfg2['VTUNE_VCT_'+str(PROFILE)+'<1:0>']
            
            ctune_status=self.vco_manual_ctune(F_TARGET=F_VCO, XBUF_SLFBEN=XBUF_SLFBEN, PROFILE=PROFILE, IntN_Mode=IntN_Mode, PDIV2=PDIV2, VTUNE_VCT=VTUNE_VCT, dbgMode=dbgMode)
        elif (CTUNE_METHOD=='CLOSE-LOOP'):
            # Read PLL_EN_FB_PDIV2_n value - use user defined values
            reg_pll_enable=self.chip.getRegisterByName("PLL_ENABLE_"+str(PROFILE))
            PDIV2=reg_pll_enable['PLL_EN_FB_PDIV2_'+str(PROFILE)]

            
            ctune_status=self.vco_manual_cloop_tune(F_VCO, PROFILE=PROFILE, XBUF_SLFBEN=XBUF_SLFBEN, IntN_Mode=IntN_Mode, PDIV2=PDIV2, dbgMode=dbgMode)
        else:
            if (dbgMode):
                self.chip.log('Bad CTUNE_METHOD selected. Possible Options: OPEN-LOOP and CLOSE-LOOP.')
            self.chip.log('Setting LO Frequency failed.')
            return False
        
        if not (self.chip.PLL.VTUNE_HIGH==0 and self.chip.PLL.VTUNE_LOW==0):
            self.centerVTUNE(PROFILE=PROFILE, dbgMode=dbgMode)

        if (ctune_status):
            if (dbgMode):
                self.chip.log('Setting LO Frequency finished succesfully.')
            return True
        else:
            self.chip.log('Setting LO Frequency failed.')
            return False

    def optim_PLL_LoopBW(self, PM_deg=49.8, fc=120.0e3, FIT_KVCO=False, PROFILE=0, dbgMode=False):
        """
        This method finds optimal PLL configuration, CP pulse current and LPF element values.
        Optimization finds maximal CP current which can results with targeted PLL Loop BW using Loop-Filter elements which can be implemented in LMS8001 IC.
        Result should be PLL configuration with best phase noise performance for targeted loop bandwidth.
        """

        # Get initial CP current settings
        reg_pll_cp_cfg0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        PULSE_INIT=reg_pll_cp_cfg0['PULSE_'+str(PROFILE)+'<5:0>']
        OFS_INIT=reg_pll_cp_cfg0['OFS_'+str(PROFILE)+'<5:0>']
        reg_pll_cp_cfg1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        ICT_CP_INIT=reg_pll_cp_cfg1['ICT_CP_'+str(PROFILE)+'<4:0>']
        


        # Pulse control word of CP inside LMS8001 will be swept from 63 to 4.
        # First value that gives implementable PLL configuration will be used.    
        cp_pulse_vals=range(4,64)
        cp_pulse_vals.reverse()
    
        # Estimate the value of KVCO for settings in the PLL Profile PROFILE
        KVCO_avg=self.estim_KVCO(FIT_KVCO=FIT_KVCO, PROFILE=PROFILE)

        # Read Feedback-Divider Modulus
        N=self.getNDIV(PROFILE=PROFILE)
        #Kvco=2*math.pi*KVCO_avg

        
        
        for cp_pulse in cp_pulse_vals:
            # Calculate CP Current Value
            Icp=ICT_CP_INIT*25.0e-6/16.0*cp_pulse
                
            gamma=1.045 
            T31=0.1
        
            LPF_IDEAL_VALS=self.calc_ideal_LPF(fc=fc, PM_deg=PM_deg, Icp=Icp, KVCO_HzV=KVCO_avg, N=N, gamma=gamma, T31=T31)
            (LPFvals_OK, LPF_REAL_VALS)=self.calc_real_LPF(LPF_IDEAL_VALS)

            
            if (LPFvals_OK):
                # Set CP Pulse Current to the optimized value
                self.setCP(PULSE=cp_pulse, OFS=OFS_INIT, ICT_CP=ICT_CP_INIT, PROFILE=PROFILE)

                # Set LPF Components to the optimized values
                self.setLPF(C1=LPF_REAL_VALS['C1_CODE'], C2=LPF_REAL_VALS['C2_CODE'], R2=LPF_REAL_VALS['R2_CODE'], C3=LPF_REAL_VALS['C3_CODE'], R3=LPF_REAL_VALS['R3_CODE'], PROFILE=PROFILE)
                
                if (dbgMode):
                    self.chip.log('PLL LoopBW Optimization finished successfuly.')
                    self.chip.log('-'*45)
                    self.chip.log('\tIcp=%.2f uA' %(Icp/1.0e-6))
                    self.chip.log('\tUsed Value for KVCO=%.2f MHz/V' %(KVCO_avg/1.0e6))
                    self.chip.log('\tNDIV=%.2f' % (N))
                    self.chip.log('-'*45)
                    self.chip.log('')
                    self.chip.log('Ideal LPF Values')
                    self.chip.log('-'*45)
                    self.chip.log('\tC1= %.2f pF' %(LPF_IDEAL_VALS['C1']/1.0e-12))
                    self.chip.log('\tC2= %.2f pF' %(LPF_IDEAL_VALS['C2']/1.0e-12))
                    self.chip.log('\tR2= %.2f kOhm' %(LPF_IDEAL_VALS['R2']/1.0e3))
                    self.chip.log('\tC3= %.2f pF' %(LPF_IDEAL_VALS['C3']/1.0e-12))
                    self.chip.log('\tR3= %.2f kOhm' %(LPF_IDEAL_VALS['R3']/1.0e3))
                    self.chip.log('')
                return True
        if (dbgMode):
            self.chip.log('PLL LoopBW Optimization failed.')
            self.chip.log('Some of the LPF component(s) out of implementable range.')
        
        # Set back to initial settings of CP
        self.setCP(PULSE=PULSE_INIT, OFS=OFS_INIT, ICT_CP=ICT_CP_INIT, PROFILE=PROFILE)
        return False

    def optimCPandLD(self, PROFILE=0, dbgMode=False):
        """This method checks if PLL works in fractional-N Mode. If this condition is true, it sets the offset CP current to optimize phase noise performance in FracN operation mode.
        When CP offset current is used, it is recommended to set ICP_OFS ~ 1.9% of ICP_PULSE for Frac-N Mode, 1.2% of ICP_PULSE for Int-N Mode""" 
        
        # Check operating mode of LMS8001 PLL
        reg_pll_sdm_cfg=self.chip.getRegisterByName('PLL_SDM_CFG_'+str(PROFILE))
        INTMOD_EN=reg_pll_sdm_cfg['INTMOD_EN_'+str(PROFILE)]

        # Read CP current configuration
        reg_pll_cp_cfg0=self.chip.getRegisterByName('PLL_CP_CFG0_'+str(PROFILE))
        reg_pll_cp_cfg1=self.chip.getRegisterByName('PLL_CP_CFG1_'+str(PROFILE))
        PULSE=reg_pll_cp_cfg0['PULSE_'+str(PROFILE)+'<5:0>']
        OFS=reg_pll_cp_cfg0['OFS_'+str(PROFILE)+'<5:0>']
        ICT_CP=reg_pll_cp_cfg1['ICT_CP_'+str(PROFILE)+'<4:0>']

        # Read Lock Detector Threashold Voltage
        LD_VCT=reg_pll_cp_cfg1['LD_VCT_'+str(PROFILE)+'<1:0>']

        
        
        # Calculate OFS and LD_VCT optimal values
        if (INTMOD_EN):
            # Set Offset Current and Lock Detector Threashold for IntN-Operating Mode
            LD_VCT=2
            Icp=(25.0*ICT_CP/16.0)*PULSE
            # Calculate Target Value for Offset Current, as 1.2% of Pulse current value
            Icp_OFS=1.2/100.0*Icp
            Icp_OFS_step=(25.0*ICT_CP/16.0)*0.25
            OFS=int(round(Icp_OFS/Icp_OFS_step))
        else:
            # Set Offset Current and Lock Detector Threashold for FracN-Operating Mode
            LD_VCT=0
            Icp=(25.0*ICT_CP/16.0)*PULSE
            # Calculate Target Value for Offset Current, as 1.9% of Pulse current value
            Icp_OFS=1.9/100.0*Icp
            Icp_OFS_step=(25.0*ICT_CP/16.0)*0.25
            OFS=int(max(1, round(Icp_OFS/Icp_OFS_step)))

        self.setCP(PULSE=PULSE, OFS=OFS, ICT_CP=ICT_CP, PROFILE=PROFILE)
        self.setLD(LD_VCT=LD_VCT, PROFILE=PROFILE)

        if (dbgMode):
            self.chip.log('')
            self.chip.log('Optimization of CP-OFS and LD-VCT Settings')
            self.chip.log('-'*60)
            self.chip.log('OFS=%d' %(OFS))
            self.chip.log('LD_VCT=%d' %(LD_VCT))
            self.chip.log('-'*60)
            self.chip.log('')

        return True


    def configPLL(self, F_LO, IQ=False, autoConfXBUF=True, autoConfVREG=True, IntN_Mode=False, LoopBW=340.0e3, PM=55.0, FIT_KVCO=True, BWEF=1.0, FLOCK_N=200, SKIP_STEPS=[], CTUNE_METHOD='OPEN-LOOP', FLOCK_METHOD='SIMPLE', FLOCK_VCO_SPDUP=1, PROFILE=0, dbgMode=False):
        """This method does complete configuration of LMS8001 IC PLL in 5 steps:
            1. 'VCO_CTUNE' STEP
               Runs VCO Coarse Frequency Tuning and Sets FF-DIV Ratios needed for generation of F_LO frequency
                CTUNE_METHOD='OPEN-LOOP' calls the vco_auto_tune method to tune VCO to the desired frequency
                CTUNE_METHOD='OPEN-LOOP-MANUAL' calls the vco_manual_ctune method to tune VCO to the desired frequency
                CTUNE_METHOD='CLOSE-LOOP' calls the vco_manual_cloop_tune method to tune VCO to the desired frequency
            2. 'OPTIM_PLL_LOOPBW' STEP
               Optimizes PLL configuration for targeted LoopBW and Phase Margin (PM)
            3. 'OPTIM_CP_OFFSET' STEP
               Optimize CP offset current and Lock-Detector threashold settings depending on chosen PLL operating mode
            4. 'OPTIM_FAST_LOCK' STEP
               Sets Fast-Lock Settings for PLL Profile PROFILE
        """        


        # Calculate Loop-Crossover frequency
        fc=LoopBW/1.65

        # Set VCO Bias Parameters
        if (autoConfVREG):
            self.setVCOBIAS(EN=1, BYP_VCOREG=1)
        else:
            self.chip.PLL.EN_VCOBIAS=1
        
        
        # Set XBUF_SLFBEN Parameter
        if (autoConfXBUF):
            XBUF_SLFBEN=1
        else:
            XBUF_SLFBEN=self.chip.PLL.PLL_XBUF_SLFBEN
        
        
        # Step 1 - Tune PLL to generate F_LO frequency at LODIST outputs that should be manualy enabled outside this method
        if not ((1 in SKIP_STEPS) or ('VCO_CTUNE' in SKIP_STEPS)):
            # Set VCO Core Parameters
            self.setVCO(AMP=3, VDIV_SWVDD=2, PROFILE=PROFILE)
            
            status1=self.setLOFREQ(F_LO, IQ=IQ, XBUF_SLFBEN=XBUF_SLFBEN, IntN_Mode=IntN_Mode, CTUNE_METHOD=CTUNE_METHOD, PROFILE=PROFILE, dbgMode=dbgMode)
            if not (status1):
                self.chip.log('PLL Tuning to F_LO=%.5f GHz failed.' %(F_LO/1.0e9))
                return status1
        else:
            status1=True
              
        
        # Step 2 - Optimize PLL settings for targeted LoopBW
        if not ((2 in SKIP_STEPS) or ('OPTIM_PLL_LOOPBW' in SKIP_STEPS)):
            status2=self.optim_PLL_LoopBW(PM_deg=PM, fc=fc, FIT_KVCO=FIT_KVCO, PROFILE=PROFILE, dbgMode=dbgMode)
            if not (status2):
                self.chip.log('Optimization of PLL at F_LO=%.5f GHz, LoopBW=%.2f kHz and PM=%.2f deg failed.' %(F_LO/1.0e9, LoopBW/1.0e3, PM))
        else:
            status2=True
        
        # Step 3 - Optimize CP offset current Lock Detector Threashold depending on operating mode chosen (IntN or FracN)
        if not ((3 in SKIP_STEPS) or ('OPTIM_CP_OFFSET' in SKIP_STEPS)):
            status3=self.optimCPandLD(PROFILE=PROFILE, dbgMode=dbgMode)
            if not (status3):
                self.chip.log('Optimization of CP-OFS and LD-VCT at F_LO=%.5f GHz.' %(F_LO/1.0e9))
        else:
            status3=True

        # Step 4 - Configure Fast-Lock Mode Registers
        if not ((4 in SKIP_STEPS) or ('OPTIM_FAST_LOCK' in SKIP_STEPS)):
            if (BWEF>=1.0):
                self.setFLOCK(BWEF, LoopBW=BWEF*LoopBW, PM=PM, FLOCK_N=FLOCK_N, Ch_EN=[], METHOD=FLOCK_METHOD, FIT_KVCO=FIT_KVCO, FLOCK_VCO_SPDUP=FLOCK_VCO_SPDUP, PROFILE=PROFILE)
        else:
            status4=True    
        return (status1 and status2 and status3)

