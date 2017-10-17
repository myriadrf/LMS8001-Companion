//
// This file is part of the GNU ARM Eclipse distribution.
// Copyright (c) 2014 Liviu Ionescu.
//
// ----------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "diag/Trace.h"
#include "stm32f10x_rcc.h"

#include "cmsis_device.h"
#include "usbd_cdc_vcp.h"
#include "usbd_usr.h"
#include "usb_conf.h"
#include "usbd_desc.h"

#include "stm32f10x_gpio.h"
#include "stm32f10x_spi.h"
//#include "stm32f10x_i2c.h"
#include "stm32f10x_usart.h"
#include "stm32f10x_adc.h"
#include "misc.h"
#include "stm32f10x_rcc.h"

#include "LMS64C_protocol.h"
#include "i2csw.h"
//msavic
//#include "RFESpark_brd.h"
#include "lms8_evb_brd.h"
#include "main.h"

#define TRUE 1
#define FALSE 0

//CMD_PROG_MCU
#define PROG_EEPROM 1
#define PROG_SRAM	2
#define BOOT_MCU	3

////CMD_PROG_MCU
#define MCU_CONTROL_REG	0x02
#define MCU_STATUS_REG	0x03
#define MCU_FIFO_WR_REG	0x04

#define MAX_MCU_RETRIES	30

#define ADC_REF_MV	2500


// ----- Timing definitions -------------------------------------------------
#define TIMER_FREQUENCY_HZ (1000u)
#define LED_WINK_PERIOD		180
#define LED_BLINK1_PERIOD	200
#define LED_BLINK2_PERIOD	100

// ----- I2C addresses ------------------------------------------------------
#define ADG715_I2C_ADDR 0x90
#define SI5351_I2C_ADDR 0xC0

// ----- main() ---------------------------------------------------------------

// Sample pragmas to cope with warnings. Please note the related line at
// the end of this function, used to pop the compiler diagnostics status.
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wmissing-declarations"
#pragma GCC diagnostic ignored "-Wreturn-type"

__ALIGN_BEGIN USB_OTG_CORE_HANDLE    USB_OTG_dev __ALIGN_END ;

/* Extern variables ----------------------------------------------------------*/
extern __IO uint8_t Receive_Buffer[64];
extern __IO  uint32_t Receive_length ;
uint8_t Send_Buffer[64];
uint32_t packet_receive=1;

//lms vars
unsigned char tx_buff[LMS_CTRL_PACKET_SIZE], rx_buff[LMS_CTRL_PACKET_SIZE], count, reg_idx, MCU_mode, USB_V_old, USB_V_new;

tLMS_Ctrl_Packet *LMS_Ctrl_Packet_Tx = (tLMS_Ctrl_Packet*)tx_buff;
tLMS_Ctrl_Packet *LMS_Ctrl_Packet_Rx = (tLMS_Ctrl_Packet*)Receive_Buffer;//rx_buff;

unsigned char block, cmd_errors, last_portion = 0, temp_status, MCU_retries, current_portion;
unsigned char GPIO_states[] = {0, 0};

//unsigned char LED_mode = LED_MODE_OFF, LED_timeout; //variables for LED

unsigned int adc_val, LED_mode[3] = {LED_MODE_OFF, LED_MODE_OFF, LED_MODE_OFF}, LED_timeout[3];
unsigned long adc_vals[32];
/**	This function checks if all blocks could fit in data field.
*	If blocks will not fit, function returns TRUE. */
unsigned char Check_many_blocks (unsigned char block_size)
{
	if (LMS_Ctrl_Packet_Rx->Header.Data_blocks > (sizeof(LMS_Ctrl_Packet_Tx->Data_field)/block_size))
	{
		LMS_Ctrl_Packet_Tx->Header.Status = STATUS_BLOCKS_ERROR_CMD;
		return TRUE;
	}
	else return FALSE;
	return FALSE;
}

void Init_SPI1 (void)
{
	GPIO_InitTypeDef GPIO_InitStruct;
	SPI_InitTypeDef SPI_InitStruct;

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD , ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_SPI1, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO, ENABLE);

	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE); //JTAG-DP Disabled and SW-DP Enabled

    //Configure SPI pins:  SCLK=PA5, MOSI=PA7
    GPIO_InitStruct.GPIO_Pin = SCLK_PIN | SDIO_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_AF_PP;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(SCLK_PORT, &GPIO_InitStruct);

    //Configure SPI pins:  MISO
    GPIO_InitStruct.GPIO_Pin = SDO_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_IN_FLOATING;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(SDO_PORT, &GPIO_InitStruct);
/*
    ///SS pins
	GPIO_InitStruct.GPIO_Pin = FMC_SPI_FPGA_SS_M2C_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(FMC_SPI_FPGA_SS_M2C_PORT, &GPIO_InitStruct);
	GPIO_SetBits(FMC_SPI_FPGA_SS_M2C_PORT, FMC_SPI_FPGA_SS_M2C_PIN); //high level
*/
	GPIO_InitStruct.GPIO_Pin = SAEN_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(SAEN_PORT, &GPIO_InitStruct);
	GPIO_SetBits(SAEN_PORT, SAEN_PIN); //high level

	GPIO_InitStruct.GPIO_Pin = SBEN_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(SBEN_PORT, &GPIO_InitStruct);
	GPIO_SetBits(SBEN_PORT, SBEN_PIN); //high level

	SPI_InitStruct.SPI_Direction = SPI_Direction_2Lines_FullDuplex; //duplex mode
	SPI_InitStruct.SPI_Mode = SPI_Mode_Master; //SPI Master mode
	SPI_InitStruct.SPI_DataSize = SPI_DataSize_8b; //8 bits of data
	SPI_InitStruct.SPI_CPOL = SPI_CPOL_Low; //CPOL = 0 --> clock is low when idle
	SPI_InitStruct.SPI_CPHA = SPI_CPHA_1Edge; //CPHA = 0 --> data is sampled at the first edge
	SPI_InitStruct.SPI_NSS = SPI_NSS_Soft;// | SPI_NSSInternalSoft_Set;
	SPI_InitStruct.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_16; //clock prescaler
	SPI_InitStruct.SPI_FirstBit = SPI_FirstBit_MSB; //MSB is transmitted first
	SPI_InitStruct.SPI_CRCPolynomial =7;
	SPI_Init(SPI1, &SPI_InitStruct);

	SPI_Cmd(SPI1, ENABLE); //Enable SPI1
}

