�J8      �Z�m�� �Z�m��ƃ     ƃ                �A  **********************
 *
 * Copyright (C) 2015 Atmel Corporation
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright
 *   notice, this list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright
 *   notice, this list of conditions and the following disclaimer in
 *   the documentation and/or other materials provided with the
 *   distribution.
 *
 * * Neither the name of the copyright holders nor the names of
 *   contributors may be used to endorse or promote products derived
 *   from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 ****************************************************************************/


#ifndef _AVR_IO_H_
#  error "Include <avr/io.h> instead of this file."
#endif

#ifndef _AVR_IOXXX_H_
#  define _AVR_IOXXX_H_ "iox64b1.h"
#else
#  error "Attempt to include more than one <avr/ioXXX.h> file."
#endif

#ifndef _AVR_ATXMEGA64B1_H_INCLUDED
#define _AVR_ATXMEGA64B1_H_INCLUDED

/* Ungrouped common registers */
#define GPIOR0  _SFR_MEM8(0x0000)  /* General Purpose IO Register 0 */
#define GPIOR1  _SFR_MEM8(0x0001)  /* General Purpose IO Register 1 */
#define GPIOR2  _SFR_MEM8(0x0002)  /* General Purpose IO Register 2 */
#define GPIOR3  _SFR_MEM8(0x0003)  /* General Purpose IO Register 3 */

/* Deprecated */
#define GPIO0  _SFR_MEM8(0x0000)  /* General Purpose IO Register 0 */
#define GPIO1  _SFR_MEM8(0x0001)  /* General Purpose IO Register 1 */
#define GPIO2  _SFR_MEM8(0x0002)  /* General Purpose IO Register 2 */
#define GPIO3  _SFR_MEM8(0x0003)  /* General Purpose IO Register 3 */

#define CCP  _SFR_MEM8(0x0034)  /* Configuration Change Protection */
#define RAMPD  _SFR_MEM8(0x0038)  /* Ramp D */
#define RAMPX  _SFR_MEM8(0x0039)  /* Ramp X */
#define RAMPY  _SFR_MEM8(0x003A)  /* Ramp Y */
#define RAMPZ  _SFR_MEM8(0x003B)  /* Ramp Z */
#define EIND  _SFR_MEM8(0x003C)  /* Extended Indirect Jump */
#define SPL  _SFR_MEM8(0x003D)  /* Stack Pointer Low */
#define SPH  _SFR_MEM8(0x003E)  /* Stack Pointer High */
#define SREG  _SFR_MEM8(0x003F)  /* Status Register */

/* C Language Only */
#if !defined (__ASSEMBLER__)

#include <stdint.h>

typedef volatile uint8_t register8_t;
typedef volatile uint16_t register16_t;
typedef volatile uint32_t register32_t;


#ifdef _WORDREGISTER
#undef _WORDREGISTER
#endif
#define _WORDREGISTER(regname)   \
    __extension__ union \
    { \
        register16_t regname; \
        struct \
        { \
            register8_t regname ## L; \
            register8_t regname ## H; \
        }; \
    }

#ifdef _DWORDREGISTER
#undef _DWORDREGISTER
#endif
#define _DWORDREGISTER(regname)  \
    __extension__ union \
    { \
        register32_t regname; \
        struct \
        { \
            register8_t regname ## 0; \
            register8_t regname ## 1; \
            register8_t regname ## 2; \
            register8_t regname ## 3; \
        }; \
    }


/*
==========================================================================
IO Module Structures
==========================================================================
*/


/*
--------------------------------------------------------------------------
VPORT - Virtual Ports
--------------------------------------------------------------------------
*/

/* Virtual Port */
typedef struct VPORT_struct
{
    register8_t DIR;  /* I/O Port Data Direction */
    register8_t OUT;  /* I/O Port Output */
    register8_t IN;  /* I/O Port Input */
    register8_t INTFLAGS;  /* Interrupt Flag Register */
} VPORT_t;


/*
--------------------------------------------------------------------------
XOCD - On-Chip Debug System
--------------------------------------------------------------------------
*/

/* On-Chip Debug System */
typedef struct OCD_struct
{
    register8_t OCDR0;  /* OCD Register 0 */
    register8_t OCDR1;  /* OCD Register 1 */
} OCD_t;


/*
--------------------------------------------------------------------------
CPU - CPU
--------------------------------------------------------------------------
*/

/* CCP signatures */
typedef enum CCP_enum
{
    CCP_SPM_gc = (0x9D<<0),  /* SPM Instruction Protection */
    CCP_IOREG_gc = (0xD8<<0),  /* IO Register Protection */
} CCP_t;


/*
--------------------------------------------------------------------------
CLK - Clock System
--------------------------------------------------------------------------
*/

/* Clock System */
typedef struct CLK_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t PSCTRL;  /* Prescaler Control Register */
    register8_t LOCK;  /* Lock register */
    register8_t RTCCTRL;  /* RTC Control Register */
    register8_t USBCTRL;  /* USB Control Register */
} CLK_t;

/* System Clock Selection */
typedef enum CLK_SCLKSEL_enum
{
    CLK_SCLKSEL_RC2M_gc = (0x00<<0),  /* Internal 2 MHz RC Oscillator */
    CLK_SCLKSEL_RC32M_gc = (0x01<<0),  /* Internal 32 MHz RC Oscillator */
    CLK_SCLKSEL_RC32K_gc = (0x02<<0),  /* Internal 32.768 kHz RC Oscillator */
    CLK_SCLKSEL_XOSC_gc = (0x03<<0),  /* External Crystal Oscillator or Clock */
    CLK_SCLKSEL_PLL_gc = (0x04<<0),  /* Phase Locked Loop */
} CLK_SCLKSEL_t;

/* Prescaler A Division Factor */
typedef enum CLK_PSADIV_enum
{
    CLK_PSADIV_1_gc = (0x00<<2),  /* Divide by 1 */
    CLK_PSADIV_2_gc = (0x01<<2),  /* Divide by 2 */
    CLK_PSADIV_4_gc = (0x03<<2),  /* Divide by 4 */
    CLK_PSADIV_8_gc = (0x05<<2),  /* Divide by 8 */
    CLK_PSADIV_16_gc = (0x07<<2),  /* Divide by 16 */
    CLK_PSADIV_32_gc = (0x09<<2),  /* Divide by 32 */
    CLK_PSADIV_64_gc = (0x0B<<2),  /* Divide by 64 */
    CLK_PSADIV_128_gc = (0x0D<<2),  /* Divide by 128 */
    CLK_PSADIV_256_gc = (0x0F<<2),  /* Divide by 256 */
    CLK_PSADIV_512_gc = (0x11<<2),  /* Divide by 512 */
} CLK_PSADIV_t;

/* Prescaler B and C Division Factor */
typedef enum CLK_PSBCDIV_enum
{
    CLK_PSBCDIV_1_1_gc = (0x00<<0),  /* Divide B by 1 and C by 1 */
    CLK_PSBCDIV_1_2_gc = (0x01<<0),  /* Divide B by 1 and C by 2 */
    CLK_PSBCDIV_4_1_gc = (0x02<<0),  /* Divide B by 4 and C by 1 */
    CLK_PSBCDIV_2_2_gc = (0x03<<0),  /* Divide B by 2 and C by 2 */
} CLK_PSBCDIV_t;

/* RTC Clock Source */
typedef enum CLK_RTCSRC_enum
{
    CLK_RTCSRC_ULP_gc = (0x00<<1),  /* 1.024 kHz from internal 32kHz ULP */
    CLK_RTCSRC_TOSC_gc = (0x01<<1),  /* 1.024 kHz from 32.768 kHz crystal oscillator on TOSC */
    CLK_RTCSRC_RCOSC_gc = (0x02<<1),  /* 1.024 kHz from internal 32.768 kHz RC oscillator */
    CLK_RTCSRC_TOSC32_gc = (0x05<<1),  /* 32.768 kHz from 32.768 kHz crystal oscillator on TOSC */
    CLK_RTCSRC_RCOSC32_gc = (0x06<<1),  /* 32.768 kHz from internal 32.768 kHz RC oscillator */
    CLK_RTCSRC_EXTCLK_gc = (0x07<<1),  /* External Clock from TOSC1 */
} CLK_RTCSRC_t;

/* USB Prescaler Division Factor */
typedef enum CLK_USBPSDIV_enum
{
    CLK_USBPSDIV_1_gc = (0x00<<3),  /* Divide by 1 */
    CLK_USBPSDIV_2_gc = (0x01<<3),  /* Divide by 2 */
    CLK_USBPSDIV_4_gc = (0x02<<3),  /* Divide by 4 */
    CLK_USBPSDIV_8_gc = (0x03<<3),  /* Divide by 8 */
    CLK_USBPSDIV_16_gc = (0x04<<3),  /* Divide by 16 */
    CLK_USBPSDIV_32_gc = (0x05<<3),  /* Divide by 32 */
} CLK_USBPSDIV_t;

/* USB Clock Source */
typedef enum CLK_USBSRC_enum
{
    CLK_USBSRC_PLL_gc = (0x00<<1),  /* PLL */
    CLK_USBSRC_RC32M_gc = (0x01<<1),  /* Internal 32 MHz RC Oscillator */
} CLK_USBSRC_t;


/*
--------------------------------------------------------------------------
SLEEP - Sleep Controller
--------------------------------------------------------------------------
*/

/* Sleep Controller */
typedef struct SLEEP_struct
{
    register8_t CTRL;  /* Control Register */
} SLEEP_t;

/* Sleep Mode */
typedef enum SLEEP_SMODE_enum
{
    SLEEP_SMODE_IDLE_gc = (0x00<<1),  /* Idle mode */
    SLEEP_SMODE_PDOWN_gc = (0x02<<1),  /* Power-down Mode */
    SLEEP_SMODE_PSAVE_gc = (0x03<<1),  /* Power-save Mode */
    SLEEP_SMODE_STDBY_gc = (0x06<<1),  /* Standby Mode */
    SLEEP_SMODE_ESTDBY_gc = (0x07<<1),  /* Extended Standby Mode */
} SLEEP_SMODE_t;



#define SLEEP_MODE_IDLE (0x00<<1)
#define SLEEP_MODE_PWR_DOWN (0x02<<1)
#define SLEEP_MODE_PWR_SAVE (0x03<<1)
#define SLEEP_MODE_STANDBY (0x06<<1)
#define SLEEP_MODE_EXT_STANDBY (0x07<<1)
/*
--------------------------------------------------------------------------
OSC - Oscillator
--------------------------------------------------------------------------
*/

/* Oscillator */
typedef struct OSC_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t STATUS;  /* Status Register */
    register8_t XOSCCTRL;  /* External Oscillator Control Register */
    register8_t XOSCFAIL;  /* Oscillator Failure Detection Register */
    register8_t RC32KCAL;  /* 32.768 kHz Internal Oscillator Calibration Register */
    register8_t PLLCTRL;  /* PLL Control Register */
    register8_t DFLLCTRL;  /* DFLL Control Register */
} OSC_t;

/* Oscillator Frequency Range */
typedef enum OSC_FRQRANGE_enum
{
    OSC_FRQRANGE_04TO2_gc = (0x00<<6),  /* 0.4 - 2 MHz */
    OSC_FRQRANGE_2TO9_gc = (0x01<<6),  /* 2 - 9 MHz */
    OSC_FRQRANGE_9TO12_gc = (0x02<<6),  /* 9 - 12 MHz */
    OSC_FRQRANGE_12TO16_gc = (0x03<<6),  /* 12 - 16 MHz */
} OSC_FRQRANGE_t;

/* External Oscillator Selection and Startup Time */
typedef enum OSC_XOSCSEL_enum
{
    OSC_XOSCSEL_EXTCLK_gc = (0x00<<0),  /* External Clock on port R1 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C0_gc = (0x01<<0),  /* External Clock on port C0 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C1_gc = (0x05<<0),  /* External Clock on port C1 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C2_gc = (0x09<<0),  /* External Clock on port C2 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C3_gc = (0x0D<<0),  /* External Clock on port C3 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C4_gc = (0x11<<0),  /* External Clock on port C4 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C5_gc = (0x15<<0),  /* External Clock on port C5 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C6_gc = (0x19<<0),  /* External Clock on port C6 - 6 CLK */
    OSC_XOSCSEL_EXTCLK_C7_gc = (0x1D<<0),  /* External Clock on port C7 - 6 CLK */
    OSC_XOSCSEL_32KHz_gc = (0x02<<0),  /* 32kHz TOSC - 32K CLK */
    OSC_XOSCSEL_XTAL_256CLK_gc = (0x03<<0),  /* 0.4-16MHz XTAL - 256 CLK */
    OSC_XOSCSEL_XTAL_1KCLK_gc = (0x07<<0),  /* 0.4-16MHz XTAL - 1K CLK */
    OSC_XOSCSEL_XTAL_16KCLK_gc = (0x0B<<0),  /* 0.4-16MHz XTAL - 16K CLK */
} OSC_XOSCSEL_t;

/* PLL Clock Source */
typedef enum OSC_PLLSRC_enum
{
    OSC_PLLSRC_RC2M_gc = (0x00<<6),  /* Internal 2 MHz RC Oscillator */
    OSC_PLLSRC_RC32M_gc = (0x02<<6),  /* Internal 32 MHz RC Oscillator */
    OSC_PLLSRC_XOSC_gc = (0x03<<6),  /* External Oscillator */
} OSC_PLLSRC_t;

/* 2 MHz DFLL Calibration Reference */
typedef enum OSC_RC2MCREF_enum
{
    OSC_RC2MCREF_RC32K_gc = (0x00<<0),  /* Internal 32.768 kHz RC Oscillator */
    OSC_RC2MCREF_XOSC32K_gc = (0x01<<0),  /* External 32.768 kHz Crystal Oscillator */
} OSC_RC2MCREF_t;

/* 32 MHz DFLL Calibration Reference */
typedef enum OSC_RC32MCREF_enum
{
    OSC_RC32MCREF_RC32K_gc = (0x00<<1),  /* Internal 32.768 kHz RC Oscillator */
    OSC_RC32MCREF_XOSC32K_gc = (0x01<<1),  /* External 32.768 kHz Crystal Oscillator */
    OSC_RC32MCREF_USBSOF_gc = (0x02<<1),  /* USB Start of Frame */
} OSC_RC32MCREF_t;


/*
--------------------------------------------------------------------------
DFLL - DFLL
--------------------------------------------------------------------------
*/

/* DFLL */
typedef struct DFLL_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t reserved_0x01;
    register8_t CALA;  /* Calibration Register A */
    register8_t CALB;  /* Calibration Register B */
    register8_t COMP0;  /* Oscillator Compare Register 0 */
    register8_t COMP1;  /* Oscillator Compare Register 1 */
    register8_t COMP2;  /* Oscillator Compare Register 2 */
    register8_t reserved_0x07;
} DFLL_t;


/*
--------------------------------------------------------------------------
PR - Power Reduction
--------------------------------------------------------------------------
*/

/* Power Reduction */
typedef struct PR_struct
{
    register8_t PRGEN;  /* General Power Reduction */
    register8_t PRPA;  /* Power Reduction Port A */
    register8_t PRPB;  /* Power Reduction Port B */
    register8_t PRPC;  /* Power Reduction Port C */
    register8_t reserved_0x04;
    register8_t PRPE;  /* Power Reduction Port E */
} PR_t;


/*
--------------------------------------------------------------------------
RST - Reset
--------------------------------------------------------------------------
*/

/* Reset */
typedef struct RST_struct
{
    register8_t STATUS;  /* Status Register */
    register8_t CTRL;  /* Control Register */
} RST_t;


/*
--------------------------------------------------------------------------
WDT - Watch-Dog Timer
--------------------------------------------------------------------------
*/

/* Watch-Dog Timer */
typedef struct WDT_struct
{
    register8_t CTRL;  /* Control */
    register8_t WINCTRL;  /* Windowed Mode Control */
    register8_t STATUS;  /* Status */
} WDT_t;

/* Period setting */
typedef enum WDT_PER_enum
{
    WDT_PER_8CLK_gc = (0x00<<2),  /* 8 cycles (8ms @ 3.3V) */
    WDT_PER_16CLK_gc = (0x01<<2),  /* 16 cycles (16ms @ 3.3V) */
    WDT_PER_32CLK_gc = (0x02<<2),  /* 32 cycles (32ms @ 3.3V) */
    WDT_PER_64CLK_gc = (0x03<<2),  /* 64 cycles (64ms @ 3.3V) */
    WDT_PER_128CLK_gc = (0x04<<2),  /* 128 cycles (0.128s @ 3.3V) */
    WDT_PER_256CLK_gc = (0x05<<2),  /* 256 cycles (0.256s @ 3.3V) */
    WDT_PER_512CLK_gc = (0x06<<2),  /* 512 cycles (0.512s @ 3.3V) */
    WDT_PER_1KCLK_gc = (0x07<<2),  /* 1K cycles (1s @ 3.3V) */
    WDT_PER_2KCLK_gc = (0x08<<2),  /* 2K cycles (2s @ 3.3V) */
    WDT_PER_4KCLK_gc = (0x09<<2),  /* 4K cycles (4s @ 3.3V) */
    WDT_PER_8KCLK_gc = (0x0A<<2),  /* 8K cycles (8s @ 3.3V) */
} WDT_PER_t;

/* Closed window period */
typedef enum WDT_WPER_enum
{
    WDT_WPER_8CLK_gc = (0x00<<2),  /* 8 cycles (8ms @ 3.3V) */
    WDT_WPER_16CLK_gc = (0x01<<2),  /* 16 cycles (16ms @ 3.3V) */
    WDT_WPER_32CLK_gc = (0x02<<2),  /* 32 cycles (32ms @ 3.3V) */
    WDT_WPER_64CLK_gc = (0x03<<2),  /* 64 cycles (64ms @ 3.3V) */
    WDT_WPER_128CLK_gc = (0x04<<2),  /* 128 cycles (0.128s @ 3.3V) */
    WDT_WPER_256CLK_gc = (0x05<<2),  /* 256 cycles (0.256s @ 3.3V) */
    WDT_WPER_512CLK_gc = (0x06<<2),  /* 512 cycles (0.512s @ 3.3V) */
    WDT_WPER_1KCLK_gc = (0x07<<2),  /* 1K cycles (1s @ 3.3V) */
    WDT_WPER_2KCLK_gc = (0x08<<2),  /* 2K cycles (2s @ 3.3V) */
    WDT_WPER_4KCLK_gc = (0x09<<2),  /* 4K cycles (4s @ 3.3V) */
    WDT_WPER_8KCLK_gc = (0x0A<<2),  /* 8K cycles (8s @ 3.3V) */
} WDT_WPER_t;


/*
--------------------------------------------------------------------------
MCU - MCU Control
--------------------------------------------------------------------------
*/

/* MCU Control */
typedef struct MCU_struct
{
    register8_t DEVID0;  /* Device ID byte 0 */
    register8_t DEVID1;  /* Device ID byte 1 */
    register8_t DEVID2;  /* Device ID byte 2 */
    register8_t REVID;  /* Revision ID */
    register8_t JTAGUID;  /* JTAG User ID */
    register8_t reserved_0x05;
    register8_t MCUCR;  /* MCU Control */
    register8_t ANAINIT;  /* Analog Startup Delay */
    register8_t EVSYSLOCK;  /* Event System Lock */
    register8_t AWEXLOCK;  /* AWEX Lock */
    register8_t reserved_0x0A;
    register8_t reserved_0x0B;
} MCU_t;


/*
--------------------------------------------------------------------------
PMIC - Programmable Multi-level Interrupt Controller
--------------------------------------------------------------------------
*/

/* Programmable Multi-level Interrupt Controller */
typedef struct PMIC_struct
{
    register8_t STATUS;  /* Status Register */
    register8_t INTPRI;  /* Interrupt Priority */
    register8_t CTRL;  /* Control Register */
    register8_t reserved_0x03;
    register8_t reserved_0x04;
    register8_t reserved_0x05;
    register8_t reserved_0x06;
    register8_t reserved_0x07;
    register8_t reserved_0x08;
    register8_t reserved_0x09;
    register8_t reserved_0x0A;
    register8_t reserved_0x0B;
    register8_t reserved_0x0C;
    register8_t reserved_0x0D;
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
} PMIC_t;


/*
--------------------------------------------------------------------------
PORTCFG - Port Configuration
--------------------------------------------------------------------------
*/

/* I/O port Configuration */
typedef struct PORTCFG_struct
{
    register8_t MPCMASK;  /* Multi-pin Configuration Mask */
    register8_t reserved_0x01;
    register8_t VPCTRLA;  /* Virtual Port Control Register A */
    register8_t VPCTRLB;  /* Virtual Port Control Register B */
    register8_t CLKEVOUT;  /* Clock and Event Out Register */
    register8_t reserved_0x05;
    register8_t EVOUTSEL;  /* Event Output Select */
} PORTCFG_t;

/* Virtual Port Mapping */
typedef enum PORTCFG_VP02MAP_enum
{
    PORTCFG_VP02MAP_PORTA_gc = (0x00<<0),  /* Mapped To PORTA */
    PORTCFG_VP02MAP_PORTB_gc = (0x01<<0),  /* Mapped To PORTB */
    PORTCFG_VP02MAP_PORTC_gc = (0x02<<0),  /* Mapped To PORTC */
    PORTCFG_VP02MAP_PORTD_gc = (0x03<<0),  /* Mapped To PORTD */
    PORTCFG_VP02MAP_PORTE_gc = (0x04<<0),  /* Mapped To PORTE */
    PORTCFG_VP02MAP_PORTG_gc = (0x06<<0),  /* Mapped To PORTG */
    PORTCFG_VP02MAP_PORTM_gc = (0x0B<<0),  /* Mapped To PORTM */
    PORTCFG_VP02MAP_PORTR_gc = (0x0F<<0),  /* Mapped To PORTR */
} PORTCFG_VP02MAP_t;

/* Virtual Port Mapping */
typedef enum PORTCFG_VP13MAP_enum
{
    PORTCFG_VP13MAP_PORTA_gc = (0x00<<4),  /* Mapped To PORTA */
    PORTCFG_VP13MAP_PORTB_gc = (0x01<<4),  /* Mapped To PORTB */
    PORTCFG_VP13MAP_PORTC_gc = (0x02<<4),  /* Mapped To PORTC */
    PORTCFG_VP13MAP_PORTD_gc = (0x03<<4),  /* Mapped To PORTD */
    PORTCFG_VP13MAP_PORTE_gc = (0x04<<4),  /* Mapped To PORTE */
    PORTCFG_VP13MAP_PORTG_gc = (0x06<<4),  /* Mapped To PORTG */
    PORTCFG_VP13MAP_PORTM_gc = (0x0B<<4),  /* Mapped To PORTM */
    PORTCFG_VP13MAP_PORTR_gc = (0x0F<<4),  /* Mapped To PORTR */
} PORTCFG_VP13MAP_t;

