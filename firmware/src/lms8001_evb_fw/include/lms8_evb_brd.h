/**
-- ----------------------------------------------------------------------------	
-- FILE:	lms8_evb_brd.h
-- DESCRIPTION:	LMS8001 EVB Board Firmware
-- DATE:	2015.11.26
-- AUTHOR(s):	Lime Microsystems
-- REVISION: v0r1
-- ----------------------------------------------------------------------------	

*/

#ifndef _LMS8_EVB_BRD_H_
#define _LMS8_EVB_BRD_H_

#include "LMS64C_protocol.h"

#define sbi(p,n) ((p) |= (1UL << (n)))
#define cbi(p,n) ((p) &= ~(1 << (n)))

/*********************
*      GPIOA
**********************/

//GPIO_Pin_0 - Not Connected
//GPIO_Pin_1 - Not Connected
//GPIO_Pin_2 - Not Connected
//GPIO_Pin_3 - Not Connected

#define MCU_LED0_PIN	GPIO_Pin_4
#define MCU_LED0_PORT	GPIOA
#define MCU_LED0_RCC	RCC_APB2Periph_GPIOA

//MCU_SPI_SCLK_PIN is now SCLK_PIN
#define SCLK_PIN		GPIO_Pin_5
#define SCLK_PORT		GPIOA
#define SCLK_RCC		RCC_APB2Periph_GPIOA

//MCU_SPI_MISO_PIN is now SDO_PIN
#define SDO_PIN			GPIO_Pin_6
#define SDO_PORT		GPIOA
#define SDO_RCC			RCC_APB2Periph_GPIOA

//MCU_SPI_MOSI_PIN is now SDIO_PIN
#define SDIO_PIN		GPIO_Pin_7
#define SDIO_PORT		GPIOA
#define SDIO_RCC		RCC_APB2Periph_GPIOA

//GPIO_Pin_8 - Not Connected
//GPIO_Pin_9 - Not Connected
//GPIO_Pin_10 - Not Connected

//USB2_D2_N_PIN is now USB_ESD_DM_PIN
#define USB_ESD_DM_PIN	GPIO_Pin_11
#define USB_ESD_DM_PORT	GPIOA
#define USB_ESD_DM_RCC	RCC_APB2Periph_GPIOA

//USB2_D2_P_PIN is now USB_ESD_DP_PIN
#define USB_ESD_DP_PIN	GPIO_Pin_12
#define USB_ESD_DP_PORT	GPIOA
#define USB_ESD_DP_RCC	RCC_APB2Periph_GPIOA

#define MCU_SWD_SWDIO_PIN	GPIO_Pin_13
#define MCU_SWD_SWDIO_PORT	GPIOA
#define MCU_SWD_SWDIO_RCC	RCC_APB2Periph_GPIOA

#define MCU_SWD_SWCLK_PIN	GPIO_Pin_14
#define MCU_SWD_SWCLK_PORT	GPIOA
#define MCU_SWD_SWCLK_RCC	RCC_APB2Periph_GPIOA

//MCU_SPI_LMS_SS_PIN is now SAEN_PIN
#define SAEN_PIN		GPIO_Pin_15
#define SAEN_PORT		GPIOA
#define SAEN_RCC		RCC_APB2Periph_GPIOA

/*********************
*      GPIOB
**********************/

#define GPIO6_PIN		GPIO_Pin_0
#define GPIO6_PORT		GPIOB
#define GPIO6_RCC		RCC_APB2Periph_GPIOB

#define GPIO7_PIN		GPIO_Pin_1
#define GPIO7_PORT		GPIOB
#define GPIO7_RCC		RCC_APB2Periph_GPIOB

#define MCU_BOOT1_PIN		GPIO_Pin_2
#define MCU_BOOT1_PORT		GPIOB
#define MCU_BOOT1_RCC		RCC_APB2Periph_GPIOB

#define MCU_SWD_SWO_PIN		GPIO_Pin_3
#define MCU_SWD_SWO_PORT	GPIOB
#define MCU_SWD_SWO_RCC		RCC_APB2Periph_GPIOB

#define MCU_LED1_PIN		GPIO_Pin_4
#define MCU_LED1_PORT		GPIOB
#define MCU_LED1_RCC		RCC_APB2Periph_GPIOB