/*
void Init_ADC1 (void)
{
	ADC_InitTypeDef  ADC_InitStructure;
	GPIO_InitTypeDef GPIO_InitStructure;

	//GPIO
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);//Enable GPIOA clock

	// Configure as analog inputs
	GPIO_InitStructure.GPIO_Pin =  MCU_ADC_IN1_PIN | MCU_ADC_REF_PIN |MCU_ADC_IN0_PIN;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AIN;
	GPIO_Init( MCU_ADC_IN0_PORT, &GPIO_InitStructure);

	// PCLK2 is the APB2 clock
	RCC_ADCCLKConfig(RCC_PCLK2_Div4);

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_ADC1, ENABLE); //Enable ADC1 clock so that we can talk to it

	ADC_DeInit(ADC1); //Put everything back to power-on defaults

	// ADC1 Configuration ------------------------------------------------------
	ADC_InitStructure.ADC_Mode = ADC_Mode_Independent; //ADC1 and ADC2 operate independently
	ADC_InitStructure.ADC_ScanConvMode = DISABLE; //Disable the scan conversion so we do one at a time
	ADC_InitStructure.ADC_ContinuousConvMode = DISABLE; //Don't do continuous conversions - do them on demand
	ADC_InitStructure.ADC_ExternalTrigConv = ADC_ExternalTrigConv_None; //Start conversion by software, not an external trigger
	ADC_InitStructure.ADC_DataAlign = ADC_DataAlign_Right; //Conversions are 12 bit - put them in the lower 12 bits of the result
	ADC_InitStructure.ADC_NbrOfChannel = 1; //Say how many channels would be used by the sequencer

	ADC_Init(ADC1, &ADC_InitStructure); //Now do the setup

	ADC_TempSensorVrefintCmd(ENABLE); //Enable temperature and Vrefint measurment on ch16 and ch17

	ADC_Cmd(ADC1, ENABLE); //Enable ADC1

	ADC_ResetCalibration(ADC1); //Enable ADC1 reset calibaration register
	while(ADC_GetResetCalibrationStatus(ADC1)); //Check the end of ADC1 reset calibration register
	ADC_StartCalibration(ADC1); //Start ADC1 calibaration
	while(ADC_GetCalibrationStatus(ADC1)); //Check the end of ADC1 calibration
}
*/

void Init_GPIOs (void)
{
	GPIO_InitTypeDef GPIO_InitStruct;

	//enable all RCC
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD, ENABLE);

	//MCU LED
	GPIO_InitStruct.GPIO_Pin = MCU_LED0_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(MCU_LED0_PORT, &GPIO_InitStruct);
	GPIO_ResetBits(MCU_LED0_PORT, MCU_LED0_PIN); //turn off led

	GPIO_InitStruct.GPIO_Pin = MCU_LED1_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(MCU_LED1_PORT, &GPIO_InitStruct);
	GPIO_ResetBits(MCU_LED1_PORT, MCU_LED1_PIN); //turn off led

	GPIO_InitStruct.GPIO_Pin = MCU_LED2_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(MCU_LED2_PORT, &GPIO_InitStruct);
	GPIO_ResetBits(MCU_LED2_PORT, MCU_LED2_PIN); //turn off led

/*
	//MUX control
	GPIO_InitStruct.GPIO_Pin = MUX_A0_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(MUX_A0_PORT, &GPIO_InitStruct);
...

	//UART
	GPIO_InitStruct.GPIO_Pin = MCU_UART_TX_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(MCU_UART_TX_PORT, &GPIO_InitStruct);
...

	//MCU GPIO
	GPIO_InitStruct.GPIO_Pin = MCU_GPIO0_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_IPU;
	GPIO_Init(MCU_GPIO0_PORT, &GPIO_InitStruct);
...

	//LMS GPIOS
	GPIO_InitStruct.GPIO_Pin = DIQ1TX_DIR_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_OD;
	GPIO_Init(DIQ1TX_DIR_PORT, &GPIO_InitStruct);
...
*/

//msavic - Is GPIO_Mode_Out_PP appropriate?
	GPIO_InitStruct.GPIO_Pin = GPIO8_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(GPIO8_PORT, &GPIO_InitStruct);

//msavic - Is GPIO_Mode_Out_PP appropriate?
	GPIO_InitStruct.GPIO_Pin = GPIO03_DIR_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(GPIO03_DIR_PORT, &GPIO_InitStruct);

//msavic - Is GPIO_Mode_Out_PP appropriate?
	GPIO_InitStruct.GPIO_Pin = GPIO47_DIR_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(GPIO47_DIR_PORT, &GPIO_InitStruct);

	GPIO_InitStruct.GPIO_Pin = CORE_LDO_EN_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
//	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_OD;
// milans - There is a difference between ESpark board (there is a pull up resistor) and LMS8_EVB board
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(CORE_LDO_EN_PORT, &GPIO_InitStruct);

/*
	GPIO_InitStruct.GPIO_Pin = DIG_RST_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_OD;
	GPIO_Init(DIG_RST_PORT, &GPIO_InitStruct);
...
*/

	GPIO_InitStruct.GPIO_Pin = RESETN_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
//	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_OD;
// milans - There is a difference between ESpark board (there is a pull up resistor) and LMS8_EVB board
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(RESETN_PORT, &GPIO_InitStruct);
	GPIO_SetBits(RESETN_PORT, RESETN_PIN); //high level

	//USB
	/*GPIO_InitStruct.GPIO_Pin = USB_VBUS_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_IN_FLOATING;//GPIO_Mode_IPU;
	GPIO_Init(USB_VBUS_PORT, &GPIO_InitStruct);*/
}

