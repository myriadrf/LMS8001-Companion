// ST7DFU.cpp : Defines the entry point for the DLL application.
//

#include "stdafx.h"
#include <winioctl.h>
#include "STDFU.h"

// DFU Commands
//////////////////////////////////////////////////////////////////////

#define DFU_DETACH							0x00
#define DFU_DNLOAD							0x01
#define DFU_UPLOAD							0x02
#define DFU_GETSTATUS						0x03
#define DFU_CLRSTATUS						0x04
#define DFU_GETSTATE						0x05
#define DFU_ABORT							0x06

// DLL Entry
//////////////////////////////////////////////////////////////////////

extern "C"
BOOL WINAPI DllMain(HINSTANCE, DWORD dwReason, LPVOID /*lpReserved*/)
{
	return TRUE;    // ok
}

//////////////////////////////////////////////////////////////////////
//  Gets an handle on the device
//////////////////////////////////////////////////////////////////////
#define PU_SET_TIMEOUT CTL_CODE(FILE_DEVICE_UNKNOWN, 0x0807, METHOD_BUFFERED, FILE_ANY_ACCESS)

STDFU_API STDFU_Open(LPSTR szDevicePath, PHANDLE phDevice)
{
/*	DWORD Result;

	HANDLE Hand=CreateFile(szDevicePath,
					GENERIC_READ | GENERIC_WRITE,
					0,
					NULL,
					OPEN_EXISTING,
					0,
					NULL);
	if (Hand)
	{
		DWORD ByteCount;
		ULONG TimeOut=10000;

		if (DeviceIoControl(Hand,
		                PU_SET_TIMEOUT,
						&TimeOut,
						sizeof(TimeOut),
						NULL,
						0,
						&ByteCount,
						NULL))
			MessageBox(0, "Success", "Success", MB_OK);

		CloseHandle(Hand);
	}*/
	return STDevice_Open(szDevicePath, phDevice, NULL);
}

//////////////////////////////////////////////////////////////////////
//  Releases an handle on the device
//////////////////////////////////////////////////////////////////////
STDFU_API STDFU_Close(PHANDLE phDevice)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	return STDevice_Close(*phDevice);
}

//////////////////////////////////////////////////////////////////////
//  Get the device descriptor
//////////////////////////////////////////////////////////////////////
STDFU_API STDFU_GetDeviceDescriptor(PHANDLE phDevice, PUSB_DEVICE_DESCRIPTOR pDesc)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetDeviceDescriptor(*phDevice, pDesc);
}

//////////////////////////////////////////////////////////////////////
//  Get a string descriptor
//////////////////////////////////////////////////////////////////////
STDFU_API STDFU_GetStringDescriptor	(PHANDLE phDevice, 
											 DWORD Index, 
											 LPSTR szString, 
											 UINT nStringLength)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetStringDescriptor(*phDevice, Index, szString, nStringLength);
}

STDFU_API STDFU_GetNbOfConfigurations(PHANDLE phDevice, PUINT pNbOfConfigs)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetNbOfConfigurations(*phDevice, pNbOfConfigs);
}

STDFU_API STDFU_GetConfigurationDescriptor(PHANDLE phDevice, 
												  UINT nConfigIdx, 
												  PUSB_CONFIGURATION_DESCRIPTOR pDesc)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetConfigurationDescriptor(*phDevice, nConfigIdx, pDesc);
}

STDFU_API STDFU_GetNbOfInterfaces(PHANDLE phDevice, 
										 UINT nConfigIdx, 
										 PUINT pNbOfInterfaces)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetNbOfInterfaces(*phDevice, nConfigIdx, pNbOfInterfaces);
}

STDFU_API STDFU_GetNbOfAlternates(PHANDLE phDevice, 
										 UINT nConfigIdx, 
										 UINT nInterfaceIdx, 
										 PUINT pNbOfAltSets)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetNbOfAlternates(*phDevice, nConfigIdx, nInterfaceIdx, pNbOfAltSets);
}

