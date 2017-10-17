#include "stdafx.h"
#include "usb100.h"
#include "STTubeDeviceErr30.h"
#include "STTubeDeviceTyp30.h"
#include "STDevice.h"
#include "STDevicesMgr.h"

CSTDevicesManager::CSTDevicesManager()
{
}

CSTDevicesManager::~CSTDevicesManager()
{
	int i;
	
	// Close all still-open device objects
	if (m_OpenDevices.GetSize())
	{
		CSTDevice *pDevice;

		for (i=0;i<m_OpenDevices.GetSize();i++)
		{
			pDevice=(CSTDevice*)(m_OpenDevices[i]);
			if (pDevice)
				delete pDevice;
		}
	}
}

DWORD CSTDevicesManager::Open(CString sSymbName, 
								LPHANDLE phDevice, 
								LPHANDLE phUnPlugEvent)
{
	CSTDevice *pDevice=NULL;
	DWORD nRet=STDEVICE_MEMORY;

	if (!phDevice)
		return STDEVICE_BADPARAMETER;

	// Tries to create an object
	pDevice=new CSTDevice(sSymbName);
	if (!pDevice)
		return STDEVICE_BADPARAMETER;

	// Tries to open the device
	nRet=pDevice->Open(phUnPlugEvent);
	if (nRet!=STDEVICE_NOERROR)
	{
		delete pDevice;
		pDevice=NULL;
		return nRet;
	}

	// OK our STDevice object was successfully created. Let's add it to our collection
	m_OpenDevices.Add(pDevice);

	*phDevice=(HANDLE)pDevice;
	return STDEVICE_NOERROR;
}