/*
u16 readADC1(u8 channel)
{
	ADC_RegularChannelConfig(ADC1, channel, 1, ADC_SampleTime_41Cycles5);
	// Start the conversion
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);
	// Wait until conversion completion
	while(ADC_GetFlagStatus(ADC1, ADC_FLAG_EOC) == RESET);
	// Get the conversion value
	return ADC_GetConversionValue(ADC1);
}
*/

/**	Function to update GPIO outputs. */
/*
void Update_GPIO_outs (void)
{
	i2cSend(ADG715_I2C_ADDR, GPIO_states[0], 0, NULL); //write data to analog switch

	//DIO_DIR_CTRL1 control - GPIO8
	if (GPIO_states[1] & 0x01) GPIO_SetBits(DIQ1TX_DIR_PORT, DIQ1TX_DIR_PIN);
		else GPIO_ResetBits(DIQ1TX_DIR_PORT, DIQ1TX_DIR_PIN);

	//DIO_DIR_CTRL2 control - GPIO9
	if (GPIO_states[1] & 0x02) GPIO_SetBits(DIQ2RX_DIR_PORT, DIQ2RX_DIR_PIN);
		else GPIO_ResetBits(DIQ2RX_DIR_PORT, DIQ2RX_DIR_PIN);

	//DIO_BUFF_OE control - GPIO10
	if (GPIO_states[1] & 0x04) GPIO_SetBits(DIO_BUF_OE_PORT, DIO_BUF_OE_PIN);
		else GPIO_ResetBits(DIO_BUF_OE_PORT, DIO_BUF_OE_PIN);

	//IQSEL1_DIR control - GPIO11
	if (GPIO_states[1] & 0x08) GPIO_SetBits(IQSELEN1TX_DIR_PORT, IQSELEN1TX_DIR_PIN);
	else GPIO_ResetBits(IQSELEN1TX_DIR_PORT, IQSELEN1TX_DIR_PIN);

	//IQSEL2_DIR control - GPIO12
	if (GPIO_states[1] & 0x10) GPIO_SetBits(IQSELEN2RX_DIR_PORT, IQSELEN2RX_DIR_PIN);
		else GPIO_ResetBits(IQSELEN2RX_DIR_PORT, IQSELEN2RX_DIR_PIN);

	//G_PWR_DWN control - GPIO13
	if (GPIO_states[1] & 0x20) GPIO_SetBits(CORE_LDO_EN_PORT, CORE_LDO_EN_PIN);
		else GPIO_ResetBits(CORE_LDO_EN_PORT, CORE_LDO_EN_PIN);

	//DIG_RST control - GPIO14
	if (GPIO_states[1] & 0x40) GPIO_SetBits(DIG_RST_PORT, DIG_RST_PIN);
		else GPIO_ResetBits(DIG_RST_PORT, DIG_RST_PIN);

	//gap - GPIO15

	//RXEN - GPIO16+
	if (GPIO_states[2] & 0x01) GPIO_SetBits(RXEN_LMS_PORT, RXEN_LMS_PIN);
		else GPIO_ResetBits(RXEN_LMS_PORT, RXEN_LMS_PIN);

	//TXEN -  - GPIO17+
	if (GPIO_states[2] & 0x02) GPIO_SetBits(TXEN_LMS_PORT, TXEN_LMS_PIN);
		else GPIO_ResetBits(TXEN_LMS_PORT, TXEN_LMS_PIN);
}
*/

/**	Function to update GPIOs */