/* System Clock Output Port */
typedef enum PORTCFG_CLKOUT_enum
{
    PORTCFG_CLKOUT_OFF_gc = (0x00<<0),  /* System Clock Output Disabled */
    PORTCFG_CLKOUT_PC_gc = (0x01<<0),  /* System Clock Output on Port C */
    PORTCFG_CLKOUT_PE_gc = (0x03<<0),  /* System Clock Output on Port E */
} PORTCFG_CLKOUT_t;

/* Peripheral Clock Output Select */
typedef enum PORTCFG_CLKOUTSEL_enum
{
    PORTCFG_CLKOUTSEL_CLK1X_gc = (0x00<<2),  /* 1x Peripheral Clock Output to pin */
    PORTCFG_CLKOUTSEL_CLK2X_gc = (0x01<<2),  /* 2x Peripheral Clock Output to pin */
    PORTCFG_CLKOUTSEL_CLK4X_gc = (0x02<<2),  /* 4x Peripheral Clock Output to pin */
} PORTCFG_CLKOUTSEL_t;

/* Event Output Port */
typedef enum PORTCFG_EVOUT_enum
{
    PORTCFG_EVOUT_OFF_gc = (0x00<<4),  /* Event Output Disabled */
    PORTCFG_EVOUT_PC_gc = (0x01<<4),  /* Event Channel 0 Output on Port C */
    PORTCFG_EVOUT_PE_gc = (0x03<<4),  /* Event Channel 0 Output on Port E */
} PORTCFG_EVOUT_t;

/* Clock and Event Output Port */
typedef enum PORTCFG_CLKEVPIN_enum
{
    PORTCFG_CLKEVPIN_PIN7_gc = (0x00<<7),  /* Clock and Event Ouput on PIN 7 */
    PORTCFG_CLKEVPIN_PIN4_gc = (0x01<<7),  /* Clock and Event Ouput on PIN 4 */
} PORTCFG_CLKEVPIN_t;

/* Event Output Select */
typedef enum PORTCFG_EVOUTSEL_enum
{
    PORTCFG_EVOUTSEL_0_gc = (0x00<<2),  /* Event Channel 0 output to pin */
    PORTCFG_EVOUTSEL_1_gc = (0x01<<2),  /* Event Channel 1 output to pin */
    PORTCFG_EVOUTSEL_2_gc = (0x02<<2),  /* Event Channel 2 output to pin */
    PORTCFG_EVOUTSEL_3_gc = (0x03<<2),  /* Event Channel 3 output to pin */
} PORTCFG_EVOUTSEL_t;


/*
--------------------------------------------------------------------------
AES - AES Module
--------------------------------------------------------------------------
*/

/* AES Module */
typedef struct AES_struct
{
    register8_t CTRL;  /* AES Control Register */
    register8_t STATUS;  /* AES Status Register */
    register8_t STATE;  /* AES State Register */
    register8_t KEY;  /* AES Key Register */
    register8_t INTCTRL;  /* AES Interrupt Control Register */
} AES_t;

/* Interrupt level */
typedef enum AES_INTLVL_enum
{
    AES_INTLVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    AES_INTLVL_LO_gc = (0x01<<0),  /* Low Level */
    AES_INTLVL_MED_gc = (0x02<<0),  /* Medium Level */
    AES_INTLVL_HI_gc = (0x03<<0),  /* High Level */
} AES_INTLVL_t;


/*
--------------------------------------------------------------------------
CRC - Cyclic Redundancy Checker
--------------------------------------------------------------------------
*/

/* Cyclic Redundancy Checker */
typedef struct CRC_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t STATUS;  /* Status Register */
    register8_t reserved_0x02;
    register8_t DATAIN;  /* Data Input */
    register8_t CHECKSUM0;  /* Checksum byte 0 */
    register8_t CHECKSUM1;  /* Checksum byte 1 */
    register8_t CHECKSUM2;  /* Checksum byte 2 */
    register8_t CHECKSUM3;  /* Checksum byte 3 */
} CRC_t;

/* Reset */
typedef enum CRC_RESET_enum
{
    CRC_RESET_NO_gc = (0x00<<6),  /* No Reset */
    CRC_RESET_RESET0_gc = (0x02<<6),  /* Reset CRC with CHECKSUM to all zeros */
    CRC_RESET_RESET1_gc = (0x03<<6),  /* Reset CRC with CHECKSUM to all ones */
} CRC_RESET_t;

/* Input Source */
typedef enum CRC_SOURCE_enum
{
    CRC_SOURCE_DISABLE_gc = (0x00<<0),  /* Disabled */
    CRC_SOURCE_IO_gc = (0x01<<0),  /* I/O Interface */
    CRC_SOURCE_FLASH_gc = (0x02<<0),  /* Flash */
    CRC_SOURCE_DMAC0_gc = (0x04<<0),  /* DMAC Channel 0 */
    CRC_SOURCE_DMAC1_gc = (0x05<<0),  /* DMAC Channel 1 */
} CRC_SOURCE_t;


/*
--------------------------------------------------------------------------
DMA - DMA Controller
--------------------------------------------------------------------------
*/

/* DMA Channel */
typedef struct DMA_CH_struct
{
    register8_t CTRLA;  /* Channel Control */
    register8_t CTRLB;  /* Channel Control */
    register8_t ADDRCTRL;  /* Address Control */
    register8_t TRIGSRC;  /* Channel Trigger Source */
    _WORDREGISTER(TRFCNT);  /* Channel Block Transfer Count */
    register8_t REPCNT;  /* Channel Repeat Count */
    register8_t reserved_0x07;
    register8_t SRCADDR0;  /* Channel Source Address 0 */
    register8_t SRCADDR1;  /* Channel Source Address 1 */
    register8_t reserved_0x0A;
    register8_t reserved_0x0B;
    register8_t DESTADDR0;  /* Channel Destination Address 0 */
    register8_t DESTADDR1;  /* Channel Destination Address 1 */
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
} DMA_CH_t;


/* DMA Controller */
typedef struct DMA_struct
{
    register8_t CTRL;  /* Control */
    register8_t reserved_0x01;
    register8_t reserved_0x02;
    register8_t INTFLAGS;  /* Transfer Interrupt Status */
    register8_t STATUS;  /* Status */
    register8_t reserved_0x05;
    _WORDREGISTER(TEMP);  /* Temporary Register For 16-bit Access */
    register8_t reserved_0x08;
    register8_t reserved_0x09;
    register8_t reserved_0x0A;
    register8_t reserved_0x0B;
    register8_t reserved_0x0C;
    register8_t reserved_0x0D;
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
    DMA_CH_t CH0;  /* DMA Channel 0 */
    DMA_CH_t CH1;  /* DMA Channel 1 */
} DMA_t;

/* Burst mode */
typedef enum DMA_CH_BURSTLEN_enum
{
    DMA_CH_BURSTLEN_1BYTE_gc = (0x00<<0),  /* 1-byte burst mode */
    DMA_CH_BURSTLEN_2BYTE_gc = (0x01<<0),  /* 2-byte burst mode */
    DMA_CH_BURSTLEN_4BYTE_gc = (0x02<<0),  /* 4-byte burst mode */
    DMA_CH_BURSTLEN_8BYTE_gc = (0x03<<0),  /* 8-byte burst mode */
} DMA_CH_BURSTLEN_t;

/* Source address reload mode */
typedef enum DMA_CH_SRCRELOAD_enum
{
    DMA_CH_SRCRELOAD_NONE_gc = (0x00<<6),  /* No reload */
    DMA_CH_SRCRELOAD_BLOCK_gc = (0x01<<6),  /* Reload at end of block */
    DMA_CH_SRCRELOAD_BURST_gc = (0x02<<6),  /* Reload at end of burst */
    DMA_CH_SRCRELOAD_TRANSACTION_gc = (0x03<<6),  /* Reload at end of transaction */
} DMA_CH_SRCRELOAD_t;

/* Source addressing mode */
typedef enum DMA_CH_SRCDIR_enum
{
    DMA_CH_SRCDIR_FIXED_gc = (0x00<<4),  /* Fixed */
    DMA_CH_SRCDIR_INC_gc = (0x01<<4),  /* Increment */
    DMA_CH_SRCDIR_DEC_gc = (0x02<<4),  /* Decrement */
} DMA_CH_SRCDIR_t;

/* Destination adress reload mode */
typedef enum DMA_CH_DESTRELOAD_enum
{
    DMA_CH_DESTRELOAD_NONE_gc = (0x00<<2),  /* No reload */
    DMA_CH_DESTRELOAD_BLOCK_gc = (0x01<<2),  /* Reload at end of block */
    DMA_CH_DESTRELOAD_BURST_gc = (0x02<<2),  /* Reload at end of burst */
    DMA_CH_DESTRELOAD_TRANSACTION_gc = (0x03<<2),  /* Reload at end of transaction */
} DMA_CH_DESTRELOAD_t;

/* Destination adressing mode */
typedef enum DMA_CH_DESTDIR_enum
{
    DMA_CH_DESTDIR_FIXED_gc = (0x00<<0),  /* Fixed */
    DMA_CH_DESTDIR_INC_gc = (0x01<<0),  /* Increment */
    DMA_CH_DESTDIR_DEC_gc = (0x02<<0),  /* Decrement */
} DMA_CH_DESTDIR_t;

/* Transfer trigger source */
typedef enum DMA_CH_TRIGSRC_enum
{
    DMA_CH_TRIGSRC_OFF_gc = (0x00<<0),  /* Off software triggers only */
    DMA_CH_TRIGSRC_EVSYS_CH0_gc = (0x01<<0),  /* Event System Channel 0 */
    DMA_CH_TRIGSRC_EVSYS_CH1_gc = (0x02<<0),  /* Event System Channel 1 */
    DMA_CH_TRIGSRC_EVSYS_CH2_gc = (0x03<<0),  /* Event System Channel 2 */
    DMA_CH_TRIGSRC_ADCA_CH0_gc = (0x10<<0),  /* ADCA Channel 0 */
    DMA_CH_TRIGSRC_ADCB_CH0_gc = (0x20<<0),  /* ADCB Channel 0 */
    DMA_CH_TRIGSRC_TCC0_OVF_gc = (0x40<<0),  /* Timer/Counter C0 Overflow */
    DMA_CH_TRIGSRC_TCC0_ERR_gc = (0x41<<0),  /* Timer/Counter C0 Error */
    DMA_CH_TRIGSRC_TCC0_CCA_gc = (0x42<<0),  /* Timer/Counter C0 Compare or Capture A */
    DMA_CH_TRIGSRC_TCC0_CCB_gc = (0x43<<0),  /* Timer/Counter C0 Compare or Capture B */
    DMA_CH_TRIGSRC_TCC0_CCC_gc = (0x44<<0),  /* Timer/Counter C0 Compare or Capture C */
    DMA_CH_TRIGSRC_TCC0_CCD_gc = (0x45<<0),  /* Timer/Counter C0 Compare or Capture D */
    DMA_CH_TRIGSRC_TCC1_OVF_gc = (0x46<<0),  /* Timer/Counter C1 Overflow */
    DMA_CH_TRIGSRC_TCC1_ERR_gc = (0x47<<0),  /* Timer/Counter C1 Error */
    DMA_CH_TRIGSRC_TCC1_CCA_gc = (0x48<<0),  /* Timer/Counter C1 Compare or Capture A */
    DMA_CH_TRIGSRC_TCC1_CCB_gc = (0x49<<0),  /* Timer/Counter C1 Compare or Capture B */
    DMA_CH_TRIGSRC_SPIC_gc = (0x4A<<0),  /* SPI C Transfer Complete */
    DMA_CH_TRIGSRC_USARTC0_RXC_gc = (0x4B<<0),  /* USART C0 Receive Complete */
    DMA_CH_TRIGSRC_USARTC0_DRE_gc = (0x4C<<0),  /* USART C0 Data Register Empty */
    DMA_CH_TRIGSRC_TCE0_OVF_gc = (0x80<<0),  /* Timer/Counter E0 Overflow */
    DMA_CH_TRIGSRC_TCE0_ERR_gc = (0x81<<0),  /* Timer/Counter E0 Error */
    DMA_CH_TRIGSRC_TCE0_CCA_gc = (0x82<<0),  /* Timer/Counter E0 Compare or Capture A */
    DMA_CH_TRIGSRC_TCE0_CCB_gc = (0x83<<0),  /* Timer/Counter E0 Compare or Capture B */
    DMA_CH_TRIGSRC_TCE0_CCC_gc = (0x84<<0),  /* Timer/Counter E0 Compare or Capture C */
    DMA_CH_TRIGSRC_TCE0_CCD_gc = (0x85<<0),  /* Timer/Counter E0 Compare or Capture D */
    DMA_CH_TRIGSRC_USARTE0_RXC_gc = (0x8B<<0),  /* USART E0 Receive Complete */
    DMA_CH_TRIGSRC_USARTE0_DRE_gc = (0x8C<<0),  /* USART E0 Data Register Empty */
} DMA_CH_TRIGSRC_t;

/* Double buffering mode */
typedef enum DMA_DBUFMODE_enum
{
    DMA_DBUFMODE_DISABLED_gc = (0x00<<2),  /* Double buffering disabled */
    DMA_DBUFMODE_CH01_gc = (0x01<<2),  /* Double buffering enabled on channel 0/1 */
} DMA_DBUFMODE_t;

/* Priority mode */
typedef enum DMA_PRIMODE_enum
{
    DMA_PRIMODE_RR01_gc = (0x00<<0),  /* Round Robin */
    DMA_PRIMODE_CH0RR1_gc = (0x01<<0),  /* Channel 0 > channel 1 */
} DMA_PRIMODE_t;

/* Interrupt level */
typedef enum DMA_CH_ERRINTLVL_enum
{
    DMA_CH_ERRINTLVL_OFF_gc = (0x00<<2),  /* Interrupt disabled */
    DMA_CH_ERRINTLVL_LO_gc = (0x01<<2),  /* Low level */
    DMA_CH_ERRINTLVL_MED_gc = (0x02<<2),  /* Medium level */
    DMA_CH_ERRINTLVL_HI_gc = (0x03<<2),  /* High level */
} DMA_CH_ERRINTLVL_t;

/* Interrupt level */
typedef enum DMA_CH_TRNINTLVL_enum
{
    DMA_CH_TRNINTLVL_OFF_gc = (0x00<<0),  /* Interrupt disabled */
    DMA_CH_TRNINTLVL_LO_gc = (0x01<<0),  /* Low level */
    DMA_CH_TRNINTLVL_MED_gc = (0x02<<0),  /* Medium level */
    DMA_CH_TRNINTLVL_HI_gc = (0x03<<0),  /* High level */
} DMA_CH_TRNINTLVL_t;


/*
--------------------------------------------------------------------------
EVSYS - Event System
--------------------------------------------------------------------------
*/

/* Event System */
typedef struct EVSYS_struct
{
    register8_t CH0MUX;  /* Event Channel 0 Multiplexer */
    register8_t CH1MUX;  /* Event Channel 1 Multiplexer */
    register8_t CH2MUX;  /* Event Channel 2 Multiplexer */
    register8_t CH3MUX;  /* Event Channel 3 Multiplexer */
    register8_t reserved_0x04;
    register8_t reserved_0x05;
    register8_t reserved_0x06;
    register8_t reserved_0x07;
    register8_t CH0CTRL;  /* Channel 0 Control Register */
    register8_t CH1CTRL;  /* Channel 1 Control Register */
    register8_t CH2CTRL;  /* Channel 2 Control Register */
    register8_t CH3CTRL;  /* Channel 3 Control Register */
    register8_t reserved_0x0C;
    register8_t reserved_0x0D;
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
    register8_t STROBE;  /* Event Strobe */
    register8_t DATA;  /* Event Data */
} EVSYS_t;

/* Quadrature Decoder Index Recognition Mode */
typedef enum EVSYS_QDIRM_enum
{
    EVSYS_QDIRM_00_gc = (0x00<<5),  /* QDPH0 = 0, QDPH90 = 0 */
    EVSYS_QDIRM_01_gc = (0x01<<5),  /* QDPH0 = 0, QDPH90 = 1 */
    EVSYS_QDIRM_10_gc = (0x02<<5),  /* QDPH0 = 1, QDPH90 = 0 */
    EVSYS_QDIRM_11_gc = (0x03<<5),  /* QDPH0 = 1, QDPH90 = 1 */
} EVSYS_QDIRM_t;

/* Digital filter coefficient */
typedef enum EVSYS_DIGFILT_enum
{
    EVSYS_DIGFILT_1SAMPLE_gc = (0x00<<0),  /* 1 SAMPLE */
    EVSYS_DIGFILT_2SAMPLES_gc = (0x01<<0),  /* 2 SAMPLES */
    EVSYS_DIGFILT_3SAMPLES_gc = (0x02<<0),  /* 3 SAMPLES */
    EVSYS_DIGFILT_4SAMPLES_gc = (0x03<<0),  /* 4 SAMPLES */
    EVSYS_DIGFILT_5SAMPLES_gc = (0x04<<0),  /* 5 SAMPLES */
    EVSYS_DIGFILT_6SAMPLES_gc = (0x05<<0),  /* 6 SAMPLES */
    EVSYS_DIGFILT_7SAMPLES_gc = (0x06<<0),  /* 7 SAMPLES */
    EVSYS_DIGFILT_8SAMPLES_gc = (0x07<<0),  /* 8 SAMPLES */
} EVSYS_DIGFILT_t;

/* Event Channel multiplexer input selection */
typedef enum EVSYS_CHMUX_enum
{
    EVSYS_CHMUX_OFF_gc = (0x00<<0),  /* Off */
    EVSYS_CHMUX_RTC_OVF_gc = (0x08<<0),  /* RTC Overflow */
    EVSYS_CHMUX_RTC_CMP_gc = (0x09<<0),  /* RTC Compare Match */
    EVSYS_CHMUX_USB_gc = (0x0A<<0),  /* USB Setup, SOF, CRC error and UNF/OVF */
    EVSYS_CHMUX_ACA_CH0_gc = (0x10<<0),  /* Analog Comparator A Channel 0 */
    EVSYS_CHMUX_ACA_CH1_gc = (0x11<<0),  /* Analog Comparator A Channel 1 */
    EVSYS_CHMUX_ACA_WIN_gc = (0x12<<0),  /* Analog Comparator A Window */
    EVSYS_CHMUX_ACB_CH0_gc = (0x13<<0),  /* Analog Comparator B Channel 0 */
    EVSYS_CHMUX_ACB_CH1_gc = (0x14<<0),  /* Analog Comparator B Channel 1 */
    EVSYS_CHMUX_ACB_WIN_gc = (0x15<<0),  /* Analog Comparator B Window */
    EVSYS_CHMUX_ADCA_CH0_gc = (0x20<<0),  /* ADC A Channel */
    EVSYS_CHMUX_ADCB_CH0_gc = (0x24<<0),  /* ADC B Channel */
    EVSYS_CHMUX_PORTA_PIN0_gc = (0x50<<0),  /* Port A, Pin0 */
    EVSYS_CHMUX_PORTA_PIN1_gc = (0x51<<0),  /* Port A, Pin1 */
    EVSYS_CHMUX_PORTA_PIN2_gc = (0x52<<0),  /* Port A, Pin2 */
    EVSYS_CHMUX_PORTA_PIN3_gc = (0x53<<0),  /* Port A, Pin3 */
    EVSYS_CHMUX_PORTA_PIN4_gc = (0x54<<0),  /* Port A, Pin4 */
    EVSYS_CHMUX_PORTA_PIN5_gc = (0x55<<0),  /* Port A, Pin5 */
    EVSYS_CHMUX_PORTA_PIN6_gc = (0x56<<0),  /* Port A, Pin6 */
    EVSYS_CHMUX_PORTA_PIN7_gc = (0x57<<0),  /* Port A, Pin7 */
    EVSYS_CHMUX_PORTB_PIN0_gc = (0x58<<0),  /* Port B, Pin0 */
    EVSYS_CHMUX_PORTB_PIN1_gc = (0x59<<0),  /* Port B, Pin1 */
    EVSYS_CHMUX_PORTB_PIN2_gc = (0x5A<<0),  /* Port B, Pin2 */
    EVSYS_CHMUX_PORTB_PIN3_gc = (0x5B<<0),  /* Port B, Pin3 */
    EVSYS_CHMUX_PORTB_PIN4_gc = (0x5C<<0),  /* Port B, Pin4 */
    EVSYS_CHMUX_PORTB_PIN5_gc = (0x5D<<0),  /* Port B, Pin5 */
    EVSYS_CHMUX_PORTB_PIN6_gc = (0x5E<<0),  /* Port B, Pin6 */
    EVSYS_CHMUX_PORTB_PIN7_gc = (0x5F<<0),  /* Port B, Pin7 */
    EVSYS_CHMUX_PORTC_PIN0_gc = (0x60<<0),  /* Port C, Pin0 */
    EVSYS_CHMUX_PORTC_PIN1_gc = (0x61<<0),  /* Port C, Pin1 */
    EVSYS_CHMUX_PORTC_PIN2_gc = (0x62<<0),  /* Port C, Pin2 */
    EVSYS_CHMUX_PORTC_PIN3_gc = (0x63<<0),  /* Port C, Pin3 */
    EVSYS_CHMUX_PORTC_PIN4_gc = (0x64<<0),  /* Port C, Pin4 */
    EVSYS_CHMUX_PORTC_PIN5_gc = (0x65<<0),  /* Port C, Pin5 */
    EVSYS_CHMUX_PORTC_PIN6_gc = (0x66<<0),  /* Port C, Pin6 */
    EVSYS_CHMUX_PORTC_PIN7_gc = (0x67<<0),  /* Port C, Pin7 */
    EVSYS_CHMUX_PORTD_PIN0_gc = (0x68<<0),  /* Port D, Pin0 */
    EVSYS_CHMUX_PORTD_PIN1_gc = (0x69<<0),  /* Port D, Pin1 */
    EVSYS_CHMUX_PORTD_PIN2_gc = (0x6A<<0),  /* Port D, Pin2 */
    EVSYS_CHMUX_PORTE_PIN0_gc = (0x70<<0),  /* Port E, Pin0 */
    EVSYS_CHMUX_PORTE_PIN1_gc = (0x71<<0),  /* Port E, Pin1 */
    EVSYS_CHMUX_PORTE_PIN2_gc = (0x72<<0),  /* Port E, Pin2 */
    EVSYS_CHMUX_PORTE_PIN3_gc = (0x73<<0),  /* Port E, Pin3 */
    EVSYS_CHMUX_PORTE_PIN4_gc = (0x74<<0),  /* Port E, Pin4 */
    EVSYS_CHMUX_PORTE_PIN5_gc = (0x75<<0),  /* Port E, Pin5 */
    EVSYS_CHMUX_PORTE_PIN6_gc = (0x76<<0),  /* Port E, Pin6 */
    EVSYS_CHMUX_PORTE_PIN7_gc = (0x77<<0),  /* Port E, Pin7 */
    EVSYS_CHMUX_PRESCALER_1_gc = (0x80<<0),  /* Prescaler, divide by 1 */
    EVSYS_CHMUX_PRESCALER_2_gc = (0x81<<0),  /* Prescaler, divide by 2 */
    EVSYS_CHMUX_PRESCALER_4_gc = (0x82<<0),  /* Prescaler, divide by 4 */
    EVSYS_CHMUX_PRESCALER_8_gc = (0x83<<0),  /* Prescaler, divide by 8 */
    EVSYS_CHMUX_PRESCALER_16_gc = (0x84<<0),  /* Prescaler, divide by 16 */
    EVSYS_CHMUX_PRESCALER_32_gc = (0x85<<0),  /* Prescaler, divide by 32 */
    EVSYS_CHMUX_PRESCALER_64_gc = (0x86<<0),  /* Prescaler, divide by 64 */
    EVSYS_CHMUX_PRESCALER_128_gc = (0x87<<0),  /* Prescaler, divide by 128 */
    EVSYS_CHMUX_PRESCALER_256_gc = (0x88<<0),  /* Prescaler, divide by 256 */
    EVSYS_CHMUX_PRESCALER_512_gc = (0x89<<0),  /* Prescaler, divide by 512 */
    EVSYS_CHMUX_PRESCALER_1024_gc = (0x8A<<0),  /* Prescaler, divide by 1024 */
    EVSYS_CHMUX_PRESCALER_2048_gc = (0x8B<<0),  /* Prescaler, divide by 2048 */
    EVSYS_CHMUX_PRESCALER_4096_gc = (0x8C<<0),  /* Prescaler, divide by 4096 */
    EVSYS_CHMUX_PRESCALER_8192_gc = (0x8D<<0),  /* Prescaler, divide by 8192 */
    EVSYS_CHMUX_PRESCALER_16384_gc = (0x8E<<0),  /* Prescaler, divide by 16384 */
    EVSYS_CHMUX_PRESCALER_32768_gc = (0x8F<<0),  /* Prescaler, divide by 32768 */
    EVSYS_CHMUX_TCC0_OVF_gc = (0xC0<<0),  /* Timer/Counter C0 Overflow */
    EVSYS_CHMUX_TCC0_ERR_gc = (0xC1<<0),  /* Timer/Counter C0 Error */
    EVSYS_CHMUX_TCC0_CCA_gc = (0xC4<<0),  /* Timer/Counter C0 Compare or Capture A */
    EVSYS_CHMUX_TCC0_CCB_gc = (0xC5<<0),  /* Timer/Counter C0 Compare or Capture B */
    EVSYS_CHMUX_TCC0_CCC_gc = (0xC6<<0),  /* Timer/Counter C0 Compare or Capture C */
    EVSYS_CHMUX_TCC0_CCD_gc = (0xC7<<0),  /* Timer/Counter C0 Compare or Capture D */
    EVSYS_CHMUX_TCC1_OVF_gc = (0xC8<<0),  /* Timer/Counter C1 Overflow */
    EVSYS_CHMUX_TCC1_ERR_gc = (0xC9<<0),  /* Timer/Counter C1 Error */
    EVSYS_CHMUX_TCC1_CCA_gc = (0xCC<<0),  /* Timer/Counter C1 Compare or Capture A */
    EVSYS_CHMUX_TCC1_CCB_gc = (0xCD<<0),  /* Timer/Counter C1 Compare or Capture B */
    EVSYS_CHMUX_TCE0_OVF_gc = (0xE0<<0),  /* Timer/Counter E0 Overflow */
    EVSYS_CHMUX_TCE0_ERR_gc = (0xE1<<0),  /* Timer/Counter E0 Error */
    EVSYS_CHMUX_TCE0_CCA_gc = (0xE4<<0),  /* Timer/Counter E0 Compare or Capture A */
    EVSYS_CHMUX_TCE0_CCB_gc = (0xE5<<0),  /* Timer/Counter E0 Compare or Capture B */
    EVSYS_CHMUX_TCE0_CCC_gc = (0xE6<<0),  /* Timer/Counter E0 Compare or Capture C */
    EVSYS_CHMUX_TCE0_CCD_gc = (0xE7<<0),  /* Timer/Counter E0 Compare or Capture D */
} EVSYS_CHMUX_t;