STDFU_API STDFU_GetInterfaceDescriptor(PHANDLE phDevice, 
											  UINT nConfigIdx, 
											  UINT nInterfaceIdx, 
											  UINT nAltSetIdx, 
											  PUSB_INTERFACE_DESCRIPTOR pDesc)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
		return STDevice_GetInterfaceDescriptor(*phDevice, nConfigIdx, nInterfaceIdx, nAltSetIdx, pDesc);
}

//////////////////////////////////////////////////////////////////////
//  Get the DFU descriptor
//////////////////////////////////////////////////////////////////////
STDFU_API STDFU_GetDFUDescriptor(PHANDLE phDevice, 
									   PUINT pDFUInterfaceNum,
									   PUINT pNbOfAlternates,
									   PDFU_FUNCTIONAL_DESCRIPTOR pDesc)
{
	DWORD Ret;
	UINT NbOfAltSets, NbOfInterfaces;
	USB_INTERFACE_DESCRIPTOR ItfDesc;

	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
	{
		// DFU itnerface should alays be the latest one
		Ret=STDFU_GetNbOfInterfaces(phDevice, 0, &NbOfInterfaces);
		if (Ret==STDEVICE_NOERROR)
		{
			Ret=STDFU_GetNbOfAlternates(phDevice, 
										0, 
										NbOfInterfaces-1, 
										&NbOfAltSets);
			if (Ret==STDEVICE_NOERROR)
			{
				Ret=STDevice_GetDescriptor(*phDevice, 
											DESCRIPTOR_INTERFACEALTSET_LEVEL,
											0x21,
											0, // Configuration 0
											NbOfInterfaces-1, 
											NbOfAltSets-1, // Func desc should be on latest alt set
											0, // Unused
											0,// Index of DFU Interface: the first one
											(PBYTE)pDesc,
											sizeof(DFU_FUNCTIONAL_DESCRIPTOR));
				if (Ret==STDEVICE_NOERROR)
				{
					Ret=STDevice_GetInterfaceDescriptor(*phDevice, 
														0, 
														NbOfInterfaces-1, 
														0,  
														&ItfDesc);
					if (Ret==STDEVICE_NOERROR)
					{
						*pNbOfAlternates=NbOfAltSets;
						*pDFUInterfaceNum=ItfDesc.bInterfaceNumber;
					}

				}
			}
		}
	}
	
	return Ret;
}

/******************************************************************************
// STDFU_SelectCurrentConfiguration: selects the currently active mode for
//              a device, giving the configuration, the interface and the 
//              alternate setting. 
//******************************************************************************/

STDFU_API STDFU_SelectCurrentConfiguration(PHANDLE phDevice, 
												  UINT nConfigIdx, 
												  UINT nInterfaceIdx, 
												  UINT nAltSetIdx)
{
	if (phDevice==NULL)
		return STDFU_BADPARAMETER;
	else
	    return STDevice_SelectCurrentConfiguration(*phDevice, nConfigIdx, nInterfaceIdx, nAltSetIdx);
}

//////////////////////////////////////////////////////////////////////
//  DFU DETACH REQUEST
//////////////////////////////////////////////////////////////////////

STDFU_API STDFU_Detach(PHANDLE phDevice, UCHAR DFUInterfaceNumber )
{
    DWORD Result;
	CNTRPIPE_RQ Request;

	if (phDevice==NULL)
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;
	Request.Direction=VENDOR_DIRECTION_OUT;
	Request.Request=DFU_DETACH;
	Request.Value=5000;
	Request.Index=DFUInterfaceNumber;
	Request.Length=0;
	
	Result= STDevice_ControlPipeRequest(*phDevice, &Request, NULL);
	if (Result==STDEVICE_NOERROR) 
	{
		STDevice_Close(*phDevice);
		*phDevice=NULL;
	}

	return Result;
}


//////////////////////////////////////////////////////////////////////
//  DFU DOWNLOAD REQUEST
//////////////////////////////////////////////////////////////////////

STDFU_API STDFU_Dnload(PHANDLE phDevice, BYTE * pBuffer, ULONG nBytes, USHORT nBlock)
{	
	DWORD Result;
	CNTRPIPE_RQ Request;

	if ( (phDevice==NULL) ||
		 (pBuffer==NULL) )
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;
	Request.Direction=VENDOR_DIRECTION_OUT;
	Request.Request=DFU_DNLOAD;
	Request.Value=nBlock;
	Request.Index=0;
	Request.Length=nBytes;

	Result= STDevice_ControlPipeRequest(*phDevice, &Request, pBuffer);
	return Result;
	
}