DWORD CSTDevicesManager::Close(HANDLE hDevice)
{
	DWORD nRet=STDEVICE_NOERROR;
	int i;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			// Do our best to destroy the object if possible
			pDevice->Close();
			delete pDevice;
			pDevice=NULL;

			m_OpenDevices.RemoveAt(i);
			nRet=STDEVICE_NOERROR;
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::OpenPipes(HANDLE hDevice)
{
	DWORD nRet=STDEVICE_NOERROR;
	int i;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->OpenPipes();
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::ClosePipes(HANDLE hDevice)
{
	DWORD nRet=STDEVICE_NOERROR;
	int i;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->ClosePipes();
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetStringDescriptor( HANDLE hDevice, 
						   UINT nIndex, 
						   CString &sString)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetStringDescriptor(nIndex, sString);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetDeviceDescriptor( HANDLE hDevice, 
						   PUSB_DEVICE_DESCRIPTOR pDesc)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetDeviceDescriptor(pDesc);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetNbOfConfigurations(HANDLE hDevice, PUINT pNbOfConfigs)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetNbOfConfigurations(pNbOfConfigs);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetConfigurationDescriptor( HANDLE hDevice, 
								  UINT nConfigIdx, 
								  PUSB_CONFIGURATION_DESCRIPTOR pDesc)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetConfigurationDescriptor(nConfigIdx, pDesc);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetNbOfInterfaces(HANDLE hDevice, 
						UINT nConfigIdx, 
						PUINT pNbOfInterfaces)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetNbOfInterfaces(nConfigIdx, pNbOfInterfaces);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetNbOfAlternates(HANDLE hDevice, 
						UINT nConfigIdx, 
						UINT nInterfaceIdx, 
						PUINT pNbOfAltSets)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetNbOfAlternates(nConfigIdx, nInterfaceIdx, pNbOfAltSets);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetInterfaceDescriptor( HANDLE hDevice, 
							  UINT nConfigIdx, 
							  UINT nInterfaceIdx, 
							  UINT nAltSetIdx, 
							  PUSB_INTERFACE_DESCRIPTOR pDesc)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetInterfaceDescriptor(nConfigIdx, nInterfaceIdx, nAltSetIdx, pDesc);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetNbOfEndPoints( HANDLE hDevice, 
						UINT nConfigIdx, 
						UINT nInterfaceIdx, 
						UINT nAltSetIdx, 
						PUINT pNbOfEndPoints)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetNbOfEndPoints(nConfigIdx, nInterfaceIdx, nAltSetIdx, pNbOfEndPoints);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetEndPointDescriptor( HANDLE hDevice, 
							 UINT nConfigIdx, 
							 UINT nInterfaceIdx, 
							 UINT nAltSetIdx, 
							 UINT nEndPointIdx, 
							 PUSB_ENDPOINT_DESCRIPTOR pDesc)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetEndPointDescriptor(nConfigIdx, nInterfaceIdx, nAltSetIdx, nEndPointIdx, pDesc);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetNbOfDescriptors(HANDLE hDevice, 
											BYTE nLevel,
											BYTE nType,
											UINT nConfigIdx, 
											UINT nInterfaceIdx, 
											UINT nAltSetIdx, 
											UINT nEndPointIdx, 
											PUINT pNbOfDescriptors)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetNbOfDescriptors(nLevel, nType, nConfigIdx, nInterfaceIdx, nAltSetIdx, nEndPointIdx, pNbOfDescriptors);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetDescriptor(HANDLE hDevice, 
										BYTE nLevel,
										BYTE nType,
										UINT nConfigIdx, 
										UINT nInterfaceIdx, 
										UINT nAltSetIdx, 
										UINT nEndPointIdx, 
										UINT nIdx,
										PBYTE pDesc,
										UINT nDescSize)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetDescriptor(nLevel, nType, nConfigIdx, nInterfaceIdx, nAltSetIdx, nEndPointIdx, nIdx, pDesc, nDescSize);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::SelectCurrentConfiguration( HANDLE hDevice, 
								  UINT nConfigIdx, 
								  UINT nInterfaceIdx, 
								  UINT nAltSetIdx)

{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->SelectCurrentConfiguration(nConfigIdx, nInterfaceIdx, nAltSetIdx);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::SetDefaultTimeOut(HANDLE hDevice, DWORD nTimeOut)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->SetDefaultTimeOut(nTimeOut);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::SetMaxNumInterruptInputBuffer(HANDLE hDevice, WORD nMaxNumInputBuffer)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->SetMaxNumInterruptInputBuffer(nMaxNumInputBuffer);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::GetMaxNumInterruptInputBuffer(HANDLE hDevice, PWORD pMaxNumInputBuffer)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->GetMaxNumInterruptInputBuffer(pMaxNumInputBuffer);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::SetSuspendModeBehaviour(HANDLE hDevice, BOOL Allow)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->SetSuspendModeBehaviour(Allow);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::EndPointControl( HANDLE hDevice, 
					   UINT nEndPointIdx, 
					   UINT nOperation)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->EndPointControl(nEndPointIdx, nOperation);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::Reset(HANDLE hDevice)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->Reset();
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::ControlPipeRequest(HANDLE hDevice, PCNTRPIPE_RQ pRequest, PBYTE pData)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->ControlPipeRequest(pRequest, pData);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::Read(  HANDLE hDevice, 
							    UINT nEndPointIdx,
								PBYTE pBuffer, 
								PUINT pSize, 
								DWORD nTimeOut)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->Read(nEndPointIdx, pBuffer, pSize, nTimeOut);
			break;
		}
	}

	return nRet;
}

DWORD CSTDevicesManager::Write(HANDLE hDevice, 
							    UINT nEndPointIdx,
								PBYTE pBuffer, 
								PUINT pSize, 
								DWORD nTimeOut)
{
	int i;
	DWORD nRet=STDEVICE_BADPARAMETER;

	for (i=0;i<m_OpenDevices.GetSize();i++)
	{
		if (hDevice==(HANDLE)m_OpenDevices[i])
		{
			CSTDevice *pDevice=(CSTDevice *)hDevice;

			nRet=pDevice->Write(nEndPointIdx, pBuffer, pSize, nTimeOut);
			break;
		}
	}

	return nRet;
}
