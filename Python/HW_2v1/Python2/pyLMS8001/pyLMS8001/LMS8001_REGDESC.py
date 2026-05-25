
LMS8001_REGDESC="""

REGBANK ChipConfig 0x000X
REGBANK BiasLDOConfig 0x001X
REGBANK Channel_A 0b00010000000XXXXX
REGBANK Channel_B 0b00010000001XXXXX
REGBANK Channel_C 0b00010000010XXXXX
REGBANK Channel_D 0b00010000011XXXXX
REGBANK HLMIXA 0x200X
REGBANK HLMIXB 0x201X
REGBANK HLMIXC 0x202X
REGBANK HLMIXD 0x203X
REGBANK PLL_CONFIGURATION 0b01000000000XXXXX
REGBANK PLL_PROFILE_0 0x410X
REGBANK PLL_PROFILE_1 0x411X
REGBANK PLL_PROFILE_2 0x412X
REGBANK PLL_PROFILE_3 0x413X
REGBANK PLL_PROFILE_4 0x414X
REGBANK PLL_PROFILE_5 0x415X
REGBANK PLL_PROFILE_6 0x416X
REGBANK PLL_PROFILE_7 0x417X
REGISTER    SPIConfig    0x0000
    BITFIELD   SPI_SDIO_DS
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Driver strength of SPI_SDIO pad.
        #!      0 - Driver strength is 4mA (default)
        #!      1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   SPI_SDO_DS
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Driver strength of SPI_SDO pad.
        #!      0 - Driver strength is 4mA (default)
        #!      1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   SPI_SDIO_PE
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! Pull up control of SPI_SDIO pad.
        #!      0 - Pull up disengaged
        #!      1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SPI_SDO_PE
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Pull up control of SPI_SDO pad.
        #!      0 - Pull up disengaged
        #!      1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SPI_SCLK_PE
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Pull up control of SPI_SCLK pad.
        #!      0 - Pull up disengaged
        #!      1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SPI_SEN_PE
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Pull up control of SPI_SEN pad.
        #!      0 - Pull up disengaged
        #!      1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SPIMODE
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! SPI communication mode.
        #!     0 - 3 wire mode
        #!     1 - 4 wire mode (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOOutData    0x0004
    BITFIELD   GPIO_OUT_SPI<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
        #! Output data for GPIO pads from SPI
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOOUT_SEL0    0x0005
    BITFIELD   GPIO4_SEL<2:0>
        POSITION=<14:12>
        DEFAULT=000
        MODE=RWI
        #! GPIO4 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO3_SEL<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! GPIO3 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO2_SEL<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! GPIO2 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO1_SEL<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! GPIO1 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO0_SEL<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! GPIO0 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOOUT_SEL1    0x0006
    BITFIELD   GPIO9_SEL<2:0>
        POSITION=<14:12>
        DEFAULT=000
        MODE=RWI
        #! GPIO9 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO8_SEL<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! GPIO8 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO7_SEL<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! GPIO7 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO6_SEL<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! GPIO6 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
    BITFIELD   GPIO5_SEL<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! GPIO5 source select
        #!     000 - from SPI
        #!     001 - PLL_LOCK
        #!     010 - VTUNE_LOW
        #!     011 - VTUNE_HIGH
        #!     100 - Fast lock active
        #!     others - reserved
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOInData    0x0008
    BITFIELD   GPIO_IN<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=R
        #! Data read from GPIO pads.
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOConfig_PE    0x0009
    BITFIELD   GPIO_PE<8:0>
        POSITION=<8:0>
        DEFAULT=111111111
        MODE=RW
        #! GPIO pull up control
        #!      0 - Pull up disengaged
        #!      1 - Pull up engaged (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOConfig_DS    0x000A
    BITFIELD   GPIO_DS<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RW
        #! GPIO drive strength
        #!      0 - Driver strength is 4mA (default)
        #!      1 - Driver strength is 8mA
    ENDBITFIELD
ENDREGISTER

REGISTER    GPIOConfig_IO    0x000B
    BITFIELD   GPIO_InO<8:0>
        POSITION=<8:0>
        DEFAULT=111111111
        MODE=RW
        #! GPIO input/output control
        #!      0 - Pin is output
        #!      1 - Pin is input (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TEMP_SENS    0x000C
    BITFIELD   TEMP_SENS_EN
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enable the temperature sensor biasing.
    ENDBITFIELD
    BITFIELD   TEMP_SENS_CLKEN
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Temperature sensor clock enable.
    ENDBITFIELD
    BITFIELD   TEMP_START_CONV
        POSITION=8
        DEFAULT=0
        MODE=STICKYBIT
        #! Start the temperature conversion.
        #! Bit is cleared when the conversion is complete.
    ENDBITFIELD
    BITFIELD   TEMP_READ<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! Readout of temperature sensor
    ENDBITFIELD
ENDREGISTER

REGISTER    ChipInfo    0x000F
    BITFIELD   VER<4:0>
        POSITION=<15:11>
        DEFAULT=01000
        MODE=RI
        #! Chip version.
        #!     01000 - Chip version is 8.
    ENDBITFIELD
    BITFIELD   REV<4:0>
        POSITION=<10:6>
        DEFAULT=00001
        MODE=RI
        #! Chip revision.
        #!     00001 - Chip revision is 1.
    ENDBITFIELD
    BITFIELD   MASK<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RI
        #! Chip mask.
        #!     000000 - Chip mask is 0.
    ENDBITFIELD
ENDREGISTER

REGISTER    BiasConfig    0x0010
    BITFIELD   PD_CALIB_COMP
        POSITION=12
        DEFAULT=1
        MODE=RW
        #! Calibration comparator power down.
        #!      0 - Enabled
        #!      1 - Powered down (default)
    ENDBITFIELD
    BITFIELD   RP_CALIB_COMP
        POSITION=11
        DEFAULT=0
        MODE=R
        #! Comparator output. Used in rppolywo calibration algorithm.
    ENDBITFIELD
    BITFIELD   RP_CALIB_BIAS<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RW
        #! Calibration code for rppolywo. This code is set by calibration algorithm.
        #! Default value : 10000 (16)
    ENDBITFIELD
    BITFIELD   PD_FRP_BIAS
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Power down signal for Fix/RP
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_F_BIAS
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Power down signal for Fix
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_PTRP_BIAS
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down signal for PTAT/RP block
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_PT_BIAS
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power down signal for PTAT block
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_BIAS
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enable signal for central bias block
        #!     0 - Sub blocks may be selectively powered down (default)
        #!     1 - Poweres down all BIAS blocks
    ENDBITFIELD
ENDREGISTER

REGISTER    LOBUFA_LDO_Config    0x0011
    BITFIELD   EN_LOADIMP_LDO_LOBUFA
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_LOBUFA
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_LOBUFA
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_LOBUFA<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    LOBUFB_LDO_Config    0x0012
    BITFIELD   EN_LOADIMP_LDO_LOBUFB
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_LOBUFB
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_LOBUFB
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_LOBUFB<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    LOBUFC_LDO_Config    0x0013
    BITFIELD   EN_LOADIMP_LDO_LOBUFC
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_LOBUFC
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_LOBUFC
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_LOBUFC<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    LOBUFD_LDO_Config    0x0014
    BITFIELD   EN_LOADIMP_LDO_LOBUFD
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_LOBUFD
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_LOBUFD
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_LOBUFD<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    HFLNAA_LDO_Config    0x0015
    BITFIELD   EN_LOADIMP_LDO_HFLNAA
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_HFLNAA
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_HFLNAA
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_HFLNAA<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    HFLNAB_LDO_Config    0x0016
    BITFIELD   EN_LOADIMP_LDO_HFLNAB
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_HFLNAB
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_HFLNAB
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_HFLNAB<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    HFLNAC_LDO_Config    0x0017
    BITFIELD   EN_LOADIMP_LDO_HFLNAC
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_HFLNAC
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_HFLNAC
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_HFLNAC<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    HFLNAD_LDO_Config    0x0018
    BITFIELD   EN_LOADIMP_LDO_HFLNAD
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_HFLNAD
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_HFLNAD
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_HFLNAD<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    CLK_BUF_LDO_Config    0x001A
    BITFIELD   EN_LOADIMP_LDO_CLK_BUF
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_CLK_BUF
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_CLK_BUF
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LO buffer LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_CLK_BUF<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LO buffer LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_DIV_LDO_Config    0x001B
    BITFIELD   EN_LOADIMP_LDO_PLL_DIV
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_PLL_DIV
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_PLL_DIV
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the PLL divider LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_PLL_DIV<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the PLL divider LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_LDO_Config    0x001C
    BITFIELD   EN_LOADIMP_LDO_PLL_CP
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_PLL_CP
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   EN_LDO_PLL_CP
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the PLL CP LDO
        #!     0 - LDO powered down  (default)
        #!     1 - LDO enabled
    ENDBITFIELD
    BITFIELD   RDIV_PLL_CP<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the PLL CP LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    DIG_CORE_LDO_Config    0x001F
    BITFIELD   EN_LOADIMP_LDO_DIG_CORE
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependant bias
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIG_CORE
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
    ENDBITFIELD
    BITFIELD   PD_LDO_DIG_CORE
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Power down the digital core and IO ring pre-drivers LDO
        #!     0 - LDO on  (default)
        #!     1 - LDO powered down
    ENDBITFIELD
    BITFIELD   RDIV_DIG_CORE<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the digital core and IO ring pre-drivers LDO by setting the resistive voltage divider ratio.
        #! Vout = 860 mV + 3.92 mV * RDIV
        #! Default : 01100101 (101) Vout = 1.25 V
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_MIX_ICT    0x1000
    BITFIELD   CHA_MIXB_ICT<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHA_MIXB_ICT/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_MIXA_ICT<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHA_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_HFPAD_ICT    0x1001
    BITFIELD   CHA_PA_ILIN2X
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Double the linearization bias current
        #!     0 - Ilin * 1
        #!     1 - Ilin * 2
        #!     Default : 0
    ENDBITFIELD
    BITFIELD   CHA_PA_ICT_LIN<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of linearization section of HFPAD
        #!     I = Inom * CHA_PA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_PA_ICT_MAIN<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of main gm section of HFPAD
        #!     I = Inom * CHA_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD0    0x1004
    BITFIELD   CHA_PA_R50_EN0
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHA_PA_BYPASS0
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHA_PA_PD0
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_LOBUFF_PD0
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_BIAS_PD0
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_LOBUFF_PD0
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_LNA_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD1    0x1005
    BITFIELD   CHA_PA_R50_EN1
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHA_PA_BYPASS1
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHA_PA_PD1
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_LOBUFF_PD1
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_BIAS_PD1
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_LOBUFF_PD1
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_LNA_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD2    0x1006
    BITFIELD   CHA_PA_R50_EN2
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHA_PA_BYPASS2
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHA_PA_PD2
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_LOBUFF_PD2
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_BIAS_PD2
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_LOBUFF_PD2
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_LNA_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD3    0x1007
    BITFIELD   CHA_PA_R50_EN3
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHA_PA_BYPASS3
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHA_PA_PD3
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_LOBUFF_PD3
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXB_BIAS_PD3
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_LOBUFF_PD3
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_MIXA_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHA_LNA_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_CTRL0    0x1008
    BITFIELD   CHA_LNA_ICT_LIN0<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHA_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_ICT_MAIN0<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHA_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_CGSCTRL0<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_GCTRL0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_CTRL1    0x1009
    BITFIELD   CHA_LNA_ICT_LIN1<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHA_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_ICT_MAIN1<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHA_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_CGSCTRL1<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_GCTRL1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_CTRL2    0x100A
    BITFIELD   CHA_LNA_ICT_LIN2<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHA_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_ICT_MAIN2<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHA_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_CGSCTRL2<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_GCTRL2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_CTRL3    0x100B
    BITFIELD   CHA_LNA_ICT_LIN3<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHA_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_ICT_MAIN3<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHA_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHA_LNA_CGSCTRL3<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_GCTRL3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_CTRL0    0x100C
    BITFIELD   CHA_PA_LIN_LOSS0<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHA_PA_MAIN_LOSS0<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_CTRL1    0x100D
    BITFIELD   CHA_PA_LIN_LOSS1<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHA_PA_MAIN_LOSS1<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_CTRL2    0x100E
    BITFIELD   CHA_PA_LIN_LOSS2<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHA_PA_MAIN_LOSS2<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_CTRL3    0x100F
    BITFIELD   CHA_PA_LIN_LOSS3<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHA_PA_MAIN_LOSS3<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD_SEL0    0x1010
    BITFIELD   CHA_PD_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PD_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PD_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD_SEL1    0x1011
    BITFIELD   CHA_PD_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PD_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PD_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_SEL0    0x1012
    BITFIELD   CHA_LNA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_SEL1    0x1013
    BITFIELD   CHA_LNA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_SEL0    0x1014
    BITFIELD   CHA_PA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_SEL1    0x1015
    BITFIELD   CHA_PA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_INT_SEL    0x1016
    BITFIELD   CHA_PA_INT_SEL<1:0>
        POSITION=<5:4>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_LNA_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHA_PD_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PD_RB    0x101D
    BITFIELD   CHA_PA_R50_EN_RB
        POSITION=7
        DEFAULT=CHA_PA_R50_EN0
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_PA_BYPASS_RB
        POSITION=6
        DEFAULT=CHA_PA_BYPASS
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_PA_PD_RB
        POSITION=5
        DEFAULT=CHA_PA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_MIXB_LOBUFF_PD_RB
        POSITION=4
        DEFAULT=CHA_MIXB_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_MIXB_BIAS_PD_RB
        POSITION=3
        DEFAULT=CHA_MIXB_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_MIXA_LOBUFF_PD_RB
        POSITION=2
        DEFAULT=CHA_MIXA_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_MIXA_BIAS_PD_RB
        POSITION=1
        DEFAULT=CHA_MIXA_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_LNA_PD_RB
        POSITION=0
        DEFAULT=CHA_LNA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_LNA_CTRL_RB    0x101E
    BITFIELD   CHA_LNA_ICT_LIN_RB<4:0>
        POSITION=<15:11>
        DEFAULT=CHA_LNA_ICT_LIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_LNA_ICT_MAIN_RB<4:0>
        POSITION=<10:6>
        DEFAULT=CHA_LNA_ICT_MAIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_LNA_CGSCTRL_RB<1:0>
        POSITION=<5:4>
        DEFAULT=CHA_LNA_CGSCTRL<1:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_LNA_GCTRL_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHA_LNA_GCTRL<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHA_PA_CTRL_RB    0x101F
    BITFIELD   CHA_PA_LIN_LOSS_RB<3:0>
        POSITION=<7:4>
        DEFAULT=CHA_PA_LIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHA_PA_MAIN_LOSS_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHA_PA_MAIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_MIX_ICT    0x1020
    BITFIELD   CHB_MIXB_ICT<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHB_MIXB_ICT/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_MIXA_ICT<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHB_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_HFPAD_ICT    0x1021
    BITFIELD   CHB_PA_ILIN2X
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Double the linearization bias current
        #!     0 - Ilin * 1
        #!     1 - Ilin * 2
        #!     Default : 0
    ENDBITFIELD
    BITFIELD   CHB_PA_ICT_LIN<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of linearization section of HFPAD
        #!     I = Inom * CHB_PA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_PA_ICT_MAIN<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of main gm section of HFPAD
        #!     I = Inom * CHB_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD0    0x1024
    BITFIELD   CHB_PA_R50_EN0
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHB_PA_BYPASS0
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHB_PA_PD0
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_LOBUFF_PD0
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_BIAS_PD0
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_LOBUFF_PD0
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_LNA_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD1    0x1025
    BITFIELD   CHB_PA_R50_EN1
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHB_PA_BYPASS1
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHB_PA_PD1
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_LOBUFF_PD1
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_BIAS_PD1
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_LOBUFF_PD1
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_LNA_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD2    0x1026
    BITFIELD   CHB_PA_R50_EN2
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHB_PA_BYPASS2
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHB_PA_PD2
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_LOBUFF_PD2
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_BIAS_PD2
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_LOBUFF_PD2
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_LNA_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD3    0x1027
    BITFIELD   CHB_PA_R50_EN3
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHB_PA_BYPASS3
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHB_PA_PD3
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_LOBUFF_PD3
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXB_BIAS_PD3
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_LOBUFF_PD3
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_MIXA_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHB_LNA_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_CTRL0    0x1028
    BITFIELD   CHB_LNA_ICT_LIN0<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHB_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_ICT_MAIN0<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHB_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_CGSCTRL0<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_GCTRL0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_CTRL1    0x1029
    BITFIELD   CHB_LNA_ICT_LIN1<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHB_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_ICT_MAIN1<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHB_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_CGSCTRL1<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_GCTRL1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_CTRL2    0x102A
    BITFIELD   CHB_LNA_ICT_LIN2<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHB_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_ICT_MAIN2<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHB_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_CGSCTRL2<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_GCTRL2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_CTRL3    0x102B
    BITFIELD   CHB_LNA_ICT_LIN3<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHB_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_ICT_MAIN3<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHB_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHB_LNA_CGSCTRL3<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_GCTRL3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_CTRL0    0x102C
    BITFIELD   CHB_PA_LIN_LOSS0<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHB_PA_MAIN_LOSS0<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_CTRL1    0x102D
    BITFIELD   CHB_PA_LIN_LOSS1<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHB_PA_MAIN_LOSS1<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_CTRL2    0x102E
    BITFIELD   CHB_PA_LIN_LOSS2<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHB_PA_MAIN_LOSS2<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_CTRL3    0x102F
    BITFIELD   CHB_PA_LIN_LOSS3<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHB_PA_MAIN_LOSS3<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD_SEL0    0x1030
    BITFIELD   CHB_PD_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PD_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PD_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD_SEL1    0x1031
    BITFIELD   CHB_PD_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PD_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PD_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_SEL0    0x1032
    BITFIELD   CHB_LNA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_SEL1    0x1033
    BITFIELD   CHB_LNA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_SEL0    0x1034
    BITFIELD   CHB_PA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_SEL1    0x1035
    BITFIELD   CHB_PA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_INT_SEL    0x1036
    BITFIELD   CHB_PA_INT_SEL<1:0>
        POSITION=<5:4>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_LNA_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHB_PD_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PD_RB    0x103D
    BITFIELD   CHB_PA_R50_EN_RB
        POSITION=7
        DEFAULT=CHB_PA_R50_EN0
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_PA_BYPASS_RB
        POSITION=6
        DEFAULT=CHB_PA_BYPASS
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_PA_PD_RB
        POSITION=5
        DEFAULT=CHB_PA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_MIXB_LOBUFF_PD_RB
        POSITION=4
        DEFAULT=CHB_MIXB_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_MIXB_BIAS_PD_RB
        POSITION=3
        DEFAULT=CHB_MIXB_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_MIXA_LOBUFF_PD_RB
        POSITION=2
        DEFAULT=CHB_MIXA_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_MIXA_BIAS_PD_RB
        POSITION=1
        DEFAULT=CHB_MIXA_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_LNA_PD_RB
        POSITION=0
        DEFAULT=CHB_LNA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_LNA_CTRL_RB    0x103E
    BITFIELD   CHB_LNA_ICT_LIN_RB<4:0>
        POSITION=<15:11>
        DEFAULT=CHB_LNA_ICT_LIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_LNA_ICT_MAIN_RB<4:0>
        POSITION=<10:6>
        DEFAULT=CHB_LNA_ICT_MAIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_LNA_CGSCTRL_RB<1:0>
        POSITION=<5:4>
        DEFAULT=CHB_LNA_CGSCTRL<1:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_LNA_GCTRL_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHB_LNA_GCTRL<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHB_PA_CTRL_RB    0x103F
    BITFIELD   CHB_PA_LIN_LOSS_RB<3:0>
        POSITION=<7:4>
        DEFAULT=CHB_PA_LIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHB_PA_MAIN_LOSS_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHB_PA_MAIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_MIX_ICT    0x1040
    BITFIELD   CHC_MIXB_ICT<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHC_MIXB_ICT/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_MIXA_ICT<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHC_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_HFPAD_ICT    0x1041
    BITFIELD   CHC_PA_ILIN2X
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Double the linearization bias current
        #!     0 - Ilin * 1
        #!     1 - Ilin * 2
        #!     Default : 0
    ENDBITFIELD
    BITFIELD   CHC_PA_ICT_LIN<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of linearization section of HFPAD
        #!     I = Inom * CHC_PA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_PA_ICT_MAIN<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of main gm section of HFPAD
        #!     I = Inom * CHC_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD0    0x1044
    BITFIELD   CHC_PA_R50_EN0
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHC_PA_BYPASS0
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHC_PA_PD0
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_LOBUFF_PD0
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_BIAS_PD0
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_LOBUFF_PD0
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_LNA_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD1    0x1045
    BITFIELD   CHC_PA_R50_EN1
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHC_PA_BYPASS1
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHC_PA_PD1
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_LOBUFF_PD1
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_BIAS_PD1
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_LOBUFF_PD1
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_LNA_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD2    0x1046
    BITFIELD   CHC_PA_R50_EN2
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHC_PA_BYPASS2
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHC_PA_PD2
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_LOBUFF_PD2
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_BIAS_PD2
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_LOBUFF_PD2
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_LNA_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD3    0x1047
    BITFIELD   CHC_PA_R50_EN3
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHC_PA_BYPASS3
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHC_PA_PD3
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_LOBUFF_PD3
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXB_BIAS_PD3
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_LOBUFF_PD3
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_MIXA_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHC_LNA_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_CTRL0    0x1048
    BITFIELD   CHC_LNA_ICT_LIN0<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHC_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_ICT_MAIN0<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHC_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_CGSCTRL0<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_GCTRL0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_CTRL1    0x1049
    BITFIELD   CHC_LNA_ICT_LIN1<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHC_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_ICT_MAIN1<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHC_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_CGSCTRL1<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_GCTRL1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_CTRL2    0x104A
    BITFIELD   CHC_LNA_ICT_LIN2<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHC_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_ICT_MAIN2<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHC_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_CGSCTRL2<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_GCTRL2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_CTRL3    0x104B
    BITFIELD   CHC_LNA_ICT_LIN3<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHC_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_ICT_MAIN3<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHC_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHC_LNA_CGSCTRL3<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_GCTRL3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_CTRL0    0x104C
    BITFIELD   CHC_PA_LIN_LOSS0<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHC_PA_MAIN_LOSS0<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_CTRL1    0x104D
    BITFIELD   CHC_PA_LIN_LOSS1<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHC_PA_MAIN_LOSS1<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_CTRL2    0x104E
    BITFIELD   CHC_PA_LIN_LOSS2<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHC_PA_MAIN_LOSS2<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_CTRL3    0x104F
    BITFIELD   CHC_PA_LIN_LOSS3<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHC_PA_MAIN_LOSS3<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD_SEL0    0x1050
    BITFIELD   CHC_PD_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PD_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PD_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD_SEL1    0x1051
    BITFIELD   CHC_PD_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PD_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PD_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_SEL0    0x1052
    BITFIELD   CHC_LNA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_SEL1    0x1053
    BITFIELD   CHC_LNA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_SEL0    0x1054
    BITFIELD   CHC_PA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_SEL1    0x1055
    BITFIELD   CHC_PA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_INT_SEL    0x1056
    BITFIELD   CHC_PA_INT_SEL<1:0>
        POSITION=<5:4>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_LNA_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHC_PD_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PD_RB    0x105D
    BITFIELD   CHC_PA_R50_EN_RB
        POSITION=7
        DEFAULT=CHC_PA_R50_EN0
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_PA_BYPASS_RB
        POSITION=6
        DEFAULT=CHC_PA_BYPASS
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_PA_PD_RB
        POSITION=5
        DEFAULT=CHC_PA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_MIXB_LOBUFF_PD_RB
        POSITION=4
        DEFAULT=CHC_MIXB_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_MIXB_BIAS_PD_RB
        POSITION=3
        DEFAULT=CHC_MIXB_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_MIXA_LOBUFF_PD_RB
        POSITION=2
        DEFAULT=CHC_MIXA_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_MIXA_BIAS_PD_RB
        POSITION=1
        DEFAULT=CHC_MIXA_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_LNA_PD_RB
        POSITION=0
        DEFAULT=CHC_LNA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_LNA_CTRL_RB    0x105E
    BITFIELD   CHC_LNA_ICT_LIN_RB<4:0>
        POSITION=<15:11>
        DEFAULT=CHC_LNA_ICT_LIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_LNA_ICT_MAIN_RB<4:0>
        POSITION=<10:6>
        DEFAULT=CHC_LNA_ICT_MAIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_LNA_CGSCTRL_RB<1:0>
        POSITION=<5:4>
        DEFAULT=CHC_LNA_CGSCTRL<1:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_LNA_GCTRL_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHC_LNA_GCTRL<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHC_PA_CTRL_RB    0x105F
    BITFIELD   CHC_PA_LIN_LOSS_RB<3:0>
        POSITION=<7:4>
        DEFAULT=CHC_PA_LIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHC_PA_MAIN_LOSS_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHC_PA_MAIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_MIX_ICT    0x1060
    BITFIELD   CHD_MIXB_ICT<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHD_MIXB_ICT/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_MIXA_ICT<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of polarization circuit
        #!     I = Inom * CHD_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_HFPAD_ICT    0x1061
    BITFIELD   CHD_PA_ILIN2X
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Double the linearization bias current
        #!     0 - Ilin * 1
        #!     1 - Ilin * 2
        #!     Default : 0
    ENDBITFIELD
    BITFIELD   CHD_PA_ICT_LIN<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of linearization section of HFPAD
        #!     I = Inom * CHD_PA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_PA_ICT_MAIN<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias current of main gm section of HFPAD
        #!     I = Inom * CHD_MIXA_ICT/16
        #!     Default : 16
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD0    0x1064
    BITFIELD   CHD_PA_R50_EN0
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHD_PA_BYPASS0
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHD_PA_PD0
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_LOBUFF_PD0
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_BIAS_PD0
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_LOBUFF_PD0
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_LNA_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD1    0x1065
    BITFIELD   CHD_PA_R50_EN1
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHD_PA_BYPASS1
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHD_PA_PD1
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_LOBUFF_PD1
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_BIAS_PD1
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_LOBUFF_PD1
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_LNA_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD2    0x1066
    BITFIELD   CHD_PA_R50_EN2
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHD_PA_BYPASS2
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHD_PA_PD2
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_LOBUFF_PD2
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_BIAS_PD2
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_LOBUFF_PD2
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_LNA_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD3    0x1067
    BITFIELD   CHD_PA_R50_EN3
        POSITION=7
        DEFAULT=1
        MODE=RWI
        #! Controls the switch in series with 50 Ohm resistor to ground at HFPAD input.
        #!     0 - Switch is open
        #!     1 - Switch is closed
    ENDBITFIELD
    BITFIELD   CHD_PA_BYPASS3
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Controls the HFPAD bypass switches.
        #!     0 - HFPAD in not bypassed
        #!     1 - HFPAD is bypassed
        #! Note : HFPAD must be manually disabled when bypassed.
    ENDBITFIELD
    BITFIELD   CHD_PA_PD3
        POSITION=5
        DEFAULT=1
        MODE=RWI
        #! Power down for HFPAD
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_LOBUFF_PD3
        POSITION=4
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXB_BIAS_PD3
        POSITION=3
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXB bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_LOBUFF_PD3
        POSITION=2
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA LO buffer
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_MIXA_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
        #! Power down for MIXA bias
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   CHD_LNA_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
        #! Power down for LNA
        #!     0 - Enabled
        #!     1 - Powered down
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_CTRL0    0x1068
    BITFIELD   CHD_LNA_ICT_LIN0<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHD_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_ICT_MAIN0<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHD_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_CGSCTRL0<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_GCTRL0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_CTRL1    0x1069
    BITFIELD   CHD_LNA_ICT_LIN1<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHD_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_ICT_MAIN1<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHD_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_CGSCTRL1<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_GCTRL1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_CTRL2    0x106A
    BITFIELD   CHD_LNA_ICT_LIN2<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHD_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_ICT_MAIN2<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHD_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_CGSCTRL2<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_GCTRL2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_CTRL3    0x106B
    BITFIELD   CHD_LNA_ICT_LIN3<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of linearization section of LNA
        #!     I = Inom * CHD_LNA_ICT_LIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_ICT_MAIN3<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RWI
        #! Controls the bias current of main gm section of LNA
        #!     I = Inom * CHD_LNA_ICT_MAIN/16
        #!     Default : 16
    ENDBITFIELD
    BITFIELD   CHD_LNA_CGSCTRL3<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_GCTRL3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_CTRL0    0x106C
    BITFIELD   CHD_PA_LIN_LOSS0<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHD_PA_MAIN_LOSS0<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_CTRL1    0x106D
    BITFIELD   CHD_PA_LIN_LOSS1<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHD_PA_MAIN_LOSS1<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_CTRL2    0x106E
    BITFIELD   CHD_PA_LIN_LOSS2<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHD_PA_MAIN_LOSS2<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_CTRL3    0x106F
    BITFIELD   CHD_PA_LIN_LOSS3<3:0>
        POSITION=<7:4>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD linearizing section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
    BITFIELD   CHD_PA_MAIN_LOSS3<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RWI
        #! Controls the gain of HFPAD main section
        #! Pout = Pout_max - Loss
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD_SEL0    0x1070
    BITFIELD   CHD_PD_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PD_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PD_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD_SEL1    0x1071
    BITFIELD   CHD_PD_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PD_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PD_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_SEL0    0x1072
    BITFIELD   CHD_LNA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_SEL1    0x1073
    BITFIELD   CHD_LNA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_SEL0    0x1074
    BITFIELD   CHD_PA_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PA_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PA_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_SEL1    0x1075
    BITFIELD   CHD_PA_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PA_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PA_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_INT_SEL    0x1076
    BITFIELD   CHD_PA_INT_SEL<1:0>
        POSITION=<5:4>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_LNA_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   CHD_PD_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PD_RB    0x107D
    BITFIELD   CHD_PA_R50_EN_RB
        POSITION=7
        DEFAULT=CHD_PA_R50_EN0
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_PA_BYPASS_RB
        POSITION=6
        DEFAULT=CHD_PA_BYPASS
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_PA_PD_RB
        POSITION=5
        DEFAULT=CHD_PA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_MIXB_LOBUFF_PD_RB
        POSITION=4
        DEFAULT=CHD_MIXB_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_MIXB_BIAS_PD_RB
        POSITION=3
        DEFAULT=CHD_MIXB_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_MIXA_LOBUFF_PD_RB
        POSITION=2
        DEFAULT=CHD_MIXA_LOBUFF_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_MIXA_BIAS_PD_RB
        POSITION=1
        DEFAULT=CHD_MIXA_BIAS_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_LNA_PD_RB
        POSITION=0
        DEFAULT=CHD_LNA_PD
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_LNA_CTRL_RB    0x107E
    BITFIELD   CHD_LNA_ICT_LIN_RB<4:0>
        POSITION=<15:11>
        DEFAULT=CHD_LNA_ICT_LIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_LNA_ICT_MAIN_RB<4:0>
        POSITION=<10:6>
        DEFAULT=CHD_LNA_ICT_MAIN<4:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_LNA_CGSCTRL_RB<1:0>
        POSITION=<5:4>
        DEFAULT=CHD_LNA_CGSCTRL<1:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_LNA_GCTRL_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHD_LNA_GCTRL<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    CHD_PA_CTRL_RB    0x107F
    BITFIELD   CHD_PA_LIN_LOSS_RB<3:0>
        POSITION=<7:4>
        DEFAULT=CHD_PA_LIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
    BITFIELD   CHD_PA_MAIN_LOSS_RB<3:0>
        POSITION=<3:0>
        DEFAULT=CHD_PA_MAIN_LOSS<3:0>
        MODE=RB
        #! Readback the actual controlling value
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONFIG0    0x2000
    BITFIELD   HLMIXA_VGCAS0<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_ICT_BIAS0<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOBUF_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONFIG1    0x2001
    BITFIELD   HLMIXA_VGCAS1<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_ICT_BIAS1<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOBUF_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONFIG2    0x2002
    BITFIELD   HLMIXA_VGCAS2<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_ICT_BIAS2<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOBUF_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONFIG3    0x2003
    BITFIELD   HLMIXA_VGCAS3<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_ICT_BIAS3<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOBUF_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS0    0x2004
    BITFIELD   HLMIXA_MIXLOSS0<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_MIXLOSS_FINE0<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS1    0x2005
    BITFIELD   HLMIXA_MIXLOSS1<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_MIXLOSS_FINE1<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS2    0x2006
    BITFIELD   HLMIXA_MIXLOSS2<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_MIXLOSS_FINE2<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS3    0x2007
    BITFIELD   HLMIXA_MIXLOSS3<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_MIXLOSS_FINE3<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONF_SEL0    0x2008
    BITFIELD   HLMIXA_CONF_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_CONF_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_CONF_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONF_SEL1    0x2009
    BITFIELD   HLMIXA_CONF_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_CONF_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_CONF_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS_SEL0    0x200A
    BITFIELD   HLMIXA_LOSS_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOSS_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOSS_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS_SEL1    0x200B
    BITFIELD   HLMIXA_LOSS_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOSS_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_LOSS_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_INT_SEL    0x200C
    BITFIELD   HLMIXA_LOSS_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXA_CONF_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_CONFIG_RB    0x200E
    BITFIELD   HLMIXA_VGCAS_RB<6:0>
        POSITION=<13:7>
        DEFAULT=HLMIXA_VGCAS<6:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXA_ICT_BIAS_RB<4:0>
        POSITION=<6:2>
        DEFAULT=HLMIXA_ICT_BIAS<4:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXA_BIAS_PD_RB
        POSITION=1
        DEFAULT=HLMIXA_BIAS_PD
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXA_LOBUF_PD_RB
        POSITION=0
        DEFAULT=HLMIXA_LOBUF_PD
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXA_LOSS_RB    0x200F
    BITFIELD   HLMIXA_MIXLOSS_RB<3:0>
        POSITION=<5:2>
        DEFAULT=HLMIXA_MIXLOSS<3:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXA_MIXLOSS_FINE_RB<1:0>
        POSITION=<1:0>
        DEFAULT=HLMIXA_MIXLOSS_FINE<1:0>
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONFIG0    0x2010
    BITFIELD   HLMIXB_VGCAS0<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_ICT_BIAS0<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOBUF_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONFIG1    0x2011
    BITFIELD   HLMIXB_VGCAS1<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_ICT_BIAS1<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOBUF_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONFIG2    0x2012
    BITFIELD   HLMIXB_VGCAS2<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_ICT_BIAS2<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOBUF_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONFIG3    0x2013
    BITFIELD   HLMIXB_VGCAS3<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_ICT_BIAS3<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOBUF_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS0    0x2014
    BITFIELD   HLMIXB_MIXLOSS0<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_MIXLOSS_FINE0<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS1    0x2015
    BITFIELD   HLMIXB_MIXLOSS1<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_MIXLOSS_FINE1<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS2    0x2016
    BITFIELD   HLMIXB_MIXLOSS2<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_MIXLOSS_FINE2<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS3    0x2017
    BITFIELD   HLMIXB_MIXLOSS3<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_MIXLOSS_FINE3<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONF_SEL0    0x2018
    BITFIELD   HLMIXB_CONF_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_CONF_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_CONF_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONF_SEL1    0x2019
    BITFIELD   HLMIXB_CONF_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_CONF_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_CONF_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS_SEL0    0x201A
    BITFIELD   HLMIXB_LOSS_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOSS_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOSS_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS_SEL1    0x201B
    BITFIELD   HLMIXB_LOSS_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOSS_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_LOSS_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_INT_SEL    0x201C
    BITFIELD   HLMIXB_LOSS_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXB_CONF_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_CONFIG_RB    0x201E
    BITFIELD   HLMIXB_VGCAS_RB<6:0>
        POSITION=<13:7>
        DEFAULT=HLMIXB_VGCAS<6:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXB_ICT_BIAS_RB<4:0>
        POSITION=<6:2>
        DEFAULT=HLMIXB_ICT_BIAS<4:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXB_BIAS_PD_RB
        POSITION=1
        DEFAULT=HLMIXB_BIAS_PD
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXB_LOBUF_PD_RB
        POSITION=0
        DEFAULT=HLMIXB_LOBUF_PD
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXB_LOSS_RB    0x201F
    BITFIELD   HLMIXB_MIXLOSS_RB<3:0>
        POSITION=<5:2>
        DEFAULT=HLMIXB_MIXLOSS<3:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXB_MIXLOSS_FINE_RB<1:0>
        POSITION=<1:0>
        DEFAULT=HLMIXB_MIXLOSS_FINE<1:0>
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONFIG0    0x2020
    BITFIELD   HLMIXC_VGCAS0<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_ICT_BIAS0<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOBUF_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONFIG1    0x2021
    BITFIELD   HLMIXC_VGCAS1<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_ICT_BIAS1<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOBUF_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONFIG2    0x2022
    BITFIELD   HLMIXC_VGCAS2<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_ICT_BIAS2<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOBUF_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONFIG3    0x2023
    BITFIELD   HLMIXC_VGCAS3<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_ICT_BIAS3<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOBUF_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS0    0x2024
    BITFIELD   HLMIXC_MIXLOSS0<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_MIXLOSS_FINE0<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS1    0x2025
    BITFIELD   HLMIXC_MIXLOSS1<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_MIXLOSS_FINE1<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS2    0x2026
    BITFIELD   HLMIXC_MIXLOSS2<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_MIXLOSS_FINE2<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS3    0x2027
    BITFIELD   HLMIXC_MIXLOSS3<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_MIXLOSS_FINE3<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONF_SEL0    0x2028
    BITFIELD   HLMIXC_CONF_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_CONF_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_CONF_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONF_SEL1    0x2029
    BITFIELD   HLMIXC_CONF_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_CONF_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_CONF_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS_SEL0    0x202A
    BITFIELD   HLMIXC_LOSS_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOSS_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOSS_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS_SEL1    0x202B
    BITFIELD   HLMIXC_LOSS_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOSS_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_LOSS_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_INT_SEL    0x202C
    BITFIELD   HLMIXC_LOSS_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXC_CONF_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_CONFIG_RB    0x202E
    BITFIELD   HLMIXC_VGCAS_RB<6:0>
        POSITION=<13:7>
        DEFAULT=HLMIXC_VGCAS<6:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXC_ICT_BIAS_RB<4:0>
        POSITION=<6:2>
        DEFAULT=HLMIXC_ICT_BIAS<4:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXC_BIAS_PD_RB
        POSITION=1
        DEFAULT=HLMIXC_BIAS_PD
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXC_LOBUF_PD_RB
        POSITION=0
        DEFAULT=HLMIXC_LOBUF_PD
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXC_LOSS_RB    0x202F
    BITFIELD   HLMIXC_MIXLOSS_RB<3:0>
        POSITION=<5:2>
        DEFAULT=HLMIXC_MIXLOSS<3:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXC_MIXLOSS_FINE_RB<1:0>
        POSITION=<1:0>
        DEFAULT=HLMIXC_MIXLOSS_FINE<1:0>
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONFIG0    0x2030
    BITFIELD   HLMIXD_VGCAS0<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_ICT_BIAS0<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_BIAS_PD0
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOBUF_PD0
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONFIG1    0x2031
    BITFIELD   HLMIXD_VGCAS1<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_ICT_BIAS1<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_BIAS_PD1
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOBUF_PD1
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONFIG2    0x2032
    BITFIELD   HLMIXD_VGCAS2<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_ICT_BIAS2<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_BIAS_PD2
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOBUF_PD2
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONFIG3    0x2033
    BITFIELD   HLMIXD_VGCAS3<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_ICT_BIAS3<4:0>
        POSITION=<6:2>
        DEFAULT=10000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_BIAS_PD3
        POSITION=1
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOBUF_PD3
        POSITION=0
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS0    0x2034
    BITFIELD   HLMIXD_MIXLOSS0<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_MIXLOSS_FINE0<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS1    0x2035
    BITFIELD   HLMIXD_MIXLOSS1<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_MIXLOSS_FINE1<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS2    0x2036
    BITFIELD   HLMIXD_MIXLOSS2<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_MIXLOSS_FINE2<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS3    0x2037
    BITFIELD   HLMIXD_MIXLOSS3<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_MIXLOSS_FINE3<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONF_SEL0    0x2038
    BITFIELD   HLMIXD_CONF_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_CONF_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_CONF_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONF_SEL1    0x2039
    BITFIELD   HLMIXD_CONF_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_CONF_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_CONF_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS_SEL0    0x203A
    BITFIELD   HLMIXD_LOSS_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOSS_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOSS_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS_SEL1    0x203B
    BITFIELD   HLMIXD_LOSS_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOSS_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_LOSS_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_INT_SEL    0x203C
    BITFIELD   HLMIXD_LOSS_INT_SEL<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
    BITFIELD   HLMIXD_CONF_INT_SEL<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_CONFIG_RB    0x203E
    BITFIELD   HLMIXD_VGCAS_RB<6:0>
        POSITION=<13:7>
        DEFAULT=HLMIXD_VGCAS<6:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXD_ICT_BIAS_RB<4:0>
        POSITION=<6:2>
        DEFAULT=HLMIXD_ICT_BIAS<4:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXD_BIAS_PD_RB
        POSITION=1
        DEFAULT=HLMIXD_BIAS_PD
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXD_LOBUF_PD_RB
        POSITION=0
        DEFAULT=HLMIXD_LOBUF_PD
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    HLMIXD_LOSS_RB    0x203F
    BITFIELD   HLMIXD_MIXLOSS_RB<3:0>
        POSITION=<5:2>
        DEFAULT=HLMIXD_MIXLOSS<3:0>
        MODE=RB
    ENDBITFIELD
    BITFIELD   HLMIXD_MIXLOSS_FINE_RB<1:0>
        POSITION=<1:0>
        DEFAULT=HLMIXD_MIXLOSS_FINE<1:0>
        MODE=RB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VREG    0x4000
    BITFIELD   EN_VCOBIAS
        POSITION=11
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   BYP_VCOREG
        POSITION=10
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   CURLIM_VCOREG
        POSITION=9
        DEFAULT=1
        MODE=RW
    ENDBITFIELD
    BITFIELD   SPDUP_VCOREG
        POSITION=8
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   VDIV_VCOREG<7:0>
        POSITION=<7:0>
        DEFAULT=00010000
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CFG_XBUF    0x4001
    BITFIELD   PLL_XBUF_SLFBEN
        POSITION=2
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_XBUF_BYPEN
        POSITION=1
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_XBUF_EN
        POSITION=0
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CAL_AUTO0    0x4002
    BITFIELD   FCAL_START
        POSITION=12
        DEFAULT=0
        MODE=STICKYBIT
    ENDBITFIELD
    BITFIELD   VCO_SEL_FINAL_VAL
        POSITION=11
        DEFAULT=0
        MODE=R
    ENDBITFIELD
    BITFIELD   VCO_SEL_FINAL<1:0>
        POSITION=<10:9>
        DEFAULT=00
        MODE=R
    ENDBITFIELD
    BITFIELD   FREQ_FINAL_VAL
        POSITION=8
        DEFAULT=0
        MODE=R
    ENDBITFIELD
    BITFIELD   FREQ_FINAL<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CAL_AUTO1    0x4003
    BITFIELD   VCO_SEL_FORCE
        POSITION=13
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   VCO_SEL_INIT<1:0>
        POSITION=<12:11>
        DEFAULT=10
        MODE=RW
    ENDBITFIELD
    BITFIELD   FREQ_INIT_POS<2:0>
        POSITION=<10:8>
        DEFAULT=111
        MODE=RW
    ENDBITFIELD
    BITFIELD   FREQ_INIT<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CAL_AUTO2    0x4004
    BITFIELD   FREQ_SETTLING_N<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RW
    ENDBITFIELD
    BITFIELD   VTUNE_WAIT_N<7:0>
        POSITION=<7:0>
        DEFAULT=01000000
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CAL_AUTO3    0x4005
    BITFIELD   VCO_SEL_FREQ_MAX<7:0>
        POSITION=<15:8>
        DEFAULT=11111010
        MODE=RW
    ENDBITFIELD
    BITFIELD   VCO_SEL_FREQ_MIN<7:0>
        POSITION=<7:0>
        DEFAULT=00000101
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CAL_MAN    0x4006
    BITFIELD   VCO_FREQ_MAN<7:0>
        POSITION=<15:8>
        DEFAULT=10000000
        MODE=RW
    ENDBITFIELD
    BITFIELD   VCO_SEL_MAN<1:0>
        POSITION=<7:6>
        DEFAULT=10
        MODE=RW
    ENDBITFIELD
    BITFIELD   FREQ_HIGH
        POSITION=5
        DEFAULT=0
        MODE=R
    ENDBITFIELD
    BITFIELD   FREQ_EQUAL
        POSITION=4
        DEFAULT=0
        MODE=R
    ENDBITFIELD
    BITFIELD   FREQ_LOW
        POSITION=3
        DEFAULT=0
        MODE=R
    ENDBITFIELD
    BITFIELD   CTUNE_STEP_DONE
        POSITION=2
        DEFAULT=0
        MODE=R
    ENDBITFIELD
    BITFIELD   CTUNE_START
        POSITION=1
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   CTUNE_EN
        POSITION=0
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CFG_SEL0    0x4008
    BITFIELD   PLL_CFG_SEL0_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   PLL_CFG_SEL0_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   PLL_CFG_SEL0_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CFG_SEL1    0x4009
    BITFIELD   PLL_CFG_SEL1_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   PLL_CFG_SEL1_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   PLL_CFG_SEL1_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CFG_SEL2    0x400A
    BITFIELD   PLL_CFG_SEL2_INTERNAL
        POSITION=11
        DEFAULT=1
        MODE=RWI
    ENDBITFIELD
    BITFIELD   PLL_CFG_SEL2_INVERT
        POSITION=10
        DEFAULT=0
        MODE=RWI
    ENDBITFIELD
    BITFIELD   PLL_CFG_SEL2_MASK<8:0>
        POSITION=<8:0>
        DEFAULT=000000000
        MODE=RWI
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CFG    0x400B
    BITFIELD   PLL_RSTN
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! PLL reset, active low.
    ENDBITFIELD
    BITFIELD   CTUNE_RES<1:0>
        POSITION=<8:7>
        DEFAULT=01
        MODE=RW
        #! PLL capacitor bank tuning resolution.
    ENDBITFIELD
    BITFIELD   PLL_CALIBRATION_MODE
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! PLL calibration mode.
        #!     0 - Automatic calibration (default)
        #!     1 - Manual calibration
    ENDBITFIELD
    BITFIELD   PLL_CALIBRATION_EN
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Activate PLL calibration.
        #!     0 - Normal mode (default)
        #!     1 - Calibration mode
    ENDBITFIELD
    BITFIELD   PLL_FLOCK_INTERNAL
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Fast lock control.
        #!     0 - Normal operation. Fast lock select signal comes from fast lock state machine. (default)
        #!     1 - Debug mode. Fast lock select signal is forced by PLL_FLOCK_INTVAL
    ENDBITFIELD
    BITFIELD   PLL_FLOCK_INTVAL
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Fast lock control internal select value.
    ENDBITFIELD
    BITFIELD   PLL_CFG_INT_SEL<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! Internal PLL profile control.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CFG_STATUS    0x400C
    BITFIELD   VTUNE_HIGH
        POSITION=2
        DEFAULT=0
        MODE=R
        #! Tuning voltage high.
    ENDBITFIELD
    BITFIELD   VTUNE_LOW
        POSITION=1
        DEFAULT=0
        MODE=R
        #! Tuning voltage low.
    ENDBITFIELD
    BITFIELD   PLL_LOCK
        POSITION=0
        DEFAULT=0
        MODE=R
        #! PLL lock detect.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG1    0x400E
    BITFIELD   SEL_BIAS_CORE
        POSITION=10
        DEFAULT=0
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_LODIST_ICT_CORE<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_LODIST_ICT_BUF<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG2    0x400F
    BITFIELD   PLL_ICT_OUT3<1:0>
        POSITION=<7:6>
        DEFAULT=10
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_ICT_OUT2<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_ICT_OUT1<1:0>
        POSITION=<3:2>
        DEFAULT=10
        MODE=RW
    ENDBITFIELD
    BITFIELD   PLL_ICT_OUT0<1:0>
        POSITION=<1:0>
        DEFAULT=10
        MODE=RW
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_BIST1    0x4010
    BITFIELD   BSIGL<6:0>
        POSITION=<15:9>
        DEFAULT=0000000
        MODE=RI
        #! BIST signature. Read only.
    ENDBITFIELD
    BITFIELD   BSTATE
        POSITION=8
        DEFAULT=0
        MODE=RI
        #! BIST state indicator
        #!     0 - BIST not running (default)
        #!     1 - BIST running
    ENDBITFIELD
    BITFIELD   EN_SDM_TSTO
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enable test buffer output
    ENDBITFIELD
    BITFIELD   BEN
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable BIST
    ENDBITFIELD
    BITFIELD   BSTART
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Starts BIST
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_BIST2    0x4011
    BITFIELD   BSIGH<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RI
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_0    0x4100
    BITFIELD   PLL_LODIST_EN_BIAS_0
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_0
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_0
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_0
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_0
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_0
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_0
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_0
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_0
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_0
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_0
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_0
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_0
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_0    0x4101
    BITFIELD   R3_0<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_0<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_0<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_0    0x4102
    BITFIELD   VTUNE_VCT_0<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_0
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_0    0x4103
    BITFIELD   FLIP_0
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_0<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_0<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_0<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_0    0x4104
    BITFIELD   LD_VCT_0<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_0<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_0    0x4105
    BITFIELD   VCO_FREQ_0<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_0    0x4106
    BITFIELD   SPDUP_VCO_0
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_0
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_0<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_0<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_0<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_0    0x4107
    BITFIELD   FFDIV_SEL_0
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_0<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_0<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_0    0x4108
    BITFIELD   INTMOD_EN_0
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_0
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_0
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_0
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_0<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_0    0x4109
    BITFIELD   FRACMODL_0<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_0    0x410A
    BITFIELD   FRACMODH_0<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_0    0x410B
    BITFIELD   PLL_LODIST_EN_OUT_0<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_0<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_0<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_0<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_0<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_0    0x410C
    BITFIELD   FLOCK_R3_0<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_0<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_0<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_0<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_0    0x410D
    BITFIELD   FLOCK_C3_0<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_0<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_0<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_0    0x410E
    BITFIELD   FLOCK_LODIST_EN_OUT_0<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_0
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_0<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_1    0x4110
    BITFIELD   PLL_LODIST_EN_BIAS_1
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_1
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_1
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_1
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_1
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_1
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_1
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_1
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_1
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_1
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_1
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_1
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_1
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_1    0x4111
    BITFIELD   R3_1<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_1<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_1<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_1    0x4112
    BITFIELD   VTUNE_VCT_1<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_1
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_1    0x4113
    BITFIELD   FLIP_1
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_1<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_1<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_1<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_1    0x4114
    BITFIELD   LD_VCT_1<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_1<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_1    0x4115
    BITFIELD   VCO_FREQ_1<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_1    0x4116
    BITFIELD   SPDUP_VCO_1
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_1
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_1<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_1<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_1<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_1    0x4117
    BITFIELD   FFDIV_SEL_1
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_1<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_1<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_1    0x4118
    BITFIELD   INTMOD_EN_1
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_1
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_1
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_1
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_1<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_1    0x4119
    BITFIELD   FRACMODL_1<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_1    0x411A
    BITFIELD   FRACMODH_1<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_1    0x411B
    BITFIELD   PLL_LODIST_EN_OUT_1<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_1<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_1<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_1<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_1<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_1    0x411C
    BITFIELD   FLOCK_R3_1<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_1<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_1<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_1<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_1    0x411D
    BITFIELD   FLOCK_C3_1<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_1<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_1<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_1    0x411E
    BITFIELD   FLOCK_LODIST_EN_OUT_1<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_1
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_1<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_2    0x4120
    BITFIELD   PLL_LODIST_EN_BIAS_2
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_2
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_2
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_2
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_2
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_2
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_2
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_2
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_2
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_2
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_2
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_2
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_2
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_2    0x4121
    BITFIELD   R3_2<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_2<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_2<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_2    0x4122
    BITFIELD   VTUNE_VCT_2<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_2
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_2    0x4123
    BITFIELD   FLIP_2
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_2<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_2<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_2<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_2    0x4124
    BITFIELD   LD_VCT_2<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_2<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_2    0x4125
    BITFIELD   VCO_FREQ_2<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_2    0x4126
    BITFIELD   SPDUP_VCO_2
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_2
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_2<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_2<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_2<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_2    0x4127
    BITFIELD   FFDIV_SEL_2
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_2<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_2<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_2    0x4128
    BITFIELD   INTMOD_EN_2
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_2
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_2
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_2
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_2<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_2    0x4129
    BITFIELD   FRACMODL_2<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_2    0x412A
    BITFIELD   FRACMODH_2<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_2    0x412B
    BITFIELD   PLL_LODIST_EN_OUT_2<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_2<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_2<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_2<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_2<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_2    0x412C
    BITFIELD   FLOCK_R3_2<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_2<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_2<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_2<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_2    0x412D
    BITFIELD   FLOCK_C3_2<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_2<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_2<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_2    0x412E
    BITFIELD   FLOCK_LODIST_EN_OUT_2<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_2
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_2<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_3    0x4130
    BITFIELD   PLL_LODIST_EN_BIAS_3
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_3
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_3
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_3
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_3
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_3
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_3
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_3
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_3
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_3
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_3
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_3
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_3
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_3    0x4131
    BITFIELD   R3_3<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_3<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_3<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_3    0x4132
    BITFIELD   VTUNE_VCT_3<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_3
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_3    0x4133
    BITFIELD   FLIP_3
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_3<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_3<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_3<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_3    0x4134
    BITFIELD   LD_VCT_3<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_3<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_3    0x4135
    BITFIELD   VCO_FREQ_3<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_3    0x4136
    BITFIELD   SPDUP_VCO_3
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_3
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_3<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_3<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_3<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_3    0x4137
    BITFIELD   FFDIV_SEL_3
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_3<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_3<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_3    0x4138
    BITFIELD   INTMOD_EN_3
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_3
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_3
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_3
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_3<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_3    0x4139
    BITFIELD   FRACMODL_3<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_3    0x413A
    BITFIELD   FRACMODH_3<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_3    0x413B
    BITFIELD   PLL_LODIST_EN_OUT_3<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_3<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_3<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_3<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_3<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_3    0x413C
    BITFIELD   FLOCK_R3_3<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_3<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_3<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_3<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_3    0x413D
    BITFIELD   FLOCK_C3_3<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_3<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_3<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_3    0x413E
    BITFIELD   FLOCK_LODIST_EN_OUT_3<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_3
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_3<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_4    0x4140
    BITFIELD   PLL_LODIST_EN_BIAS_4
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_4
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_4
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_4
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_4
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_4
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_4
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_4
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_4
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_4
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_4
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_4
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_4
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_4    0x4141
    BITFIELD   R3_4<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_4<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_4<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_4<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_4    0x4142
    BITFIELD   VTUNE_VCT_4<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_4
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_4<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_4    0x4143
    BITFIELD   FLIP_4
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_4<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_4<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_4<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_4    0x4144
    BITFIELD   LD_VCT_4<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_4<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_4    0x4145
    BITFIELD   VCO_FREQ_4<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_4    0x4146
    BITFIELD   SPDUP_VCO_4
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_4
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_4<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_4<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_4<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_4    0x4147
    BITFIELD   FFDIV_SEL_4
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_4<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_4<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_4    0x4148
    BITFIELD   INTMOD_EN_4
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_4
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_4
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_4
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_4<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_4    0x4149
    BITFIELD   FRACMODL_4<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_4    0x414A
    BITFIELD   FRACMODH_4<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_4    0x414B
    BITFIELD   PLL_LODIST_EN_OUT_4<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_4<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_4<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_4<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_4<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_4    0x414C
    BITFIELD   FLOCK_R3_4<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_4<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_4<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_4<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_4    0x414D
    BITFIELD   FLOCK_C3_4<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_4<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_4<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_4    0x414E
    BITFIELD   FLOCK_LODIST_EN_OUT_4<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_4
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_4<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_5    0x4150
    BITFIELD   PLL_LODIST_EN_BIAS_5
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_5
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_5
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_5
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_5
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_5
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_5
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_5
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_5
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_5
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_5
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_5
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_5
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_5    0x4151
    BITFIELD   R3_5<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_5<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_5<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_5<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_5    0x4152
    BITFIELD   VTUNE_VCT_5<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_5
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_5<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_5    0x4153
    BITFIELD   FLIP_5
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_5<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_5<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_5<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_5    0x4154
    BITFIELD   LD_VCT_5<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_5<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_5    0x4155
    BITFIELD   VCO_FREQ_5<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_5    0x4156
    BITFIELD   SPDUP_VCO_5
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_5
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_5<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_5<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_5<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_5    0x4157
    BITFIELD   FFDIV_SEL_5
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_5<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_5<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_5    0x4158
    BITFIELD   INTMOD_EN_5
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_5
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_5
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_5
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_5<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_5    0x4159
    BITFIELD   FRACMODL_5<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_5    0x415A
    BITFIELD   FRACMODH_5<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_5    0x415B
    BITFIELD   PLL_LODIST_EN_OUT_5<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_5<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_5<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_5<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_5<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_5    0x415C
    BITFIELD   FLOCK_R3_5<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_5<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_5<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_5<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_5    0x415D
    BITFIELD   FLOCK_C3_5<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_5<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_5<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_5    0x415E
    BITFIELD   FLOCK_LODIST_EN_OUT_5<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_5
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_5<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_6    0x4160
    BITFIELD   PLL_LODIST_EN_BIAS_6
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_6
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_6
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_6
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_6
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_6
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_6
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_6
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_6
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_6
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_6
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_6
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_6
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_6    0x4161
    BITFIELD   R3_6<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_6<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_6<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_6<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_6    0x4162
    BITFIELD   VTUNE_VCT_6<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_6
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_6<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_6    0x4163
    BITFIELD   FLIP_6
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_6<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_6<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_6<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_6    0x4164
    BITFIELD   LD_VCT_6<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_6<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_6    0x4165
    BITFIELD   VCO_FREQ_6<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_6    0x4166
    BITFIELD   SPDUP_VCO_6
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_6
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_6<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_6<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_6<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_6    0x4167
    BITFIELD   FFDIV_SEL_6
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_6<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_6<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_6    0x4168
    BITFIELD   INTMOD_EN_6
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_6
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_6
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_6
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_6<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_6    0x4169
    BITFIELD   FRACMODL_6<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_6    0x416A
    BITFIELD   FRACMODH_6<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_6    0x416B
    BITFIELD   PLL_LODIST_EN_OUT_6<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_6<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_6<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_6<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_6<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_6    0x416C
    BITFIELD   FLOCK_R3_6<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_6<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_6<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_6<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_6    0x416D
    BITFIELD   FLOCK_C3_6<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_6<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_6<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_6    0x416E
    BITFIELD   FLOCK_LODIST_EN_OUT_6<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_6
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_6<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_ENABLE_7    0x4170
    BITFIELD   PLL_LODIST_EN_BIAS_7
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Enable for LO distribution bias.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_EN_DIV2IQ_7
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Enable for IQ generator in LO distribution.
        #!     0 - Clock is not divided by 2
        #!     1 - Clock is divided by 2, I and Q are generated
    ENDBITFIELD
    BITFIELD   PLL_EN_VTUNE_COMP_7
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! Enable for tuning voltage comparator in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_LD_7
        POSITION=9
        DEFAULT=0
        MODE=RWI
        #! Lock detector enable.
    ENDBITFIELD
    BITFIELD   PLL_EN_PFD_7
        POSITION=8
        DEFAULT=0
        MODE=RWI
        #! Enable for PFD in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CP_7
        POSITION=7
        DEFAULT=0
        MODE=RWI
        #! Enable for charge pump in PLL.
    ENDBITFIELD
    BITFIELD   PLL_EN_CPOFS_7
        POSITION=6
        DEFAULT=0
        MODE=RWI
        #! Enable for offset (bleeding) current in charge pump.
    ENDBITFIELD
    BITFIELD   PLL_EN_VCO_7
        POSITION=5
        DEFAULT=0
        MODE=RWI
        #! Enable for VCO.
    ENDBITFIELD
    BITFIELD   PLL_EN_FFDIV_7
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider in PLL.
        #!     0 - Output clock is not divided
    ENDBITFIELD
    BITFIELD   PLL_EN_FB_PDIV2_7
        POSITION=3
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback pre-divider.
        #!     0 - Output clock is directly fed to feedback divider
    ENDBITFIELD
    BITFIELD   PLL_EN_FFCORE_7
        POSITION=2
        DEFAULT=0
        MODE=RWI
        #! Enable for feed-forward divider core
    ENDBITFIELD
    BITFIELD   PLL_EN_FBDIV_7
        POSITION=1
        DEFAULT=0
        MODE=RWI
        #! Enable for feedback divider core
    ENDBITFIELD
    BITFIELD   PLL_SDM_CLK_EN_7
        POSITION=0
        DEFAULT=0
        MODE=RWI
        #! Enable for sigma-delta modulator
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG1_7    0x4171
    BITFIELD   R3_7<3:0>
        POSITION=<15:12>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R3_val = 9 kOhm/R3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   R2_7<3:0>
        POSITION=<11:8>
        DEFAULT=0001
        MODE=RWI
        #! Control word for loop filter.
        #! R2_val = 15.6 kOhm/R2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C2_7<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C2 in PLL loop filter.
        #! C2_val = 300 pF+7.5 pF * C2<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
    BITFIELD   C1_7<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C1 in PLL loop filter.
        #! C1_val = 1.8 pF*C1<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LPF_CFG2_7    0x4172
    BITFIELD   VTUNE_VCT_7<1:0>
        POSITION=<6:5>
        DEFAULT=01
        MODE=RWI
        #! Tuning voltage control word during coarse tuning (LPFSW=1).
        #!     00 - 300 mV,
        #!     01 - 600 mV,
        #!     10 - 750 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   LPFSW_7
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Loop filter control.
        #!     0 - PLL loop is closed,
        #!     1 - PLL loop is open and tuning voltage is set to value specified by VTUNE_VCT<1:0>.
        #! When LFPSW=1 PLL is in open-loop configuration for coarse tuning.
    ENDBITFIELD
    BITFIELD   C3_7<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Control word for C3 in PLL loop filter.
        #! C3_val = 3 pF * C3<3:0>
        #! When fast lock mode is enabled, this is the final value.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG0_7    0x4173
    BITFIELD   FLIP_7
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Flip for PFD inputs
        #!     0 - Normal operation,
        #!     1 - Inputs are interchanged
    ENDBITFIELD
    BITFIELD   DEL_7<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RWI
        #! Reset path delay
    ENDBITFIELD
    BITFIELD   PULSE_7<5:0>
        POSITION=<11:6>
        DEFAULT=000100
        MODE=RWI
        #! Charge pump pulse current
        #!     I = 25 uA * PULSE<5:0>
    ENDBITFIELD
    BITFIELD   OFS_7<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current
        #!     I = 6.25 uA * OFS<5:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_CP_CFG1_7    0x4174
    BITFIELD   LD_VCT_7<1:0>
        POSITION=<6:5>
        DEFAULT=10
        MODE=RWI
        #! Threshold voltage for lock detector
        #!     00 - 600 mV,
        #!     01 - 700 mV,
        #!     10 - 800 mV,
        #!     11 - 900 mV.
    ENDBITFIELD
    BITFIELD   ICT_CP_7<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RWI
        #! Charge pump bias current.
        #! ICP_BIAS = ICP_BIAS_NOM * ICT_CP<4:0>/16
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_FREQ_7    0x4175
    BITFIELD   VCO_FREQ_7<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RWI
        #! VCO cap bank code.
        #!     00000000 - lowest frequency
        #!     11111111 - highest frequency
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_VCO_CFG_7    0x4176
    BITFIELD   SPDUP_VCO_7
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Speed-up VCO core by bypassing the noise filter
    ENDBITFIELD
    BITFIELD   VCO_AAC_EN_7
        POSITION=11
        DEFAULT=1
        MODE=RWI
        #! Enable for automatic VCO amplitude control.
    ENDBITFIELD
    BITFIELD   VDIV_SWVDD_7<1:0>
        POSITION=<10:9>
        DEFAULT=10
        MODE=RWI
        #! Capacitor bank switches bias voltage
        #!     00 - 600 mV,
        #!     01 - 800 mV,
        #!     10 - 1000 mV,
        #!     11 - 1200 mV.
    ENDBITFIELD
    BITFIELD   VCO_SEL_7<1:0>
        POSITION=<8:7>
        DEFAULT=11
        MODE=RWI
        #! VCO core selection
        #!     00 - External VCO,
        #!     01 - Low-frequency band VCO (4 - 6 GHz),
        #!     10 - Mid-frequency band VCO (6 - 8 GHz),
        #!     11 - High-frequency band VCO (8 - 10 GHz).
    ENDBITFIELD
    BITFIELD   VCO_AMP_7<6:0>
        POSITION=<6:0>
        DEFAULT=0000001
        MODE=RWI
        #! VCO amplitude control word.
        #!     0000000 - minimum amplitude
        #! Lowest two bits control the VCO core current.
        #! Other bits are used for fine amplitude control, automatically determined when VCO_AAC_EN=1
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FF_CFG_7    0x4177
    BITFIELD   FFDIV_SEL_7
        POSITION=4
        DEFAULT=0
        MODE=RWI
        #! Feed-forward divider multiplexer select bit
        #!     0 - No division,
        #!     1 - Input frequency is divided
    ENDBITFIELD
    BITFIELD   FFCORE_MOD_7<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RWI
        #! Feed-forward divider core modulus
        #!     00 - No division
        #!     01 - Div by 2
        #!     10 - Div by 4
        #!     11 - Div by 8
    ENDBITFIELD
    BITFIELD   FF_MOD_7<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RWI
        #! Multiplexer for divider outputs. In normal operation FF_MOD should be equal to FFCORE_MOD.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_SDM_CFG_7    0x4178
    BITFIELD   INTMOD_EN_7
        POSITION=14
        DEFAULT=0
        MODE=RWI
        #! Integer mode enable
    ENDBITFIELD
    BITFIELD   DITHER_EN_7
        POSITION=13
        DEFAULT=0
        MODE=RWI
        #! Enable dithering in SDM
        #!     0 - Disabled
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_7
        POSITION=12
        DEFAULT=0
        MODE=RWI
        #! Selects between the feedback divider output and FREF for SDM
        #!     0 - CLK CLK_DIV
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   REV_SDMCLK_7
        POSITION=11
        DEFAULT=0
        MODE=RWI
        #! Reverses the SDM clock
        #!     0 - Normal
        #!     1 - Reversed (after INV)
    ENDBITFIELD
    BITFIELD   INTMOD_7<9:0>
        POSITION=<9:0>
        DEFAULT=0011011000
        MODE=RWI
        #! Integer section of division ratio.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODL_7    0x4179
    BITFIELD   FRACMODL_7<15:0>
        POSITION=<15:0>
        DEFAULT=0101011100110000
        MODE=RWI
        #! Fractional control of the division ratio LSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FRACMODH_7    0x417A
    BITFIELD   FRACMODH_7<3:0>
        POSITION=<3:0>
        DEFAULT=0101
        MODE=RWI
        #! Fractional control of the division ratio MSB
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_LODIST_CFG_7    0x417B
    BITFIELD   PLL_LODIST_EN_OUT_7<3:0>
        POSITION=<15:12>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals.
        #! Each bit is an enable for individual channel.
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT3_7<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 3 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT2_7<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 2 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT1_7<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 1 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
    BITFIELD   PLL_LODIST_FSP_OUT0_7<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RWI
        #! LO distribution channel 0 frequency, sign and phase control.
        #!     FSP_OUT<2> - Frequency division control
        #!         0 - LO is divided by 2,
        #!         1 - LO is not divided.
        #!     FSP_OUT<1> - LO sign
        #!         0 - LO is not inverted
        #!         1 - LO is inverted
        #!     FSP_OUT<0> - LO phase
        #!         0 - LO phase 0 deg (I)
        #!         1 - LO phase 90 deg (Q)
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG1_7    0x417C
    BITFIELD   FLOCK_R3_7<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R3 used during fact lock.
    ENDBITFIELD
    BITFIELD   FLOCK_R2_7<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RWI
        #! Loop filter R2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C2_7<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C2 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_C1_7<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C1 used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG2_7    0x417D
    BITFIELD   FLOCK_C3_7<3:0>
        POSITION=<15:12>
        DEFAULT=1000
        MODE=RWI
        #! Loop filter C3 used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_PULSE_7<5:0>
        POSITION=<11:6>
        DEFAULT=111111
        MODE=RWI
        #! Charge pump pulse current used during fast lock.
    ENDBITFIELD
    BITFIELD   FLOCK_OFS_7<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RWI
        #! Charge pump offset (bleeding) current used during fast lock.
    ENDBITFIELD
ENDREGISTER

REGISTER    PLL_FLOCK_CFG3_7    0x417E
    BITFIELD   FLOCK_LODIST_EN_OUT_7<3:0>
        POSITION=<14:11>
        DEFAULT=0000
        MODE=RWI
        #! LO distribution enable signals used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_VCO_SPDUP_7
        POSITION=10
        DEFAULT=0
        MODE=RWI
        #! VCO speedup used during fast lock
    ENDBITFIELD
    BITFIELD   FLOCK_N_7<9:0>
        POSITION=<9:0>
        DEFAULT=0110010000
        MODE=RWI
        #! Duration of fast lock in PLL reference frequency clock cycles.
    ENDBITFIELD
ENDREGISTER

"""