void Update_GPIOs (void)
{
	GPIO_InitTypeDef GPIO_InitStruct;
/*
	GPIO_InitStruct.GPIO_Pin = GPIO47_DIR_PIN;
	GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStruct.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_Init(GPIO47_DIR_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = SDO_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO_Mode_IN_FLOATING;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(SDO_PORT, &GPIO_InitStruct);
 */

	GPIOSpeed_TypeDef GPIO03_Mode, GPIO47_Mode;

/*
	//GPIO03_DIR
	if(GPIO_states[1] & 0x02)
	{
		//GPIO pins 0-3 are OUTPUT for STM32
		//msavic - Is GPIO_Mode_Out_PP appropriate?
		GPIO03_Mode = GPIO_Mode_Out_PP;
	} else {
		//GPIO pins 0-3 are INPUT for STM32
		//msavic - Is GPIO_Mode_IN_FLOATING appropriate?
		GPIO03_Mode = GPIO_Mode_IN_FLOATING;
	}

	//GPIO47_DIR
	if(GPIO_states[1] & 0x04)
	{
		//GPIO pins 4-7 are OUTPUT for STM32
		//msavic - Is GPIO_Mode_Out_PP appropriate?
		GPIO47_Mode = GPIO_Mode_Out_PP;
	} else {
		//GPIO pins 4-7 are INPUT for STM32
		//msavic - Is GPIO_Mode_IN_FLOATING appropriate?
		GPIO47_Mode = GPIO_Mode_IN_FLOATING;
	}
*/
	GPIO03_Mode = (GPIO_states[1] & 0x02)?GPIO_Mode_Out_PP:GPIO_Mode_IN_FLOATING;
	GPIO47_Mode = (GPIO_states[1] & 0x04)?GPIO_Mode_Out_PP:GPIO_Mode_IN_FLOATING;

    GPIO_InitStruct.GPIO_Pin = GPIO0_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO03_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO0_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO1_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO03_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO1_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO2_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO03_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO2_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO3_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO03_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO3_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO4_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO47_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO4_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO5_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO47_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO5_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO6_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO47_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO6_PORT, &GPIO_InitStruct);

    GPIO_InitStruct.GPIO_Pin = GPIO7_PIN;
    GPIO_InitStruct.GPIO_Mode = GPIO47_Mode;
    GPIO_InitStruct.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(GPIO7_PORT, &GPIO_InitStruct);

	if(GPIO_states[1] & 0x02){
		GPIO_SetBits(GPIO03_DIR_PORT, GPIO03_DIR_PIN);
		//GPIO pins 0-3 are OUTPUT for STM32
		(GPIO_states[0] & 0x01)?GPIO_SetBits(GPIO0_PORT, GPIO0_PIN):GPIO_ResetBits(GPIO0_PORT, GPIO0_PIN);
		(GPIO_states[0] & 0x02)?GPIO_SetBits(GPIO1_PORT, GPIO1_PIN):GPIO_ResetBits(GPIO1_PORT, GPIO1_PIN);
		(GPIO_states[0] & 0x04)?GPIO_SetBits(GPIO2_PORT, GPIO2_PIN):GPIO_ResetBits(GPIO2_PORT, GPIO2_PIN);
		(GPIO_states[0] & 0x08)?GPIO_SetBits(GPIO3_PORT, GPIO3_PIN):GPIO_ResetBits(GPIO3_PORT, GPIO3_PIN);
	} else
		GPIO_ResetBits(GPIO03_DIR_PORT, GPIO03_DIR_PIN);

	if(GPIO_states[1] & 0x04){
		GPIO_SetBits(GPIO47_DIR_PORT, GPIO47_DIR_PIN);
		//GPIO pins 4-7 are OUTPUT for STM32
		(GPIO_states[0] & 0x10)?GPIO_SetBits(GPIO4_PORT, GPIO4_PIN):GPIO_ResetBits(GPIO4_PORT, GPIO4_PIN);
		(GPIO_states[0] & 0x20)?GPIO_SetBits(GPIO5_PORT, GPIO5_PIN):GPIO_ResetBits(GPIO5_PORT, GPIO5_PIN);
		(GPIO_states[0] & 0x40)?GPIO_SetBits(GPIO6_PORT, GPIO6_PIN):GPIO_ResetBits(GPIO6_PORT, GPIO6_PIN);
		(GPIO_states[0] & 0x80)?GPIO_SetBits(GPIO7_PORT, GPIO7_PIN):GPIO_ResetBits(GPIO7_PORT, GPIO7_PIN);
	} else
		GPIO_ResetBits(GPIO47_DIR_PORT, GPIO47_DIR_PIN);

	//GPIO8 control - GPIO_states[1] bit 0 - Always output
	(GPIO_states[1] & 0x01)?GPIO_SetBits(GPIO8_PORT, GPIO8_PIN):GPIO_ResetBits(GPIO8_PORT, GPIO8_PIN);

	//CORE_LDO_EN control - GPIO_states[1] bit 3
	(GPIO_states[1] & 0x08)?GPIO_SetBits(CORE_LDO_EN_PORT, CORE_LDO_EN_PIN):GPIO_ResetBits(CORE_LDO_EN_PORT, CORE_LDO_EN_PIN);
/*
	if (GPIO_states[1] & 0x10)
		GPIO_SetBits(CORE_LDO_EN_PORT, CORE_LDO_EN_PIN);
	else
		GPIO_ResetBits(CORE_LDO_EN_PORT, CORE_LDO_EN_PIN);
*/
}

/*
void Measure_all_ADC_ch ()
{
	unsigned char mux_ch;
	unsigned int ref;

	//measure reference, used for calibration
	ref = readADC1(3);

	for (mux_ch = 0; mux_ch <16; mux_ch++)
	{
		//comutate mux channel
		if (mux_ch & 0x01) GPIO_SetBits(MUX_A0_PORT, MUX_A0_PIN);
			else GPIO_ResetBits(MUX_A0_PORT, MUX_A0_PIN);

		if (mux_ch & 0x02) GPIO_SetBits(MUX_A1_PORT, MUX_A1_PIN);
			else GPIO_ResetBits(MUX_A1_PORT, MUX_A1_PIN);

		if (mux_ch & 0x04) GPIO_SetBits(MUX_A2_PORT, MUX_A2_PIN);
				else GPIO_ResetBits(MUX_A2_PORT, MUX_A2_PIN);

		if (mux_ch & 0x08) GPIO_SetBits(MUX_A3_PORT, MUX_A3_PIN);
			else GPIO_ResetBits(MUX_A3_PORT, MUX_A3_PIN);

		//calculate voltages based on reference value:
		//ref = 2500 mV (ADC_REF_MV)
		//readADC = x (adc_vals[]);
		adc_vals[0  + mux_ch] = readADC1(1)*ADC_REF_MV/ref; //read data from mux 0
		adc_vals[16 + mux_ch] = readADC1(2)*ADC_REF_MV/ref; //read data from mux 1
	}

}
*/

uint8_t SPI1_transfer_byte(uint8_t cmd)
{
    uint8_t result;

    while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_TXE) == RESET); //Wait until the transmit buffer is empty
    SPI_I2S_SendData(SPI1, cmd);
    //while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_BSY) == SET); //wait finish sending

    while(SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_RXNE) == RESET); // wait data received

   	result = SPI_I2S_ReceiveData(SPI1);

    return result;
}

/**	Inaccurate software delay function to get required delay in microseconds. */
void Delay_us (unsigned int cycles)
{
	while (cycles--)
	{
		asm volatile("nop");
		asm volatile("nop");
		asm volatile("nop");
	}
}