/*
--------------------------------------------------------------------------
NVM - Non Volatile Memory Controller
--------------------------------------------------------------------------
*/

/* Non-volatile Memory Controller */
typedef struct NVM_struct
{
    register8_t ADDR0;  /* Address Register 0 */
    register8_t ADDR1;  /* Address Register 1 */
    register8_t ADDR2;  /* Address Register 2 */
    register8_t reserved_0x03;
    register8_t DATA0;  /* Data Register 0 */
    register8_t DATA1;  /* Data Register 1 */
    register8_t DATA2;  /* Data Register 2 */
    register8_t reserved_0x07;
    register8_t reserved_0x08;
    register8_t reserved_0x09;
    register8_t CMD;  /* Command */
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t INTCTRL;  /* Interrupt Control */
    register8_t reserved_0x0E;
    register8_t STATUS;  /* Status */
    register8_t LOCK_BITS;  /* Lock Bits (Changed from LOCKBITS to avoid avr-libc collision) */
} NVM_t;

/* NVM Command */
typedef enum NVM_CMD_enum
{
    NVM_CMD_NO_OPERATION_gc = (0x00<<0),  /* Noop/Ordinary LPM */
    NVM_CMD_READ_USER_SIG_ROW_gc = (0x01<<0),  /* Read user signature row */
    NVM_CMD_READ_CALIB_ROW_gc = (0x02<<0),  /* Read calibration row */
    NVM_CMD_READ_EEPROM_gc = (0x06<<0),  /* Read EEPROM */
    NVM_CMD_READ_FUSES_gc = (0x07<<0),  /* Read fuse byte */
    NVM_CMD_WRITE_LOCK_BITS_gc = (0x08<<0),  /* Write lock bits */
    NVM_CMD_ERASE_USER_SIG_ROW_gc = (0x18<<0),  /* Erase user signature row */
    NVM_CMD_WRITE_USER_SIG_ROW_gc = (0x1A<<0),  /* Write user signature row */
    NVM_CMD_ERASE_APP_gc = (0x20<<0),  /* Erase Application Section */
    NVM_CMD_ERASE_APP_PAGE_gc = (0x22<<0),  /* Erase Application Section page */
    NVM_CMD_LOAD_FLASH_BUFFER_gc = (0x23<<0),  /* Load Flash page buffer */
    NVM_CMD_WRITE_APP_PAGE_gc = (0x24<<0),  /* Write Application Section page */
    NVM_CMD_ERASE_WRITE_APP_PAGE_gc = (0x25<<0),  /* Erase-and-write Application Section page */
    NVM_CMD_ERASE_FLASH_BUFFER_gc = (0x26<<0),  /* Erase/flush Flash page buffer */
    NVM_CMD_ERASE_BOOT_PAGE_gc = (0x2A<<0),  /* Erase Boot Section page */
    NVM_CMD_ERASE_FLASH_PAGE_gc = (0x2B<<0),  /* Erase Flash Page */
    NVM_CMD_WRITE_BOOT_PAGE_gc = (0x2C<<0),  /* Write Boot Section page */
    NVM_CMD_ERASE_WRITE_BOOT_PAGE_gc = (0x2D<<0),  /* Erase-and-write Boot Section page */
    NVM_CMD_WRITE_FLASH_PAGE_gc = (0x2E<<0),  /* Write Flash Page */
    NVM_CMD_ERASE_WRITE_FLASH_PAGE_gc = (0x2F<<0),  /* Erase-and-write Flash Page */
    NVM_CMD_ERASE_EEPROM_gc = (0x30<<0),  /* Erase EEPROM */
    NVM_CMD_ERASE_EEPROM_PAGE_gc = (0x32<<0),  /* Erase EEPROM page */
    NVM_CMD_LOAD_EEPROM_BUFFER_gc = (0x33<<0),  /* Load EEPROM page buffer */
    NVM_CMD_WRITE_EEPROM_PAGE_gc = (0x34<<0),  /* Write EEPROM page */
    NVM_CMD_ERASE_WRITE_EEPROM_PAGE_gc = (0x35<<0),  /* Erase-and-write EEPROM page */
    NVM_CMD_ERASE_EEPROM_BUFFER_gc = (0x36<<0),  /* Erase/flush EEPROM page buffer */
    NVM_CMD_APP_CRC_gc = (0x38<<0),  /* Application section CRC */
    NVM_CMD_BOOT_CRC_gc = (0x39<<0),  /*  Boot Section CRC */
    NVM_CMD_FLASH_RANGE_CRC_gc = (0x3A<<0),  /* Flash Range CRC */
    NVM_CMD_CHIP_ERASE_gc = (0x40<<0),  /* Erase Chip */
    NVM_CMD_READ_NVM_gc = (0x43<<0),  /* Read NVM */
    NVM_CMD_WRITE_FUSE_gc = (0x4C<<0),  /* Write Fuse byte */
    NVM_CMD_ERASE_BOOT_gc = (0x68<<0),  /* Erase Boot Section */
    NVM_CMD_FLASH_CRC_gc = (0x78<<0),  /* Flash CRC */
} NVM_CMD_t;

/* SPM ready interrupt level */
typedef enum NVM_SPMLVL_enum
{
    NVM_SPMLVL_OFF_gc = (0x00<<2),  /* Interrupt disabled */
    NVM_SPMLVL_LO_gc = (0x01<<2),  /* Low level */
    NVM_SPMLVL_MED_gc = (0x02<<2),  /* Medium level */
    NVM_SPMLVL_HI_gc = (0x03<<2),  /* High level */
} NVM_SPMLVL_t;

/* EEPROM ready interrupt level */
typedef enum NVM_EELVL_enum
{
    NVM_EELVL_OFF_gc = (0x00<<0),  /* Interrupt disabled */
    NVM_EELVL_LO_gc = (0x01<<0),  /* Low level */
    NVM_EELVL_MED_gc = (0x02<<0),  /* Medium level */
    NVM_EELVL_HI_gc = (0x03<<0),  /* High level */
} NVM_EELVL_t;

/* Boot lock bits - boot setcion */
typedef enum NVM_BLBB_enum
{
    NVM_BLBB_RWLOCK_gc = (0x00<<6),  /* Read and write not allowed */
    NVM_BLBB_RLOCK_gc = (0x01<<6),  /* Read not allowed */
    NVM_BLBB_WLOCK_gc = (0x02<<6),  /* Write not allowed */
    NVM_BLBB_NOLOCK_gc = (0x03<<6),  /* No locks */
} NVM_BLBB_t;

/* Boot lock bits - application section */
typedef enum NVM_BLBA_enum
{
    NVM_BLBA_RWLOCK_gc = (0x00<<4),  /* Read and write not allowed */
    NVM_BLBA_RLOCK_gc = (0x01<<4),  /* Read not allowed */
    NVM_BLBA_WLOCK_gc = (0x02<<4),  /* Write not allowed */
    NVM_BLBA_NOLOCK_gc = (0x03<<4),  /* No locks */
} NVM_BLBA_t;

/* Boot lock bits - application table section */
typedef enum NVM_BLBAT_enum
{
    NVM_BLBAT_RWLOCK_gc = (0x00<<2),  /* Read and write not allowed */
    NVM_BLBAT_RLOCK_gc = (0x01<<2),  /* Read not allowed */
    NVM_BLBAT_WLOCK_gc = (0x02<<2),  /* Write not allowed */
    NVM_BLBAT_NOLOCK_gc = (0x03<<2),  /* No locks */
} NVM_BLBAT_t;

/* Lock bits */
typedef enum NVM_LB_enum
{
    NVM_LB_RWLOCK_gc = (0x00<<0),  /* Read and write not allowed */
    NVM_LB_WLOCK_gc = (0x02<<0),  /* Write not allowed */
    NVM_LB_NOLOCK_gc = (0x03<<0),  /* No locks */
} NVM_LB_t;


/*
--------------------------------------------------------------------------
ADC - Analog/Digital Converter
--------------------------------------------------------------------------
*/

/* ADC Channel */
typedef struct ADC_CH_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t MUXCTRL;  /* MUX Control */
    register8_t INTCTRL;  /* Channel Interrupt Control Register */
    register8_t INTFLAGS;  /* Interrupt Flags */
    _WORDREGISTER(RES);  /* Channel Result */
    register8_t SCAN;  /* Input Channel Scan */
    register8_t reserved_0x07;
} ADC_CH_t;


/* Analog-to-Digital Converter */
typedef struct ADC_struct
{
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t REFCTRL;  /* Reference Control */
    register8_t EVCTRL;  /* Event Control */
    register8_t PRESCALER;  /* Clock Prescaler */
    register8_t reserved_0x05;
    register8_t INTFLAGS;  /* Interrupt Flags */
    register8_t TEMP;  /* Temporary Register */
    register8_t SAMPCTRL;  /* ADC Sampling Time Control Register */
    register8_t reserved_0x09;
    register8_t reserved_0x0A;
    register8_t reserved_0x0B;
    _WORDREGISTER(CAL);  /* Calibration Value */
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
    _WORDREGISTER(CH0RES);  /* Channel 0 Result */
    register8_t reserved_0x12;
    register8_t reserved_0x13;
    register8_t reserved_0x14;
    register8_t reserved_0x15;
    register8_t reserved_0x16;
    register8_t reserved_0x17;
    _WORDREGISTER(CMP);  /* Compare Value */
    register8_t reserved_0x1A;
    register8_t reserved_0x1B;
    register8_t reserved_0x1C;
    register8_t reserved_0x1D;
    register8_t reserved_0x1E;
    register8_t reserved_0x1F;
    ADC_CH_t CH0;  /* ADC Channel 0 */
} ADC_t;

/* Current Limitation */
typedef enum ADC_CURRLIMIT_enum
{
    ADC_CURRLIMIT_NO_gc = (0x00<<5),  /* No current limit,     300ksps max sampling rate */
    ADC_CURRLIMIT_LOW_gc = (0x01<<5),  /* Low current limit,    250ksps max sampling rate */
    ADC_CURRLIMIT_MED_gc = (0x02<<5),  /* Medium current limit, 150ksps max sampling rate */
    ADC_CURRLIMIT_HIGH_gc = (0x03<<5),  /* High current limit,   50ksps max sampling rate */
} ADC_CURRLIMIT_t;

/* Positive input multiplexer selection */
typedef enum ADC_CH_MUXPOS_enum
{
    ADC_CH_MUXPOS_PIN0_gc = (0x00<<3),  /* Input pin 0 */
    ADC_CH_MUXPOS_PIN1_gc = (0x01<<3),  /* Input pin 1 */
    ADC_CH_MUXPOS_PIN2_gc = (0x02<<3),  /* Input pin 2 */
    ADC_CH_MUXPOS_PIN3_gc = (0x03<<3),  /* Input pin 3 */
    ADC_CH_MUXPOS_PIN4_gc = (0x04<<3),  /* Input pin 4 */
    ADC_CH_MUXPOS_PIN5_gc = (0x05<<3),  /* Input pin 5 */
    ADC_CH_MUXPOS_PIN6_gc = (0x06<<3),  /* Input pin 6 */
    ADC_CH_MUXPOS_PIN7_gc = (0x07<<3),  /* Input pin 7 */
    ADC_CH_MUXPOS_PIN8_gc = (0x08<<3),  /* Input pin 8 */
    ADC_CH_MUXPOS_PIN9_gc = (0x09<<3),  /* Input pin 9 */
    ADC_CH_MUXPOS_PIN10_gc = (0x0A<<3),  /* Input pin 10 */
    ADC_CH_MUXPOS_PIN11_gc = (0x0B<<3),  /* Input pin 11 */
    ADC_CH_MUXPOS_PIN12_gc = (0x0C<<3),  /* Input pin 12 */
    ADC_CH_MUXPOS_PIN13_gc = (0x0D<<3),  /* Input pin 13 */
    ADC_CH_MUXPOS_PIN14_gc = (0x0E<<3),  /* Input pin 14 */
    ADC_CH_MUXPOS_PIN15_gc = (0x0F<<3),  /* Input pin 15 */
} ADC_CH_MUXPOS_t;

/* Internal input multiplexer selections */
typedef enum ADC_CH_MUXINT_enum
{
    ADC_CH_MUXINT_TEMP_gc = (0x00<<3),  /* Temperature Reference */
    ADC_CH_MUXINT_BANDGAP_gc = (0x01<<3),  /* Bandgap Reference */
    ADC_CH_MUXINT_SCALEDVCC_gc = (0x02<<3),  /* 1/10 scaled VCC */
} ADC_CH_MUXINT_t;

/* Negative input multiplexer selection */
typedef enum ADC_CH_MUXNEG_enum
{
    ADC_CH_MUXNEG_PIN0_gc = (0x00<<0),  /* Input pin 0 */
    ADC_CH_MUXNEG_PIN1_gc = (0x01<<0),  /* Input pin 1 */
    ADC_CH_MUXNEG_PIN2_gc = (0x02<<0),  /* Input pin 2 */
    ADC_CH_MUXNEG_PIN3_gc = (0x03<<0),  /* Input pin 3 */
    ADC_CH_MUXNEG_PIN4_gc = (0x00<<0),  /* Input pin 4 */
    ADC_CH_MUXNEG_PIN5_gc = (0x01<<0),  /* Input pin 5 */
    ADC_CH_MUXNEG_PIN6_gc = (0x02<<0),  /* Input pin 6 */
    ADC_CH_MUXNEG_PIN7_gc = (0x03<<0),  /* Input pin 7 */
} ADC_CH_MUXNEG_t;

/* Input mode */
typedef enum ADC_CH_INPUTMODE_enum
{
    ADC_CH_INPUTMODE_INTERNAL_gc = (0x00<<0),  /* Internal inputs, no gain */
    ADC_CH_INPUTMODE_SINGLEENDED_gc = (0x01<<0),  /* Single-ended input, no gain */
    ADC_CH_INPUTMODE_DIFF_gc = (0x02<<0),  /* Differential input, no gain */
    ADC_CH_INPUTMODE_DIFFWGAIN_gc = (0x03<<0),  /* Differential input, with gain */
} ADC_CH_INPUTMODE_t;

/* Gain factor */
typedef enum ADC_CH_GAIN_enum
{
    ADC_CH_GAIN_1X_gc = (0x00<<2),  /* 1x gain */
    ADC_CH_GAIN_2X_gc = (0x01<<2),  /* 2x gain */
    ADC_CH_GAIN_4X_gc = (0x02<<2),  /* 4x gain */
    ADC_CH_GAIN_8X_gc = (0x03<<2),  /* 8x gain */
    ADC_CH_GAIN_16X_gc = (0x04<<2),  /* 16x gain */
    ADC_CH_GAIN_32X_gc = (0x05<<2),  /* 32x gain */
    ADC_CH_GAIN_64X_gc = (0x06<<2),  /* 64x gain */
    ADC_CH_GAIN_DIV2_gc = (0x07<<2),  /* x/2 gain */
} ADC_CH_GAIN_t;

/* Conversion result resolution */
typedef enum ADC_RESOLUTION_enum
{
    ADC_RESOLUTION_12BIT_gc = (0x00<<1),  /* 12-bit right-adjusted result */
    ADC_RESOLUTION_8BIT_gc = (0x02<<1),  /* 8-bit right-adjusted result */
    ADC_RESOLUTION_LEFT12BIT_gc = (0x03<<1),  /* 12-bit left-adjusted result */
} ADC_RESOLUTION_t;

/* Voltage reference selection */
typedef enum ADC_REFSEL_enum
{
    ADC_REFSEL_INT1V_gc = (0x00<<4),  /* Internal 1V */
    ADC_REFSEL_INTVCC_gc = (0x01<<4),  /* Internal VCC / 1.6 */
    ADC_REFSEL_AREFA_gc = (0x02<<4),  /* External reference on PORT A */
    ADC_REFSEL_AREFB_gc = (0x03<<4),  /* External reference on PORT B */
    ADC_REFSEL_INTVCC2_gc = (0x04<<4),  /* Internal VCC / 2 */
} ADC_REFSEL_t;

/* Event channel input selection */
typedef enum ADC_EVSEL_enum
{
    ADC_EVSEL_0_gc = (0x00<<3),  /* Event Channel 0 */
    ADC_EVSEL_1_gc = (0x01<<3),  /* Event Channel 1 */
    ADC_EVSEL_2_gc = (0x02<<3),  /* Event Channel 2 */
    ADC_EVSEL_3_gc = (0x03<<3),  /* Event Channel 3 */
} ADC_EVSEL_t;

/* Event action selection */
typedef enum ADC_EVACT_enum
{
    ADC_EVACT_NONE_gc = (0x00<<0),  /* No event action */
    ADC_EVACT_CH0_gc = (0x01<<0),  /* First event triggers channel 0 */
    ADC_EVACT_SYNCSWEEP_gc = (0x06<<0),  /* The ADC is flushed and restarted for accurate timing */
} ADC_EVACT_t;

/* Interupt mode */
typedef enum ADC_CH_INTMODE_enum
{
    ADC_CH_INTMODE_COMPLETE_gc = (0x00<<2),  /* Interrupt on conversion complete */
    ADC_CH_INTMODE_BELOW_gc = (0x01<<2),  /* Interrupt on result below compare value */
    ADC_CH_INTMODE_ABOVE_gc = (0x03<<2),  /* Interrupt on result above compare value */
} ADC_CH_INTMODE_t;

/* Interrupt level */
typedef enum ADC_CH_INTLVL_enum
{
    ADC_CH_INTLVL_OFF_gc = (0x00<<0),  /* Interrupt disabled */
    ADC_CH_INTLVL_LO_gc = (0x01<<0),  /* Low level */
    ADC_CH_INTLVL_MED_gc = (0x02<<0),  /* Medium level */
    ADC_CH_INTLVL_HI_gc = (0x03<<0),  /* High level */
} ADC_CH_INTLVL_t;

/* Clock prescaler */
typedef enum ADC_PRESCALER_enum
{
    ADC_PRESCALER_DIV4_gc = (0x00<<0),  /* Divide clock by 4 */
    ADC_PRESCALER_DIV8_gc = (0x01<<0),  /* Divide clock by 8 */
    ADC_PRESCALER_DIV16_gc = (0x02<<0),  /* Divide clock by 16 */
    ADC_PRESCALER_DIV32_gc = (0x03<<0),  /* Divide clock by 32 */
    ADC_PRESCALER_DIV64_gc = (0x04<<0),  /* Divide clock by 64 */
    ADC_PRESCALER_DIV128_gc = (0x05<<0),  /* Divide clock by 128 */
    ADC_PRESCALER_DIV256_gc = (0x06<<0),  /* Divide clock by 256 */
    ADC_PRESCALER_DIV512_gc = (0x07<<0),  /* Divide clock by 512 */
} ADC_PRESCALER_t;


/*
--------------------------------------------------------------------------
AC - Analog Comparator
--------------------------------------------------------------------------
*/

/* Analog Comparator */
typedef struct AC_struct
{
    register8_t AC0CTRL;  /* Analog Comparator 0 Control */
    register8_t AC1CTRL;  /* Analog Comparator 1 Control */
    register8_t AC0MUXCTRL;  /* Analog Comparator 0 MUX Control */
    register8_t AC1MUXCTRL;  /* Analog Comparator 1 MUX Control */
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t WINCTRL;  /* Window Mode Control */
    register8_t STATUS;  /* Status */
    register8_t CURRCTRL;  /* Current Source Control Register */
    register8_t CURRCALIB;  /* Current Source Calibration Register */
} AC_t;

