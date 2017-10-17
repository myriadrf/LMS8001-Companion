#define DESCRIPTOR_CONFIGURATION_LEVEL				0
#define DESCRIPTOR_INTERFACEALTSET_LEVEL			1
#define DESCRIPTOR_ENDPOINT_LEVEL					2

#define URB_FUNCTION_VENDOR_DEVICE                   0x0017
#define URB_FUNCTION_VENDOR_INTERFACE                0x0018
#define URB_FUNCTION_VENDOR_ENDPOINT                 0x0019
#define URB_FUNCTION_VENDOR_OTHER                    0x0020

#define URB_FUNCTION_CLASS_DEVICE                    0x001A
#define URB_FUNCTION_CLASS_INTERFACE                 0x001B
#define URB_FUNCTION_CLASS_ENDPOINT                  0x001C
#define URB_FUNCTION_CLASS_OTHER                     0x001F

#define PIPE_RESET						1
#define ABORT_TRANSFER					0

#define VENDOR_DIRECTION_IN				1
#define VENDOR_DIRECTION_OUT			0

typedef struct {
	USHORT Function;
	ULONG Direction;
	UCHAR Request;
	USHORT Value;
	USHORT Index;
	ULONG Length;
} CNTRPIPE_RQ, *PCNTRPIPE_RQ;
