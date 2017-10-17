#include "stdafx.h"
#include <winioctl.h>
#include "usb100.h"
#include "iocode.h"
#include "STTubeDeviceTyp30.h"
#include "STTubeDeviceErr30.h"
#include "stdevice.h"

#define DEFAULT_TIMEOUT 2000

void print2file(char * c,...)
{
	static char s[1024];
	va_list argptr;
	int cnt;
	va_start(argptr, c);
	cnt = vsprintf(s, c, argptr);
	va_end(argptr);
	OutputDebugString(s);
}

CSTDevice::CSTDevice(CString SymbolicName)
{
	m_SymbolicName=SymbolicName;
	m_DeviceHandle=NULL;
	m_pConfigs=NULL;
	m_CurrentConfig=0;
	m_CurrentInterf=0;
	m_CurrentAltSet=0;
	m_bDeviceIsOpen=FALSE;
	m_nDefaultTimeOut=DEFAULT_TIMEOUT;
	m_nbEndPoints=0;
	m_pPipeHandles=NULL;
}

CSTDevice::~CSTDevice()
{
	Close();
}

DWORD CSTDevice::Open(PHANDLE phUnPlugEvent)
{
	DWORD nRet;

	if (m_bDeviceIsOpen)
		return STDEVICE_NOERROR;

	// 1- Opens the device
	nRet=OpenDevice(phUnPlugEvent);
	if (nRet==STDEVICE_NOERROR)
	{
		// 2- Get the descriptors
		nRet=AllocDescriptors();
		if (nRet!=STDEVICE_NOERROR)
			CloseDevice();
		else
			m_bDeviceIsOpen=TRUE;
	}
	return nRet;
}

DWORD CSTDevice::Close()
{
	if (!m_bDeviceIsOpen)
		return STDEVICE_NOERROR;

	// 1- Close the pipes, if needed
	ClosePipes();
	// 2- Release the descriptors
	ReleaseDescriptors();
	// 3- Close the device
	CloseDevice();

	m_bDeviceIsOpen=FALSE;
	return STDEVICE_NOERROR;
}

DWORD CSTDevice::SelectCurrentConfiguration(UINT ConfigIdx, UINT InterfaceIdx, UINT AltSetIdx)
{
	DWORD nRet;
	BYTE TheConfig[3];
	DWORD ByteCount;
	USB_INTERFACE_DESCRIPTOR Desc;
	PUSB_CONFIGURATION_DESCRIPTOR pConfDesc;

	// Put the InterfaceIdx to -1 if it should not be a search criterion.
	// Put the AltSetIdx to -1 if it should not be a search criterion.

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;
	if (m_pPipeHandles)
		return STDEVICE_PIPESAREOPEN;

	pConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
	nRet=GetInterfaceDescriptor(ConfigIdx,
								InterfaceIdx,
								AltSetIdx,
								&Desc);
	if (nRet!=STDEVICE_NOERROR)
		return nRet;
	m_bDeviceIsOpen=FALSE;
	// 1- Release the descriptors
	ReleaseDescriptors();
	// 2- Set the config
	m_CurrentConfig=ConfigIdx;
	m_CurrentInterf=InterfaceIdx;
	m_CurrentAltSet=AltSetIdx;
	// 3- Get the descriptors
	nRet=AllocDescriptors();
	// 4- Change the current config in the driver
	if (nRet==STDEVICE_NOERROR)
	{
		TheConfig[0]=pConfDesc->bConfigurationValue-1;
		TheConfig[1]=Desc.bInterfaceNumber;
		TheConfig[2]=Desc.bAlternateSetting;
		if (DeviceIoControl(m_DeviceHandle,
							PU_CONFIG,
							TheConfig,
							3,
							NULL,
							0,
							&ByteCount,
							NULL))
			nRet=STDEVICE_NOERROR;
		else
			nRet=STDEVICE_BADPARAMETER;
	}
	if (nRet==STDEVICE_NOERROR)
		m_bDeviceIsOpen=TRUE;
	else
	{
		ClosePipes();
		// 2- Release the descriptors
		ReleaseDescriptors();
		// 3- Close the device
		CloseDevice();
		m_bDeviceIsOpen=FALSE;
	}
	return nRet;
}

DWORD  CSTDevice::OpenDevice(PHANDLE phUnPlugEvent)
{
	// Close first
	CloseDevice();

	m_DeviceHandle=CreateFile(	m_SymbolicName,
								GENERIC_WRITE | GENERIC_READ,
								0,
								NULL,
								OPEN_EXISTING,
								0,
								NULL);
	if (m_DeviceHandle)
	{
		BOOL bFake=m_bDeviceIsOpen;
		DWORD nRet=STDEVICE_NOERROR;

		m_bDeviceIsOpen=TRUE;
		// BUG BUG: Do not issue a reset as Composite devices do not support this !
		//nRet=Reset();
		m_bDeviceIsOpen=bFake;

		// The symbolic name exists. Let's create the disconnect event if needed
		if ( (nRet==STDEVICE_NOERROR) && phUnPlugEvent )
		{
			*phUnPlugEvent=CreateEvent(NULL, FALSE, FALSE, NULL);	// Disconnect event;
  		    if (*phUnPlugEvent)
			{
				DWORD ByteCount;
				if (DeviceIoControl(m_DeviceHandle,
									PU_SET_EVENT_DISCONNECT,
									phUnPlugEvent,
									sizeof(HANDLE),
									NULL,
									0,
									&ByteCount,
									NULL))
					nRet=STDEVICE_NOERROR;
				else
					nRet=STDEVICE_CANTUSEUNPLUGEVENT;
			}
		}
		return nRet;
	}
	return STDEVICE_OPENDRIVERERROR;
}

DWORD CSTDevice::CloseDevice()
{
	if (m_DeviceHandle)
	{
		CloseHandle(m_DeviceHandle);
		m_DeviceHandle=NULL;
	}
	return STDEVICE_NOERROR;
}