//////////////////////////////////////////////////////////////////////
//  DFU UPLOAD REQUEST
//////////////////////////////////////////////////////////////////////


STDFU_API STDFU_Upload(PHANDLE phDevice, BYTE  * pBuffer, ULONG nBytes, USHORT nBlock)
{
	DWORD Result;
	CNTRPIPE_RQ Request;
	
	if ( (phDevice==NULL) ||
		 (pBuffer==NULL) )
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;
	Request.Direction=VENDOR_DIRECTION_IN;
	Request.Request=DFU_UPLOAD;
	Request.Value=nBlock;
	Request.Index=0;
	Request.Length=nBytes; //nBytes;
	
	Result=STDevice_ControlPipeRequest(*phDevice, &Request, pBuffer);
	if (Result!=STDFU_NOERROR)
		Result=GetLastError();
	return Result;
}

//////////////////////////////////////////////////////////////////////
//  DFU GETSTATUS REQUEST
//////////////////////////////////////////////////////////////////////

STDFU_API STDFU_Getstatus(PHANDLE phDevice, DFUSTATUS * DfuStatus)
{
	DWORD Result;
	CNTRPIPE_RQ Request;

	if ( (phDevice==NULL) ||
		 (DfuStatus==NULL) )
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;
	Request.Direction=VENDOR_DIRECTION_IN;
	Request.Request=DFU_GETSTATUS;
	Request.Value=0;
	Request.Index=0;
	Request.Length=6;
	
	Result=STDevice_ControlPipeRequest(*phDevice, &Request, (PBYTE)DfuStatus);
	
	if ( (Result==STDEVICE_NOERROR) && 
		 ( (DfuStatus->bState==STATE_DFU_MANIFEST_WAIT_RESET) ||
		   (DfuStatus->bState==STATE_DFU_MANIFEST) ) )
	{
		STDevice_Close(*phDevice);
		*phDevice=NULL;
	}

	return Result;
}

//////////////////////////////////////////////////////////////////////
//  DFU CLRSTATUS REQUEST
//////////////////////////////////////////////////////////////////////
STDFU_API STDFU_Clrstatus(PHANDLE phDevice)
{
	DWORD Result;
	CNTRPIPE_RQ Request;

	if (phDevice==NULL)
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;;
	Request.Direction=VENDOR_DIRECTION_OUT;
	Request.Request=DFU_CLRSTATUS;
	Request.Value=0;
	Request.Index=0;
	Request.Length=0;
	
	Result= STDevice_ControlPipeRequest(*phDevice, &Request, NULL);
	return Result;

}

//////////////////////////////////////////////////////////////////////
//  DFU GETSTATE REQUEST
//////////////////////////////////////////////////////////////////////

STDFU_API STDFU_Getstate(PHANDLE phDevice, UCHAR * pState)
{

	DWORD Result;
	CNTRPIPE_RQ Request;

	if ( (phDevice==NULL) ||
		 (pState==NULL) )
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;;
	Request.Direction=VENDOR_DIRECTION_IN;
	Request.Request=DFU_GETSTATE;
	Request.Value=0;
	Request.Index=0;
	Request.Length=1;

	Result= STDevice_ControlPipeRequest(*phDevice, &Request, pState);

	return Result;
	
}

//////////////////////////////////////////////////////////////////////
//  DFU ABORT REQUEST
//////////////////////////////////////////////////////////////////////

STDFU_API STDFU_Abort(PHANDLE phDevice)
{
	DWORD Result;
	CNTRPIPE_RQ Request;

	if (phDevice==NULL)
		return STDFU_BADPARAMETER;

	Request.Function=URB_FUNCTION_CLASS_INTERFACE;;
	Request.Direction=VENDOR_DIRECTION_OUT;
	Request.Request=DFU_ABORT;
	Request.Value=0;
	Request.Index=0;
	Request.Length=0;
	
	Result=STDevice_ControlPipeRequest(*phDevice, &Request, NULL);

	return Result;
}