/* Interrupt mode */
typedef enum AC_INTMODE_enum
{
    AC_INTMODE_BOTHEDGES_gc = (0x00<<6),  /* Interrupt on both edges */
    AC_INTMODE_FALLING_gc = (0x02<<6),  /* Interrupt on falling edge */
    AC_INTMODE_RISING_gc = (0x03<<6),  /* Interrupt on rising edge */
} AC_INTMODE_t;

/* Interrupt level */
typedef enum AC_INTLVL_enum
{
    AC_INTLVL_OFF_gc = (0x00<<4),  /* Interrupt disabled */
    AC_INTLVL_LO_gc = (0x01<<4),  /* Low level */
    AC_INTLVL_MED_gc = (0x02<<4),  /* Medium level */
    AC_INTLVL_HI_gc = (0x03<<4),  /* High level */
} AC_INTLVL_t;

/* Hysteresis mode selection */
typedef enum AC_HYSMODE_enum
{
    AC_HYSMODE_NO_gc = (0x00<<1),  /* No hysteresis */
    AC_HYSMODE_SMALL_gc = (0x01<<1),  /* Small hysteresis */
    AC_HYSMODE_LARGE_gc = (0x02<<1),  /* Large hysteresis */
} AC_HYSMODE_t;

/* Positive input multiplexer selection */
typedef enum AC_MUXPOS_enum
{
    AC_MUXPOS_PIN0_gc = (0x00<<3),  /* Pin 0 */
    AC_MUXPOS_PIN1_gc = (0x01<<3),  /* Pin 1 */
    AC_MUXPOS_PIN2_gc = (0x02<<3),  /* Pin 2 */
    AC_MUXPOS_PIN3_gc = (0x03<<3),  /* Pin 3 */
    AC_MUXPOS_PIN4_gc = (0x04<<3),  /* Pin 4 */
    AC_MUXPOS_PIN5_gc = (0x05<<3),  /* Pin 5 */
    AC_MUXPOS_PIN6_gc = (0x06<<3),  /* Pin 6 */
} AC_MUXPOS_t;

/* Negative input multiplexer selection */
typedef enum AC_MUXNEG_enum
{
    AC_MUXNEG_PIN0_gc = (0x00<<0),  /* Pin 0 */
    AC_MUXNEG_PIN1_gc = (0x01<<0),  /* Pin 1 */
    AC_MUXNEG_PIN3_gc = (0x02<<0),  /* Pin 3 */
    AC_MUXNEG_PIN5_gc = (0x03<<0),  /* Pin 5 */
    AC_MUXNEG_PIN7_gc = (0x04<<0),  /* Pin 7 */
    AC_MUXNEG_BANDGAP_gc = (0x06<<0),  /* Bandgap Reference */
    AC_MUXNEG_SCALER_gc = (0x07<<0),  /* Internal voltage scaler */
} AC_MUXNEG_t;

/* Windows interrupt mode */
typedef enum AC_WINTMODE_enum
{
    AC_WINTMODE_ABOVE_gc = (0x00<<2),  /* Interrupt on above window */
    AC_WINTMODE_INSIDE_gc = (0x01<<2),  /* Interrupt on inside window */
    AC_WINTMODE_BELOW_gc = (0x02<<2),  /* Interrupt on below window */
    AC_WINTMODE_OUTSIDE_gc = (0x03<<2),  /* Interrupt on outside window */
} AC_WINTMODE_t;

/* Window interrupt level */
typedef enum AC_WINTLVL_enum
{
    AC_WINTLVL_OFF_gc = (0x00<<0),  /* Interrupt disabled */
    AC_WINTLVL_LO_gc = (0x01<<0),  /* Low priority */
    AC_WINTLVL_MED_gc = (0x02<<0),  /* Medium priority */
    AC_WINTLVL_HI_gc = (0x03<<0),  /* High priority */
} AC_WINTLVL_t;

/* Window mode state */
typedef enum AC_WSTATE_enum
{
    AC_WSTATE_ABOVE_gc = (0x00<<6),  /* Signal above window */
    AC_WSTATE_INSIDE_gc = (0x01<<6),  /* Signal inside window */
    AC_WSTATE_BELOW_gc = (0x02<<6),  /* Signal below window */
} AC_WSTATE_t;


/*
--------------------------------------------------------------------------
RTC - Real-Time Counter
--------------------------------------------------------------------------
*/

/* Real-Time Counter */
typedef struct RTC_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t STATUS;  /* Status Register */
    register8_t INTCTRL;  /* Interrupt Control Register */
    register8_t INTFLAGS;  /* Interrupt Flags */
    register8_t TEMP;  /* Temporary register */
    register8_t reserved_0x05;
    register8_t reserved_0x06;
    register8_t reserved_0x07;
    _WORDREGISTER(CNT);  /* Count Register */
    _WORDREGISTER(PER);  /* Period Register */
    _WORDREGISTER(COMP);  /* Compare Register */
} RTC_t;

/* Prescaler Factor */
typedef enum RTC_PRESCALER_enum
{
    RTC_PRESCALER_OFF_gc = (0x00<<0),  /* RTC Off */
    RTC_PRESCALER_DIV1_gc = (0x01<<0),  /* RTC Clock */
    RTC_PRESCALER_DIV2_gc = (0x02<<0),  /* RTC Clock / 2 */
    RTC_PRESCALER_DIV8_gc = (0x03<<0),  /* RTC Clock / 8 */
    RTC_PRESCALER_DIV16_gc = (0x04<<0),  /* RTC Clock / 16 */
    RTC_PRESCALER_DIV64_gc = (0x05<<0),  /* RTC Clock / 64 */
    RTC_PRESCALER_DIV256_gc = (0x06<<0),  /* RTC Clock / 256 */
    RTC_PRESCALER_DIV1024_gc = (0x07<<0),  /* RTC Clock / 1024 */
} RTC_PRESCALER_t;

/* Compare Interrupt level */
typedef enum RTC_COMPINTLVL_enum
{
    RTC_COMPINTLVL_OFF_gc = (0x00<<2),  /* Interrupt Disabled */
    RTC_COMPINTLVL_LO_gc = (0x01<<2),  /* Low Level */
    RTC_COMPINTLVL_MED_gc = (0x02<<2),  /* Medium Level */
    RTC_COMPINTLVL_HI_gc = (0x03<<2),  /* High Level */
} RTC_COMPINTLVL_t;

/* Overflow Interrupt level */
typedef enum RTC_OVFINTLVL_enum
{
    RTC_OVFINTLVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    RTC_OVFINTLVL_LO_gc = (0x01<<0),  /* Low Level */
    RTC_OVFINTLVL_MED_gc = (0x02<<0),  /* Medium Level */
    RTC_OVFINTLVL_HI_gc = (0x03<<0),  /* High Level */
} RTC_OVFINTLVL_t;


/*
--------------------------------------------------------------------------
TWI - Two-Wire Interface
--------------------------------------------------------------------------
*/

/*  */
typedef struct TWI_MASTER_struct
{
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t CTRLC;  /* Control Register C */
    register8_t STATUS;  /* Status Register */
    register8_t BAUD;  /* Baurd Rate Control Register */
    register8_t ADDR;  /* Address Register */
    register8_t DATA;  /* Data Register */
} TWI_MASTER_t;


/*  */
typedef struct TWI_SLAVE_struct
{
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t STATUS;  /* Status Register */
    register8_t ADDR;  /* Address Register */
    register8_t DATA;  /* Data Register */
    register8_t ADDRMASK;  /* Address Mask Register */
} TWI_SLAVE_t;


/* Two-Wire Interface */
typedef struct TWI_struct
{
    register8_t CTRL;  /* TWI Common Control Register */
    TWI_MASTER_t MASTER;  /* TWI master module */
    TWI_SLAVE_t SLAVE;  /* TWI slave module */
} TWI_t;

/* SDA Hold Time */
typedef enum TWI_SDAHOLD_enum
{
    TWI_SDAHOLD_OFF_gc = (0x00<<1),  /* SDA Hold Time off */
    TWI_SDAHOLD_50NS_gc = (0x01<<1),  /* SDA Hold Time 50 ns */
    TWI_SDAHOLD_300NS_gc = (0x02<<1),  /* SDA Hold Time 300 ns */
    TWI_SDAHOLD_400NS_gc = (0x03<<1),  /* SDA Hold Time 400 ns */
} TWI_SDAHOLD_t;

/* Master Interrupt Level */
typedef enum TWI_MASTER_INTLVL_enum
{
    TWI_MASTER_INTLVL_OFF_gc = (0x00<<6),  /* Interrupt Disabled */
    TWI_MASTER_INTLVL_LO_gc = (0x01<<6),  /* Low Level */
    TWI_MASTER_INTLVL_MED_gc = (0x02<<6),  /* Medium Level */
    TWI_MASTER_INTLVL_HI_gc = (0x03<<6),  /* High Level */
} TWI_MASTER_INTLVL_t;

/* Inactive Timeout */
typedef enum TWI_MASTER_TIMEOUT_enum
{
    TWI_MASTER_TIMEOUT_DISABLED_gc = (0x00<<2),  /* Bus Timeout Disabled */
    TWI_MASTER_TIMEOUT_50US_gc = (0x01<<2),  /* 50 Microseconds */
    TWI_MASTER_TIMEOUT_100US_gc = (0x02<<2),  /* 100 Microseconds */
    TWI_MASTER_TIMEOUT_200US_gc = (0x03<<2),  /* 200 Microseconds */
} TWI_MASTER_TIMEOUT_t;

/* Master Command */
typedef enum TWI_MASTER_CMD_enum
{
    TWI_MASTER_CMD_NOACT_gc = (0x00<<0),  /* No Action */
    TWI_MASTER_CMD_REPSTART_gc = (0x01<<0),  /* Issue Repeated Start Condition */
    TWI_MASTER_CMD_RECVTRANS_gc = (0x02<<0),  /* Receive or Transmit Data */
    TWI_MASTER_CMD_STOP_gc = (0x03<<0),  /* Issue Stop Condition */
} TWI_MASTER_CMD_t;

/* Master Bus State */
typedef enum TWI_MASTER_BUSSTATE_enum
{
    TWI_MASTER_BUSSTATE_UNKNOWN_gc = (0x00<<0),  /* Unknown Bus State */
    TWI_MASTER_BUSSTATE_IDLE_gc = (0x01<<0),  /* Bus is Idle */
    TWI_MASTER_BUSSTATE_OWNER_gc = (0x02<<0),  /* This Module Controls The Bus */
    TWI_MASTER_BUSSTATE_BUSY_gc = (0x03<<0),  /* The Bus is Busy */
} TWI_MASTER_BUSSTATE_t;

/* Slave Interrupt Level */
typedef enum TWI_SLAVE_INTLVL_enum
{
    TWI_SLAVE_INTLVL_OFF_gc = (0x00<<6),  /* Interrupt Disabled */
    TWI_SLAVE_INTLVL_LO_gc = (0x01<<6),  /* Low Level */
    TWI_SLAVE_INTLVL_MED_gc = (0x02<<6),  /* Medium Level */
    TWI_SLAVE_INTLVL_HI_gc = (0x03<<6),  /* High Level */
} TWI_SLAVE_INTLVL_t;

/* Slave Command */
typedef enum TWI_SLAVE_CMD_enum
{
    TWI_SLAVE_CMD_NOACT_gc = (0x00<<0),  /* No Action */
    TWI_SLAVE_CMD_COMPTRANS_gc = (0x02<<0),  /* Used To Complete a Transaction */
    TWI_SLAVE_CMD_RESPONSE_gc = (0x03<<0),  /* Used in Response to Address/Data Interrupt */
} TWI_SLAVE_CMD_t;


/*
--------------------------------------------------------------------------
USB - USB
--------------------------------------------------------------------------
*/

/* USB Endpoint */
typedef struct USB_EP_struct
{
    register8_t STATUS;  /* Endpoint Status */
    register8_t CTRL;  /* Endpoint Control */
    _WORDREGISTER(CNT);  /* USB Endpoint Counter */
    _WORDREGISTER(DATAPTR);  /* Data Pointer */
    _WORDREGISTER(AUXDATA);  /* Auxiliary Data */
} USB_EP_t;


/* Universal Serial Bus */
typedef struct USB_struct
{
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t STATUS;  /* Status Register */
    register8_t ADDR;  /* Address Register */
    register8_t FIFOWP;  /* FIFO Write Pointer Register */
    register8_t FIFORP;  /* FIFO Read Pointer Register */
    _WORDREGISTER(EPPTR);  /* Endpoint Configuration Table Pointer */
    register8_t INTCTRLA;  /* Interrupt Control Register A */
    register8_t INTCTRLB;  /* Interrupt Control Register B */
    register8_t INTFLAGSACLR;  /* Clear Interrupt Flag Register A */
    register8_t INTFLAGSASET;  /* Set Interrupt Flag Register A */
    register8_t INTFLAGSBCLR;  /* Clear Interrupt Flag Register B */
    register8_t INTFLAGSBSET;  /* Set Interrupt Flag Register B */
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
    register8_t reserved_0x10;
    register8_t reserved_0x11;
    register8_t reserved_0x12;
    register8_t reserved_0x13;
    register8_t reserved_0x14;
    register8_t reserved_0x15;
    register8_t reserved_0x16;
    register8_t reserved_0x17;
    register8_t reserved_0x18;
    register8_t reserved_0x19;
    register8_t reserved_0x1A;
    register8_t reserved_0x1B;
    register8_t reserved_0x1C;
    register8_t reserved_0x1D;
    register8_t reserved_0x1E;
    register8_t reserved_0x1F;
    register8_t reserved_0x20;
    register8_t reserved_0x21;
    register8_t reserved_0x22;
    register8_t reserved_0x23;
    register8_t reserved_0x24;
    register8_t reserved_0x25;
    register8_t reserved_0x26;
    register8_t reserved_0x27;
    register8_t reserved_0x28;
    register8_t reserved_0x29;
    register8_t reserved_0x2A;
    register8_t reserved_0x2B;
    register8_t reserved_0x2C;
    register8_t reserved_0x2D;
    register8_t reserved_0x2E;
    register8_t reserved_0x2F;
    register8_t reserved_0x30;
    register8_t reserved_0x31;
    register8_t reserved_0x32;
    register8_t reserved_0x33;
    register8_t reserved_0x34;
    register8_t reserved_0x35;
    register8_t reserved_0x36;
    register8_t reserved_0x37;
    register8_t reserved_0x38;
    register8_t reserved_0x39;
    register8_t CAL0;  /* Calibration Byte 0 */
    register8_t CAL1;  /* Calibration Byte 1 */
} USB_t;


/* USB Endpoint Table */
typedef struct USB_EP_TABLE_struct
{
    USB_EP_t EP0OUT;  /* Endpoint 0 */
    USB_EP_t EP0IN;  /* Endpoint 0 */
    USB_EP_t EP1OUT;  /* Endpoint 1 */
    USB_EP_t EP1IN;  /* Endpoint 1 */
    USB_EP_t EP2OUT;  /* Endpoint 2 */
    USB_EP_t EP2IN;  /* Endpoint 2 */
    USB_EP_t EP3OUT;  /* Endpoint 3 */
    USB_EP_t EP3IN;  /* Endpoint 3 */
    USB_EP_t EP4OUT;  /* Endpoint 4 */
    USB_EP_t EP4IN;  /* Endpoint 4 */
    USB_EP_t EP5OUT;  /* Endpoint 5 */
    USB_EP_t EP5IN;  /* Endpoint 5 */
    USB_EP_t EP6OUT;  /* Endpoint 6 */
    USB_EP_t EP6IN;  /* Endpoint 6 */
    USB_EP_t EP7OUT;  /* Endpoint 7 */
    USB_EP_t EP7IN;  /* Endpoint 7 */
    USB_EP_t EP8OUT;  /* Endpoint 8 */
    USB_EP_t EP8IN;  /* Endpoint 8 */
    USB_EP_t EP9OUT;  /* Endpoint 9 */
    USB_EP_t EP9IN;  /* Endpoint 9 */
    USB_EP_t EP10OUT;  /* Endpoint 10 */
    USB_EP_t EP10IN;  /* Endpoint 10 */
    USB_EP_t EP11OUT;  /* Endpoint 11 */
    USB_EP_t EP11IN;  /* Endpoint 11 */
    USB_EP_t EP12OUT;  /* Endpoint 12 */
    USB_EP_t EP12IN;  /* Endpoint 12 */
    USB_EP_t EP13OUT;  /* Endpoint 13 */
    USB_EP_t EP13IN;  /* Endpoint 13 */
    USB_EP_t EP14OUT;  /* Endpoint 14 */
    USB_EP_t EP14IN;  /* Endpoint 14 */
    USB_EP_t EP15OUT;  /* Endpoint 15 */
    USB_EP_t EP15IN;  /* Endpoint 15 */
    register8_t reserved_0x100;
    register8_t reserved_0x101;
    register8_t reserved_0x102;
    register8_t reserved_0x103;
    register8_t reserved_0x104;
    register8_t reserved_0x105;
    register8_t reserved_0x106;
    register8_t reserved_0x107;
    register8_t reserved_0x108;
    register8_t reserved_0x109;
    register8_t reserved_0x10A;
    register8_t reserved_0x10B;
    register8_t reserved_0x10C;
    register8_t reserved_0x10D;
    register8_t reserved_0x10E;
    register8_t reserved_0x10F;
    register8_t FRAMENUML;  /* Frame Number Low Byte */
    register8_t FRAMENUMH;  /* Frame Number High Byte */
} USB_EP_TABLE_t;

/* Interrupt level */
typedef enum USB_INTLVL_enum
{
    USB_INTLVL_OFF_gc = (0x00<<0),  /* Interrupt disabled */
    USB_INTLVL_LO_gc = (0x01<<0),  /* Low level */
    USB_INTLVL_MED_gc = (0x02<<0),  /* Medium level */
    USB_INTLVL_HI_gc = (0x03<<0),  /* High level */
} USB_INTLVL_t;

/* USB Endpoint Type */
typedef enum USB_EP_TYPE_enum
{
    USB_EP_TYPE_DISABLE_gc = (0x00<<6),  /* Endpoint Disabled */
    USB_EP_TYPE_CONTROL_gc = (0x01<<6),  /* Control */
    USB_EP_TYPE_BULK_gc = (0x02<<6),  /* Bulk/Interrupt */
    USB_EP_TYPE_ISOCHRONOUS_gc = (0x03<<6),  /* Isochronous */
} USB_EP_TYPE_t;

/* USB Endpoint Buffersize */
typedef enum USB_EP_BUFSIZE_enum
{
    USB_EP_BUFSIZE_8_gc = (0x00<<0),  /* 8 bytes buffer size */
    USB_EP_BUFSIZE_16_gc = (0x01<<0),  /* 16 bytes buffer size */
    USB_EP_BUFSIZE_32_gc = (0x02<<0),  /* 32 bytes buffer size */
    USB_EP_BUFSIZE_64_gc = (0x03<<0),  /* 64 bytes buffer size */
    USB_EP_BUFSIZE_128_gc = (0x04<<0),  /* 128 bytes buffer size */
    USB_EP_BUFSIZE_256_gc = (0x05<<0),  /* 256 bytes buffer size */
    USB_EP_BUFSIZE_512_gc = (0x06<<0),  /* 512 bytes buffer size */
    USB_EP_BUFSIZE_1023_gc = (0x07<<0),  /* 1023 bytes buffer size */
} USB_EP_BUFSIZE_t;


/*
--------------------------------------------------------------------------
PORT - I/O Port Configuration
--------------------------------------------------------------------------
*/

/* I/O Ports */
typedef struct PORT_struct
{
    register8_t DIR;  /* I/O Port Data Direction */
    register8_t DIRSET;  /* I/O Port Data Direction Set */
    register8_t DIRCLR;  /* I/O Port Data Direction Clear */
    register8_t DIRTGL;  /* I/O Port Data Direction Toggle */
    register8_t OUT;  /* I/O Port Output */
    register8_t OUTSET;  /* I/O Port Output Set */
    register8_t OUTCLR;  /* I/O Port Output Clear */
    register8_t OUTTGL;  /* I/O Port Output Toggle */
    register8_t IN;  /* I/O port Input */
    register8_t INTCTRL;  /* Interrupt Control Register */
    register8_t INT0MASK;  /* Port Interrupt 0 Mask */
    register8_t INT1MASK;  /* Port Interrupt 1 Mask */
    register8_t INTFLAGS;  /* Interrupt Flag Register */
    register8_t reserved_0x0D;
    register8_t REMAP;  /* I/O Port Pin Remap Register */
    register8_t reserved_0x0F;
    register8_t PIN0CTRL;  /* Pin 0 Control Register */
    register8_t PIN1CTRL;  /* Pin 1 Control Register */
    register8_t PIN2CTRL;  /* Pin 2 Control Register */
    register8_t PIN3CTRL;  /* Pin 3 Control Register */
    register8_t PIN4CTRL;  /* Pin 4 Control Register */
    register8_t PIN5CTRL;  /* Pin 5 Control Register */
    register8_t PIN6CTRL;  /* Pin 6 Control Register */
    register8_t PIN7CTRL;  /* Pin 7 Control Register */
} PORT_t;

/* Port Interrupt 0 Level */
typedef enum PORT_INT0LVL_enum
{
    PORT_INT0LVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    PORT_INT0LVL_LO_gc = (0x01<<0),  /* Low Level */
    PORT_INT0LVL_MED_gc = (0x02<<0),  /* Medium Level */
    PORT_INT0LVL_HI_gc = (0x03<<0),  /* High Level */
} PORT_INT0LVL_t;

/* Port Interrupt 1 Level */
typedef enum PORT_INT1LVL_enum
{
    PORT_INT1LVL_OFF_gc = (0x00<<2),  /* Interrupt Disabled */
    PORT_INT1LVL_LO_gc = (0x01<<2),  /* Low Level */
    PORT_INT1LVL_MED_gc = (0x02<<2),  /* Medium Level */
    PORT_INT1LVL_HI_gc = (0x03<<2),  /* High Level */
} PORT_INT1LVL_t;

/* Output/Pull Configuration */
typedef enum PORT_OPC_enum
{
    PORT_OPC_TOTEM_gc = (0x00<<3),  /* Totempole */
    PORT_OPC_BUSKEEPER_gc = (0x01<<3),  /* Totempole w/ Bus keeper on Input and Output */
    PORT_OPC_PULLDOWN_gc = (0x02<<3),  /* Totempole w/ Pull-down on Input */
    PORT_OPC_PULLUP_gc = (0x03<<3),  /* Totempole w/ Pull-up on Input */
    PORT_OPC_WIREDOR_gc = (0x04<<3),  /* Wired OR */
    PORT_OPC_WIREDAND_gc = (0x05<<3),  /* Wired AND */
    PORT_OPC_WIREDORPULL_gc = (0x06<<3),  /* Wired OR w/ Pull-down */
    PORT_OPC_WIREDANDPULL_gc = (0x07<<3),  /* Wired AND w/ Pull-up */
} PORT_OPC_t;

