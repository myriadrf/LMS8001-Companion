#ifndef _STDEVICESMGR_H_
#define _STDEVICESMGR_H_

// This class handles all ST devics using Tube Driver

class CSTDevicesManager : public CObject
{
public:	
	CSTDevicesManager();
	~CSTDevicesManager();

	// Functions which are DLL interfaces
	// - Device info functions
	DWORD Open( CString sSymbName, 
			    LPHANDLE phDevice, 
			    LPHANDLE phUnPlugEvent);
	DWORD Close(HANDLE hDevice);
	DWORD OpenPipes(HANDLE hDevice);
	DWORD ClosePipes(HANDLE hDevice);
	DWORD GetStringDescriptor( HANDLE hDevice, 
							   UINT nIndex, 
							   CString &sString);
	DWORD GetDeviceDescriptor( HANDLE hDevice, 
							   PUSB_DEVICE_DESCRIPTOR pDesc);
	DWORD GetNbOfConfigurations(HANDLE hDevice, PUINT pNbOfConfigs);
	DWORD GetConfigurationDescriptor( HANDLE hDevice, 
									  UINT nConfigIdx, 
									  PUSB_CONFIGURATION_DESCRIPTOR pDesc);
	DWORD GetNbOfInterfaces(HANDLE hDevice, 
							UINT nConfigIdx, 
							PUINT pNbOfInterfaces);
	DWORD GetNbOfAlternates(HANDLE hDevice, 
							UINT nConfigIdx, 
							UINT nInterfaceIdx, 
							PUINT pNbOfAltSets);
	DWORD GetInterfaceDescriptor( HANDLE hDevice, 
								  UINT nConfigIdx, 
								  UINT nInterfaceIdx, 
								  UINT nAltSetIdx, 
								  PUSB_INTERFACE_DESCRIPTOR pDesc);
	DWORD GetNbOfEndPoints( HANDLE hDevice, 
							UINT nConfigIdx, 
							UINT nInterfaceIdx, 
							UINT nAltSetIdx, 
							PUINT pNbOfEndPoints);
	DWORD GetEndPointDescriptor( HANDLE hDevice, 
								 UINT nConfigIdx, 
								 UINT nInterfaceIdx, 
								 UINT nAltSetIdx, 
								 UINT nEndPointIdx, 
								 PUSB_ENDPOINT_DESCRIPTOR pDesc);
	DWORD GetNbOfDescriptors(HANDLE hDevice, 
							 BYTE nLevel,
							 BYTE nType,
							 UINT nConfigIdx, 
							 UINT nInterfaceIdx, 
							 UINT nAltSetIdx, 
							 UINT nEndPointIdx, 
							 PUINT pNbOfDescriptors);
	DWORD GetDescriptor(HANDLE hDevice, 
						BYTE nLevel,
						BYTE nType,
						UINT nConfigIdx, 
						UINT nInterfaceIdx, 
						UINT nAltSetIdx, 
						UINT nEndPointIdx, 
						UINT nIdx,
						PBYTE pDesc,
						UINT nDescSize);
	DWORD SelectCurrentConfiguration( HANDLE hDevice, 
									  UINT nConfigIdx, 
									  UINT nInterfaceIdx, 
									  UINT nAltSetIdx);
	
	DWORD SetDefaultTimeOut(HANDLE hDevice, DWORD nTimeOut);
	DWORD SetMaxNumInterruptInputBuffer(HANDLE hDevice, WORD nMaxNumInputBuffer);
	DWORD GetMaxNumInterruptInputBuffer(HANDLE hDevice, PWORD pMaxNumInputBuffer);
	DWORD SetSuspendModeBehaviour(HANDLE hDevice, BOOL Allow);
	DWORD EndPointControl( HANDLE hDevice, 
						   UINT nEndPointIdx, 
						   UINT nOperation);
	DWORD Reset(HANDLE hDevice);
	DWORD ControlPipeRequest(HANDLE hDevice, PCNTRPIPE_RQ pRequest, LPBYTE pData);
	DWORD Read( HANDLE hDevice, 
			    UINT nEndPointIdx,
				PBYTE pBuffer, 
				PUINT pSize, 
				DWORD nTimeOut);
	DWORD Write(HANDLE hDevice, 
			    UINT nEndPointIdx,
				PBYTE pBuffer, 
				PUINT pSize, 
				DWORD nTimeOut);

private:
	CObArray m_OpenDevices;
};

#endif