void SysTick_Handler (void)
{
  //timer_tick ();

  unsigned char LED;

 	for (LED = 0; LED < 3; LED++)
  	{

 		uint16_t LED_PIN;
 		GPIO_TypeDef* LED_PORT;
 		//LED_mode[LED] = mode;//save new LED mode

 		switch(LED)
 		{
 			default:
 			case 0:
 				LED_PIN = MCU_LED0_PIN;
 				LED_PORT = MCU_LED0_PORT;
 				break;
 			case 1:
 				LED_PIN = MCU_LED1_PIN;
 				LED_PORT = MCU_LED1_PORT;
 				break;
 			case 2:
 				LED_PIN = MCU_LED2_PIN;
 				LED_PORT = MCU_LED2_PORT;
 				break;
 		}

 		unsigned char LED_GPIO_state;
  		LED_GPIO_state = GPIO_ReadOutputDataBit(LED_PORT, LED_PIN);

			if (LED_mode[LED] != LED_MODE_OFF)
			{
				if (LED_timeout[LED]) LED_timeout[LED]--;

				if(LED_timeout[LED] == 0)
				{
					switch(LED_mode[LED])
					{
						case LED_MODE_WINK:
							GPIO_ResetBits(LED_PORT, LED_PIN); //turn off led

							LED_mode[LED]= LED_MODE_OFF;
							break;

						case LED_MODE_BLINK1:
							if(LED_GPIO_state) GPIO_ResetBits(LED_PORT, LED_PIN); //turn off led
							else GPIO_SetBits(LED_PORT, LED_PIN); //turn on led

							LED_timeout[LED] = LED_BLINK1_PERIOD;
							break;

						case LED_MODE_BLINK2:
							if(LED_GPIO_state) GPIO_ResetBits(LED_PORT, LED_PIN); //turn off led
							else GPIO_SetBits(LED_PORT, LED_PIN); //turn on led

							LED_timeout[LED] = LED_BLINK2_PERIOD;
							break;

						case LED_MODE_ON:
							break;

						default:
						case LED_MODE_OFF:
							break;
					}
				}
			}

  	}

}

/**	Function to control LED mode. */
void Set_LED_mode (unsigned char LED, unsigned char mode)
{
	uint16_t LED_PIN;
	GPIO_TypeDef* LED_PORT;
	LED_mode[LED] = mode;//save new LED mode

	switch(LED)
	{
		default:
		case 0:
			LED_PIN = MCU_LED0_PIN;
			LED_PORT = MCU_LED0_PORT;
			break;
		case 1:
			LED_PIN = MCU_LED1_PIN;
			LED_PORT = MCU_LED1_PORT;
			break;
		case 2:
			LED_PIN = MCU_LED2_PIN;
			LED_PORT = MCU_LED2_PORT;
			break;
	}

	switch (LED_mode[LED])
	{
		case LED_MODE_OFF:
			GPIO_ResetBits(LED_PORT, LED_PIN); //turn off led
			break;

		case LED_MODE_ON:
			GPIO_SetBits(LED_PORT, LED_PIN); //turn on led
			break;

		case LED_MODE_WINK:
			GPIO_SetBits(LED_PORT, LED_PIN); //turn on led
			LED_timeout[LED] = LED_WINK_PERIOD; //set LED timeout
			break;
	}
}




int
main(int argc, char* argv[])
{
  //RCC_OTGFSCLKConfig(RCC_OTGFSCLKSource_PLLVCO_Div2);
  RCC_HSICmd(DISABLE);

  Init_SPI1 ();
  Init_GPIOs ();
  i2cInit (); //sw i2c
//  Init_ADC1 ();

  USBD_Init(&USB_OTG_dev, USB_OTG_FS_CORE_ID, &USR_desc, &USBD_CDC_cb, &USR_cb);

// msavic ovdi!!!
  Set_LED_mode (2, LED_MODE_BLINK1);
//  Set_LED_mode (1, LED_MODE_BLINK1);

//  Update_GPIO_outs ();
  Update_GPIOs();

// msavic - TMP TMP TMP TMP TMP
// Reset the LMS8
	GPIO_ResetBits(RESETN_PORT, RESETN_PIN); //low level
	asm volatile("nop");
	asm volatile("nop");
	asm volatile("nop");
	asm volatile("nop");
	GPIO_SetBits(RESETN_PORT, RESETN_PIN); //high level

  SysTick_Config (SystemCoreClock / TIMER_FREQUENCY_HZ);
  // Infinite loop
  while (1)
  {
	      if (Receive_length  >= 64)
	      {
	    	Set_LED_mode (0, LED_MODE_ON);
	        Receive_length = 0;

	    	  ////LMS64C
			memset (tx_buff, 0, sizeof(tx_buff)); //fill whole tx buffer with zeros
			cmd_errors = 0;

			LMS_Ctrl_Packet_Tx->Header.Command = LMS_Ctrl_Packet_Rx->Header.Command;
			LMS_Ctrl_Packet_Tx->Header.Data_blocks = LMS_Ctrl_Packet_Rx->Header.Data_blocks;
			LMS_Ctrl_Packet_Tx->Header.Status = STATUS_BUSY_CMD;

     		switch(LMS_Ctrl_Packet_Rx->Header.Command)
     		{

 				case CMD_GET_INFO:

 					LMS_Ctrl_Packet_Tx->Data_field[0] = FW_VER;
 					LMS_Ctrl_Packet_Tx->Data_field[1] = DEV_TYPE;
 					LMS_Ctrl_Packet_Tx->Data_field[2] = LMS_PROTOCOL_VER;
 					LMS_Ctrl_Packet_Tx->Data_field[3] = HW_VER;
 					LMS_Ctrl_Packet_Tx->Data_field[4] = EXP_BOARD;

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;

 					break;

 				case CMD_LMS_RST:
 					switch (LMS_Ctrl_Packet_Rx->Data_field[0])
 					{
 						case LMS_RST_DEACTIVATE:
 							//sbi(PORTB, RESET); //high level
 							GPIO_SetBits(RESETN_PORT, RESETN_PIN); //high level
 							break;

 						case LMS_RST_ACTIVATE:
 							GPIO_ResetBits(RESETN_PORT, RESETN_PIN); //low level
 							break;

 						case LMS_RST_PULSE:
 							GPIO_ResetBits(RESETN_PORT, RESETN_PIN); //low level
 							asm volatile("nop");
 							asm volatile("nop");
 							asm volatile("nop");
 							asm volatile("nop");
 							GPIO_SetBits(RESETN_PORT, RESETN_PIN); //high level
 							break;

 						default:
 							cmd_errors++;
 							break;
 					}

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;

 				case CMD_LMS8001_WR:
//msavic
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Check this, is this OK???? There were problems on Open in GUI
// Commented
 					if(Check_many_blocks (4)) break;
//Added
// 					if(Check_many_blocks (1)) break;

 					//Reconfigure_SPI_for_LMS ();

 					GPIO_ResetBits(SAEN_PORT, SAEN_PIN); //Enable LMS's SPI
//msavic IMPORTANT
//Here there were 2 blocks, so there were 2 write commands, the wanted one,
//and the second "parasitic" writing to 0x00
//In LMS7002 there is nothing on that address, so it was not a problem
//but with LMS8001 we have register at that position (an important one) so we had to avoid
//writing to it
					for(block = 0; block < LMS_Ctrl_Packet_Rx->Header.Data_blocks; block++)
 					{
 						//write reg addr
//msavic commented out this line
// 						sbi(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)], 7); //set write bit
//msavic added these 2 lines
						//write reg addr for block 0
						//ovdi!!!
//						if(block == 0)
//							sbi(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)], 7); //set write bit
						unsigned char false_write_to_0x0000 = 0;

						if(	(LMS_Ctrl_Packet_Rx->Header.Data_blocks == 4) &&
							(block != 0) &&
							(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)] == 0x00) &&
							(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 4)] == 0x00) )
							false_write_to_0x0000 = 1;

//						if(	(block != 0) &&
//							(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)] == 0x00) &&
//							(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 4)] == 0x00) )
//							false_write_to_0x0000 = 1;

//						if(	(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)] == 0x00) &&
//							(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 4)] == 0x00) )
//							false_write_to_0x0000 = 1;

//						if(	(block != 4) &&
//							(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)] == 0x00) &&
//							(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 4)] == 0x04) )
//							false_write_to_0x0000 = 10;

						if(false_write_to_0x0000 == 0)
							sbi(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)], 7); //set write bit

 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 4)]); //reg addr MSB with write bit
 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 4)]); //reg addr LSB*/

 						//write reg data
 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[2 + (block * 4)]); //reg data MSB
 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[3 + (block * 4)]); //reg data LSB
 					}

 					GPIO_SetBits(SAEN_PORT, SAEN_PIN); //Disable LMS's SPI

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;

 				case CMD_LMS8001_RD:
 					if(Check_many_blocks (4)) break;
 					//Reconfigure_SPI_for_LMS ();

 					GPIO_ResetBits(SAEN_PORT, SAEN_PIN); //Enable LMS's SPI
 					//ovdi!!!