DWORD CSTDevice::AllocDescriptors()
{
	BOOL Success;
	DWORD ByteCount;
	int i;
	DWORD nRet=STDEVICE_ERRORDESCRIPTORBUILDING;

	ReleaseDescriptors();

	// Begin to get Device descriptor
	memset(&m_DeviceDescriptor, 0, sizeof(m_DeviceDescriptor));

	Success=DeviceIoControl(m_DeviceHandle,
 			 			    PU_GET_DEVICE_DESCRIPTOR,
							NULL,
							0,
							&m_DeviceDescriptor,
							sizeof(m_DeviceDescriptor),
  							&ByteCount,
							NULL);

	if ( (Success) && (ByteCount==sizeof(m_DeviceDescriptor)) )
	{
		// Get the full configuration
		m_pConfigs=new FULL_CONFIG_INFO[m_DeviceDescriptor.bNumConfigurations];

		if (m_pConfigs)
		{
			for (i=0;i<m_DeviceDescriptor.bNumConfigurations;i++)
			{
				Success=DeviceIoControl(m_DeviceHandle,
										PU_GET_CONFIG_DESCRIPTOR,
										&i,
										 1,
										m_pConfigs[i],
										sizeof(m_pConfigs[i]),
										&ByteCount,
										 NULL);

				if (!Success)
					break;
			}

			if (Success)
			{
				nRet=STDEVICE_NOERROR;
			}
			else
			{
				delete[] m_pConfigs;
				m_pConfigs=NULL;
			}
		}
	}
	return nRet;
}

DWORD CSTDevice::ReleaseDescriptors()
{
	if (m_pConfigs)
	{
		delete[] m_pConfigs;
		m_pConfigs=NULL;
	}

	return STDEVICE_NOERROR;
}

DWORD CSTDevice::OpenPipes()
{
	CString PipeSymbName;
	int i;
	DWORD nRet;
	BOOL bTmp;
	UINT _uiNbOfInterfaces = 0;
	UINT _uiNbOfEndpointsTmp = 0;
	UINT _j = 0, _k = 0;

	ClosePipes();
	// Fake open
	bTmp=m_bDeviceIsOpen;
	m_bDeviceIsOpen=TRUE;

	/*### ===> DE-1184 du 08/03/2009  ML */
	// We must open all the endpoints available on all the configured interfaces 
	nRet = GetNbOfInterfaces(m_CurrentConfig, &_uiNbOfInterfaces);
	if (nRet!=STDEVICE_NOERROR)
	{
		m_bDeviceIsOpen=bTmp;
		return nRet;
	}

	for(_j=0; _j<_uiNbOfInterfaces; _j++)
	{
		nRet=GetNbOfEndPoints(m_CurrentConfig, _j, m_CurrentAltSet, &_uiNbOfEndpointsTmp);
		if (nRet!=STDEVICE_NOERROR)
		{
			m_bDeviceIsOpen=bTmp;
			return nRet;
		}

		m_nbEndPoints += _uiNbOfEndpointsTmp;
	}


	m_pPipeHandles=new HANDLE[m_nbEndPoints];
	
	for(_j=0; _j<_uiNbOfInterfaces; _j++)
	{
		nRet=GetNbOfEndPoints(m_CurrentConfig, _j, m_CurrentAltSet, &_uiNbOfEndpointsTmp);

		if (nRet!=STDEVICE_NOERROR)
		{
			m_bDeviceIsOpen=bTmp;
			return nRet;
		}

		for (i=0;i<(int)_uiNbOfEndpointsTmp;i++)
		{
			// Get endpoint description to see if it's an input or output pipe, and get its address
			USB_ENDPOINT_DESCRIPTOR Desc;
			nRet=GetEndPointDescriptor(m_CurrentConfig, m_CurrentInterf, m_CurrentAltSet, _k, &Desc);
			if (nRet==STDEVICE_NOERROR)
			{
				PipeSymbName.Format("%s\\%02x", m_SymbolicName, Desc.bEndpointAddress);
				m_pPipeHandles[_k]= CreateFile( PipeSymbName,
											   (USB_ENDPOINT_DIRECTION_IN(Desc.bEndpointAddress))?GENERIC_READ:GENERIC_WRITE,
											   0,
											   NULL,
											   OPEN_EXISTING,
											   FILE_FLAG_OVERLAPPED,
											   NULL);

				if ( (!m_pPipeHandles[_k]) || (m_pPipeHandles[_k]==INVALID_HANDLE_VALUE) )
				{
					while (_k>0)
					{
						_k--;
						CloseHandle(m_pPipeHandles[_k]);
						m_pPipeHandles[_k]=INVALID_HANDLE_VALUE;
					}
					delete[] m_pPipeHandles;
					m_pPipeHandles=NULL;
					nRet=STDEVICE_PIPECREATIONERROR;
					break;
				}
				else
				{
					// reset the pipe
					BYTE InBuffer[2];
					DWORD ByteCount;
					InBuffer[0]=Desc.bEndpointAddress;
					InBuffer[1]=1;  // Reset pipe
					
					if (!DeviceIoControl(m_DeviceHandle,
		 		 					PU_PIPE_CONTROL,
									InBuffer,
									2,
									NULL,
									0,
									&ByteCount,
									NULL))
					{
						while (_k>0)
						{
							_k--;
							CloseHandle(m_pPipeHandles[_k]);
							m_pPipeHandles[_k]=INVALID_HANDLE_VALUE;
						}
						delete[] m_pPipeHandles;
						m_pPipeHandles=NULL;
						nRet=STDEVICE_PIPERESETERROR;
						break;
					}
					else
					{
						// Abort any transfer
						BYTE InBuffer[2];
						DWORD ByteCount;
						InBuffer[0]=Desc.bEndpointAddress;
						InBuffer[1]=0;  // Abort
						
						if (!DeviceIoControl(m_DeviceHandle,
					  		 				 PU_PIPE_CONTROL,
											 InBuffer,
											 2,
											 NULL,
											 0,
											 &ByteCount,
											 NULL))
						{
							while (_k>0)
							{
								_k--;
								CloseHandle(m_pPipeHandles[_k]);
								m_pPipeHandles[_k]=INVALID_HANDLE_VALUE;
							}
							delete[] m_pPipeHandles;
							m_pPipeHandles=NULL;
							nRet=STDEVICE_PIPEABORTERROR;
							break;
						}
					}
				}
			}
			else
			{
				while (_k>0)
				{
					_k--;
					CloseHandle(m_pPipeHandles[_k]);
					m_pPipeHandles[_k]=INVALID_HANDLE_VALUE;
				}
				delete[] m_pPipeHandles;
				m_pPipeHandles=NULL;
				nRet=STDEVICE_PIPECREATIONERROR;
				break;
			}

			_k++;
		}
	}
	/*### <=== DE-1184 */
	
	m_bDeviceIsOpen=bTmp;

	return nRet;
}

