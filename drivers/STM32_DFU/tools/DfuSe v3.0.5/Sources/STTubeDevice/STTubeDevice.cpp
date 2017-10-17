// STTubeDevice.cpp : Defines the initialization routines for the DLL.
//

#include "stdafx.h"
#include "usb100.h"
#include "STTubeDevice.h"
#include "STTubeDeviceErr30.h"
#include "STTubeDeviceTyp30.h"
#include "STDevicesMgr.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

//
//	Note!
//
//		If this DLL is dynamically linked against the MFC
//		DLLs, any functions exported from this DLL which
//		call into MFC must have the AFX_MANAGE_STATE macro
//		added at the very beginning of the function.
//
//		For example:
//
//		extern "C" BOOL PASCAL EXPORT ExportedFunction()
//		{
//			AFX_MANAGE_STATE(AfxGetStaticModuleState());
//			// normal function body here
//		}
//
//		It is very important that this macro appear in each
//		function, prior to any calls into MFC.  This means that
//		it must appear as the first statement within the 
//		function, even before any object variable declarations
//		as their constructors may generate calls into the MFC
//		DLL.
//
//		Please see MFC Technical Notes 33 and 58 for additional
//		details.
//

/////////////////////////////////////////////////////////////////////////////
// CSTTubeDeviceApp

BEGIN_MESSAGE_MAP(CSTTubeDeviceApp, CWinApp)
	//{{AFX_MSG_MAP(CSTTubeDeviceApp)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CSTTubeDeviceApp construction

CSTTubeDeviceApp::CSTTubeDeviceApp()
{
	m_pMgr=NULL;
}
 
/////////////////////////////////////////////////////////////////////////////
// The one and only CSTTubeDeviceApp object

CSTTubeDeviceApp theApp;

BOOL CSTTubeDeviceApp::InitInstance() 
{
	m_pMgr=new CSTDevicesManager();
	return CWinApp::InitInstance();
}

int CSTTubeDeviceApp::ExitInstance() 
{
	if (m_pMgr)
		delete m_pMgr;
	m_pMgr=NULL;

	return CWinApp::ExitInstance();
}

/////////////////////////////////////////////////////////////////////////////
// Exported functions bodies