// 					Delay_us (30);

 					for(block = 0; block < LMS_Ctrl_Packet_Rx->Header.Data_blocks; block++)
 					{
 						//write reg addr
 						cbi(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)], 7);  //clear write bit

 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)]); //reg addr MSB
 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 2)]); //reg addr LSB

 						LMS_Ctrl_Packet_Tx->Data_field[0 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)];
 						LMS_Ctrl_Packet_Tx->Data_field[1 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 2)];

 						//read reg data
 						LMS_Ctrl_Packet_Tx->Data_field[2 + (block * 4)] = SPI1_transfer_byte(0x00); //reg data MSB
 						LMS_Ctrl_Packet_Tx->Data_field[3 + (block * 4)] = SPI1_transfer_byte(0x00); //reg data LSB
 					}

// msavic ovdi!!!
////// TEMP TEMP TEMP TEMP ////////
/*
 					    block = 0;
						cbi(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)], 7);  //clear write bit

						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)]); //reg addr MSB
						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 2)]); //reg addr LSB

						LMS_Ctrl_Packet_Tx->Data_field[0 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)];
						LMS_Ctrl_Packet_Tx->Data_field[1 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 2)];

						//read reg data
						LMS_Ctrl_Packet_Tx->Data_field[2 + (block * 4)] = SPI1_transfer_byte(0x00); //reg data MSB
						LMS_Ctrl_Packet_Tx->Data_field[3 + (block * 4)] = SPI1_transfer_byte(0x00); //reg data LSB

 					    block = 1;
						cbi(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)], 7);  //clear write bit

						SPI1_transfer_byte(0x40); //reg addr MSB
						SPI1_transfer_byte(0x00); //reg addr LSB

						LMS_Ctrl_Packet_Tx->Data_field[0 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 2)];
						LMS_Ctrl_Packet_Tx->Data_field[1 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 2)];

						//read reg data
						LMS_Ctrl_Packet_Tx->Data_field[2 + (block * 4)] = SPI1_transfer_byte(0x00); //reg data MSB
						LMS_Ctrl_Packet_Tx->Data_field[3 + (block * 4)] = SPI1_transfer_byte(0x00); //reg data LSB
*/

 					GPIO_SetBits(SAEN_PORT, SAEN_PIN); //Disable LMS's SPI

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;

 				case CMD_SI5351_WR:
 					if(Check_many_blocks (2)) break;

 					for(block = 0; block < LMS_Ctrl_Packet_Rx->Header.Data_blocks; block++)
 					{
 						if (!i2cSend(SI5351_I2C_ADDR, LMS_Ctrl_Packet_Rx->Data_field[block * 2], 1, &LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 2)])) cmd_errors++;
 					}

 					if(cmd_errors) LMS_Ctrl_Packet_Tx->Header.Status = STATUS_ERROR_CMD;
 						else LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;

 				case CMD_SI5351_RD:
 					if(Check_many_blocks (2)) break;

 					for(block = 0; block < LMS_Ctrl_Packet_Rx->Header.Data_blocks; block++)
 					{
 						LMS_Ctrl_Packet_Tx->Data_field[block * 2] = LMS_Ctrl_Packet_Rx->Data_field[block];
 						if (!i2cReceive(SI5351_I2C_ADDR, LMS_Ctrl_Packet_Rx->Data_field[block], 1, &LMS_Ctrl_Packet_Tx->Data_field[1 + block * 2])) cmd_errors++;
 					}

 					if(cmd_errors) LMS_Ctrl_Packet_Tx->Header.Status = STATUS_ERROR_CMD;
 						else LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;

 					break;

 				case CMD_GPIO_WR:
 					//write data to analog switch

 					GPIO_states [0] = LMS_Ctrl_Packet_Rx->Data_field[0];
 					GPIO_states [1] = LMS_Ctrl_Packet_Rx->Data_field[1];