DWORD CSTDevice::ClosePipes()
{
	UINT i;
	DWORD nRet=STDEVICE_NOERROR;

	if (m_pPipeHandles)
	{
		for (i=0;i<m_nbEndPoints;i++)
		{
			if (m_pPipeHandles[i])
			{
				CloseHandle(m_pPipeHandles[i]);
				m_pPipeHandles[i]=NULL;
			}
		}
		m_nbEndPoints = 0;
		delete[] m_pPipeHandles;
		m_pPipeHandles=NULL;
	}
	return nRet;
}


DWORD CSTDevice::GetStringDescriptor(UINT Index, CString &Desc)
{
	BOOL Success;
	DWORD ByteCount;
	BYTE	strID[4];
	BYTE	OutBuffer[512];
	LPCWSTR lpStr;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if (Index==0)
		return FALSE;

	strID[0]=Index;
	// US Language
	strID[1]=0x04;
	strID[2]=0x09;

	memset(OutBuffer, 0, 512);

	Success=DeviceIoControl(m_DeviceHandle,
							PU_GET_STRING_DESCRIPTOR,
							strID,
							3,
							OutBuffer,
							512,
  							&ByteCount,
							NULL);

	if ( (Success) && (ByteCount>2) && (OutBuffer[1]==3) ) // check string decsriptor type == 3
	{
		lpStr=(LPCWSTR)(OutBuffer+2);
		Desc=lpStr;
		return STDEVICE_NOERROR;
	}
	else
		return STDEVICE_STRINGDESCRIPTORERROR;
}

DWORD CSTDevice::GetDeviceDescriptor(PUSB_DEVICE_DESCRIPTOR pDevDescr)
{
	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	memcpy(pDevDescr, &m_DeviceDescriptor, sizeof(m_DeviceDescriptor));
	return STDEVICE_NOERROR;
}

DWORD CSTDevice::GetNbOfConfigurations(PUINT pNbOfConfigs)
{
	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	*pNbOfConfigs=m_DeviceDescriptor.bNumConfigurations;
	return STDEVICE_NOERROR;
}

DWORD CSTDevice::GetConfigurationDescriptor(UINT ConfigIdx, PUSB_CONFIGURATION_DESCRIPTOR Desc)
{
	DWORD nRet=STDEVICE_NOERROR;
	UINT NbOfConfigs;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	nRet=GetNbOfConfigurations(&NbOfConfigs);
	if (nRet==STDEVICE_NOERROR)
	{
		if (ConfigIdx>=NbOfConfigs)
			nRet=STDEVICE_BADPARAMETER;
		else
			memcpy(Desc, m_pConfigs[ConfigIdx], sizeof(USB_CONFIGURATION_DESCRIPTOR));
	}

	return nRet;
}

DWORD CSTDevice::GetNbOfInterfaces(UINT ConfigIdx, PUINT pNbOfInterfaces)
{
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	DWORD nRet=STDEVICE_NOERROR;
	UINT NbOfConfigs;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	nRet=GetNbOfConfigurations(&NbOfConfigs);
	if (nRet==STDEVICE_NOERROR)
	{
		if (ConfigIdx>=NbOfConfigs)
			nRet=STDEVICE_BADPARAMETER;
		else
		{
			ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
			*pNbOfInterfaces=ConfDesc->bNumInterfaces;
		}
	}
	return nRet;
}

DWORD CSTDevice::GetNbOfAlternates(UINT ConfigIdx, UINT InterfIdx, PUINT pNbOfAltSets)
{
	int Res=1;
	UINT Cnt=0;
	PBYTE pTmp;
	int TotalLength;
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	DWORD nRet=STDEVICE_NOERROR;
	UINT NbOfInterfaces;
	PUSB_INTERFACE_DESCRIPTOR pPreviousInterf=NULL;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	nRet=GetNbOfInterfaces(ConfigIdx, &NbOfInterfaces);
	if (nRet!=STDEVICE_NOERROR)
		return nRet;
	if (InterfIdx>=NbOfInterfaces)
		return STDEVICE_BADPARAMETER;

	pTmp=m_pConfigs[ConfigIdx];
	ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
	TotalLength=ConfDesc->wTotalLength;
	pTmp+=pTmp[0];

	while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
	{
		if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
			return STDEVICE_DESCRIPTORNOTFOUND;

		if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
		{
			PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;

			// increment our index to look for the InterfIdx
			if (pPreviousInterf)
			{
				// See if the current interface descriptor is a different interface or
				// an aleternate of the same one
				if (Cnt==InterfIdx)
				{
					if  (pPreviousInterf->bInterfaceNumber==pInterf->bInterfaceNumber)
						Res++;
					else
						if (Res>1)
							break;
				}
				else
					Cnt++;
			}
			pPreviousInterf=pInterf;
		}
		pTmp+=pTmp[0]; // Switch to next descriptor
	}
	*pNbOfAltSets=Res;
	return STDEVICE_NOERROR;
}