/* Input/Sense Configuration */
typedef enum PORT_ISC_enum
{
    PORT_ISC_BOTHEDGES_gc = (0x00<<0),  /* Sense Both Edges */
    PORT_ISC_RISING_gc = (0x01<<0),  /* Sense Rising Edge */
    PORT_ISC_FALLING_gc = (0x02<<0),  /* Sense Falling Edge */
    PORT_ISC_LEVEL_gc = (0x03<<0),  /* Sense Level (Transparent For Events) */
    PORT_ISC_INPUT_DISABLE_gc = (0x07<<0),  /* Disable Digital Input Buffer */
} PORT_ISC_t;


/*
--------------------------------------------------------------------------
TC - 16-bit Timer/Counter With PWM
--------------------------------------------------------------------------
*/

/* 16-bit Timer/Counter 0 */
typedef struct TC0_struct
{
    register8_t CTRLA;  /* Control  Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t CTRLC;  /* Control register C */
    register8_t CTRLD;  /* Control Register D */
    register8_t CTRLE;  /* Control Register E */
    register8_t reserved_0x05;
    register8_t INTCTRLA;  /* Interrupt Control Register A */
    register8_t INTCTRLB;  /* Interrupt Control Register B */
    register8_t CTRLFCLR;  /* Control Register F Clear */
    register8_t CTRLFSET;  /* Control Register F Set */
    register8_t CTRLGCLR;  /* Control Register G Clear */
    register8_t CTRLGSET;  /* Control Register G Set */
    register8_t INTFLAGS;  /* Interrupt Flag Register */
    register8_t reserved_0x0D;
    register8_t reserved_0x0E;
    register8_t TEMP;  /* Temporary Register For 16-bit Access */
    register8_t reserved_0x10;
    register8_t reserved_0x11;
    register8_t reserved_0x12;
    register8_t reserved_0x13;
    register8_t reserved_0x14;
    register8_t reserved_0x15;
    register8_t reserved_0x16;
    register8_t reserved_0x17;
    register8_t reserved_0x18;
    register8_t reserved_0x19;
    register8_t reserved_0x1A;
    register8_t reserved_0x1B;
    register8_t reserved_0x1C;
    register8_t reserved_0x1D;
    register8_t reserved_0x1E;
    register8_t reserved_0x1F;
    _WORDREGISTER(CNT);  /* Count */
    register8_t reserved_0x22;
    register8_t reserved_0x23;
    register8_t reserved_0x24;
    register8_t reserved_0x25;
    _WORDREGISTER(PER);  /* Period */
    _WORDREGISTER(CCA);  /* Compare or Capture A */
    _WORDREGISTER(CCB);  /* Compare or Capture B */
    _WORDREGISTER(CCC);  /* Compare or Capture C */
    _WORDREGISTER(CCD);  /* Compare or Capture D */
    register8_t reserved_0x30;
    register8_t reserved_0x31;
    register8_t reserved_0x32;
    register8_t reserved_0x33;
    register8_t reserved_0x34;
    register8_t reserved_0x35;
    _WORDREGISTER(PERBUF);  /* Period Buffer */
    _WORDREGISTER(CCABUF);  /* Compare Or Capture A Buffer */
    _WORDREGISTER(CCBBUF);  /* Compare Or Capture B Buffer */
    _WORDREGISTER(CCCBUF);  /* Compare Or Capture C Buffer */
    _WORDREGISTER(CCDBUF);  /* Compare Or Capture D Buffer */
} TC0_t;


/* 16-bit Timer/Counter 1 */
typedef struct TC1_struct
{
    register8_t CTRLA;  /* Control  Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t CTRLC;  /* Control register C */
    register8_t CTRLD;  /* Control Register D */
    register8_t CTRLE;  /* Control Register E */
    register8_t reserved_0x05;
    register8_t INTCTRLA;  /* Interrupt Control Register A */
    register8_t INTCTRLB;  /* Interrupt Control Register B */
    register8_t CTRLFCLR;  /* Control Register F Clear */
    register8_t CTRLFSET;  /* Control Register F Set */
    register8_t CTRLGCLR;  /* Control Register G Clear */
    register8_t CTRLGSET;  /* Control Register G Set */
    register8_t INTFLAGS;  /* Interrupt Flag Register */
    register8_t reserved_0x0D;
    register8_t reserved_0x0E;
    register8_t TEMP;  /* Temporary Register For 16-bit Access */
    register8_t reserved_0x10;
    register8_t reserved_0x11;
    register8_t reserved_0x12;
    register8_t reserved_0x13;
    register8_t reserved_0x14;
    register8_t reserved_0x15;
    register8_t reserved_0x16;
    register8_t reserved_0x17;
    register8_t reserved_0x18;
    register8_t reserved_0x19;
    register8_t reserved_0x1A;
    register8_t reserved_0x1B;
    register8_t reserved_0x1C;
    register8_t reserved_0x1D;
    register8_t reserved_0x1E;
    register8_t reserved_0x1F;
    _WORDREGISTER(CNT);  /* Count */
    register8_t reserved_0x22;
    register8_t reserved_0x23;
    register8_t reserved_0x24;
    register8_t reserved_0x25;
    _WORDREGISTER(PER);  /* Period */
    _WORDREGISTER(CCA);  /* Compare or Capture A */
    _WORDREGISTER(CCB);  /* Compare or Capture B */
    register8_t reserved_0x2C;
    register8_t reserved_0x2D;
    register8_t reserved_0x2E;
    register8_t reserved_0x2F;
    register8_t reserved_0x30;
    register8_t reserved_0x31;
    register8_t reserved_0x32;
    register8_t reserved_0x33;
    register8_t reserved_0x34;
    register8_t reserved_0x35;
    _WORDREGISTER(PERBUF);  /* Period Buffer */
    _WORDREGISTER(CCABUF);  /* Compare Or Capture A Buffer */
    _WORDREGISTER(CCBBUF);  /* Compare Or Capture B Buffer */
} TC1_t;

/* Clock Selection */
typedef enum TC_CLKSEL_enum
{
    TC_CLKSEL_OFF_gc = (0x00<<0),  /* Timer Off */
    TC_CLKSEL_DIV1_gc = (0x01<<0),  /* System Clock */
    TC_CLKSEL_DIV2_gc = (0x02<<0),  /* System Clock / 2 */
    TC_CLKSEL_DIV4_gc = (0x03<<0),  /* System Clock / 4 */
    TC_CLKSEL_DIV8_gc = (0x04<<0),  /* System Clock / 8 */
    TC_CLKSEL_DIV64_gc = (0x05<<0),  /* System Clock / 64 */
    TC_CLKSEL_DIV256_gc = (0x06<<0),  /* System Clock / 256 */
    TC_CLKSEL_DIV1024_gc = (0x07<<0),  /* System Clock / 1024 */
    TC_CLKSEL_EVCH0_gc = (0x08<<0),  /* Event Channel 0 */
    TC_CLKSEL_EVCH1_gc = (0x09<<0),  /* Event Channel 1 */
    TC_CLKSEL_EVCH2_gc = (0x0A<<0),  /* Event Channel 2 */
    TC_CLKSEL_EVCH3_gc = (0x0B<<0),  /* Event Channel 3 */
} TC_CLKSEL_t;

/* Waveform Generation Mode */
typedef enum TC_WGMODE_enum
{
    TC_WGMODE_NORMAL_gc = (0x00<<0),  /* Normal Mode */
    TC_WGMODE_FRQ_gc = (0x01<<0),  /* Frequency Generation Mode */
    TC_WGMODE_SINGLESLOPE_gc = (0x03<<0),  /* Single Slope */
    TC_WGMODE_SS_gc = (0x03<<0),  /* Single Slope */
    TC_WGMODE_DSTOP_gc = (0x05<<0),  /* Dual Slope, Update on TOP */
    TC_WGMODE_DS_T_gc = (0x05<<0),  /* Dual Slope, Update on TOP */
    TC_WGMODE_DSBOTH_gc = (0x06<<0),  /* Dual Slope, Update on both TOP and BOTTOM */
    TC_WGMODE_DS_TB_gc = (0x06<<0),  /* Dual Slope, Update on both TOP and BOTTOM */
    TC_WGMODE_DSBOTTOM_gc = (0x07<<0),  /* Dual Slope, Update on BOTTOM */
    TC_WGMODE_DS_B_gc = (0x07<<0),  /* Dual Slope, Update on BOTTOM */
} TC_WGMODE_t;

/* Byte Mode */
typedef enum TC_BYTEM_enum
{
    TC_BYTEM_NORMAL_gc = (0x00<<0),  /* 16-bit mode */
    TC_BYTEM_BYTEMODE_gc = (0x01<<0),  /* Timer/Counter operating in byte mode only */
    TC_BYTEM_SPLITMODE_gc = (0x02<<0),  /* Timer/Counter split into two 8-bit Counters */
} TC_BYTEM_t;

/* Event Action */
typedef enum TC_EVACT_enum
{
    TC_EVACT_OFF_gc = (0x00<<5),  /* No Event Action */
    TC_EVACT_CAPT_gc = (0x01<<5),  /* Input Capture */
    TC_EVACT_UPDOWN_gc = (0x02<<5),  /* Externally Controlled Up/Down Count */
    TC_EVACT_QDEC_gc = (0x03<<5),  /* Quadrature Decode */
    TC_EVACT_RESTART_gc = (0x04<<5),  /* Restart */
    TC_EVACT_FRQ_gc = (0x05<<5),  /* Frequency Capture */
    TC_EVACT_PW_gc = (0x06<<5),  /* Pulse-width Capture */
} TC_EVACT_t;

/* Event Selection */
typedef enum TC_EVSEL_enum
{
    TC_EVSEL_OFF_gc = (0x00<<0),  /* No Event Source */
    TC_EVSEL_CH0_gc = (0x08<<0),  /* Event Channel 0 */
    TC_EVSEL_CH1_gc = (0x09<<0),  /* Event Channel 1 */
    TC_EVSEL_CH2_gc = (0x0A<<0),  /* Event Channel 2 */
    TC_EVSEL_CH3_gc = (0x0B<<0),  /* Event Channel 3 */
} TC_EVSEL_t;

/* Error Interrupt Level */
typedef enum TC_ERRINTLVL_enum
{
    TC_ERRINTLVL_OFF_gc = (0x00<<2),  /* Interrupt Disabled */
    TC_ERRINTLVL_LO_gc = (0x01<<2),  /* Low Level */
    TC_ERRINTLVL_MED_gc = (0x02<<2),  /* Medium Level */
    TC_ERRINTLVL_HI_gc = (0x03<<2),  /* High Level */
} TC_ERRINTLVL_t;

/* Overflow Interrupt Level */
typedef enum TC_OVFINTLVL_enum
{
    TC_OVFINTLVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    TC_OVFINTLVL_LO_gc = (0x01<<0),  /* Low Level */
    TC_OVFINTLVL_MED_gc = (0x02<<0),  /* Medium Level */
    TC_OVFINTLVL_HI_gc = (0x03<<0),  /* High Level */
} TC_OVFINTLVL_t;

/* Compare or Capture D Interrupt Level */
typedef enum TC_CCDINTLVL_enum
{
    TC_CCDINTLVL_OFF_gc = (0x00<<6),  /* Interrupt Disabled */
    TC_CCDINTLVL_LO_gc = (0x01<<6),  /* Low Level */
    TC_CCDINTLVL_MED_gc = (0x02<<6),  /* Medium Level */
    TC_CCDINTLVL_HI_gc = (0x03<<6),  /* High Level */
} TC_CCDINTLVL_t;

/* Compare or Capture C Interrupt Level */
typedef enum TC_CCCINTLVL_enum
{
    TC_CCCINTLVL_OFF_gc = (0x00<<4),  /* Interrupt Disabled */
    TC_CCCINTLVL_LO_gc = (0x01<<4),  /* Low Level */
    TC_CCCINTLVL_MED_gc = (0x02<<4),  /* Medium Level */
    TC_CCCINTLVL_HI_gc = (0x03<<4),  /* High Level */
} TC_CCCINTLVL_t;

/* Compare or Capture B Interrupt Level */
typedef enum TC_CCBINTLVL_enum
{
    TC_CCBINTLVL_OFF_gc = (0x00<<2),  /* Interrupt Disabled */
    TC_CCBINTLVL_LO_gc = (0x01<<2),  /* Low Level */
    TC_CCBINTLVL_MED_gc = (0x02<<2),  /* Medium Level */
    TC_CCBINTLVL_HI_gc = (0x03<<2),  /* High Level */
} TC_CCBINTLVL_t;

/* Compare or Capture A Interrupt Level */
typedef enum TC_CCAINTLVL_enum
{
    TC_CCAINTLVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    TC_CCAINTLVL_LO_gc = (0x01<<0),  /* Low Level */
    TC_CCAINTLVL_MED_gc = (0x02<<0),  /* Medium Level */
    TC_CCAINTLVL_HI_gc = (0x03<<0),  /* High Level */
} TC_CCAINTLVL_t;

/* Timer/Counter Command */
typedef enum TC_CMD_enum
{
    TC_CMD_NONE_gc = (0x00<<2),  /* No Command */
    TC_CMD_UPDATE_gc = (0x01<<2),  /* Force Update */
    TC_CMD_RESTART_gc = (0x02<<2),  /* Force Restart */
    TC_CMD_RESET_gc = (0x03<<2),  /* Force Hard Reset */
} TC_CMD_t;


/*
--------------------------------------------------------------------------
AWEX - Timer/Counter Advanced Waveform Extension
--------------------------------------------------------------------------
*/

/* Advanced Waveform Extension */
typedef struct AWEX_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t reserved_0x01;
    register8_t FDEMASK;  /* Fault Detection Event Mask */
    register8_t FDCTRL;  /* Fault Detection Control Register */
    register8_t STATUS;  /* Status Register */
    register8_t STATUSSET;  /* Status Set Register */
    register8_t DTBOTH;  /* Dead Time Both Sides */
    register8_t DTBOTHBUF;  /* Dead Time Both Sides Buffer */
    register8_t DTLS;  /* Dead Time Low Side */
    register8_t DTHS;  /* Dead Time High Side */
    register8_t DTLSBUF;  /* Dead Time Low Side Buffer */
    register8_t DTHSBUF;  /* Dead Time High Side Buffer */
    register8_t OUTOVEN;  /* Output Override Enable */
} AWEX_t;

/* Fault Detect Action */
typedef enum AWEX_FDACT_enum
{
    AWEX_FDACT_NONE_gc = (0x00<<0),  /* No Fault Protection */
    AWEX_FDACT_CLEAROE_gc = (0x01<<0),  /* Clear Output Enable Bits */
    AWEX_FDACT_CLEARDIR_gc = (0x03<<0),  /* Clear I/O Port Direction Bits */
} AWEX_FDACT_t;


/*
--------------------------------------------------------------------------
HIRES - Timer/Counter High-Resolution Extension
--------------------------------------------------------------------------
*/

/* High-Resolution Extension */
typedef struct HIRES_struct
{
    register8_t CTRLA;  /* Control Register */
} HIRES_t;

/* High Resolution Enable */
typedef enum HIRES_HREN_enum
{
    HIRES_HREN_NONE_gc = (0x00<<0),  /* No Fault Protection */
    HIRES_HREN_TC0_gc = (0x01<<0),  /* Enable High Resolution on Timer/Counter 0 */
    HIRES_HREN_TC1_gc = (0x02<<0),  /* Enable High Resolution on Timer/Counter 1 */
    HIRES_HREN_BOTH_gc = (0x03<<0),  /* Enable High Resolution both Timer/Counters */
} HIRES_HREN_t;


/*
--------------------------------------------------------------------------
USART - Universal Asynchronous Receiver-Transmitter
--------------------------------------------------------------------------
*/

/* Universal Synchronous/Asynchronous Receiver/Transmitter */
typedef struct USART_struct
{
    register8_t DATA;  /* Data Register */
    register8_t STATUS;  /* Status Register */
    register8_t reserved_0x02;
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t CTRLC;  /* Control Register C */
    register8_t BAUDCTRLA;  /* Baud Rate Control Register A */
    register8_t BAUDCTRLB;  /* Baud Rate Control Register B */
} USART_t;

/* Receive Complete Interrupt level */
typedef enum USART_RXCINTLVL_enum
{
    USART_RXCINTLVL_OFF_gc = (0x00<<4),  /* Interrupt Disabled */
    USART_RXCINTLVL_LO_gc = (0x01<<4),  /* Low Level */
    USART_RXCINTLVL_MED_gc = (0x02<<4),  /* Medium Level */
    USART_RXCINTLVL_HI_gc = (0x03<<4),  /* High Level */
} USART_RXCINTLVL_t;

/* Transmit Complete Interrupt level */
typedef enum USART_TXCINTLVL_enum
{
    USART_TXCINTLVL_OFF_gc = (0x00<<2),  /* Interrupt Disabled */
    USART_TXCINTLVL_LO_gc = (0x01<<2),  /* Low Level */
    USART_TXCINTLVL_MED_gc = (0x02<<2),  /* Medium Level */
    USART_TXCINTLVL_HI_gc = (0x03<<2),  /* High Level */
} USART_TXCINTLVL_t;

/* Data Register Empty Interrupt level */
typedef enum USART_DREINTLVL_enum
{
    USART_DREINTLVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    USART_DREINTLVL_LO_gc = (0x01<<0),  /* Low Level */
    USART_DREINTLVL_MED_gc = (0x02<<0),  /* Medium Level */
    USART_DREINTLVL_HI_gc = (0x03<<0),  /* High Level */
} USART_DREINTLVL_t;

/* Character Size */
typedef enum USART_CHSIZE_enum
{
    USART_CHSIZE_5BIT_gc = (0x00<<0),  /* Character size: 5 bit */
    USART_CHSIZE_6BIT_gc = (0x01<<0),  /* Character size: 6 bit */
    USART_CHSIZE_7BIT_gc = (0x02<<0),  /* Character size: 7 bit */
    USART_CHSIZE_8BIT_gc = (0x03<<0),  /* Character size: 8 bit */
    USART_CHSIZE_9BIT_gc = (0x07<<0),  /* Character size: 9 bit */
} USART_CHSIZE_t;

/* Communication Mode */
typedef enum USART_CMODE_enum
{
    USART_CMODE_ASYNCHRONOUS_gc = (0x00<<6),  /* Asynchronous Mode */
    USART_CMODE_SYNCHRONOUS_gc = (0x01<<6),  /* Synchronous Mode */
    USART_CMODE_IRDA_gc = (0x02<<6),  /* IrDA Mode */
    USART_CMODE_MSPI_gc = (0x03<<6),  /* Master SPI Mode */
} USART_CMODE_t;

/* Parity Mode */
typedef enum USART_PMODE_enum
{
    USART_PMODE_DISABLED_gc = (0x00<<4),  /* No Parity */
    USART_PMODE_EVEN_gc = (0x02<<4),  /* Even Parity */
    USART_PMODE_ODD_gc = (0x03<<4),  /* Odd Parity */
} USART_PMODE_t;


/*
--------------------------------------------------------------------------
SPI - Serial Peripheral Interface
--------------------------------------------------------------------------
*/

/* Serial Peripheral Interface */
typedef struct SPI_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t INTCTRL;  /* Interrupt Control Register */
    register8_t STATUS;  /* Status Register */
    register8_t DATA;  /* Data Register */
} SPI_t;

/* SPI Mode */
typedef enum SPI_MODE_enum
{
    SPI_MODE_0_gc = (0x00<<2),  /* SPI Mode 0 */
    SPI_MODE_1_gc = (0x01<<2),  /* SPI Mode 1 */
    SPI_MODE_2_gc = (0x02<<2),  /* SPI Mode 2 */
    SPI_MODE_3_gc = (0x03<<2),  /* SPI Mode 3 */
} SPI_MODE_t;

/* Prescaler setting */
typedef enum SPI_PRESCALER_enum
{
    SPI_PRESCALER_DIV4_gc = (0x00<<0),  /* System Clock / 4 */
    SPI_PRESCALER_DIV16_gc = (0x01<<0),  /* System Clock / 16 */
    SPI_PRESCALER_DIV64_gc = (0x02<<0),  /* System Clock / 64 */
    SPI_PRESCALER_DIV128_gc = (0x03<<0),  /* System Clock / 128 */
} SPI_PRESCALER_t;

/* Interrupt level */
typedef enum SPI_INTLVL_enum
{
    SPI_INTLVL_OFF_gc = (0x00<<0),  /* Interrupt Disabled */
    SPI_INTLVL_LO_gc = (0x01<<0),  /* Low Level */
    SPI_INTLVL_MED_gc = (0x02<<0),  /* Medium Level */
    SPI_INTLVL_HI_gc = (0x03<<0),  /* High Level */
} SPI_INTLVL_t;


/*
--------------------------------------------------------------------------
IRCOM - IR Communication Module
--------------------------------------------------------------------------
*/

/* IR Communication Module */
typedef struct IRCOM_struct
{
    register8_t CTRL;  /* Control Register */
    register8_t TXPLCTRL;  /* IrDA Transmitter Pulse Length Control Register */
    register8_t RXPLCTRL;  /* IrDA Receiver Pulse Length Control Register */
} IRCOM_t;

/* Event channel selection */
typedef enum IRDA_EVSEL_enum
{
    IRDA_EVSEL_OFF_gc = (0x00<<0),  /* No Event Source */
    IRDA_EVSEL_0_gc = (0x08<<0),  /* Event Channel 0 */
    IRDA_EVSEL_1_gc = (0x09<<0),  /* Event Channel 1 */
    IRDA_EVSEL_2_gc = (0x0A<<0),  /* Event Channel 2 */
    IRDA_EVSEL_3_gc = (0x0B<<0),  /* Event Channel 3 */
} IRDA_EVSEL_t;


/*
--------------------------------------------------------------------------
LCD - LCD Controller
--------------------------------------------------------------------------
*/

/* LCD Controller */
typedef struct LCD_struct
{
    register8_t CTRLA;  /* Control Register A */
    register8_t CTRLB;  /* Control Register B */
    register8_t CTRLC;  /* Control Register C */
    register8_t INTCTRL;  /* Interrupt Enable Register */
    register8_t INTFLAG;  /* Interrupt Flag Register */
    register8_t CTRLD;  /* Control Register D */
    register8_t CTRLE;  /* Control Register E */
    register8_t CTRLF;  /* Control Register F */
    register8_t CTRLG;  /* Control Register G */
    register8_t CTRLH;  /* Control Register H */
    register8_t reserved_0x0A;
    register8_t reserved_0x0B;
    register8_t reserved_0x0C;
    register8_t reserved_0x0D;
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
    register8_t DATA0;  /* LCD Data Register 0 */
    register8_t DATA1;  /* LCD Data Register 1 */
    register8_t DATA2;  /* LCD Data Register 2 */
    register8_t DATA3;  /* LCD Data Register 3 */
    register8_t DATA4;  /* LCD Data Register 4 */
    register8_t DATA5;  /* LCD Data Register 5 */
    register8_t DATA6;  /* LCD Data Register 6 */
    register8_t DATA7;  /* LCD Data Register 7 */
    register8_t DATA8;  /* LCD Data Register 8 */
    register8_t DATA9;  /* LCD Data Register 9 */
    register8_t DATA10;  /* LCD Data Register 10 */
    register8_t DATA11;  /* LCD Data Register 11 */
    register8_t DATA12;  /* LCD Data Register 12 */
    register8_t DATA13;  /* LCD Data Register 13 */
    register8_t DATA14;  /* LCD Data Register 14 */
    register8_t DATA15;  /* LCD Data Register 15 */
    register8_t DATA16;  /* LCD Data Register 16 */
    register8_t DATA17;  /* LCD Data Register 17 */
    register8_t DATA18;  /* LCD Data Register 18 */
    register8_t DATA19;  /* LCD Data Register 19 */
} LCD_t;

