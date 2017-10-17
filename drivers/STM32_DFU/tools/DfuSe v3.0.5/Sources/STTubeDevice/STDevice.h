#ifndef _STDEVICE_H_
#define _STDEVICE_H_

typedef BYTE FULL_CONFIG_INFO[512];
typedef FULL_CONFIG_INFO* PFULL_CONFIG_INFO;

class CSTDevice : public CObject
{
public:	
	CSTDevice(CString sSymbolicName);
	~CSTDevice();
public:
	// Connection state
	DWORD Open(PHANDLE);
	DWORD Close();
	DWORD OpenPipes();
	DWORD ClosePipes();
	DWORD SelectCurrentConfiguration(UINT ConfigIdx, UINT InterfaceIdx, UINT AltSetIdx);
	DWORD ControlPipeRequest(PCNTRPIPE_RQ pRequest, LPBYTE pData);
	DWORD EndPointControl(UINT nEndPointIdx, UINT nOperation);
	DWORD Reset();
	DWORD Read(UINT nEndPointIdx, PBYTE pBuffer, PUINT pSize, DWORD nTimeOut);
	DWORD Write(UINT nEndPointIdx, PBYTE pBuffer, PUINT pSize, DWORD nTimeOut);

	// Accessors
	// - Default Time out
	DWORD SetDefaultTimeOut(DWORD nTimeOut) { m_nDefaultTimeOut=nTimeOut; return STDEVICE_NOERROR; }
	
	// - Number of interrupt IN frames to bufferize
	DWORD SetMaxNumInterruptInputBuffer(WORD nMaxNumInputBuffer);
	DWORD GetMaxNumInterruptInputBuffer(PWORD pMaxNumInputBuffer);

	// - String descriptors
	DWORD GetStringDescriptor(UINT Index, CString &Desc);
	// - Device descriptors
	DWORD GetDeviceDescriptor(PUSB_DEVICE_DESCRIPTOR Desc);
	
	// - Config numbers
	DWORD GetNbOfConfigurations(PUINT);
	// - Config descriptors
	DWORD GetConfigurationDescriptor(UINT ConfigIdx, PUSB_CONFIGURATION_DESCRIPTOR Desc);
	
	// - Interface numbers
	DWORD GetNbOfInterfaces(UINT ConfigIdx, PUINT);
	// - Alternate Settings numbers
	DWORD GetNbOfAlternates(UINT ConfigIdx, UINT InterfIdx, PUINT);
	// - Interface descriptors
	DWORD GetInterfaceDescriptor(UINT ConfigIdx, UINT InterfIdx, UINT AltIdx, PUSB_INTERFACE_DESCRIPTOR Desc);
	
	// - Endpoint numbers
	DWORD GetNbOfEndPoints(UINT ConfigIdx, UINT InterfIdx, UINT AltIdx, PUINT);
	// - Endpoint descriptors
	DWORD GetEndPointDescriptor(UINT ConfigIdx, 
								UINT InterfIdx, 
								UINT AltIdx, 
								UINT EndPointIdx,
								PUSB_ENDPOINT_DESCRIPTOR Desc);
	// - Other descriptors (Class f.i)
	//   * Nb of descriptors
	DWORD GetNbOfDescriptors(BYTE nLevel,
							 BYTE nType,
							 UINT ConfigIdx, 
							 UINT InterfIdx, 
							 UINT AltIdx, 
							 UINT EndPointIdx, 
							 PUINT pNbOfDescriptors);
	//   * Descriptor itself
	DWORD GetDescriptor(BYTE nLevel,
						BYTE nType,
						UINT ConfigIdx, 
						UINT InterfIdx, 
						UINT AltIdx, 
						UINT EndPointIdx, 
						UINT nIdx,
						PBYTE pDesc,
						UINT nDescSize);

	// - Get symbolic name of the driver
	CString GetSymbolicName() { return m_SymbolicName; }

	// - Set current driver behaviour regarding Suspend mode
	DWORD SetSuspendModeBehaviour(BOOL Allow);
private:
	int					  m_CurrentConfig;
	int					  m_CurrentInterf;
	int					  m_CurrentAltSet;

	CString				  m_SymbolicName;
	HANDLE				  m_DeviceHandle;
	BOOL				  m_bDeviceIsOpen;
	DWORD				  m_nDefaultTimeOut;

	USB_DEVICE_DESCRIPTOR m_DeviceDescriptor;
	FULL_CONFIG_INFO*	  m_pConfigs;
	HANDLE				  *m_pPipeHandles;
	UINT				  m_nbEndPoints;

	DWORD				  OpenDevice(PHANDLE);
	DWORD				  CloseDevice();
	DWORD				  AllocDescriptors();
	DWORD				  ReleaseDescriptors();
};

#endif