DWORD CSTDevice::GetInterfaceDescriptor(UINT ConfigIdx,
									   UINT InterfIdx,
									   UINT AltIdx,
									   PUSB_INTERFACE_DESCRIPTOR Desc)
{
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	PBYTE pTmp;
	int TotalLength;
	DWORD nRet=STDEVICE_NOERROR;
	UINT NbOfAltSets;
	UINT CntAlt=1, CntInterf=0;
	PUSB_INTERFACE_DESCRIPTOR pPreviousInterf=NULL;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	nRet=GetNbOfAlternates(ConfigIdx, InterfIdx, &NbOfAltSets);
	if (nRet!=STDEVICE_NOERROR)
		return nRet;
	if (AltIdx>=NbOfAltSets)
		return STDEVICE_BADPARAMETER;

	pTmp=m_pConfigs[ConfigIdx];
	ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
	TotalLength=ConfDesc->wTotalLength;
	pTmp+=pTmp[0];

	while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
	{
		if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
			return STDEVICE_DESCRIPTORNOTFOUND;

		if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
		{
			PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;

			// increment our index to look for the InterfIdx
			if (pPreviousInterf)
			{
				// See if the current interface descriptor is a different interface or
				// an aleternate of the same one
				if (CntInterf==InterfIdx)
				{
					if  (pPreviousInterf->bInterfaceNumber==pInterf->bInterfaceNumber)
					{
						if (CntAlt==AltIdx)
						{
							memcpy(Desc, pInterf, sizeof(USB_INTERFACE_DESCRIPTOR));
							break;
						}
						else
							CntAlt++;
					}
					else
						if (CntAlt>0)
							return STDEVICE_DESCRIPTORNOTFOUND;
				}
				else
					CntInterf++;
			}
			else
			{
				if ( (InterfIdx==0) && (AltIdx==0) )
				{
					memcpy(Desc, pInterf, sizeof(USB_INTERFACE_DESCRIPTOR));
					break;
				}
			}
			pPreviousInterf=pInterf;
		}
		pTmp+=pTmp[0]; // Switch to next descriptor
	}

	return STDEVICE_NOERROR;
}

DWORD CSTDevice::GetNbOfEndPoints(UINT ConfigIdx, UINT InterfIdx, UINT AltIdx, PUINT pNbOfEndPoints)
{
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	PBYTE pTmp;
	int TotalLength;
	DWORD nRet=STDEVICE_NOERROR;
	UINT NbOfAltSets;
	UINT CntAlt=1, CntInterf=0;
	PUSB_INTERFACE_DESCRIPTOR pPreviousInterf=NULL;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	nRet=GetNbOfAlternates(ConfigIdx, InterfIdx, &NbOfAltSets);
	if (nRet!=STDEVICE_NOERROR)
		return nRet;
	if (AltIdx>=NbOfAltSets)
		return STDEVICE_BADPARAMETER;

	pTmp=m_pConfigs[ConfigIdx];
	ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
	TotalLength=ConfDesc->wTotalLength;
	pTmp+=pTmp[0];

	while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
	{
		if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
			return STDEVICE_DESCRIPTORNOTFOUND;

		if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
		{
			PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;
			
			// increment our index to look for the InterfIdx
			if (pPreviousInterf)
			{
				// See if the current interface descriptor is a different interface or
				// an aleternate of the same one
				/*### ===> DE-1184 du 08/03/2009  ML */
				// We check that the founded interface is the same as the wanted
				// and has the good alternate setting
				/*if (CntInterf==InterfIdx)
				{*/
					//if  (pPreviousInterf->bInterfaceNumber==pInterf->bInterfaceNumber)
					if(pInterf->bInterfaceNumber == InterfIdx)
					{
						//if (CntAlt==AltIdx)
						if(AltIdx == pInterf->bAlternateSetting)
						{
							*pNbOfEndPoints=pInterf->bNumEndpoints;
							break;
						}
						/*else
							CntAlt++;*/
					}
					/*else
					{
						if (CntAlt>0)
						{
							nRet=STDEVICE_DESCRIPTORNOTFOUND;
							break;
						}
					}*/
				/*}
				else
					CntInterf++;*/
				/*### <=== DE-1184 */
			}
			else
			{
				if ( (InterfIdx==0) && (AltIdx==0) )
				{
					*pNbOfEndPoints=pInterf->bNumEndpoints;
					break;
				}
			}
			pPreviousInterf=pInterf;
		}
		
		pTmp+=pTmp[0]; // Switch to next descriptor
	}

	return nRet;
}