/* LCD Blink Rate */
typedef enum LCD_BLINKRATE_enum
{
    LCD_BLINKRATE_4Hz_gc = (0x00<<0),  /* 4Hz Blink Rate */
    LCD_BLINKRATE_2Hz_gc = (0x01<<0),  /* 2Hz Blink Rate */
    LCD_BLINKRATE_1Hz_gc = (0x02<<0),  /* 1Hz Blink Rate */
    LCD_BLINKRATE_0Hz5_gc = (0x03<<0),  /* 0.5Hz Blink Rate */
} LCD_BLINKRATE_t;

/* LCD Clock Divide */
typedef enum LCD_CLKDIV_enum
{
    LCD_CLKDIV_DivBy1_gc = (0x00<<4),  /* frame rate of 256 Hz */
    LCD_CLKDIV_DivBy2_gc = (0x01<<4),  /* frame rate of 128 Hz */
    LCD_CLKDIV_DivBy3_gc = (0x02<<4),  /* frame rate of 83.5 Hz */
    LCD_CLKDIV_DivBy4_gc = (0x03<<4),  /* frame rate of 64 Hz */
    LCD_CLKDIV_DivBy5_gc = (0x04<<4),  /* frame rate of 51.2 Hz */
    LCD_CLKDIV_DivBy6_gc = (0x05<<4),  /* frame rate of 42.7 Hz */
    LCD_CLKDIV_DivBy7_gc = (0x06<<4),  /* frame rate of 36.6 Hz */
    LCD_CLKDIV_DivBy8_gc = (0x07<<4),  /* frame rate of 32 Hz */
} LCD_CLKDIV_t;

/* Duty Select */
typedef enum LCD_DUTY_enum
{
    LCD_DUTY_1_4_gc = (0x00<<0),  /* Duty=1/4, Bias=1/3, COM0:3 */
    LCD_DUTY_Static_gc = (0x01<<0),  /* Duty=Static, Bias=Static, COM0 */
    LCD_DUTY_1_2_gc = (0x02<<0),  /* Duty=1/2, Bias=1/3, COM0:1 */
    LCD_DUTY_1_3_gc = (0x03<<0),  /* Duty=1/3, Bias=1/3, COM0:2 */
} LCD_DUTY_t;

/* LCD Prescaler Select */
typedef enum LCD_PRESC_enum
{
    LCD_PRESC_8_gc = (0x00<<7),  /* clk_lcd/8 */
    LCD_PRESC_16_gc = (0x01<<7),  /* clk_lcd/16 */
} LCD_PRESC_t;

/* Type of Digit */
typedef enum LCD_TDG_enum
{
    LCD_TDG_7S_3C_gc = (0x00<<6),  /* 7-segment with 3 COMs */
    LCD_TDG_7S_4C_gc = (0x01<<6),  /* 7-segment with 4 COMs */
    LCD_TDG_14S_4C_gc = (0x02<<6),  /* 14-segment with 4 COMs */
    LCD_TDG_16S_3C_gc = (0x03<<6),  /* 16-segment with 3 COMs */
} LCD_TDG_t;


/*
--------------------------------------------------------------------------
FUSE - Fuses and Lockbits
--------------------------------------------------------------------------
*/

/* Fuses */
typedef struct NVM_FUSES_struct
{
    register8_t FUSEBYTE0;  /* JTAG User ID */
    register8_t FUSEBYTE1;  /* Watchdog Configuration */
    register8_t FUSEBYTE2;  /* Reset Configuration */
    register8_t reserved_0x03;
    register8_t FUSEBYTE4;  /* Start-up Configuration */
    register8_t FUSEBYTE5;  /* EESAVE and BOD Level */
} NVM_FUSES_t;

/* Boot Loader Section Reset Vector */
typedef enum BOOTRST_enum
{
    BOOTRST_BOOTLDR_gc = (0x00<<6),  /* Boot Loader Reset */
    BOOTRST_APPLICATION_gc = (0x01<<6),  /* Application Reset */
} BOOTRST_t;

/* Timer Oscillator pin location */
typedef enum TOSCSEL_enum
{
    TOSCSEL_ALTERNATE_gc = (0x00<<5),  /* TOSC1 / TOSC2 on separate pins */
    TOSCSEL_XTAL_gc = (0x01<<5),  /* TOSC1 / TOSC2 shared with XTAL1 / XTAL2 */
} TOSCSEL_t;

/* BOD operation */
typedef enum BOD_enum
{
    BOD_SAMPLED_gc = (0x01<<0),  /* BOD enabled in sampled mode */
    BOD_CONTINUOUS_gc = (0x02<<0),  /* BOD enabled continuously */
    BOD_DISABLED_gc = (0x03<<0),  /* BOD Disabled */
} BOD_t;

/* BOD operation */
typedef enum BODACT_enum
{
    BODACT_SAMPLED_gc = (0x01<<4),  /* BOD enabled in sampled mode */
    BODACT_CONTINUOUS_gc = (0x02<<4),  /* BOD enabled continuously */
    BODACT_DISABLED_gc = (0x03<<4),  /* BOD Disabled */
} BODACT_t;

/* Watchdog (Window) Timeout Period */
typedef enum WD_enum
{
    WD_8CLK_gc = (0x00<<4),  /* 8 cycles (8ms @ 3.3V) */
    WD_16CLK_gc = (0x01<<4),  /* 16 cycles (16ms @ 3.3V) */
    WD_32CLK_gc = (0x02<<4),  /* 32 cycles (32ms @ 3.3V) */
    WD_64CLK_gc = (0x03<<4),  /* 64 cycles (64ms @ 3.3V) */
    WD_128CLK_gc = (0x04<<4),  /* 128 cycles (0.125s @ 3.3V) */
    WD_256CLK_gc = (0x05<<4),  /* 256 cycles (0.25s @ 3.3V) */
    WD_512CLK_gc = (0x06<<4),  /* 512 cycles (0.5s @ 3.3V) */
    WD_1KCLK_gc = (0x07<<4),  /* 1K cycles (1s @ 3.3V) */
    WD_2KCLK_gc = (0x08<<4),  /* 2K cycles (2s @ 3.3V) */
    WD_4KCLK_gc = (0x09<<4),  /* 4K cycles (4s @ 3.3V) */
    WD_8KCLK_gc = (0x0A<<4),  /* 8K cycles (8s @ 3.3V) */
} WD_t;

/* Watchdog (Window) Timeout Period */
typedef enum WDP_enum
{
    WDP_8CLK_gc = (0x00<<0),  /* 8 cycles (8ms @ 3.3V) */
    WDP_16CLK_gc = (0x01<<0),  /* 16 cycles (16ms @ 3.3V) */
    WDP_32CLK_gc = (0x02<<0),  /* 32 cycles (32ms @ 3.3V) */
    WDP_64CLK_gc = (0x03<<0),  /* 64 cycles (64ms @ 3.3V) */
    WDP_128CLK_gc = (0x04<<0),  /* 128 cycles (0.125s @ 3.3V) */
    WDP_256CLK_gc = (0x05<<0),  /* 256 cycles (0.25s @ 3.3V) */
    WDP_512CLK_gc = (0x06<<0),  /* 512 cycles (0.5s @ 3.3V) */
    WDP_1KCLK_gc = (0x07<<0),  /* 1K cycles (1s @ 3.3V) */
    WDP_2KCLK_gc = (0x08<<0),  /* 2K cycles (2s @ 3.3V) */
    WDP_4KCLK_gc = (0x09<<0),  /* 4K cycles (4s @ 3.3V) */
    WDP_8KCLK_gc = (0x0A<<0),  /* 8K cycles (8s @ 3.3V) */
} WDP_t;

/* Start-up Time */
typedef enum SUT_enum
{
    SUT_0MS_gc = (0x03<<2),  /* 0 ms */
    SUT_4MS_gc = (0x01<<2),  /* 4 ms */
    SUT_64MS_gc = (0x00<<2),  /* 64 ms */
} SUT_t;

/* Brownout Detection Voltage Level */
typedef enum BODLVL_enum
{
    BODLVL_1V6_gc = (0x07<<0),  /* 1.6 V */
    BODLVL_1V8_gc = (0x06<<0),  /* 1.8 V */
    BODLVL_2V0_gc = (0x05<<0),  /* 2.0 V */
    BODLVL_2V2_gc = (0x04<<0),  /* 2.2 V */
    BODLVL_2V4_gc = (0x03<<0),  /* 2.4 V */
    BODLVL_2V6_gc = (0x02<<0),  /* 2.6 V */
    BODLVL_2V8_gc = (0x01<<0),  /* 2.8 V */
    BODLVL_3V0_gc = (0x00<<0),  /* 3.0 V */
} BODLVL_t;


/*
--------------------------------------------------------------------------
LOCKBIT - Fuses and Lockbits
--------------------------------------------------------------------------
*/

/* Lock Bits */
typedef struct NVM_LOCKBITS_struct
{
    register8_t LOCK_BITS;  /* Lock Bits (Changed from LOCKBITS to avoid avr-libc collision) */
} NVM_LOCKBITS_t;

/* Boot lock bits - boot setcion */
typedef enum FUSE_BLBB_enum
{
    FUSE_BLBB_RWLOCK_gc = (0x00<<6),  /* Read and write not allowed */
    FUSE_BLBB_RLOCK_gc = (0x01<<6),  /* Read not allowed */
    FUSE_BLBB_WLOCK_gc = (0x02<<6),  /* Write not allowed */
    FUSE_BLBB_NOLOCK_gc = (0x03<<6),  /* No locks */
} FUSE_BLBB_t;

/* Boot lock bits - application section */
typedef enum FUSE_BLBA_enum
{
    FUSE_BLBA_RWLOCK_gc = (0x00<<4),  /* Read and write not allowed */
    FUSE_BLBA_RLOCK_gc = (0x01<<4),  /* Read not allowed */
    FUSE_BLBA_WLOCK_gc = (0x02<<4),  /* Write not allowed */
    FUSE_BLBA_NOLOCK_gc = (0x03<<4),  /* No locks */
} FUSE_BLBA_t;

/* Boot lock bits - application table section */
typedef enum FUSE_BLBAT_enum
{
    FUSE_BLBAT_RWLOCK_gc = (0x00<<2),  /* Read and write not allowed */
    FUSE_BLBAT_RLOCK_gc = (0x01<<2),  /* Read not allowed */
    FUSE_BLBAT_WLOCK_gc = (0x02<<2),  /* Write not allowed */
    FUSE_BLBAT_NOLOCK_gc = (0x03<<2),  /* No locks */
} FUSE_BLBAT_t;

/* Lock bits */
typedef enum FUSE_LB_enum
{
    FUSE_LB_RWLOCK_gc = (0x00<<0),  /* Read and write not allowed */
    FUSE_LB_WLOCK_gc = (0x02<<0),  /* Write not allowed */
    FUSE_LB_NOLOCK_gc = (0x03<<0),  /* No locks */
} FUSE_LB_t;


/*
--------------------------------------------------------------------------
SIGROW - Signature Row
--------------------------------------------------------------------------
*/

/* Production Signatures */
typedef struct NVM_PROD_SIGNATURES_struct
{
    register8_t RCOSC2M;  /* RCOSC 2 MHz Calibration Value B */
    register8_t RCOSC2MA;  /* RCOSC 2 MHz Calibration Value A */
    register8_t RCOSC32K;  /* RCOSC 32.768 kHz Calibration Value */
    register8_t RCOSC32M;  /* RCOSC 32 MHz Calibration Value B */
    register8_t RCOSC32MA;  /* RCOSC 32 MHz Calibration Value A */
    register8_t reserved_0x05;
    register8_t reserved_0x06;
    register8_t reserved_0x07;
    register8_t LOTNUM0;  /* Lot Number Byte 0, ASCII */
    register8_t LOTNUM1;  /* Lot Number Byte 1, ASCII */
    register8_t LOTNUM2;  /* Lot Number Byte 2, ASCII */
    register8_t LOTNUM3;  /* Lot Number Byte 3, ASCII */
    register8_t LOTNUM4;  /* Lot Number Byte 4, ASCII */
    register8_t LOTNUM5;  /* Lot Number Byte 5, ASCII */
    register8_t reserved_0x0E;
    register8_t reserved_0x0F;
    register8_t WAFNUM;  /* Wafer Number */
    register8_t reserved_0x11;
    register8_t COORDX0;  /* Wafer Coordinate X Byte 0 */
    register8_t COORDX1;  /* Wafer Coordinate X Byte 1 */
    register8_t COORDY0;  /* Wafer Coordinate Y Byte 0 */
    register8_t COORDY1;  /* Wafer Coordinate Y Byte 1 */
    register8_t reserved_0x16;
    register8_t reserved_0x17;
    register8_t reserved_0x18;
    register8_t reserved_0x19;
    register8_t USBCAL0;  /* USB Calibration Byte 0 */
    register8_t USBCAL1;  /* USB Calibration Byte 1 */
    register8_t USBRCOSC;  /* USB RCOSC Calibration Value B */
    register8_t USBRCOSCA;  /* USB RCOSC Calibration Value A */
    register8_t reserved_0x1E;
    register8_t reserved_0x1F;
    register8_t ADCACAL0;  /* ADCA Calibration Byte 0 */
    register8_t ADCACAL1;  /* ADCA Calibration Byte 1 */
    register8_t reserved_0x22;
    register8_t reserved_0x23;
    register8_t ADCBCAL0;  /* ADCB Calibration Byte 0 */
    register8_t ADCBCAL1;  /* ADCB Calibration Byte 1 */
    register8_t reserved_0x26;
    register8_t reserved_0x27;
    register8_t reserved_0x28;
    register8_t reserved_0x29;
    register8_t reserved_0x2A;
    register8_t reserved_0x2B;
    register8_t reserved_0x2C;
    register8_t reserved_0x2D;
    register8_t TEMPSENSE0;  /* Temperature Sensor Calibration Byte 0 */
    register8_t TEMPSENSE1;  /* Temperature Sensor Calibration Byte 1 */
    register8_t reserved_0x30;
    register8_t reserved_0x31;
    register8_t reserved_0x32;
    register8_t reserved_0x33;
    register8_t reserved_0x34;
    register8_t reserved_0x35;
    register8_t reserved_0x36;
    register8_t reserved_0x37;
    register8_t reserved_0x38;
    register8_t reserved_0x39;
    register8_t reserved_0x3A;
    register8_t reserved_0x3B;
    register8_t reserved_0x3C;
    register8_t reserved_0x3D;
    register8_t reserved_0x3E;
    register8_t reserved_0x3F;
    register8_t reserved_0x40;
    register8_t reserved_0x41;
    register8_t reserved_0x42;
    register8_t reserved_0x43;
    register8_t reserved_0x44;
    register8_t reserved_0x45;
    register8_t reserved_0x46;
    register8_t reserved_0x47;
} NVM_PROD_SIGNATURES_t;

/*
==========================================================================
IO Module Instances. Mapped to memory.
==========================================================================
*/

#define VPORT0    (*(VPORT_t *) 0x0010)  /* Virtual Port */
#define VPORT1    (*(VPORT_t *) 0x0014)  /* Virtual Port */
#define VPORT2    (*(VPORT_t *) 0x0018)  /* Virtual Port */
#define VPORT3    (*(VPORT_t *) 0x001C)  /* Virtual Port */
#define OCD    (*(OCD_t *) 0x002E)  /* On-Chip Debug System */
#define CLK    (*(CLK_t *) 0x0040)  /* Clock System */
#define SLEEP    (*(SLEEP_t *) 0x0048)  /* Sleep Controller */
#define OSC    (*(OSC_t *) 0x0050)  /* Oscillator */
#define DFLLRC32M    (*(DFLL_t *) 0x0060)  /* DFLL */
#define DFLLRC2M    (*(DFLL_t *) 0x0068)  /* DFLL */
#define PR    (*(PR_t *) 0x0070)  /* Power Reduction */
#define RST    (*(RST_t *) 0x0078)  /* Reset */
#define WDT    (*(WDT_t *) 0x0080)  /* Watch-Dog Timer */
#define MCU    (*(MCU_t *) 0x0090)  /* MCU Control */
#define PMIC    (*(PMIC_t *) 0x00A0)  /* Programmable Multi-level Interrupt Controller */
#define PORTCFG    (*(PORTCFG_t *) 0x00B0)  /* I/O port Configuration */
#define AES    (*(AES_t *) 0x00C0)  /* AES Module */
#define CRC    (*(CRC_t *) 0x00D0)  /* Cyclic Redundancy Checker */
#define DMA    (*(DMA_t *) 0x0100)  /* DMA Controller */
#define EVSYS    (*(EVSYS_t *) 0x0180)  /* Event System */
#define NVM    (*(NVM_t *) 0x01C0)  /* Non-volatile Memory Controller */
#define ADCA    (*(ADC_t *) 0x0200)  /* Analog-to-Digital Converter */
#define ADCB    (*(ADC_t *) 0x0240)  /* Analog-to-Digital Converter */
#define ACA    (*(AC_t *) 0x0380)  /* Analog Comparator */
#define ACB    (*(AC_t *) 0x0390)  /* Analog Comparator */
#define RTC    (*(RTC_t *) 0x0400)  /* Real-Time Counter */
#define TWIC    (*(TWI_t *) 0x0480)  /* Two-Wire Interface */
#define USB    (*(USB_t *) 0x04C0)  /* Universal Serial Bus */
#define PORTA    (*(PORT_t *) 0x0600)  /* I/O Ports */
#define PORTB    (*(PORT_t *) 0x0620)  /* I/O Ports */
#define PORTC    (*(PORT_t *) 0x0640)  /* I/O Ports */
#define PORTD    (*(PORT_t *) 0x0660)  /* I/O Ports */
#define PORTE    (*(PORT_t *) 0x0680)  /* I/O Ports */
#define PORTG    (*(PORT_t *) 0x06C0)  /* I/O Ports */
#define PORTM    (*(PORT_t *) 0x0760)  /* I/O Ports */
#define PORTR    (*(PORT_t *) 0x07E0)  /* I/O Ports */
#define TCC0    (*(TC0_t *) 0x0800)  /* 16-bit Timer/Counter 0 */
#define TCC1    (*(TC1_t *) 0x0840)  /* 16-bit Timer/Counter 1 */
#define AWEXC    (*(AWEX_t *) 0x0880)  /* Advanced Waveform Extension */
#define HIRESC    (*(HIRES_t *) 0x0890)  /* High-Resolution Extension */
#define USARTC0    (*(USART_t *) 0x08A0)  /* Universal Synchronous/Asynchronous Receiver/Transmitter */
#define SPIC    (*(SPI_t *) 0x08C0)  /* Serial Peripheral Interface */
#define IRCOM    (*(IRCOM_t *) 0x08F8)  /* IR Communication Module */
#define TCE0    (*(TC0_t *) 0x0A00)  /* 16-bit Timer/Counter 0 */
#define USARTE0    (*(USART_t *) 0x0AA0)  /* Universal Synchronous/Asynchronous Receiver/Transmitter */
#define LCD    (*(LCD_t *) 0x0D00)  /* LCD Controller */


#endif /* !defined (__ASSEMBLER__) */


/* ========== Flattened fully qualified IO register names ========== */

/* GPIO - General Purpose IO Registers */
#define GPIO_GPIOR0  _SFR_MEM8(0x0000)
#define GPIO_GPIOR1  _SFR_MEM8(0x0001)
#define GPIO_GPIOR2  _SFR_MEM8(0x0002)
#define GPIO_GPIOR3  _SFR_MEM8(0x0003)

/* Deprecated */
#define GPIO_GPIO0  _SFR_MEM8(0x0000)
#define GPIO_GPIO1  _SFR_MEM8(0x0001)
#define GPIO_GPIO2  _SFR_MEM8(0x0002)
#define GPIO_GPIO3  _SFR_MEM8(0x0003)

/* NVM_FUSES - Fuses */
#define FUSE_FUSEBYTE0  _SFR_MEM8(0x0000)
#define FUSE_FUSEBYTE1  _SFR_MEM8(0x0001)
#define FUSE_FUSEBYTE2  _SFR_MEM8(0x0002)
#define FUSE_FUSEBYTE4  _SFR_MEM8(0x0004)
#define FUSE_FUSEBYTE5  _SFR_MEM8(0x0005)

/* NVM_LOCKBITS - Lock Bits */
#define LOCKBIT_LOCKBITS  _SFR_MEM8(0x0000)

/* NVM_PROD_SIGNATURES - Production Signatures */
#define PRODSIGNATURES_RCOSC2M  _SFR_MEM8(0x0000)
#define PRODSIGNATURES_RCOSC2MA  _SFR_MEM8(0x0001)
#define PRODSIGNATURES_RCOSC32K  _SFR_MEM8(0x0002)
#define PRODSIGNATURES_RCOSC32M  _SFR_MEM8(0x0003)
#define PRODSIGNATURES_RCOSC32MA  _SFR_MEM8(0x0004)
#define PRODSIGNATURES_LOTNUM0  _SFR_MEM8(0x0008)
#define PRODSIGNATURES_LOTNUM1  _SFR_MEM8(0x0009)
#define PRODSIGNATURES_LOTNUM2  _SFR_MEM8(0x000A)
#define PRODSIGNATURES_LOTNUM3  _SFR_MEM8(0x000B)
#define PRODSIGNATURES_LOTNUM4  _SFR_MEM8(0x000C)
#define PRODSIGNATURES_LOTNUM5  _SFR_MEM8(0x000D)
#define PRODSIGNATURES_WAFNUM  _SFR_MEM8(0x0010)
#define PRODSIGNATURES_COORDX0  _SFR_MEM8(0x0012)
#define PRODSIGNATURES_COORDX1  _SFR_MEM8(0x0013)
#define PRODSIGNATURES_COORDY0  _SFR_MEM8(0x0014)
#define PRODSIGNATURES_COORDY1  _SFR_MEM8(0x0015)
#define PRODSIGNATURES_USBCAL0  _SFR_MEM8(0x001A)
#define PRODSIGNATURES_USBCAL1  _SFR_MEM8(0x001B)
#define PRODSIGNATURES_USBRCOSC  _SFR_MEM8(0x001C)
#define PRODSIGNATURES_USBRCOSCA  _SFR_MEM8(0x001D)
#define PRODSIGNATURES_ADCACAL0  _SFR_MEM8(0x0020)
#define PRODSIGNATURES_ADCACAL1  _SFR_MEM8(0x0021)
#define PRODSIGNATURES_ADCBCAL0  _SFR_MEM8(0x0024)
#define PRODSIGNATURES_ADCBCAL1  _SFR_MEM8(0x0025)
#define PRODSIGNATURES_TEMPSENSE0  _SFR_MEM8(0x002E)
#define PRODSIGNATURES_TEMPSENSE1  _SFR_MEM8(0x002F)

