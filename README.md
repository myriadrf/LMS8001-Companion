# LMS8001-Companion

![LimeSDR board](/images/LMS8001-Companion_Top_722w.jpg)

The [LMS8001-Companion](https://myriadrf.org/projects/lms8001-companion/) board provides a highly integrated, highly configurable, four-channel frequency shifter platform, utilising the LMS8001A integrated circuit. One of the typical applications is extending Lime Micro transceiver family RF frequency range up to 10 GHz.

* **LMS8001A Integrated Circuit**
  * Single chip up/down RF frequency shifter with continuous coverage up to 10 GHz RF output range
  * Four independent highly reconfigurable RF paths all driven by the same LO
  * Fully differential signals
  * Few external components
  * Low voltage operation, 1.2 and 1.8V. Integrated LDOs to run on a single 1.8 V supply
  * 56-pin QFN package
  * Serial Port Interface
  * Power down control available via ENABLE pins and/or equivalent SPI registers
  * Synchronous loading of pre-set operation profiles by GPIO pins. More options are also available using corresponding SPI registers
* **Connections**
  * 4 x SMA connectors - RF
  * 4 x UFL connectors – RF
  * 1 x SMA connector – External LO
  * 1 x UFL connector – External clock reference
* **RF Matching**
  * Channel A Input (UFL) – 1–3 GHz broadband, using TC1-1-13M+ balun
  * Channel B Input (UFL) – 1–3 GHz broadband, using TC1-1-13M+ balun
  * Channel C Input (SMA) – 10 GHz band, using NCR2-113+ balun
  * Channel D Input (SMA) – 5 GHz band, using NCR2-113+ balun
  * Channel A Output (SMA) – 10 GHz band, using NCR2-113+ balun
  * Channel B Output (SMA) – 5 GHz band, using NCR2-113+ balun
  * Channel C Output (UFL) – 1–3 GHz broadband, using TC1-1-13M+ balun
  * Channel D Output (UFL) – 1–3 GHz broadband, using TC1-1-13M+ balun
* **USB Interface**
  * USB - mini B (STM32 controller STM32F105RBT6)
* **Clock System**
  * 40MHz on board VCTCXO
  * Possibility to lock VCTCXO to external clock
* **Board Size**
  * 60mm x 100mm (2.36’’ x 3.94’’)

## Contents

The directory structure is as follows:

      docs/                      - Quick Starter Manual

      drivers/                   - STM32 DFU & VCP Windows drivers
         
      firmware/
          docs/                  - Flashing documentation
          firmare/               - Firmware binary build
          src/                   - Firmware sources

      hardware/<version>/
          BOM/                   - bill of materials spreadsheet
          Gerbers/               - Gerber CAM files
          KiCAD/                 - KiCAD schematic and layout files
          Manufacturing/         - Additional manufacturing information
          PDF/                   - Schematic and layout PDFs
          Reports/               - DRC, ERC and drill reports

## Associated projects

### LMS8001 PLL-Sim

An LMS8001 PLL simulator can be found in the [LMS8001-PLL-Sim repository](https://github.com/myriadrf/LMS8001-PLL-Sim).

## Licensing

### Documentation

Documentation is licensed under a Creative Commons Attribution 3.0 Unported licence.

### Hardware

The hardware design is licensed under a Creative Commons Attribution 3.0 Unported licence.

### Firmware

The firmware is licensed under the Apache 2.0 License unless otherwise stated (please see the file headers for details).
