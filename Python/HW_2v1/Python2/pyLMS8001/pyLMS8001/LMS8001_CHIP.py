
class LMS8001_CHIP(object):
    
    def __init__(self, chip):
        self.chip = chip

    #
    # Read SPI settings
    #

    def __getattr__(self, name):
        if name not in ['SPI_SDIO_DS',
                        'SPI_SDO_DS', 
                        'SPI_SDIO_PE', 
                        'SPI_SDO_PE', 
                        'SPI_SCLK_PE', 
                        'SPI_SEN_PE', 
                        'SPIMODE']:
            raise ValueError("Invalid field name "+str(name))
        return self.chip['SPIConfig'][name]

    #
    # Write SPI settings
    #

    def __setattr__(self, name, value):
        if name == "chip":
            self.__dict__["chip"] = value
            return
        if name not in ['SPI_SDIO_DS',
                        'SPI_SDO_DS', 
                        'SPI_SDIO_PE', 
                        'SPI_SDO_PE', 
                        'SPI_SCLK_PE', 
                        'SPI_SEN_PE', 
                        'SPIMODE']:
            raise ValueError("Invalid field name "+str(name))
        self.chip['SPIConfig'][name] = val
            