/* VPORT - Virtual Port */
#define VPORT0_DIR  _SFR_MEM8(0x0010)
#define VPORT0_OUT  _SFR_MEM8(0x0011)
#define VPORT0_IN  _SFR_MEM8(0x0012)
#define VPORT0_INTFLAGS  _SFR_MEM8(0x0013)

/* VPORT - Virtual Port */
#define VPORT1_DIR  _SFR_MEM8(0x0014)
#define VPORT1_OUT  _SFR_MEM8(0x0015)
#define VPORT1_IN  _SFR_MEM8(0x0016)
#define VPORT1_INTFLAGS  _SFR_MEM8(0x0017)

/* VPORT - Virtual Port */
#define VPORT2_DIR  _SFR_MEM8(0x0018)
#define VPORT2_OUT  _SFR_MEM8(0x0019)
#define VPORT2_IN  _SFR_MEM8(0x001A)
#define VPORT2_INTFLAGS  _SFR_MEM8(0x001B)

/* VPORT - Virtual Port */
#define VPORT3_DIR  _SFR_MEM8(0x001C)
#define VPORT3_OUT  _SFR_MEM8(0x001D)
#define VPORT3_IN  _SFR_MEM8(0x001E)
#define VPORT3_INTFLAGS  _SFR_MEM8(0x001F)

/* OCD - On-Chip Debug System */
#define OCD_OCDR0  _SFR_MEM8(0x002E)
#define OCD_OCDR1  _SFR_MEM8(0x002F)

/* CPU - CPU registers */
#define CPU_CCP  _SFR_MEM8(0x0034)
#define CPU_RAMPD  _SFR_MEM8(0x0038)
#define CPU_RAMPX  _SFR_MEM8(0x0039)
#define CPU_RAMPY  _SFR_MEM8(0x003A)
#define CPU_RAMPZ  _SFR_MEM8(0x003B)
#define CPU_EIND  _SFR_MEM8(0x003C)
#define CPU_SPL  _SFR_MEM8(0x003D)
#define CPU_SPH  _SFR_MEM8(0x003E)
#define CPU_SREG  _SFR_MEM8(0x003F)

/* CLK - Clock System */
#define CLK_CTRL  _SFR_MEM8(0x0040)
#define CLK_PSCTRL  _SFR_MEM8(0x0041)
#define CLK_LOCK  _SFR_MEM8(0x0042)
#define CLK_RTCCTRL  _SFR_MEM8(0x0043)
#define CLK_USBCTRL  _SFR_MEM8(0x0044)

/* SLEEP - Sleep Controller */
#define SLEEP_CTRL  _SFR_MEM8(0x0048)

/* OSC - Oscillator */
#define OSC_CTRL  _SFR_MEM8(0x0050)
#define OSC_STATUS  _SFR_MEM8(0x0051)
#define OSC_XOSCCTRL  _SFR_MEM8(0x0052)
#define OSC_XOSCFAIL  _SFR_MEM8(0x0053)
#define OSC_RC32KCAL  _SFR_MEM8(0x0054)
#define OSC_PLLCTRL  _SFR_MEM8(0x0055)
#define OSC_DFLLCTRL  _SFR_MEM8(0x0056)

/* DFLL - DFLL */
#define DFLLRC32M_CTRL  _SFR_MEM8(0x0060)
#define DFLLRC32M_CALA  _SFR_MEM8(0x0062)
#define DFLLRC32M_CALB  _SFR_MEM8(0x0063)
#define DFLLRC32M_COMP0  _SFR_MEM8(0x0064)
#define DFLLRC32M_COMP1  _SFR_MEM8(0x0065)
#define DFLLRC32M_COMP2  _SFR_MEM8(0x0066)

/* DFLL - DFLL */
#define DFLLRC2M_CTRL  _SFR_MEM8(0x0068)
#define DFLLRC2M_CALA  _SFR_MEM8(0x006A)
#define DFLLRC2M_CALB  _SFR_MEM8(0x006B)
#define DFLLRC2M_COMP0  _SFR_MEM8(0x006C)
#define DFLLRC2M_COMP1  _SFR_MEM8(0x006D)
#define DFLLRC2M_COMP2  _SFR_MEM8(0x006E)

/* PR - Power Reduction */
#define PR_PRGEN  _SFR_MEM8(0x0070)
#define PR_PRPA  _SFR_MEM8(0x0071)
#define PR_PRPB  _SFR_MEM8(0x0072)
#define PR_PRPC  _SFR_MEM8(0x0073)
#define PR_PRPE  _SFR_MEM8(0x0075)

/* RST - Reset */
#define RST_STATUS  _SFR_MEM8(0x0078)
#define RST_CTRL  _SFR_MEM8(0x0079)

/* WDT - Watch-Dog Timer */
#define WDT_CTRL  _SFR_MEM8(0x0080)
#define WDT_WINCTRL  _SFR_MEM8(0x0081)
#define WDT_STATUS  _SFR_MEM8(0x0082)

/* MCU - MCU Control */
#define MCU_DEVID0  _SFR_MEM8(0x0090)
#define MCU_DEVID1  _SFR_MEM8(0x0091)
#define MCU_DEVID2  _SFR_MEM8(0x0092)
#define MCU_REVID  _SFR_MEM8(0x0093)
#define MCU_JTAGUID  _SFR_MEM8(0x0094)
#define MCU_MCUCR  _SFR_MEM8(0x0096)
#define MCU_ANAINIT  _SFR_MEM8(0x0097)
#define MCU_EVSYSLOCK  _SFR_MEM8(0x0098)
#define MCU_AWEXLOCK  _SFR_MEM8(0x0099)

/* PMIC - Programmable Multi-level Interrupt Controller */
#define PMIC_STATUS  _SFR_MEM8(0x00A0)
#define PMIC_INTPRI  _SFR_MEM8(0x00A1)
#define PMIC_CTRL  _SFR_MEM8(0x00A2)

/* PORTCFG - I/O port Configuration */
#define PORTCFG_MPCMASK  _SFR_MEM8(0x00B0)
#define PORTCFG_VPCTRLA  _SFR_MEM8(0x00B2)
#define PORTCFG_VPCTRLB  _SFR_MEM8(0x00B3)
#define PORTCFG_CLKEVOUT  _SFR_MEM8(0x00B4)
#define PORTCFG_EVOUTSEL  _SFR_MEM8(0x00B6)

/* AES - AES Module */
#define AES_CTRL  _SFR_MEM8(0x00C0)
#define AES_STATUS  _SFR_MEM8(0x00C1)
#define AES_STATE  _SFR_MEM8(0x00C2)
#define AES_KEY  _SFR_MEM8(0x00C3)
#define AES_INTCTRL  _SFR_MEM8(0x00C4)

/* CRC - Cyclic Redundancy Checker */
#define CRC_CTRL  _SFR_MEM8(0x00D0)
#define CRC_STATUS  _SFR_MEM8(0x00D1)
#define CRC_DATAIN  _SFR_MEM8(0x00D3)
#define CRC_CHECKSUM0  _SFR_MEM8(0x00D4)
#define CRC_CHECKSUM1  _SFR_MEM8(0x00D5)
#define CRC_CHECKSUM2  _SFR_MEM8(0x00D6)
#define CRC_CHECKSUM3  _SFR_MEM8(0x00D7)

/* DMA - DMA Controller */
#define DMA_CTRL  _SFR_MEM8(0x0100)
#define DMA_INTFLAGS  _SFR_MEM8(0x0103)
#define DMA_STATUS  _SFR_MEM8(0x0104)
#define DMA_TEMP  _SFR_MEM16(0x0106)
#define DMA_CH0_CTRLA  _SFR_MEM8(0x0110)
#define DMA_CH0_CTRLB  _SFR_MEM8(0x0111)
#define DMA_CH0_ADDRCTRL  _SFR_MEM8(0x0112)
#define DMA_CH0_TRIGSRC  _SFR_MEM8(0x0113)
#define DMA_CH0_TRFCNT  _SFR_MEM16(0x0114)
#define DMA_CH0_REPCNT  _SFR_MEM8(0x0116)
#define DMA_CH0_SRCADDR0  _SFR_MEM8(0x0118)
#define DMA_CH0_SRCADDR1  _SFR_MEM8(0x0119)
#define DMA_CH0_DESTADDR0  _SFR_MEM8(0x011C)
#define DMA_CH0_DESTADDR1  _SFR_MEM8(0x011D)
#define DMA_CH1_CTRLA  _SFR_MEM8(0x0120)
#define DMA_CH1_CTRLB  _SFR_MEM8(0x0121)
#define DMA_CH1_ADDRCTRL  _SFR_MEM8(0x0122)
#define DMA_CH1_TRIGSRC  _SFR_MEM8(0x0123)
#define DMA_CH1_TRFCNT  _SFR_MEM16(0x0124)
#define DMA_CH1_REPCNT  _SFR_MEM8(0x0126)
#define DMA_CH1_SRCADDR0  _SFR_MEM8(0x0128)
#define DMA_CH1_SRCADDR1  _SFR_MEM8(0x0129)
#define DMA_CH1_DESTADDR0  _SFR_MEM8(0x012C)
#define DMA_CH1_DESTADDR1  _SFR_MEM8(0x012D)

/* EVSYS - Event System */
#define EVSYS_CH0MUX  _SFR_MEM8(0x0180)
#define EVSYS_CH1MUX  _SFR_MEM8(0x0181)
#define EVSYS_CH2MUX  _SFR_MEM8(0x0182)
#define EVSYS_CH3MUX  _SFR_MEM8(0x0183)
#define EVSYS_CH0CTRL  _SFR_MEM8(0x0188)
#define EVSYS_CH1CTRL  _SFR_MEM8(0x0189)
#define EVSYS_CH2CTRL  _SFR_MEM8(0x018A)
#define EVSYS_CH3CTRL  _SFR_MEM8(0x018B)
#define EVSYS_STROBE  _SFR_MEM8(0x0190)
#define EVSYS_DATA  _SFR_MEM8(0x0191)

/* NVM - Non-volatile Memory Controller */
#define NVM_ADDR0  _SFR_MEM8(0x01C0)
#define NVM_ADDR1  _SFR_MEM8(0x01C1)
#define NVM_ADDR2  _SFR_MEM8(0x01C2)
#define NVM_DATA0  _SFR_MEM8(0x01C4)
#define NVM_DATA1  _SFR_MEM8(0x01C5)
#define NVM_DATA2  _SFR_MEM8(0x01C6)
#define NVM_CMD  _SFR_MEM8(0x01CA)
#define NVM_CTRLA  _SFR_MEM8(0x01CB)
#define NVM_CTRLB  _SFR_MEM8(0x01CC)
#define NVM_INTCTRL  _SFR_MEM8(0x01CD)
#define NVM_STATUS  _SFR_MEM8(0x01CF)
#define NVM_LOCKBITS  _SFR_MEM8(0x01D0)

/* ADC - Analog-to-Digital Converter */
#define ADCA_CTRLA  _SFR_MEM8(0x0200)
#define ADCA_CTRLB  _SFR_MEM8(0x0201)
#define ADCA_REFCTRL  _SFR_MEM8(0x0202)
#define ADCA_EVCTRL  _SFR_MEM8(0x0203)
#define ADCA_PRESCALER  _SFR_MEM8(0x0204)
#define ADCA_INTFLAGS  _SFR_MEM8(0x0206)
#define ADCA_TEMP  _SFR_MEM8(0x0207)
#define ADCA_SAMPCTRL  _SFR_MEM8(0x0208)
#define ADCA_CAL  _SFR_MEM16(0x020C)
#define ADCA_CH0RES  _SFR_MEM16(0x0210)
#define ADCA_CMP  _SFR_MEM16(0x0218)
#define ADCA_CH0_CTRL  _SFR_MEM8(0x0220)
#define ADCA_CH0_MUXCTRL  _SFR_MEM8(0x0221)
#define ADCA_CH0_INTCTRL  _SFR_MEM8(0x0222)
#define ADCA_CH0_INTFLAGS  _SFR_MEM8(0x0223)
#define ADCA_CH0_RES  _SFR_MEM16(0x0224)
#define ADCA_CH0_SCAN  _SFR_MEM8(0x0226)

/* ADC - Analog-to-Digital Converter */
#define ADCB_CTRLA  _SFR_MEM8(0x0240)
#define ADCB_CTRLB  _SFR_MEM8(0x0241)
#define ADCB_REFCTRL  _SFR_MEM8(0x0242)
#define ADCB_EVCTRL  _SFR_MEM8(0x0243)
#define ADCB_PRESCALER  _SFR_MEM8(0x0244)
#define ADCB_INTFLAGS  _SFR_MEM8(0x0246)
#define ADCB_TEMP  _SFR_MEM8(0x0247)
#define ADCB_SAMPCTRL  _SFR_MEM8(0x0248)
#define ADCB_CAL  _SFR_MEM16(0x024C)
#define ADCB_CH0RES  _SFR_MEM16(0x0250)
#define ADCB_CMP  _SFR_MEM16(0x0258)
#define ADCB_CH0_CTRL  _SFR_MEM8(0x0260)
#define ADCB_CH0_MUXCTRL  _SFR_MEM8(0x0261)
#define ADCB_CH0_INTCTRL  _SFR_MEM8(0x0262)
#define ADCB_CH0_INTFLAGS  _SFR_MEM8(0x0263)
#define ADCB_CH0_RES  _SFR_MEM16(0x0264)
#define ADCB_CH0_SCAN  _SFR_MEM8(0x0266)

/* AC - Analog Comparator */
#define ACA_AC0CTRL  _SFR_MEM8(0x0380)
#define ACA_AC1CTRL  _SFR_MEM8(0x0381)
#define ACA_AC0MUXCTRL  _SFR_MEM8(0x0382)
#define ACA_AC1MUXCTRL  _SFR_MEM8(0x0383)
#define ACA_CTRLA  _SFR_MEM8(0x0384)
#define ACA_CTRLB  _SFR_MEM8(0x0385)
#define ACA_WINCTRL  _SFR_MEM8(0x0386)
#define ACA_STATUS  _SFR_MEM8(0x0387)
#define ACA_CURRCTRL  _SFR_MEM8(0x0388)
#define ACA_CURRCALIB  _SFR_MEM8(0x0389)

/* AC - Analog Comparator */
#define ACB_AC0CTRL  _SFR_MEM8(0x0390)
#define ACB_AC1CTRL  _SFR_MEM8(0x0391)
#define ACB_AC0MUXCTRL  _SFR_MEM8(0x0392)
#define ACB_AC1MUXCTRL  _SFR_MEM8(0x0393)
#define ACB_CTRLA  _SFR_MEM8(0x0394)
#define ACB_CTRLB  _SFR_MEM8(0x0395)
#define ACB_WINCTRL  _SFR_MEM8(0x0396)
#define ACB_STATUS  _SFR_MEM8(0x0397)
#define ACB_CURRCTRL  _SFR_MEM8(0x0398)
#define ACB_CURRCALIB  _SFR_MEM8(0x0399)

/* RTC - Real-Time Counter */
#define RTC_CTRL  _SFR_MEM8(0x0400)
#define RTC_STATUS  _SFR_MEM8(0x0401)
#define RTC_INTCTRL  _SFR_MEM8(0x0402)
#define RTC_INTFLAGS  _SFR_MEM8(0x0403)
#define RTC_TEMP  _SFR_MEM8(0x0404)
#define RTC_CNT  _SFR_MEM16(0x0408)
#define RTC_PER  _SFR_MEM16(0x040A)
#define RTC_COMP  _SFR_MEM16(0x040C)

/* TWI - Two-Wire Interface */
#define TWIC_CTRL  _SFR_MEM8(0x0480)
#define TWIC_MASTER_CTRLA  _SFR_MEM8(0x0481)
#define TWIC_MASTER_CTRLB  _SFR_MEM8(0x0482)
#define TWIC_MASTER_CTRLC  _SFR_MEM8(0x0483)
#define TWIC_MASTER_STATUS  _SFR_MEM8(0x0484)
#define TWIC_MASTER_BAUD  _SFR_MEM8(0x0485)
#define TWIC_MASTER_ADDR  _SFR_MEM8(0x0486)
#define TWIC_MASTER_DATA  _SFR_MEM8(0x0487)
#define TWIC_SLAVE_CTRLA  _SFR_MEM8(0x0488)
#define TWIC_SLAVE_CTRLB  _SFR_MEM8(0x0489)
#define TWIC_SLAVE_STATUS  _SFR_MEM8(0x048A)
#define TWIC_SLAVE_ADDR  _SFR_MEM8(0x048B)
#define TWIC_SLAVE_DATA  _SFR_MEM8(0x048C)
#define TWIC_SLAVE_ADDRMASK  _SFR_MEM8(0x048D)

/* USB - Universal Serial Bus */
#define USB_CTRLA  _SFR_MEM8(0x04C0)
#define USB_CTRLB  _SFR_MEM8(0x04C1)
#define USB_STATUS  _SFR_MEM8(0x04C2)
#define USB_ADDR  _SFR_MEM8(0x04C3)
#define USB_FIFOWP  _SFR_MEM8(0x04C4)
#define USB_FIFORP  _SFR_MEM8(0x04C5)
#define USB_EPPTR  _SFR_MEM16(0x04C6)
#define USB_INTCTRLA  _SFR_MEM8(0x04C8)
#define USB_INTCTRLB  _SFR_MEM8(0x04C9)
#define USB_INTFLAGSACLR  _SFR_MEM8(0x04CA)
#define USB_INTFLAGSASET  _SFR_MEM8(0x04CB)
#define USB_INTFLAGSBCLR  _SFR_MEM8(0x04CC)
#define USB_INTFLAGSBSET  _SFR_MEM8(0x04CD)
#define USB_CAL0  _SFR_MEM8(0x04FA)
#define USB_CAL1  _SFR_MEM8(0x04FB)

/* PORT - I/O Ports */
#define PORTA_DIR  _SFR_MEM8(0x0600)
#define PORTA_DIRSET  _SFR_MEM8(0x0601)
#define PORTA_DIRCLR  _SFR_MEM8(0x0602)
#define PORTA_DIRTGL  _SFR_MEM8(0x0603)
#define PORTA_OUT  _SFR_MEM8(0x0604)
#define PORTA_OUTSET  _SFR_MEM8(0x0605)
#define PORTA_OUTCLR  _SFR_MEM8(0x0606)
#define PORTA_OUTTGL  _SFR_MEM8(0x0607)
#define PORTA_IN  _SFR_MEM8(0x0608)
#define PORTA_INTCTRL  _SFR_MEM8(0x0609)
#define PORTA_INT0MASK  _SFR_MEM8(0x060A)
#define PORTA_INT1MASK  _SFR_MEM8(0x060B)
#define PORTA_INTFLAGS  _SFR_MEM8(0x060C)
#define PORTA_REMAP  _SFR_MEM8(0x060E)
#define PORTA_PIN0CTRL  _SFR_MEM8(0x0610)
#define PORTA_PIN1CTRL  _SFR_MEM8(0x0611)
#define PORTA_PIN2CTRL  _SFR_MEM8(0x0612)
#define PORTA_PIN3CTRL  _SFR_MEM8(0x0613)
#define PORTA_PIN4CTRL  _SFR_MEM8(0x0614)
#define PORTA_PIN5CTRL  _SFR_MEM8(0x0615)
#define PORTA_PIN6CTRL  _SFR_MEM8(0x0616)
#define PORTA_PIN7CTRL  _SFR_MEM8(0x0617)

/* PORT - I/O Ports */
#define PORTB_DIR  _SFR_MEM8(0x0620)
#define PORTB_DIRSET  _SFR_MEM8(0x0621)
#define PORTB_DIRCLR  _SFR_MEM8(0x0622)
#define PORTB_DIRTGL  _SFR_MEM8(0x0623)
#define PORTB_OUT  _SFR_MEM8(0x0624)
#define PORTB_OUTSET  _SFR_MEM8(0x0625)
#define PORTB_OUTCLR  _SFR_MEM8(0x0626)
#define PORTB_OUTTGL  _SFR_MEM8(0x0627)
#define PORTB_IN  _SFR_MEM8(0x0628)
#define PORTB_INTCTRL  _SFR_MEM8(0x0629)
#define PORTB_INT0MASK  _SFR_MEM8(0x062A)
#define PORTB_INT1MASK  _SFR_MEM8(0x062B)
#define PORTB_INTFLAGS  _SFR_MEM8(0x062C)
#define PORTB_REMAP  _SFR_MEM8(0x062E)
#define PORTB_PIN0CTRL  _SFR_MEM8(0x0630)
#define PORTB_PIN1CTRL  _SFR_MEM8(0x0631)
#define PORTB_PIN2CTRL  _SFR_MEM8(0x0632)
#define PORTB_PIN3CTRL  _SFR_MEM8(0x0633)
#define PORTB_PIN4CTRL  _SFR_MEM8(0x0634)
#define PORTB_PIN5CTRL  _SFR_MEM8(0x0635)
#define PORTB_PIN6CTRL  _SFR_MEM8(0x0636)
#define PORTB_PIN7CTRL  _SFR_MEM8(0x0637)

/* PORT - I/O Ports */
#define PORTC_DIR  _SFR_MEM8(0x0640)
#define PORTC_DIRSET  _SFR_MEM8(0x0641)
#define PORTC_DIRCLR  _SFR_MEM8(0x0642)
#define PORTC_DIRTGL  _SFR_MEM8(0x0643)
#define PORTC_OUT  _SFR_MEM8(0x0644)
#define PORTC_OUTSET  _SFR_MEM8(0x0645)
#define PORTC_OUTCLR  _SFR_MEM8(0x0646)
#define PORTC_OUTTGL  _SFR_MEM8(0x0647)
#define PORTC_IN  _SFR_MEM8(0x0648)
#define PORTC_INTCTRL  _SFR_MEM8(0x0649)
#define PORTC_INT0MASK  _SFR_MEM8(0x064A)
#define PORTC_INT1MASK  _SFR_MEM8(0x064B)
#define PORTC_INTFLAGS  _SFR_MEM8(0x064C)
#define PORTC_REMAP  _SFR_MEM8(0x064E)
#define PORTC_PIN0CTRL  _SFR_MEM8(0x0650)
#define PORTC_PIN1CTRL  _SFR_MEM8(0x0651)
#define PORTC_PIN2CTRL  _SFR_MEM8(0x0652)
#define PORTC_PIN3CTRL  _SFR_MEM8(0x0653)
#define PORTC_PIN4CTRL  _SFR_MEM8(0x0654)
#define PORTC_PIN5CTRL  _SFR_MEM8(0x0655)
#define PORTC_PIN6CTRL  _SFR_MEM8(0x0656)
#define PORTC_PIN7CTRL  _SFR_MEM8(0x0657)