// 					GPIO_states [2] = LMS_Ctrl_Packet_Rx->Data_field[2];

// 					Update_GPIO_outs ();
 					Update_GPIOs ();

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;

 					/*if (!i2cSend(ADG715_I2C_ADDR, LMS_Ctrl_Packet_Rx->Data_field[0], 0, NULL)) cmd_errors++;

 					if(cmd_errors) LMS_Ctrl_Packet_Tx->Header.Status = STATUS_ERROR_CMD;
 					else LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;*/
 					break;

 				case CMD_GPIO_RD:
 					/*******************************
 					 * msavic ovdi!!!
 					 *******************************/
 					if(!(GPIO_states[1] & 0x02)){
						//GPIO pins 0-3 are INPUT for STM32
 						(GPIO_ReadInputDataBit(GPIO0_PORT, GPIO0_PIN))?sbi(GPIO_states[0], 0):cbi(GPIO_states[0], 0);
 						(GPIO_ReadInputDataBit(GPIO1_PORT, GPIO1_PIN))?sbi(GPIO_states[0], 1):cbi(GPIO_states[0], 1);
 						(GPIO_ReadInputDataBit(GPIO2_PORT, GPIO2_PIN))?sbi(GPIO_states[0], 2):cbi(GPIO_states[0], 2);
 						(GPIO_ReadInputDataBit(GPIO3_PORT, GPIO3_PIN))?sbi(GPIO_states[0], 3):cbi(GPIO_states[0], 3);
 					}
 					if(!(GPIO_states[1] & 0x04)){
						//GPIO pins 4-7 are INPUT for STM32
 						(GPIO_ReadInputDataBit(GPIO4_PORT, GPIO4_PIN))?sbi(GPIO_states[0], 4):cbi(GPIO_states[0], 4);
 						(GPIO_ReadInputDataBit(GPIO5_PORT, GPIO5_PIN))?sbi(GPIO_states[0], 5):cbi(GPIO_states[0], 5);
 						(GPIO_ReadInputDataBit(GPIO6_PORT, GPIO6_PIN))?sbi(GPIO_states[0], 6):cbi(GPIO_states[0], 6);
 						(GPIO_ReadInputDataBit(GPIO7_PORT, GPIO7_PIN))?sbi(GPIO_states[0], 7):cbi(GPIO_states[0], 7);
 					}

 					LMS_Ctrl_Packet_Tx->Data_field[0] = GPIO_states [0];
 					LMS_Ctrl_Packet_Tx->Data_field[1] = GPIO_states [1];
