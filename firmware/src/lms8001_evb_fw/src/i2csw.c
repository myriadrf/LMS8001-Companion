/*! \file i2csw.c \brief Software I2C interface using port pins. */
//*****************************************************************************
//
// File Name	: 'i2csw.c'
// Title		: Software I2C interface using port pins
// Author		: Pascal Stang, 2013 Lime Microsystems
// Created		: 11/22/2000
// Revised		: 5/2/2002
// Version		: 1.1
// Target MCU	: Atmel AVR series
// Editor Tabs	: 4
//
// This code is distributed under the GNU Public License
//		which can be found at http://www.gnu.org/licenses/gpl.txt
//
//*****************************************************************************


#include "i2csw.h"
#include "stm32f10x_i2c.h"
//msavic
//#include "RFESpark_brd.h"
#include "lms8_evb_brd.h"

// Standard I2C bit rates are:
// 100KHz for slow speed
// 400KHz for high speed

//#define QDEL	delay(5)		// i2c quarter-bit delay
//#define HDEL	delay(10)		// i2c half-bit delay
//software i2c implementation
// i2c quarter-bit delay
#define QDEL	asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop");asm volatile("nop");
// i2c half-bit delay
#define HDEL	asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop"); asm volatile("nop");asm volatile("nop"); asm volatile("nop");

#define I2C_SDL_LO      GPIO_ResetBits(SDA_PORT, SDA_PIN)
#define I2C_SDL_HI      GPIO_SetBits(SDA_PORT, SDA_PIN)

#define I2C_SCL_LO      GPIO_ResetBits(SCL_PORT, SCL_PIN);
#define I2C_SCL_HI      GPIO_SetBits(SCL_PORT, SCL_PIN);

#define I2C_SCL_TOGGLE  HDEL; I2C_SCL_HI; HDEL; I2C_SCL_LO;
#define I2C_START       I2C_SDL_LO; QDEL; I2C_SCL_LO; 
#define I2C_STOP        HDEL; I2C_SCL_HI; QDEL; I2C_SDL_HI; HDEL;

void Configure_SDA_to_Input ()
{
    GPIO_InitTypeDef  GPIO_InitStructure;

    GPIO_InitStructure.GPIO_Pin = SDA_PIN;
    GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;
    GPIO_Init(SDA_PORT, &GPIO_InitStructure);
}

void Configure_SDA_to_Output ()
{
    GPIO_InitTypeDef  GPIO_InitStructure;

    GPIO_InitStructure.GPIO_Pin = SDA_PIN;
    GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_OD;
    GPIO_Init(SDA_PORT, &GPIO_InitStructure);
}

unsigned int i2cPutbyte(uint8_t b)
{
	int i;

	for (i=7;i>=0;i--)
	{
		if ( b & (1<<i) )
			I2C_SDL_HI;
		else
			I2C_SDL_LO;			// address bit
			I2C_SCL_TOGGLE;		// clock HI, delay, then LO
	}

	I2C_SDL_HI;					// leave SDL HI
	// added
	Configure_SDA_to_Input();			// change direction to input on SDA line (may not be needed)
	HDEL;
	I2C_SCL_HI;					// clock back up
  	b = GPIO_ReadInputDataBit(SDA_PORT, SDA_PIN);	// get the ACK bit

	HDEL;
	I2C_SCL_LO;					// not really ??
	Configure_SDA_to_Output ();			// change direction back to output
	HDEL;
	return (b == 0);			// return ACK value
}

uint8_t i2cGetbyte(unsigned int last)
{
	int i;
	uint8_t c,b = 0;

	I2C_SDL_HI;					// make sure pullups are ativated
	Configure_SDA_to_Input();			// change direction to input on SDA line (may not be needed)

	for(i=7;i>=0;i--)
	{
		HDEL;
		I2C_SCL_HI;				// clock HI
	  	c = GPIO_ReadInputDataBit(SDA_PORT, SDA_PIN);
		b <<= 1;
		if(c) b |= 1;
		HDEL;
    	I2C_SCL_LO;				// clock LO
	}

	Configure_SDA_to_Output ();				// change direction to output on SDA line

	if (last)
		I2C_SDL_HI;				// set NAK
	else
		I2C_SDL_LO;				// set ACK

	I2C_SCL_TOGGLE;				// clock pulse
	I2C_SDL_HI;					// leave with SDL HI
	return b;					// return received byte
}

//************************
//* I2C public functions *
//************************

//! Initialize I2C communication
void i2cInit(void)
{
    GPIO_InitTypeDef  GPIO_InitStructure;

    // set SDA as output
    GPIO_InitStructure.GPIO_Pin = SDA_PIN;
    GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_OD;
    GPIO_Init(SDA_PORT, &GPIO_InitStructure);

    // set SCL as output
    GPIO_InitStructure.GPIO_Pin =  SCL_PIN;
    GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_OD;
    GPIO_Init(SCL_PORT, &GPIO_InitStructure);

	I2C_SDL_HI;	// set I/O state and pull-ups
	I2C_SCL_HI;	// set I/O state and pull-ups
}

//! Send a byte sequence on the I2C bus
uint8_t i2cSend(uint8_t device, uint8_t subAddr, uint8_t length, uint8_t *data)
{
	uint8_t ACK;

	I2C_START;      			// do start transition
	ACK = i2cPutbyte(device); 		// send DEVICE address
	i2cPutbyte(subAddr);		// and the subaddress

	// send the data
	while (length--)
		i2cPutbyte(*data++);

	I2C_SDL_LO;					// clear data line and
	I2C_STOP;					// send STOP transition

	return ACK;
}

//! Retrieve a byte sequence on the I2C bus
uint8_t i2cReceive(uint8_t device, uint8_t subAddr, uint8_t length, uint8_t *data)
{
	int j = length;
	uint8_t *p = data, ACK;

	I2C_START;					// do start transition
	ACK = i2cPutbyte(device);			// send DEVICE address
	i2cPutbyte(subAddr);   		// and the subaddress
	HDEL;
	I2C_SCL_HI;      			// do a repeated START
	I2C_START;					// transition

	i2cPutbyte(device | READ);	// resend DEVICE, with READ bit set

	// receive data bytes
	while (j--)
		*p++ = i2cGetbyte(j == 0);

	I2C_SDL_LO;					// clear data line and
	I2C_STOP;					// send STOP transition

	return ACK;
}