/* PORT - I/O Ports */
#define PORTD_DIR  _SFR_MEM8(0x0660)
#define PORTD_DIRSET  _SFR_MEM8(0x0661)
#define PORTD_DIRCLR  _SFR_MEM8(0x0662)
#define PORTD_DIRTGL  _SFR_MEM8(0x0663)
#define PORTD_OUT  _SFR_MEM8(0x0664)
#define PORTD_OUTSET  _SFR_MEM8(0x0665)
#define PORTD_OUTCLR  _SFR_MEM8(0x0666)
#define PORTD_OUTTGL  _SFR_MEM8(0x0667)
#define PORTD_IN  _SFR_MEM8(0x0668)
#define PORTD_INTCTRL  _SFR_MEM8(0x0669)
#define PORTD_INT0MASK  _SFR_MEM8(0x066A)
#define PORTD_INT1MASK  _SFR_MEM8(0x066B)
#define PORTD_INTFLAGS  _SFR_MEM8(0x066C)
#define PORTD_REMAP  _SFR_MEM8(0x066E)
#define PORTD_PIN0CTRL  _SFR_MEM8(0x0670)
#define PORTD_PIN1CTRL  _SFR_MEM8(0x0671)
#define PORTD_PIN2CTRL  _SFR_MEM8(0x0672)
#define PORTD_PIN3CTRL  _SFR_MEM8(0x0673)
#define PORTD_PIN4CTRL  _SFR_MEM8(0x0674)
#define PORTD_PIN5CTRL  _SFR_MEM8(0x0675)
#define PORTD_PIN6CTRL  _SFR_MEM8(0x0676)
#define PORTD_PIN7CTRL  _SFR_MEM8(0x0677)

/* PORT - I/O Ports */
#define PORTE_DIR  _SFR_MEM8(0x0680)
#define PORTE_DIRSET  _SFR_MEM8(0x0681)
#define PORTE_DIRCLR  _SFR_MEM8(0x0682)
#define PORTE_DIRTGL  _SFR_MEM8(0x0683)
#define PORTE_OUT  _SFR_MEM8(0x0684)
#define PORTE_OUTSET  _SFR_MEM8(0x0685)
#define PORTE_OUTCLR  _SFR_MEM8(0x0686)
#define PORTE_OUTTGL  _SFR_MEM8(0x0687)
#define PORTE_IN  _SFR_MEM8(0x0688)
#define PORTE_INTCTRL  _SFR_MEM8(0x0689)
#define PORTE_INT0MASK  _SFR_MEM8(0x068A)
#define PORTE_INT1MASK  _SFR_MEM8(0x068B)
#define PORTE_INTFLAGS  _SFR_MEM8(0x068C)
#define PORTE_REMAP  _SFR_MEM8(0x068E)
#define PORTE_PIN0CTRL  _SFR_MEM8(0x0690)
#define PORTE_PIN1CTRL  _SFR_MEM8(0x0691)
#define PORTE_PIN2CTRL  _SFR_MEM8(0x0692)
#define PORTE_PIN3CTRL  _SFR_MEM8(0x0693)
#define PORTE_PIN4CTRL  _SFR_MEM8(0x0694)
#define PORTE_PIN5CTRL  _SFR_MEM8(0x0695)
#define PORTE_PIN6CTRL  _SFR_MEM8(0x0696)
#define PORTE_PIN7CTRL  _SFR_MEM8(0x0697)

/* PORT - I/O Ports */
#define PORTG_DIR  _SFR_MEM8(0x06C0)
#define PORTG_DIRSET  _SFR_MEM8(0x06C1)
#define PORTG_DIRCLR  _SFR_MEM8(0x06C2)
#define PORTG_DIRTGL  _SFR_MEM8(0x06C3)
#define PORTG_OUT  _SFR_MEM8(0x06C4)
#define PORTG_OUTSET  _SFR_MEM8(0x06C5)
#define PORTG_OUTCLR  _SFR_MEM8(0x06C6)
#define PORTG_OUTTGL  _SFR_MEM8(0x06C7)
#define PORTG_IN  _SFR_MEM8(0x06C8)
#define PORTG_INTCTRL  _SFR_MEM8(0x06C9)
#define PORTG_INT0MASK  _SFR_MEM8(0x06CA)
#define PORTG_INT1MASK  _SFR_MEM8(0x06CB)
#define PORTG_INTFLAGS  _SFR_MEM8(0x06CC)
#define PORTG_REMAP  _SFR_MEM8(0x06CE)
#define PORTG_PIN0CTRL  _SFR_MEM8(0x06D0)
#define PORTG_PIN1CTRL  _SFR_MEM8(0x06D1)
#define PORTG_PIN2CTRL  _SFR_MEM8(0x06D2)
#define PORTG_PIN3CTRL  _SFR_MEM8(0x06D3)
#define PORTG_PIN4CTRL  _SFR_MEM8(0x06D4)
#define PORTG_PIN5CTRL  _SFR_MEM8(0x06D5)
#define PORTG_PIN6CTRL  _SFR_MEM8(0x06D6)
#define PORTG_PIN7CTRL  _SFR_MEM8(0x06D7)

/* PORT - I/O Ports */
#define PORTM_DIR  _SFR_MEM8(0x0760)
#define PORTM_DIRSET  _SFR_MEM8(0x0761)
#define PORTM_DIRCLR  _SFR_MEM8(0x0762)
#define PORTM_DIRTGL  _SFR_MEM8(0x0763)
#define PORTM_OUT  _SFR_MEM8(0x0764)
#define PORTM_OUTSET  _SFR_MEM8(0x0765)
#define PORTM_OUTCLR  _SFR_MEM8(0x0766)
#define PORTM_OUTTGL  _SFR_MEM8(0x0767)
#define PORTM_IN  _SFR_MEM8(0x0768)
#define PORTM_INTCTRL  _SFR_MEM8(0x0769)
#define PORTM_INT0MASK  _SFR_MEM8(0x076A)
#define PORTM_INT1MASK  _SFR_MEM8(0x076B)
#define PORTM_INTFLAGS  _SFR_MEM8(0x076C)
#define PORTM_REMAP  _SFR_MEM8(0x076E)
#define PORTM_PIN0CTRL  _SFR_MEM8(0x0770)
#define PORTM_PIN1CTRL  _SFR_MEM8(0x0771)
#define PORTM_PIN2CTRL  _SFR_MEM8(0x0772)
#define PORTM_PIN3CTRL  _SFR_MEM8(0x0773)
#define PORTM_PIN4CTRL  _SFR_MEM8(0x0774)
#define PORTM_PIN5CTRL  _SFR_MEM8(0x0775)
#define PORTM_PIN6CTRL  _SFR_MEM8(0x0776)
#define PORTM_PIN7CTRL  _SFR_MEM8(0x0777)

/* PORT - I/O Ports */
#define PORTR_DIR  _SFR_MEM8(0x07E0)
#define PORTR_DIRSET  _SFR_MEM8(0x07E1)
#define PORTR_DIRCLR  _SFR_MEM8(0x07E2)
#define PORTR_DIRTGL  _SFR_MEM8(0x07E3)
#define PORTR_OUT  _SFR_MEM8(0x07E4)
#define PORTR_OUTSET  _SFR_MEM8(0x07E5)
#define PORTR_OUTCLR  _SFR_MEM8(0x07E6)
#define PORTR_OUTTGL  _SFR_MEM8(0x07E7)
#define PORTR_IN  _SFR_MEM8(0x07E8)
#define PORTR_INTCTRL  _SFR_MEM8(0x07E9)
#define PORTR_INT0MASK  _SFR_MEM8(0x07EA)
#define PORTR_INT1MASK  _SFR_MEM8(0x07EB)
#define PORTR_INTFLAGS  _SFR_MEM8(0x07EC)
#define PORTR_REMAP  _SFR_MEM8(0x07EE)
#define PORTR_PIN0CTRL  _SFR_MEM8(0x07F0)
#define PORTR_PIN1CTRL  _SFR_MEM8(0x07F1)
#define PORTR_PIN2CTRL  _SFR_MEM8(0x07F2)
#define PORTR_PIN3CTRL  _SFR_MEM8(0x07F3)
#define PORTR_PIN4CTRL  _SFR_MEM8(0x07F4)
#define PORTR_PIN5CTRL  _SFR_MEM8(0x07F5)
#define PORTR_PIN6CTRL  _SFR_MEM8(0x07F6)
#define PORTR_PIN7CTRL  _SFR_MEM8(0x07F7)

/* TC0 - 16-bit Timer/Counter 0 */
#define TCC0_CTRLA  _SFR_MEM8(0x0800)
#define TCC0_CTRLB  _SFR_MEM8(0x0801)
#define TCC0_CTRLC  _SFR_MEM8(0x0802)
#define TCC0_CTRLD  _SFR_MEM8(0x0803)
#define TCC0_CTRLE  _SFR_MEM8(0x0804)
#define TCC0_INTCTRLA  _SFR_MEM8(0x0806)
#define TCC0_INTCTRLB  _SFR_MEM8(0x0807)
#define TCC0_CTRLFCLR  _SFR_MEM8(0x0808)
#define TCC0_CTRLFSET  _SFR_MEM8(0x0809)
#define TCC0_CTRLGCLR  _SFR_MEM8(0x080A)
#define TCC0_CTRLGSET  _SFR_MEM8(0x080B)
#define TCC0_INTFLAGS  _SFR_MEM8(0x080C)
#define TCC0_TEMP  _SFR_MEM8(0x080F)
#define TCC0_CNT  _SFR_MEM16(0x0820)
#define TCC0_PER  _SFR_MEM16(0x0826)
#define TCC0_CCA  _SFR_MEM16(0x0828)
#define TCC0_CCB  _SFR_MEM16(0x082A)
#define TCC0_CCC  _SFR_MEM16(0x082C)
#define TCC0_CCD  _SFR_MEM16(0x082E)
#define TCC0_PERBUF  _SFR_MEM16(0x0836)
#define TCC0_CCABUF  _SFR_MEM16(0x0838)
#define TCC0_CCBBUF  _SFR_MEM16(0x083A)
#define TCC0_CCCBUF  _SFR_MEM16(0x083C)
#define TCC0_CCDBUF  _SFR_MEM16(0x083E)

/* TC1 - 16-bit Timer/Counter 1 */
#define TCC1_CTRLA  _SFR_MEM8(0x0840)
#define TCC1_CTRLB  _SFR_MEM8(0x0841)
#define TCC1_CTRLC  _SFR_MEM8(0x0842)
#define TCC1_CTRLD  _SFR_MEM8(0x0843)
#define TCC1_CTRLE  _SFR_MEM8(0x0844)
#define TCC1_INTCTRLA  _SFR_MEM8(0x0846)
#define TCC1_INTCTRLB  _SFR_MEM8(0x0847)
#define TCC1_CTRLFCLR  _SFR_MEM8(0x0848)
#define TCC1_CTRLFSET  _SFR_MEM8(0x0849)
#define TCC1_CTRLGCLR  _SFR_MEM8(0x084A)
#define TCC1_CTRLGSET  _SFR_MEM8(0x084B)
#define TCC1_INTFLAGS  _SFR_MEM8(0x084C)
#define TCC1_TEMP  _SFR_MEM8(0x084F)
#define TCC1_CNT  _SFR_MEM16(0x0860)
#define TCC1_PER  _SFR_MEM16(0x0866)
#define TCC1_CCA  _SFR_MEM16(0x0868)
#define TCC1_CCB  _SFR_MEM16(0x086A)
#define TCC1_PERBUF  _SFR_MEM16(0x0876)
#define TCC1_CCABUF  _SFR_MEM16(0x0878)
#define TCC1_CCBBUF  _SFR_MEM16(0x087A)

/* AWEX - Advanced Waveform Extension */
#define AWEXC_CTRL  _SFR_MEM8(0x0880)
#define AWEXC_FDEMASK  _SFR_MEM8(0x0882)
#define AWEXC_FDCTRL  _SFR_MEM8(0x0883)
#define AWEXC_STATUS  _SFR_MEM8(0x0884)
#define AWEXC_STATUSSET  _SFR_MEM8(0x0885)
#define AWEXC_DTBOTH  _SFR_MEM8(0x0886)
#define AWEXC_DTBOTHBUF  _SFR_MEM8(0x0887)
#define AWEXC_DTLS  _SFR_MEM8(0x0888)
#define AWEXC_DTHS  _SFR_MEM8(0x0889)
#define AWEXC_DTLSBUF  _SFR_MEM8(0x088A)
#define AWEXC_DTHSBUF  _SFR_MEM8(0x088B)
#define AWEXC_OUTOVEN  _SFR_MEM8(0x088C)

/* HIRES - High-Resolution Extension */
#define HIRESC_CTRLA  _SFR_MEM8(0x0890)

/* USART - Universal Synchronous/Asynchronous Receiver/Transmitter */
#define USARTC0_DATA  _SFR_MEM8(0x08A0)
#define USARTC0_STATUS  _SFR_MEM8(0x08A1)
#define USARTC0_CTRLA  _SFR_MEM8(0x08A3)
#define USARTC0_CTRLB  _SFR_MEM8(0x08A4)
#define USARTC0_CTRLC  _SFR_MEM8(0x08A5)
#define USARTC0_BAUDCTRLA  _SFR_MEM8(0x08A6)
#define USARTC0_BAUDCTRLB  _SFR_MEM8(0x08A7)

/* SPI - Serial Peripheral Interface */
#define SPIC_CTRL  _SFR_MEM8(0x08C0)
#define SPIC_INTCTRL  _SFR_MEM8(0x08C1)
#define SPIC_STATUS  _SFR_MEM8(0x08C2)
#define SPIC_DATA  _SFR_MEM8(0x08C3)

/* IRCOM - IR Communication Module */
#define IRCOM_CTRL  _SFR_MEM8(0x08F8)
#define IRCOM_TXPLCTRL  _SFR_MEM8(0x08F9)
#define IRCOM_RXPLCTRL  _SFR_MEM8(0x08FA)

/* TC0 - 16-bit Timer/Counter 0 */
#define TCE0_CTRLA  _SFR_MEM8(0x0A00)
#define TCE0_CTRLB  _SFR_MEM8(0x0A01)
#define TCE0_CTRLC  _SFR_MEM8(0x0A02)
#define TCE0_CTRLD  _SFR_MEM8(0x0A03)
#define TCE0_CTRLE  _SFR_MEM8(0x0A04)
#define TCE0_INTCTRLA  _SFR_MEM8(0x0A06)
#define TCE0_INTCTRLB  _SFR_MEM8(0x0A07)
#define TCE0_CTRLFCLR  _SFR_MEM8(0x0A08)
#define TCE0_CTRLFSET  _SFR_MEM8(0x0A09)
#define TCE0_CTRLGCLR  _SFR_MEM8(0x0A0A)
#define TCE0_CTRLGSET  _SFR_MEM8(0x0A0B)
#define TCE0_INTFLAGS  _SFR_MEM8(0x0A0C)
#define TCE0_TEMP  _SFR_MEM8(0x0A0F)
#define TCE0_CNT  _SFR_MEM16(0x0A20)
#define TCE0_PER  _SFR_MEM16(0x0A26)
#define TCE0_CCA  _SFR_MEM16(0x0A28)
#define TCE0_CCB  _SFR_MEM16(0x0A2A)
#define TCE0_CCC  _SFR_MEM16(0x0A2C)
#define TCE0_CCD  _SFR_MEM16(0x0A2E)
#define TCE0_PERBUF  _SFR_MEM16(0x0A36)
#define TCE0_CCABUF  _SFR_MEM16(0x0A38)
#define TCE0_CCBBUF  _SFR_MEM16(0x0A3A)
#define TCE0_CCCBUF  _SFR_MEM16(0x0A3C)
#define TCE0_CCDBUF  _SFR_MEM16(0x0A3E)

/* USART - Universal Synchronous/Asynchronous Receiver/Transmitter */
#define USARTE0_DATA  _SFR_MEM8(0x0AA0)
#define USARTE0_STATUS  _SFR_MEM8(0x0AA1)
#define USARTE0_CTRLA  _SFR_MEM8(0x0AA3)
#define USARTE0_CTRLB  _SFR_MEM8(0x0AA4)
#define USARTE0_CTRLC  _SFR_MEM8(0x0AA5)
#define USARTE0_BAUDCTRLA  _SFR_MEM8(0x0AA6)
#define USARTE0_BAUDCTRLB  _SFR_MEM8(0x0AA7)

/* LCD - LCD Controller */
#define LCD_CTRLA  _SFR_MEM8(0x0D00)
#define LCD_CTRLB  _SFR_MEM8(0x0D01)
#define LCD_CTRLC  _SFR_MEM8(0x0D02)
#define LCD_INTCTRL  _SFR_MEM8(0x0D03)
#define LCD_INTFLAG  _SFR_MEM8(0x0D04)
#define LCD_CTRLD  _SFR_MEM8(0x0D05)
#define LCD_CTRLE  _SFR_MEM8(0x0D06)
#define LCD_CTRLF  _SFR_MEM8(0x0D07)
#define LCD_CTRLG  _SFR_MEM8(0x0D08)
#define LCD_CTRLH  _SFR_MEM8(0x0D09)
#define LCD_DATA0  _SFR_MEM8(0x0D10)
#define LCD_DATA1  _SFR_MEM8(0x0D11)
#define LCD_DATA2  _SFR_MEM8(0x0D12)
#define LCD_DATA3  _SFR_MEM8(0x0D13)
#define LCD_DATA4  _SFR_MEM8(0x0D14)
#define LCD_DATA5  _SFR_MEM8(0x0D15)
#define LCD_DATA6  _SFR_MEM8(0x0D16)
#define LCD_DATA7  _SFR_MEM8(0x0D17)
#define LCD_DATA8  _SFR_MEM8(0x0D18)
#define LCD_DATA9  _SFR_MEM8(0x0D19)
#define LCD_DATA10  _SFR_MEM8(0x0D1A)
#define LCD_DATA11  _SFR_MEM8(0x0D1B)
#define LCD_DATA12  _SFR_MEM8(0x0D1C)
#define LCD_DATA13  _SFR_MEM8(0x0D1D)
#define LCD_DATA14  _SFR_MEM8(0x0D1E)
#define LCD_DATA15  _SFR_MEM8(0x0D1F)
#define LCD_DATA16  _SFR_MEM8(0x0D20)
#define LCD_DATA17  _SFR_MEM8(0x0D21)
#define LCD_DATA18  _SFR_MEM8(0x0D22)
#define LCD_DATA19  _SFR_MEM8(0x0D23)



/*================== Bitfield Definitions ================== */

/* VPORT - Virtual Ports */
/* VPORT.INTFLAGS  bit masks and bit positions */
#define VPORT_INT1IF_bm  0x02  /* Port Interrupt 1 Flag bit mask. */
#define VPORT_INT1IF_bp  1  /* Port Interrupt 1 Flag bit position. */

#define VPORT_INT0IF_bm  0x01  /* Port Interrupt 0 Flag bit mask. */
#define VPORT_INT0IF_bp  0  /* Port Interrupt 0 Flag bit position. */

/* XOCD - On-Chip Debug System */
/* OCD.OCDR0  bit masks and bit positions */
#define OCD_OCDRD_gm  0xFF  /* OCDR Dirty group mask. */
#define OCD_OCDRD_gp  0  /* OCDR Dirty group position. */
#define OCD_OCDRD0_bm  (1<<0)  /* OCDR Dirty bit 0 mask. */
#define OCD_OCDRD0_bp  0  /* OCDR Dirty bit 0 position. */
#define OCD_OCDRD1_bm  (1<<1)  /* OCDR Dirty bit 1 mask. */
#define OCD_OCDRD1_bp  1  /* OCDR Dirty bit 1 position. */
#define OCD_OCDRD2_bm  (1<<2)  /* OCDR Dirty bit 2 mask. */
#define OCD_OCDRD2_bp  2  /* OCDR Dirty bit 2 position. */
#define OCD_OCDRD3_bm  (1<<3)  /* OCDR Dirty bit 3 mask. */
#define OCD_OCDRD3_bp  3  /* OCDR Dirty bit 3 position. */
#define OCD_OCDRD4_bm  (1<<4)  /* OCDR Dirty bit 4 mask. */
#define OCD_OCDRD4_bp  4  /* OCDR Dirty bit 4 position. */
#define OCD_OCDRD5_bm  (1<<5)  /* OCDR Dirty bit 5 mask. */
#define OCD_OCDRD5_bp  5  /* OCDR Dirty bit 5 position. */
#define OCD_OCDRD6_bm  (1<<6)  /* OCDR Dirty bit 6 mask. */
#define OCD_OCDRD6_bp  6  /* OCDR Dirty bit 6 position. */
#define OCD_OCDRD7_bm  (1<<7)  /* OCDR Dirty bit 7 mask. */
#define OCD_OCDRD7_bp  7  /* OCDR Dirty bit 7 position. */

/* OCD.OCDR1  bit masks and bit positions */
/* OCD_OCDRD  Predefined. */
/* OCD_OCDRD  Predefined. */

/* CPU - CPU */
/* CPU.CCP  bit masks and bit positions */
#define CPU_CCP_gm  0xFF  /* CCP signature group mask. */
#define CPU_CCP_gp  0  /* CCP signature group position. */
#define CPU_CCP0_bm  (1<<0)  /* CCP signature bit 0 mask. */
#define CPU_CCP0_bp  0  /* CCP signature bit 0 position. */
#define CPU_CCP1_bm  (1<<1)  /* CCP signature bit 1 mask. */
#define CPU_CCP1_bp  1  /* CCP signature bit 1 position. */
#define CPU_CCP2_bm  (1<<2)  /* CCP signature bit 2 mask. */
#define CPU_CCP2_bp  2  /* CCP signature bit 2 position. */
#define CPU_CCP3_bm  (1<<3)  /* CCP signature bit 3 mask. */
#define CPU_CCP3_bp  3  /* CCP signature bit 3 position. */
#define CPU_CCP4_bm  (1<<4)  /* CCP signature bit 4 mask. */
#define CPU_CCP4_bp  4  /* CCP signature bit 4 position. */
#define CPU_CCP5_bm  (1<<5)  /* CCP signature bit 5 mask. */
#define CPU_CCP5_bp  5  /* CCP signature bit 5 position. */
#define CPU_CCP6_bm  (1<<6)  /* CCP signature bit 6 mask. */
#define CPU_CCP6_bp  6  /* CCP signature bit 6 position. */
#define CPU_CCP7_bm  (1<<7)  /* CCP signature bit 7 mask. */
#define CPU_CCP7_bp  7  /* CCP signature bit 7 position. */

/* CPU.SREG  bit masks and bit positions */
#define CPU_I_bm  0x80  /* Global Interrupt Enable Flag bit mask. */
#define CPU_I_bp  7  /* Global Interrupt Enable Flag bit position. */

#define CPU_T_bm  0x40  /* Transfer Bit bit mask. */
#define CPU_T_bp  6  /* Transfer Bit bit position. */

#define CPU_H_bm  0x20  /* Half Carry Flag bit mask. */
#define CPU_H_bp  5  /* Half Carry Fl