#define MCU_LED2_PIN		GPIO_Pin_5
#define MCU_LED2_PORT		GPIOB
#define MCU_LED2_RCC		RCC_APB2Periph_GPIOB

//GPIO_Pin_6 - Not Connected
//GPIO_Pin_7 - Not Connected

//MCU_I2C_SCL_PIN is now SCL_PIN
#define SCL_PIN				GPIO_Pin_8
#define SCL_PORT			GPIOB
#define SCL_RCC				CC_APB2Periph_GPIOB

//MCU_I2C_SDA_PIN is now SDA_PIN
#define SDA_PIN				GPIO_Pin_9
#define SDA_PORT			GPIOB
#define SDA_RCC				CC_APB2Periph_GPIOB

#define GPIO47_DIR_PIN		GPIO_Pin_10
#define GPIO47_DIR_PORT		GPIOB
#define GPIO47_DIR_RCC		RCC_APB2Periph_GPIOB

#define GPIO03_DIR_PIN		GPIO_Pin_11
#define GPIO03_DIR_PORT		GPIOB
#define GPIO03_DIR_RCC		RCC_APB2Periph_GPIOB

#define GPIO0_PIN			GPIO_Pin_12
#define GPIO0_PORT			GPIOB
#define GPIO0_RCC			RCC_APB2Periph_GPIOB

#define GPIO1_PIN			GPIO_Pin_13
#define GPIO1_PORT			GPIOB
#define GPIO1_RCC			RCC_APB2Periph_GPIOB

#define GPIO3_PIN			GPIO_Pin_14
#define GPIO3_PORT			GPIOB
#define GPIO3_RCC			RCC_APB2Periph_GPIOB

#define GPIO2_PIN			GPIO_Pin_15
#define GPIO2_PORT			GPIOB
#define GPIO2_RCC			RCC_APB2Periph_GPIOB

/*********************
*      GPIOC
**********************/

#define CORE_LDO_EN_PIN		GPIO_Pin_0
#define CORE_LDO_EN_PORT	GPIOC
#define CORE_LDO_EN_RCC		RCC_APB2Periph_GPIOC

#define GPIO8_PIN			GPIO_Pin_1
#define GPIO8_PORT			GPIOC
#define GPIO8_RCC			RCC_APB2Periph_GPIOC

//GPIO_Pin_2 - Not Connected
//GPIO_Pin_3 - Not Connected

#define GPIO5_PIN			GPIO_Pin_4
#define GPIO5_PORT			GPIOC
#define GPIO5_RCC			RCC_APB2Periph_GPIOC

#define GPIO4_PIN			GPIO_Pin_5
#define GPIO4_PORT			GPIOC
#define GPIO4_RCC			RCC_APB2Periph_GPIOC

//SI_INTR_PIN is now INTR_PIN
#define INTR_PIN			GPIO_Pin_6
#define INTRS_PORT			GPIOC
#define INTR_RCC			RCC_APB2Periph_GPIOC

//GPIO_Pin_7 - Not Connected
//GPIO_Pin_8 - Not Connected
//GPIO_Pin_9 - Not Connected
//GPIO_Pin_10 - Not Connected
//GPIO_Pin_11 - Not Connected
//GPIO_Pin_12 - Not Connected

//RESET_LMS_PIN is now RESETN_PIN
#define RESETN_PIN			GPIO_Pin_13
#define RESETN_PORT			GPIOC
#define RESETN_RCC			RCC_APB2Periph_GPIOC

//GPIO_Pin_14 - Not Connected
//GPIO_Pin_15 - Not Connected

/*********************
*      GPIOD
**********************/

//MCU_SPI_ADF_SS_PIN is now SBEN_PIN
#define SBEN_PIN			GPIO_Pin_2
#define SBEN_PORT			GPIOD
#define SBEN_RCC			RCC_APB2Periph_GPIOD

//get info
#define FW_VER 		1
#define DEV_TYPE 	LMS_DEV_LMS8_EVB
#define LMS_PROTOCOL_VER 1
#if (HSE_VALUE==8000000)
#define HW_VER 		0
#else
#define HW_VER 		1
#endif
#define EXP_BOARD 	EXP_BOARD_UNSUPPORTED

#endif