DWORD CSTDevice::GetEndPointDescriptor(	UINT ConfigIdx,
										UINT InterfIdx,
										UINT AltIdx,
										UINT EndPointIdx,
										PUSB_ENDPOINT_DESCRIPTOR Desc)
{
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	PBYTE pTmp;
	int TotalLength;
	BOOL bIspTmpOnGoodInterf=FALSE;
	DWORD nRet=STDEVICE_NOERROR;
	UINT Idx = 0;
	UINT CntAlt=1, CntInterf=0;
	PUSB_INTERFACE_DESCRIPTOR pPreviousInterf=NULL;
	BOOLEAN _bEndPointFound = FALSE;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	/* ### ===> DE-1184 du 10/03/2009  ML */
	// We check that the index is not invalid corresponding to the 
	// total number of endpoints configured
	if (EndPointIdx>=m_nbEndPoints)
		return STDEVICE_BADPARAMETER;
	/* ### <=== DE-1184 */

	pTmp=m_pConfigs[ConfigIdx];
	ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
	TotalLength=ConfDesc->wTotalLength;
	pTmp+=pTmp[0];

	/* ### ===> DE-1184 du 10/03/2009 ML */
	// We must loop on all the interfaces because the endpoint index is based
	// on all the endpoints configured
	while (pTmp-m_pConfigs[ConfigIdx]<TotalLength && !_bEndPointFound)
	{
		if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
			return STDEVICE_DESCRIPTORNOTFOUND;

		if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
		{
			PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;
			
			pTmp+=pTmp[0];

			while(pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
			{
				if (Idx==EndPointIdx)
				{
					memcpy(Desc, pTmp, sizeof(USB_ENDPOINT_DESCRIPTOR));
					_bEndPointFound = TRUE;
					break;
				}
				else
				{
					Idx++;
					pTmp+=pTmp[0];
				}
			}
			
		}
		else
			pTmp+=pTmp[0];
	}

	if(pTmp-m_pConfigs[ConfigIdx]>=TotalLength)
		nRet = STDEVICE_DESCRIPTORNOTFOUND;

	/* ### <=== DE-1184 */
	return nRet;
}

DWORD CSTDevice::GetNbOfDescriptors(BYTE nLevel,
									 BYTE nType,
									 UINT ConfigIdx,
									 UINT InterfIdx,
									 UINT AltIdx,
									 UINT EndPointIdx,
									 PUINT pNbOfDescriptors)
{
	DWORD nRet=STDEVICE_BADPARAMETER;
	UINT NbOf;
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	PBYTE pTmp;
	int TotalLength;
	UINT Idx=0;
	BOOL bIspTmpOnGoodInterf=FALSE;
	UINT EndPIdx=(UINT)-1;
	UINT CntAlt=1, CntInterf=0;
	PUSB_INTERFACE_DESCRIPTOR pPreviousInterf=NULL;
	BOOLEAN _bEndPointFound = FALSE;

	if (!pNbOfDescriptors)
		return STDEVICE_BADPARAMETER;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if ( (nType==USB_CONFIGURATION_DESCRIPTOR_TYPE) ||
		 (nType==USB_INTERFACE_DESCRIPTOR_TYPE) ||
		 (nType==USB_ENDPOINT_DESCRIPTOR_TYPE) ||
		 (nType==USB_DEVICE_DESCRIPTOR_TYPE) )
		return STDEVICE_BADPARAMETER;

	switch (nLevel)
	{
	case DESCRIPTOR_CONFIGURATION_LEVEL:
		nRet=GetNbOfConfigurations(&NbOf);
		if (nRet==STDEVICE_NOERROR)
		{
			if (ConfigIdx>=NbOf)
				nRet=STDEVICE_BADPARAMETER;
			else
			{
				pTmp=m_pConfigs[ConfigIdx];
				ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
				TotalLength=ConfDesc->wTotalLength;
				pTmp+=pTmp[0];

				while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
				{
					if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
						break;
					if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
						break;
					if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
						break;
					if (pTmp[1]==nType)
						Idx++;
					pTmp+=pTmp[0];
				}
			}
		}
		break;
	case DESCRIPTOR_INTERFACEALTSET_LEVEL:
		nRet=GetNbOfAlternates(ConfigIdx, InterfIdx, &NbOf);
		if (nRet==STDEVICE_NOERROR)
		{
			if (AltIdx>=NbOf)
				nRet=STDEVICE_BADPARAMETER;
			else
			{
				pTmp=m_pConfigs[ConfigIdx];
				ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
				TotalLength=ConfDesc->wTotalLength;
				pTmp+=pTmp[0];

				while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
				{
					if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
						break;

					if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
					{
						PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;

						// increment our index to look for the InterfIdx
						if (pPreviousInterf)
						{
							// See if the current interface descriptor is a different interface or
							// an alternate of the same one
							if (CntInterf==InterfIdx)
							{
								if  (pPreviousInterf->bInterfaceNumber==pInterf->bInterfaceNumber)
								{
									if (CntAlt==AltIdx)
									{
										// We found wanted interface and alt set !
										pTmp+=pTmp[0];
										while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
										{
											if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
												break;
											if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
												break;
											if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
												break;
											if (pTmp[1]==nType)
												Idx++;
											pTmp+=pTmp[0];
										}
										break;
									}
									else
										CntAlt++;
								}
								else
								{
									if (CntAlt>0)
									{
										nRet=STDEVICE_DESCRIPTORNOTFOUND;
										break;
									}
								}
							}
							else
								CntInterf++;
						}
						else
						{
							// Do we need to access interface 0 and altset 0 ?
							if ( (InterfIdx==0) && (AltIdx==0) )
							{
								// Yes! We are in the good place. Let's search the wanted descriptor
								pTmp+=pTmp[0];
								while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
								{
									if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
										break;
									if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
										break;
									if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
										break;
									if (pTmp[1]==nType)
										Idx++;
									pTmp+=pTmp[0];
								}
								break;
							}
						}
						pPreviousInterf=pInterf;
					}
					pTmp+=pTmp[0];
				}
			}
		}
		break;
	case DESCRIPTOR_ENDPOINT_LEVEL:
		nRet=GetNbOfEndPoints(ConfigIdx, InterfIdx, AltIdx, &NbOf);
		if (nRet==STDEVICE_NOERROR)
		{
			/* ### ===> DE-1184 du 10/03/2009 */
			// We must loop on all the interfaces because the endpoint index is based
			// on all the endpoints configured
			if (EndPointIdx>=m_nbEndPoints)
				nRet=STDEVICE_BADPARAMETER;
			else
			{
				pTmp=m_pConfigs[ConfigIdx];
				ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
				TotalLength=ConfDesc->wTotalLength;
				pTmp+=pTmp[0];

				while (pTmp-m_pConfigs[ConfigIdx]<TotalLength && !_bEndPointFound)
				{
					if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
						return STDEVICE_DESCRIPTORNOTFOUND;

					if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
					{
						PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;

						pTmp+=pTmp[0];

						while(pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
						{
							if (EndPIdx==EndPointIdx)
							{
								_bEndPointFound = TRUE;
								EndPIdx = 0;
								break;
							}
							else
							{
								EndPIdx++;
								pTmp+=pTmp[0];
							}
						}
					}
					else
						pTmp+=pTmp[0];
				}
				
				if (_bEndPointFound)
				{
					pTmp+=pTmp[0];
					while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
					{
						if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
							break;
						if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
							break;
						if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
							break;
							return STDEVICE_DESCRIPTORNOTFOUND;
						if (pTmp[1]==nType)
							Idx++;
						pTmp+=pTmp[0];
					}
				}
				else
					return STDEVICE_DESCRIPTORNOTFOUND;
			}
		}
		break;
		/* ### <=== DE-1184 */
	default:
		break;
	}
	if (nRet==STDEVICE_NOERROR)
		*pNbOfDescriptors=Idx;
	return nRet;
}

DWORD CSTDevice::GetDescriptor(BYTE nLevel,
					  		    BYTE nType,
								UINT ConfigIdx,
								UINT InterfIdx,
								UINT AltIdx,
								UINT EndPointIdx,
								UINT Idx,
								PBYTE pDesc,
								UINT nDescSize)
{
	DWORD nRet=STDEVICE_BADPARAMETER;
	UINT NbOf;
	PUSB_CONFIGURATION_DESCRIPTOR ConfDesc;
	PBYTE pTmp;
	int TotalLength;
	UINT Cnt=(UINT)-1;
	BOOL bIspTmpOnGoodInterf=FALSE;
	UINT EndPIdx=(UINT)-1;
	UINT CntAlt=1, CntInterf=0;
	PUSB_INTERFACE_DESCRIPTOR pPreviousInterf=NULL;
	BOOLEAN _bEndPointFound = FALSE;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if (!pDesc)
		return STDEVICE_BADPARAMETER;

	if ( (nType==USB_CONFIGURATION_DESCRIPTOR_TYPE) ||
		 (nType==USB_INTERFACE_DESCRIPTOR_TYPE) ||
		 (nType==USB_ENDPOINT_DESCRIPTOR_TYPE) ||
		 (nType==USB_DEVICE_DESCRIPTOR_TYPE) )
		return STDEVICE_BADPARAMETER;

	switch (nLevel)
	{
	case DESCRIPTOR_CONFIGURATION_LEVEL:
		nRet=GetNbOfConfigurations(&NbOf);
		if (nRet==STDEVICE_NOERROR)
		{
			if (ConfigIdx>=NbOf)
				nRet=STDEVICE_BADPARAMETER;
			else
			{
				pTmp=m_pConfigs[ConfigIdx];
				ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
				TotalLength=ConfDesc->wTotalLength;
				pTmp+=pTmp[0];

				while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
				{
					if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
						return STDEVICE_DESCRIPTORNOTFOUND;
					if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
						return STDEVICE_DESCRIPTORNOTFOUND;
					if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
						return STDEVICE_DESCRIPTORNOTFOUND;
					if (pTmp[1]==nType)
					{
						Cnt++;
						if (Cnt==Idx)
						{
							if (nDescSize<pTmp[0])
								nRet=STDEVICE_INCORRECTBUFFERSIZE;
							else
							{
								nRet=STDEVICE_NOERROR;
								memcpy(pDesc, pTmp, pTmp[0]);
								break;
							}
						}
					}
					pTmp+=pTmp[0];
				}
			}
		}
		break;
	case DESCRIPTOR_INTERFACEALTSET_LEVEL:
		nRet=GetNbOfAlternates(ConfigIdx, InterfIdx, &NbOf);
		if (nRet==STDEVICE_NOERROR)
		{
			if (AltIdx>=NbOf)
				nRet=STDEVICE_BADPARAMETER;
			else
			{
				pTmp=m_pConfigs[ConfigIdx];
				ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
				TotalLength=ConfDesc->wTotalLength;
				pTmp+=pTmp[0];

				while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
				{
					if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
						return STDEVICE_DESCRIPTORNOTFOUND;

					if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
					{
						PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;

						// increment our index to look for the InterfIdx
						if (pPreviousInterf)
						{
							// See if the current interface descriptor is a different interface or
							// an alternate of the same one
							if (CntInterf==InterfIdx)
							{
								if  (pPreviousInterf->bInterfaceNumber==pInterf->bInterfaceNumber)
								{
									if (CntAlt==AltIdx)
									{
										// We found wanted interface and alt set !
										pTmp+=pTmp[0];
										while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
										{
											if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
												return STDEVICE_DESCRIPTORNOTFOUND;
											if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
												return STDEVICE_DESCRIPTORNOTFOUND;
											if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
												return STDEVICE_DESCRIPTORNOTFOUND;
											if (pTmp[1]==nType)
											{
												Cnt++;
												if (Cnt==Idx)
												{
													if (nDescSize<pTmp[0])
														nRet=STDEVICE_INCORRECTBUFFERSIZE;
													else
													{
														nRet=STDEVICE_NOERROR;
														memcpy(pDesc, pTmp, pTmp[0]);
														break;
													}
												}
											}
											pTmp+=pTmp[0];
										}
										break;
									}
									else
										CntAlt++;
								}
								else
								{
									if (CntAlt>0)
									{
										nRet=STDEVICE_DESCRIPTORNOTFOUND;
										break;
									}
								}
							}
							else
								CntInterf++;
						}
						else
						{
							// Do we need to access interface 0 and altset 0 ?
							if ( (InterfIdx==0) && (AltIdx==0) )
							{
								// Yes! We are in the good place. Let's search the wanted descriptor
								pTmp+=pTmp[0];
								while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
								{
									if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
										return STDEVICE_DESCRIPTORNOTFOUND;
									if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
										return STDEVICE_DESCRIPTORNOTFOUND;
									if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
										return STDEVICE_DESCRIPTORNOTFOUND;
									if (pTmp[1]==nType)
									{
										Cnt++;
										if (Cnt==Idx)
										{
											if (nDescSize<pTmp[0])
												nRet=STDEVICE_INCORRECTBUFFERSIZE;
											else
											{
												nRet=STDEVICE_NOERROR;
												memcpy(pDesc, pTmp, pTmp[0]);
												break;
											}
										}
									}
									pTmp+=pTmp[0];
								}
								break;
							}
						}
						pPreviousInterf=pInterf;
					}
					pTmp+=pTmp[0];
				}
			}
		}
		break;
	case DESCRIPTOR_ENDPOINT_LEVEL:
		nRet=GetNbOfEndPoints(ConfigIdx, InterfIdx, AltIdx, &NbOf);
		if (nRet==STDEVICE_NOERROR)
		{
			/* ### ===> DE-1184 du 10/03/2009 */
			// We must loop on all the interfaces because the endpoint index is based
			// on all the endpoints configured
			if (EndPointIdx>=m_nbEndPoints)
				nRet=STDEVICE_BADPARAMETER;
			else
			{
				pTmp=m_pConfigs[ConfigIdx];
				ConfDesc=(PUSB_CONFIGURATION_DESCRIPTOR)(m_pConfigs[ConfigIdx]);
				TotalLength=ConfDesc->wTotalLength;
				pTmp+=pTmp[0];

				while (pTmp-m_pConfigs[ConfigIdx]<TotalLength && !_bEndPointFound)
				{
					if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
						return STDEVICE_DESCRIPTORNOTFOUND;

					if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
					{
						PUSB_INTERFACE_DESCRIPTOR pInterf=(PUSB_INTERFACE_DESCRIPTOR)pTmp;

						pTmp+=pTmp[0];

						while(pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
						{
							if (Idx==EndPointIdx)
							{
								_bEndPointFound = TRUE;
								break;
							}
							else
							{
								Idx++;
								pTmp+=pTmp[0];
							}
						}
					}
					else
						pTmp+=pTmp[0];
				}
				
				if (_bEndPointFound)
				{
					pTmp+=pTmp[0];
					while (pTmp-m_pConfigs[ConfigIdx]<TotalLength)
					{
						if (pTmp[1]==USB_CONFIGURATION_DESCRIPTOR_TYPE)
							return STDEVICE_DESCRIPTORNOTFOUND;
						if (pTmp[1]==USB_INTERFACE_DESCRIPTOR_TYPE)
							return STDEVICE_DESCRIPTORNOTFOUND;
						if (pTmp[1]==USB_ENDPOINT_DESCRIPTOR_TYPE)
							return STDEVICE_DESCRIPTORNOTFOUND;
						
						if (pTmp[1]==nType)
						{
							Cnt++;
							if (Cnt==Idx)
							{
								if (nDescSize<pTmp[0])
									nRet=STDEVICE_INCORRECTBUFFERSIZE;
								else
								{
									nRet=STDEVICE_NOERROR;
									memcpy(pDesc, pTmp, pTmp[0]);
									break;
								}
							}
						}
						pTmp+=pTmp[0];
					}
				}
				else
					return STDEVICE_DESCRIPTORNOTFOUND;
			}
		}
		/* ### <=== DE-1184 */
		break;
	default:
		break;
	}
	return nRet;
}

DWORD CSTDevice::SetMaxNumInterruptInputBuffer(WORD nMaxNumInputBuffer)
{
	BOOL Success;
	DWORD ByteCount;
	BYTE InBuffer[10];
	BYTE OutBuffer[10];

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if (m_pPipeHandles)
		return STDEVICE_PIPESAREOPEN;

	memset(OutBuffer, 0, 10);

	InBuffer[0]=1;
	*(WORD*)(&InBuffer[1])=nMaxNumInputBuffer;

	Success=DeviceIoControl(m_DeviceHandle,
							PU_NB_FRAMES_BUFFER,
							InBuffer,
							3,
							OutBuffer,
							2,
  							&ByteCount,
							NULL);

	if ( (Success) && (ByteCount==2) )
		return STDEVICE_NOERROR;
	else
		return STDEVICE_MEMORY;
}

DWORD CSTDevice::GetMaxNumInterruptInputBuffer(PWORD pMaxNumInputBuffer)
{
	BOOL Success;
	DWORD ByteCount;
	BYTE InBuffer[10];

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if (m_pPipeHandles)
		return STDEVICE_PIPESAREOPEN;

	if (!pMaxNumInputBuffer)
		return STDEVICE_BADPARAMETER;

	InBuffer[0]=0;

	Success=DeviceIoControl(m_DeviceHandle,
							PU_NB_FRAMES_BUFFER,
							InBuffer,
							1,
							pMaxNumInputBuffer,
							2,
  							&ByteCount,
							NULL);

	if ( (Success) && (ByteCount==2) )
		return STDEVICE_NOERROR;
	else
		return STDEVICE_MEMORY;
}

DWORD CSTDevice::SetSuspendModeBehaviour(BOOL Allow)
{
	BOOL Success;
	DWORD ByteCount;
	BYTE InBuffer[10];

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	InBuffer[0]=(BYTE)Allow;

	Success=DeviceIoControl(m_DeviceHandle,
							PU_SUSPEND_CONTROL,
							InBuffer,
							1,
							NULL,
							0,
  							&ByteCount,
							NULL);

	if (Success)
		return STDEVICE_NOERROR;
	else
		return STDEVICE_MEMORY;
}

DWORD CSTDevice::ControlPipeRequest(PCNTRPIPE_RQ pRequest, PBYTE pData)
{
	DWORD nOutNbBytes=0;
	PBYTE pOutBuffer=NULL;
	DWORD ByteCount=0;
	PCNTRPIPE_RQ pDriverRq;
	DWORD Ret;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if (!pRequest)
		return STDEVICE_BADPARAMETER;

	pDriverRq=(PCNTRPIPE_RQ)new BYTE[sizeof(CNTRPIPE_RQ)];
	memcpy(pDriverRq, pRequest, sizeof(CNTRPIPE_RQ));

	if (pRequest->Length!=0)
	{
		// Some bytes will be exchanged. What direction?
		if (pRequest->Direction==VENDOR_DIRECTION_IN)
		{
			// We will receive data. Let's decide the output buffer point to pData
			nOutNbBytes=pRequest->Length;
			pOutBuffer=pData;
		}
		else
		{
			// We will send data. We must send them to the driver, just after
			// the request packet. So we need to allocate a new request.
			delete[] ((PBYTE)pDriverRq);
			pDriverRq=(PCNTRPIPE_RQ)new BYTE[sizeof(CNTRPIPE_RQ)+pRequest->Length];
			memcpy(pDriverRq, pRequest, sizeof(CNTRPIPE_RQ));
			memcpy(pDriverRq+1, pData, pRequest->Length);
		}
	}

	if (DeviceIoControl(m_DeviceHandle,
						PU_VENDOR_REQUEST,
						pDriverRq,
						sizeof(CNTRPIPE_RQ)+pRequest->Length,
						pOutBuffer,
						nOutNbBytes,
						&ByteCount,
						NULL) && (ByteCount==nOutNbBytes) )
		Ret=STDEVICE_NOERROR;
	else
		Ret=STDEVICE_VENDOR_RQ_PB;
	delete[] ((PBYTE)pDriverRq);
	return Ret;
}

DWORD CSTDevice::EndPointControl(UINT nEndPointIdx, UINT nOperation)
{
	BYTE InBuffer[2];
	DWORD ByteCount;
	UINT NbOfEndPoints;
	DWORD nRet;
	USB_ENDPOINT_DESCRIPTOR Desc;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;
	
	if (!m_pPipeHandles)
		return STDEVICE_PIPESARECLOSED;
	
	nRet=GetNbOfEndPoints(m_CurrentConfig, m_CurrentInterf, m_CurrentAltSet, &NbOfEndPoints);
	if (nRet!=STDEVICE_NOERROR)
		return nRet;

	nRet=GetEndPointDescriptor(m_CurrentConfig, m_CurrentInterf, m_CurrentAltSet,
			 				   nEndPointIdx, &Desc);
	if (nRet!=STDEVICE_NOERROR)
		return nRet;

	InBuffer[0] = Desc.bEndpointAddress;
	InBuffer[1] = nOperation;

	if (DeviceIoControl(m_DeviceHandle,
		 			    PU_PIPE_CONTROL,
						InBuffer,
						2,
						NULL,
						0,
						&ByteCount,
						NULL))
		return STDEVICE_NOERROR;
	else
	{
		if (nOperation==PIPE_RESET)
			return STDEVICE_PIPERESETERROR;
		else
			return STDEVICE_PIPEABORTERROR;
	}
}

DWORD CSTDevice::Reset()
{
	BYTE InBuffer[2];
	DWORD ByteCount;

	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	InBuffer[0] = 0;
	InBuffer[1] = 2; // RESET CODE

	if (DeviceIoControl(m_DeviceHandle,
		 			    PU_PIPE_CONTROL,
						InBuffer,
						2,
						NULL,
						0,
						&ByteCount,
						NULL))
		return STDEVICE_NOERROR;
	else
		return STDEVICE_DEVICERESETERROR;
}

DWORD CSTDevice::Read(UINT nEndPointIdx, PBYTE pBuffer, PUINT pSize, DWORD nTimeOut)
{
	DWORD		ByteCount;
	HANDLE		hWait;
	OVERLAPPED	OverLapped;
	DWORD		nDelay;
	DWORD		nRet;
	UINT		_uiNbOfInterfaces = 0;
	UINT		_uiNbOfEnpointsTmp = 0;
	UINT _j = 0;
	
	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;
	
	if (!m_pPipeHandles)
		return STDEVICE_PIPESARECLOSED;
	
	if ( (!pBuffer) || (!pSize) || (*pSize==0) )
		return STDEVICE_BADPARAMETER;
	
	/*### ===> DE-1184 du 08/03/2009  ML */
	// Update to support the read from all the available endpoints 
	// on all the configured interfaces
	if (nEndPointIdx>=m_nbEndPoints)
		return STDEVICE_BADPARAMETER;
	/*### <=== DE-1184 */	

   	if (nTimeOut)
		nDelay=nTimeOut;
	else
		nDelay=m_nDefaultTimeOut;

	hWait=CreateEvent(NULL,			// no security
				      TRUE,		// Manual reset
					  FALSE,		// Initial state
					  NULL);		// Name

	OverLapped.Offset=0;
	OverLapped.OffsetHigh=0;
	OverLapped.hEvent=hWait;

	if (!ReadFile(m_pPipeHandles[nEndPointIdx], pBuffer, *pSize, &ByteCount, &OverLapped))
	{
 		switch (nRet=GetLastError())
		{
 			case ERROR_IO_PENDING:
				DWORD	Result;
				Result=WaitForSingleObject(hWait, nDelay);
				CloseHandle(hWait);
				if (Result==WAIT_OBJECT_0)
				{
					if (GetOverlappedResult(m_pPipeHandles[nEndPointIdx], &OverLapped, (DWORD*)pSize, FALSE))
						return STDEVICE_NOERROR;
					else
					{
						nRet = GetLastError();
		        		return STDEVICE_ERRORWHILEREADING;
					}
				}
				else
					return STDEVICE_ERRORWHILEREADING;
			default:
				CloseHandle(hWait);
				return STDEVICE_ERRORBEFOREREADING;
		}
	}
	else
	{
		*pSize=ByteCount;
		return STDEVICE_NOERROR;
	}
}

DWORD CSTDevice::Write(UINT nEndPointIdx, PBYTE pBuffer, PUINT pSize, DWORD nTimeOut)
{
	DWORD		ByteCount;
	HANDLE		hWait;
	OVERLAPPED	OverLapped;
	DWORD		nDelay;
	UINT		_uiNbOfInterfaces = 0;
	UINT		_j = 0;
	UINT		_uiNbOfEnpointsTmp = 0;
	
	if (!m_bDeviceIsOpen)
		return STDEVICE_DRIVERISCLOSED;

	if (!m_pPipeHandles)
		return STDEVICE_PIPESARECLOSED;

	if ( (!pBuffer) || (!pSize) || (*pSize==0) )
		return STDEVICE_BADPARAMETER;

	/*### ===> DE-1184 du 08/03/2009  ML */
	// Update to support the write from all the available endpoints 
	// on all the configured interfaces
	if (nEndPointIdx>=m_nbEndPoints)
		return STDEVICE_BADPARAMETER;
	/*### <=== DE-1184 */

   	if (nTimeOut)
		nDelay=nTimeOut;
	else
		nDelay=m_nDefaultTimeOut;

	hWait=CreateEvent(NULL,			// no security
				      TRUE,		// Manual reset
					  FALSE,		// Initial state
					  NULL);		// Name

	OverLapped.Offset=0;
	OverLapped.OffsetHigh=0;
	OverLapped.hEvent=hWait;

	if (!WriteFile(m_pPipeHandles[nEndPointIdx], pBuffer, *pSize, &ByteCount, &OverLapped))
	{
 		switch (GetLastError())
		{
 			case ERROR_IO_PENDING:
				DWORD	Result;
		        Result=WaitForSingleObject(hWait, nDelay);
				CloseHandle(hWait);
				if (Result==WAIT_OBJECT_0)
				{
					if (GetOverlappedResult(m_pPipeHandles[nEndPointIdx], &OverLapped, (DWORD *)pSize, FALSE))
						return STDEVICE_NOERROR;
					else
						return STDEVICE_ERRORWHILEREADING;
				}
				else
					return STDEVICE_ERRORWHILEREADING;
			default:
				CloseHandle(hWait);
				return STDEVICE_ERRORBEFOREREADING;
		}
	}
	else
	{
		*pSize=ByteCount;
		return STDEVICE_NOERROR;
	}
}

