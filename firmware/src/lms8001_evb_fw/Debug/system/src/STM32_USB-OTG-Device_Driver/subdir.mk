################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../system/src/STM32_USB-OTG-Device_Driver/usb_core.c \
../system/src/STM32_USB-OTG-Device_Driver/usb_dcd.c \
../system/src/STM32_USB-OTG-Device_Driver/usb_dcd_int.c \
../system/src/STM32_USB-OTG-Device_Driver/usbd_cdc_core.c \
../system/src/STM32_USB-OTG-Device_Driver/usbd_core.c \
../system/src/STM32_USB-OTG-Device_Driver/usbd_ioreq.c \
../system/src/STM32_USB-OTG-Device_Driver/usbd_req.c 

OBJS += \
./system/src/STM32_USB-OTG-Device_Driver/usb_core.o \
./system/src/STM32_USB-OTG-Device_Driver/usb_dcd.o \
./system/src/STM32_USB-OTG-Device_Driver/usb_dcd_int.o \
./system/src/STM32_USB-OTG-Device_Driver/usbd_cdc_core.o \
./system/src/STM32_USB-OTG-Device_Driver/usbd_core.o \
./system/src/STM32_USB-OTG-Device_Driver/usbd_ioreq.o \
./system/src/STM32_USB-OTG-Device_Driver/usbd_req.o 

C_DEPS += \
./system/src/STM32_USB-OTG-Device_Driver/usb_core.d \
./system/src/STM32_USB-OTG-Device_Driver/usb_dcd.d \
./system/src/STM32_USB-OTG-Device_Driver/usb_dcd_int.d \
./system/src/STM32_USB-OTG-Device_Driver/usbd_cdc_core.d \
./system/src/STM32_USB-OTG-Device_Driver/usbd_core.d \
./system/src/STM32_USB-OTG-Device_Driver/usbd_ioreq.d \
./system/src/STM32_USB-OTG-Device_Driver/usbd_req.d 


# Each subdirectory must supply rules for building sources it contributes
system/src/STM32_USB-OTG-Device_Driver/%.o: ../system/src/STM32_USB-OTG-Device_Driver/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross ARM C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m3 -mthumb -Og -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections -ffreestanding -fno-move-loop-invariants -Wall -Wextra  -g3 -DDEBUG -DUSE_USB_OTG_FS -DUSE_STM3210C_EVAL -DUSE_FULL_ASSERT -DSTM32F10X_CL -DUSE_STDPERIPH_DRIVER -DHSE_VALUE=8000000 -I"../include" -I"D:\Lime\Projects\LMS8001\svn\SW\FW\lms8001_evb_fw\system\include\STM32_USB-OTG-Device_Driver" -I"../system/include" -I"../system/include/cmsis" -I"../system/include/stm32f1-stdperiph" -std=gnu11 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