extern "C" {

DWORD WINAPI STDevice_Open(LPSTR szDevicePath, 
							LPHANDLE phDevice, 
							LPHANDLE phUnPlugEvent)
{
	CString sSymbName;

	if (!sSymbName)
		return STDEVICE_BADPARAMETER;
	
	sSymbName=szDevicePath;
	if (sSymbName.IsEmpty())
		return STDEVICE_BADPARAMETER;

	if (theApp.GetMgr())
		return theApp.GetMgr()->Open(sSymbName, phDevice, phUnPlugEvent);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_Close(HANDLE hDevice)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->Close(hDevice);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_OpenPipes(HANDLE hDevice)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->OpenPipes(hDevice);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_ClosePipes(HANDLE hDevice)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->ClosePipes(hDevice);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetStringDescriptor(HANDLE hDevice, 
								   UINT nIndex, 
								   LPSTR szString, 
								   UINT nStringLength)
{
	CString sString;
	DWORD nRet=STDEVICE_MEMORY;

	if (theApp.GetMgr())
	{
		// Check parameters we use here. Others are checked in the manager class
		if (!szString)
			return STDEVICE_BADPARAMETER;

		nRet=theApp.GetMgr()->GetStringDescriptor(hDevice, nIndex, sString);

		if (nRet==STDEVICE_NOERROR)
			strncpy(szString, (LPCSTR)sString, nStringLength);
	}
	return nRet;
}

DWORD WINAPI STDevice_GetDeviceDescriptor(HANDLE hDevice, 
								   PUSB_DEVICE_DESCRIPTOR pDesc)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetDeviceDescriptor(hDevice, pDesc);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetNbOfConfigurations(HANDLE hDevice, PUINT pNbOfConfigs)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetNbOfConfigurations(hDevice, pNbOfConfigs);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetConfigurationDescriptor(HANDLE hDevice, 
										  UINT nConfigIdx, 
										  PUSB_CONFIGURATION_DESCRIPTOR pDesc)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetConfigurationDescriptor(hDevice, nConfigIdx, pDesc);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetNbOfInterfaces(HANDLE hDevice, 
								 UINT nConfigIdx, 
								 PUINT pNbOfInterfaces)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetNbOfInterfaces(hDevice, nConfigIdx, pNbOfInterfaces);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetNbOfAlternates(HANDLE hDevice, 
								 UINT nConfigIdx, 
								 UINT nInterfaceIdx, 
								 PUINT pNbOfAltSets)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetNbOfAlternates(hDevice, nConfigIdx, nInterfaceIdx, pNbOfAltSets);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetInterfaceDescriptor(HANDLE hDevice, 
									  UINT nConfigIdx, 
									  UINT nInterfaceIdx, 
									  UINT nAltSetIdx, 
									  PUSB_INTERFACE_DESCRIPTOR pDesc)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetInterfaceDescriptor(hDevice, nConfigIdx, nInterfaceIdx, nAltSetIdx, pDesc);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetNbOfEndPoints(HANDLE hDevice, 
								UINT nConfigIdx, 
								UINT nInterfaceIdx, 
								UINT nAltSetIdx, 
								PUINT pNbOfEndPoints)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetNbOfEndPoints(hDevice, nConfigIdx, nInterfaceIdx, nAltSetIdx, pNbOfEndPoints);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetEndPointDescriptor(HANDLE hDevice, 
									 UINT nConfigIdx, 
									 UINT nInterfaceIdx, 
									 UINT nAltSetIdx, 
									 UINT nEndPointIdx, 
									 PUSB_ENDPOINT_DESCRIPTOR pDesc)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetEndPointDescriptor(hDevice, nConfigIdx, nInterfaceIdx, nAltSetIdx, nEndPointIdx, pDesc);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetNbOfDescriptors(HANDLE hDevice, 
										BYTE nLevel,
										BYTE nType,
										UINT nConfigIdx, 
										UINT nInterfaceIdx, 
										UINT nAltSetIdx, 
										UINT nEndPointIdx, 
										PUINT pNbOfDescriptors)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetNbOfDescriptors(hDevice, nLevel,
												   nType,
												   nConfigIdx, nInterfaceIdx, nAltSetIdx, nEndPointIdx, 
												   pNbOfDescriptors);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetDescriptor(HANDLE hDevice, 
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
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetDescriptor(hDevice, nLevel,
											  nType, 
											  nConfigIdx, nInterfaceIdx, nAltSetIdx, nEndPointIdx, nIdx,
											  pDesc, nDescSize);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_SelectCurrentConfiguration(HANDLE hDevice, 
										  UINT nConfigIdx, 
										  UINT nInterfaceIdx, 
										  UINT nAltSetIdx)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->SelectCurrentConfiguration(hDevice, nConfigIdx, nInterfaceIdx, nAltSetIdx);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_SetDefaultTimeOut(HANDLE hDevice, DWORD nTimeOut)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->SetDefaultTimeOut(hDevice, nTimeOut);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_SetMaxNumInterruptInputBuffer(HANDLE hDevice,
													WORD nMaxNumInputBuffer)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->SetMaxNumInterruptInputBuffer(hDevice, nMaxNumInputBuffer);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_GetMaxNumInterruptInputBuffer(HANDLE hDevice,
													PWORD pMaxNumInputBuffer)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->GetMaxNumInterruptInputBuffer(hDevice, pMaxNumInputBuffer);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_SetSuspendModeBehaviour(HANDLE hDevice, BOOL Allow)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->SetSuspendModeBehaviour(hDevice, Allow);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_EndPointControl(HANDLE hDevice, 
							   UINT nEndPointIdx, 
							   UINT nOperation)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->EndPointControl(hDevice, nEndPointIdx, nOperation);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_Reset(HANDLE hDevice)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->Reset(hDevice);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_ControlPipeRequest(HANDLE hDevice, PCNTRPIPE_RQ pRequest,
										 PBYTE pData)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->ControlPipeRequest(hDevice, pRequest, pData);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_Read(HANDLE hDevice, 
				    UINT nEndPointIdx,
					PBYTE pBuffer, 
					PUINT pSize, 
					DWORD nTimeOut)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->Read(hDevice, nEndPointIdx, pBuffer, pSize, nTimeOut);

	return STDEVICE_MEMORY;
}

DWORD WINAPI STDevice_Write(HANDLE hDevice, 
				    UINT nEndPointIdx,
					 PBYTE pBuffer, 
					 PUINT pSize, 
					 DWORD nTimeOut)
{
	if (theApp.GetMgr())
		return theApp.GetMgr()->Write(hDevice, nEndPointIdx, pBuffer, pSize, nTimeOut);

	return STDEVICE_MEMORY;
}

}