// 					LMS_Ctrl_Packet_Tx->Data_field[2] = GPIO_states [2];

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;
/*
 				case CMD_ANALOG_VAL_RD:

 					if(Check_many_blocks (4)) break;

 					Measure_all_ADC_ch ();

 					long int converted_val_long;
 					short int converted_val;

 					for(block = 0; block < LMS_Ctrl_Packet_Rx->Header.Data_blocks; block++)
 					{

 						switch (LMS_Ctrl_Packet_Rx->Data_field[block])
 						{
 							case 29: //with 1:2 divider
 							case 30:
 							case 31:
								converted_val_long = adc_vals[LMS_Ctrl_Packet_Rx->Data_field[block]] * 2;
								break;

 							default:
 								converted_val_long = adc_vals[LMS_Ctrl_Packet_Rx->Data_field[block]];
 								break;
 						}

 						//converted_val_long = adc_vals[LMS_Ctrl_Packet_Rx->Data_field[block]];
 						converted_val = converted_val_long;

 						LMS_Ctrl_Packet_Tx->Data_field[0 + (block * 4)] = LMS_Ctrl_Packet_Rx->Data_field[block]; //ch
 						LMS_Ctrl_Packet_Tx->Data_field[1 + (block * 4)] = 0x1F; //mV //units[LMS_Ctrl_Packet_Tx->Data_field[0 + (block * 4)]];// 0; //unit, power

 						LMS_Ctrl_Packet_Tx->Data_field[2 + (block * 4)] = (converted_val >> 8); //signed val, MSB byte
 						LMS_Ctrl_Packet_Tx->Data_field[3 + (block * 4)] = converted_val; //signed val, LSB byte
 					}

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;
*/
 				case CMD_ADF4002_WR:
 					if(Check_many_blocks (3)) break;

 					for(block = 0; block < LMS_Ctrl_Packet_Rx->Header.Data_blocks; block++)
 					{
 						GPIO_ResetBits(SBEN_PORT, SBEN_PIN); //Enable ADF's SPI

 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[0 + (block * 3)]);
 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[1 + (block * 3)]);
 						SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[2 + (block * 3)]);

 						GPIO_SetBits(SBEN_PORT, SBEN_PIN); //Disable ADF's SPI
 					}

 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;
 					break;

 				case CMD_PROG_MCU:

 						current_portion = LMS_Ctrl_Packet_Rx->Data_field[1];

 						//chek if portions are send in correct order
 						if(current_portion != 0) //not first portion?
 						{
 							if(last_portion != (current_portion - 1)) //portion number increments?
 							{
 								LMS_Ctrl_Packet_Tx->Header.Status = STATUS_WRONG_ORDER_CMD;
 								break;
 							}
 						}

 						GPIO_ResetBits(SAEN_PORT, SAEN_PIN); //Enable LMS's SPI

 						if (current_portion == 0) //PORTION_NR = first fifo
 						{
 							//reset mcu
 							//write reg addr - mSPI_REG2 (Controls MCU input pins)
 							SPI1_transfer_byte(0x80); //reg addr MSB with write bit
 							SPI1_transfer_byte(MCU_CONTROL_REG); //reg addr LSB

 							//write reg data
 							SPI1_transfer_byte(0x00); //reg data MSB
 							SPI1_transfer_byte(0x00); //reg data LSB //8

 							//set mode
 							//write reg addr - mSPI_REG2 (Controls MCU input pins)
 							SPI1_transfer_byte(0x80); //reg addr MSB with write bit
 							SPI1_transfer_byte(MCU_CONTROL_REG); //reg addr LSB

 							//write reg data
 							SPI1_transfer_byte(0x00); //reg data MSB

 							//reg data LSB
 							switch (LMS_Ctrl_Packet_Rx->Data_field[0]) //PROG_MODE
 							{
 								case PROG_EEPROM:
 									SPI1_transfer_byte(0x01); //Programming both EEPROM and SRAM  //8
 									break;

 								case PROG_SRAM:
 									SPI1_transfer_byte(0x02); //Programming only SRAM  //8
 									break;

 								case BOOT_MCU:
 									SPI1_transfer_byte(0x03); //Programming both EEPROM and SRAM  //8

 									/*sbi (PORTB, SAEN); //Disable LMS's SPI
 									cbi (PORTB, SAEN); //Enable LMS's SPI*/

 									//spi read
 									//write reg addr
 									SPI1_transfer_byte(0x00); //reg addr MSB
 									SPI1_transfer_byte(MCU_STATUS_REG); //reg addr LSB

 									//read reg data
 									SPI1_transfer_byte(0x00); //reg data MSB
 									temp_status = SPI1_transfer_byte(0x00); //reg data LSB

 									goto BOOTING;

 									break;

 							}
 						}

 						MCU_retries = 0;

 						//wait till EMPTY_WRITE_BUFF = 1
 						while (MCU_retries < MAX_MCU_RETRIES)
 						{
 							//read status reg

 							//spi read
 							//write reg addr
 							SPI1_transfer_byte(0x00); //reg addr MSB
 							SPI1_transfer_byte(MCU_STATUS_REG); //reg addr LSB

 							//read reg data
 							SPI1_transfer_byte(0x00); //reg data MSB
 							temp_status = SPI1_transfer_byte(0x00); //reg data LSB

 							if (temp_status &0x01) break;

 							MCU_retries++;
 							Delay_us (30);
 						}

 						//write 32 bytes to FIFO
 						for(block = 0; block < 32; block++)
 						{
 							/*
 							//wait till EMPTY_WRITE_BUFF = 1
 							while (MCU_retries < MAX_MCU_RETRIES)
 							{
 								//read status reg

 								//spi read
 								//write reg addr
 								SPI_SendByte(0x00); //reg addr MSB
 								SPI_SendByte(MCU_STATUS_REG); //reg addr LSB

 								//read reg data
 								SPI_TransferByte(0x00); //reg data MSB
 								temp_status = SPI_TransferByte(0x00); //reg data LSB

 								if (temp_status &0x01) break;

 								MCU_retries++;
 								Delay_us (30);
 							}*/

 							//write reg addr - mSPI_REG4 (Writes one byte of data to MCU  )
 							SPI1_transfer_byte(0x80); //reg addr MSB with write bit
 							SPI1_transfer_byte(MCU_FIFO_WR_REG); //reg addr LSB

 							//write reg data
 							SPI1_transfer_byte(0x00); //reg data MSB

 							SPI1_transfer_byte(LMS_Ctrl_Packet_Rx->Data_field[2 + block]); //reg data LSB

 							temp_status=0;
 							MCU_retries = 0;
 						}

 						/*sbi (PORTB, SAEN); //Enable LMS's SPI
 						cbi (PORTB, SAEN); //Enable LMS's SPI*/

 						MCU_retries = 0;

 						//wait till EMPTY_WRITE_BUFF = 1
 						while (MCU_retries < 255)
 						{
 							//read status reg

 							//spi read
 							//write reg addr
 							SPI1_transfer_byte(0x00); //reg addr MSB
 							SPI1_transfer_byte(MCU_STATUS_REG); //reg addr LSB

 							//read reg data
 							SPI1_transfer_byte(0x00); //reg data MSB
 							temp_status = SPI1_transfer_byte(0x00); //reg data LSB

 							if (temp_status &0x01) break;

 							MCU_retries++;
 							Delay_us (30);
 						}

 						if (current_portion  == 255) //PORTION_NR = last fifo
 						{
 							//chek programmed bit

 							MCU_retries = 0;

 							//wait till PROGRAMMED = 1
 							while (MCU_retries < MAX_MCU_RETRIES)
 							{
 								//read status reg

 								//spi read
 								//write reg addr
 								SPI1_transfer_byte(0x00); //reg addr MSB
 								SPI1_transfer_byte(MCU_STATUS_REG); //reg addr LSB

 								//read reg data
 								SPI1_transfer_byte(0x00); //reg data MSB
 								temp_status = SPI1_transfer_byte(0x00); //reg data LSB

 								if (temp_status &0x40) break; //PROGRAMMED = 1

 								MCU_retries++;
 								Delay_us (30);
 							}

 							if (MCU_retries == MAX_MCU_RETRIES) cmd_errors++;
 						}

 						last_portion = current_portion; //save last portion number

 						BOOTING:

 						if(cmd_errors) LMS_Ctrl_Packet_Tx->Header.Status = STATUS_ERROR_CMD;
 						else LMS_Ctrl_Packet_Tx->Header.Status = STATUS_COMPLETED_CMD;

 						GPIO_SetBits(SAEN_PORT, SAEN_PIN); //Disable LMS's SPI

 					break;

 				default:
 					LMS_Ctrl_Packet_Tx->Header.Status = STATUS_UNKNOWN_CMD;
 					break;
     		}

     		Set_LED_mode (0, LED_MODE_WINK);

     		VCP_DataTx(&tx_buff[0], 32);
     		VCP_DataTx(&tx_buff[32], 32);
	    }

    }
  // Infinite loop, never return.
}

#pragma GCC diagnostic pop
//





