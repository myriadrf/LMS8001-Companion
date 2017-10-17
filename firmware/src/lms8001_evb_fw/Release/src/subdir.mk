################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/_write.c \
../src/i2csw.c \
../src/main.c \
../src/stm32fxxx_it.c \
../src/usb_bsp.c \
../src/usbd_cdc_vcp.c \
../src/usbd_desc.c \
../src/usbd_usr.c 

OBJS += \
./src/_write.o \
./src/i2csw.o \
./src/main.o \
./src/stm32fxxx_it.o \
./src/usb_bsp.o \
./src/usbd_cdc_vcp.o \
./src/usbd_desc.o \
./src/usbd_usr.o 

C_DEPS += \
./src/_write.d \
./src/i2csw.d \
./src/main.d \
./src/stm32fxxx_it.d \
./src/usb_bsp.d \
./src/usbd_cdc_vcp.d \
./src/usbd_desc.d \
./src/usbd_usr.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross ARM C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m3 -mthumb -O3 -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections -ffreestanding -fsingle-precision-constant -flto -Wall -Wextra  -g -DOS_USE_TRACE_SEMIHOSTING_STDOUT -DUSE_STM3210C_EVAL -DUSE_USB_OTG_FS -DSTM32F10X_CL -DUSE_STDPERIPH_DRIVER -DHSE_VALUE=8000000 -I"../include" -I"C:\mihajlob\svn\lms8001\SW\FW\lms8001_evb_fw\system\include\STM32_USB-OTG-Device_Driver" -I"../system/include" -I"../system/include/cmsis" -I"../system/include/stm32f1-stdperiph" -std=gnu11 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


