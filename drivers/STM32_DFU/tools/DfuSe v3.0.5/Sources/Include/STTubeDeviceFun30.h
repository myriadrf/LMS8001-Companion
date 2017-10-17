//******************************************************************************
// STTubeDevice.h : Interface for STTubeDevice DLL
//******************************************************************************

#ifdef __cplusplus
extern "C" {
#endif

//******************************************************************************
// Driver connection functions
//******************************************************************************
//******************************************************************************
// STDevice_Open: Opens a given driver, giving access to its descriptor
// Parameters:
//   szDevicePath: string containing the driver name to open (Given by 
//                 SetupDiGetDeviceInterfaceDetail)
//   phDevice: handle returned by the function while the driver is successfully
//             open
//   phUnPlugEvent: handle returned by the function while the driver is 
//                  successfully open. This handle is an Event handle. It will
//                  be signaled if the driver is surprisly unplugged. This 
//                  pointer can be NULL.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_Open(LPSTR szDevicePath, 
						   LPHANDLE phDevice, 
						   LPHANDLE phUnPlugEvent);

//******************************************************************************
// STDevice_OpenPipes: Open all the pipes for a given device and for its
//                     current configuration
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_OpenPipes(HANDLE hDevice);

//******************************************************************************
// STDevice_ClosePipes: Close the pipes open with STDevice_OpenPipes
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_ClosePipes(HANDLE hDevice);

//******************************************************************************
// STDevice_Close: Closes a given driver
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_Close(HANDLE hDevice);

//******************************************************************************
// STDevice_GetStringDescriptor: Closes a given driver
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nIndex: desired string descriptor Index. If this index is too high, this 
//           function will return an error.
//   szString: buffer the string descriptor will be copied to
//   nStringLength: bufffer size
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetStringDescriptor(HANDLE hDevice, 
										  UINT nIndex, 
										  LPSTR szString, 
										  UINT nStringLength);

//******************************************************************************
// STDevice_GetDeviceDescriptor
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   pDesc: buffer the descriptor will be copied to.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetDeviceDescriptor(HANDLE hDevice, 
										  PUSB_DEVICE_DESCRIPTOR pDesc);

//******************************************************************************
// STDevice_GetNbOfConfigurations: Get the number of possible configurations
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   pNbOfConfigs: buffer the nb of config will be copied to.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetNbOfConfigurations(HANDLE hDevice, PUINT pNbOfConfigs);

//******************************************************************************
// STDevice_GetConfigurationDescriptor
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration descriptor
//   pDesc: buffer the descriptor will be copied to.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetConfigurationDescriptor(HANDLE hDevice, 
										  UINT nConfigIdx, 
										  PUSB_CONFIGURATION_DESCRIPTOR pDesc);

//******************************************************************************
// STDevice_GetNbOfInterfaces: Get the number of possible interfaces, for
//                             a given configuration
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration 
//   pNbOfInterfaces: buffer the nb of interfaces will be copied to.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetNbOfInterfaces(HANDLE hDevice, 
										 UINT nConfigIdx, 
										 PUINT pNbOfInterfaces);

//******************************************************************************
// STDevice_GetNbOfAlternates: Get the number of possible Alternate settings
//                             for a given configuration and a given interface
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration
//   nInterfaceIdx: number of the desired interface
//   pNbOfAltSets: buffer the nb of alternate settings will be copied to
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetNbOfAlternates(HANDLE hDevice, 
										 UINT nConfigIdx, 
										 UINT nInterfaceIdx, 
										 PUINT pNbOfAltSets);

//******************************************************************************
// STDevice_GetInterfaceDescriptor
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration 
//   nInterfaceIdx: number of the desired interface
//   nAltSetIdx: number of the desired alternate setting
//   pDesc: buffer the descriptor will be copied to.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetInterfaceDescriptor(HANDLE hDevice, 
											  UINT nConfigIdx, 
											  UINT nInterfaceIdx, 
											  UINT nAltSetIdx, 
											  PUSB_INTERFACE_DESCRIPTOR pDesc);

//******************************************************************************
// STDevice_GetNbOfEndPoints: Get the number of possible endpoints for a given
//                            configuration, interface and alterate setting
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration
//   nInterfaceIdx: number of the desired interface
//   nAltSetIdx: number of the desired alternate setting
//   pNbOfEndPoints: buffer the nb of endpoints will be copied to
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetNbOfEndPoints(HANDLE hDevice, 
										UINT nConfigIdx, 
										UINT nInterfaceIdx, 
										UINT nAltSetIdx, 
										PUINT pNbOfEndPoints);

//******************************************************************************
// STDevice_GetEndPointDescriptor
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration 
//   nInterfaceIdx: number of the desired interface
//   nAltSetIdx: number of the desired alternate setting
//   nEndPointIdx: number of the desired endpoint
//   pDesc: buffer the descriptor will be copied to.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetEndPointDescriptor(HANDLE hDevice, 
											 UINT nConfigIdx, 
											 UINT nInterfaceIdx, 
											 UINT nAltSetIdx, 
											 UINT nEndPointIdx, 
											 PUSB_ENDPOINT_DESCRIPTOR pDesc);

//******************************************************************************
// STDevice_GetNbOfDescriptors: Obtains any kind of descriptor in the 
//                         configuration buffer. For instance, some device 
//                         embeds string descriptors within the config 
//                         descriptor. These descriptors are unreachable, except 
//                         by using this. It returns the number of desciptors 
//						   of this kind, that are put inside the device
//						   THIS FUNCTION WILL RETURN AN ERROR FOR TYPES
//                         CONFIG, INTERFACE, ENDPOINT
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nLevel: the level the descriptor is attached to (Config, interface,
//           endpoint)
//   nType: type of desired descriptor
//   nConfigIdx: number of the desired configuration 
//   nInterfaceIdx: number of the desired interface if needed
//   nAltSetIdx: number of the desired alternate setting if needed
//   nEndPointIdx: number of the desired endpoint if needed
//   pNbOfDescriptors: buffer the nb of descriptors will be copied to
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetNbOfDescriptors(HANDLE hDevice, 
										BYTE nLevel,
										BYTE nType,
										UINT nConfigIdx, 
										UINT nInterfaceIdx, 
										UINT nAltSetIdx, 
										UINT nEndPointIdx, 
										PUINT pNbOfDescriptors);

//******************************************************************************
// STDevice_GetDescriptor: Obtains any kind of descriptor in the configuration
//                         buffer. For instance, some device embeds string 
//                         descriptors within the config descriptor. These
//                         descriptors are unreachable, except by using this
//                         function
//						   THIS FUNCTION WILL RETURN AN ERROR FOR TYPES
//                         CONFIG, INTERFACE, ENDPOINT
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nLevel: the level the descriptor is attached to (Config, interface,
//           endpoint)
//   nType: type of desired descriptor
//   nConfigIdx: number of the desired configuration 
//   nInterfaceIdx: number of the desired interface if needed
//   nAltSetIdx: number of the desired alternate setting if needed
//   nEndPointIdx: number of the desired endpoint if needed
//   nIdx: number of the descriptor of the type nType to retrieve
//   pDesc: buffer the descriptor will be copied to. 
//   nDescSize: buffer size
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetDescriptor(HANDLE hDevice, 
								    BYTE nLevel,
									BYTE nType,
									UINT nConfigIdx, 
									UINT nInterfaceIdx, 
									UINT nAltSetIdx, 
									UINT nEndPointIdx, 
									UINT nIdx,
									PBYTE pDesc,
									UINT nDescSize);

//******************************************************************************
// STDevice_SelectCurrentConfiguration: selects the currently active mode for
//              a device, giving the configuration, the interface and the 
//              alternate setting. The pipes must be in closed state for this
//              function to success
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nConfigIdx: number of the desired configuration 
//   nInterfaceIdx: number of the desired interface
//   nAltSetIdx: number of the desired alternate setting
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_SelectCurrentConfiguration(HANDLE hDevice, 
												  UINT nConfigIdx, 
												  UINT nInterfaceIdx, 
												  UINT nAltSetIdx);

//******************************************************************************
// I/O Functions: allow to send and receive bytes on the endpoints
//******************************************************************************
//******************************************************************************
// STDevice_SetDefaultTimeOut: I/O request will fail if they last more than
//         a given ellapsed time. This function allows to change this time.
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nTimeOut: Max time a request can last, in ms. 
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_SetDefaultTimeOut(HANDLE hDevice, DWORD nTimeOut);

//******************************************************************************
// STDevice_SetMaxNumInterruptInputBuffer: sets the number of frames the driver 
//        will remember for an interrupt IN pipe. 
//        - When the set value is 0, the driver won't issue non-end in 
//          requests on the interrupt pipe. This is not the USB spec behaviour, 
//          but this is the Windows USBD stack behaviour... Though, If an 
//          STDevice_Read is pending, the pipe is correctly requested. 
//          We say USBD has a "request-oriented" behaviour.
//        - When the value is different than 0, the driver will keep on asking
//          data on the interrupt pipes, respecting the USB spec. Read data 
//          will be bufferized and this function is here to set the buffer size
//          (How many frames to bufferize).
//        The Frames Buffer is a ring buffer. Overflow will lead to data loss.
//		  The pipes must be in a closed state for this function to success.
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nMaxNumInputBuffer: indicates the maximum number of frames to bufferize.
//                       If this value is 10, the driver will remember 9 frames
//                       maximum.
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_SetMaxNumInterruptInputBuffer(HANDLE hDevice,
													WORD nMaxNumInputBuffer);

//******************************************************************************
// STDevice_GetMaxNumInterruptInputBuffer: reads the number of frames the driver 
//        will remember for an interrupt IN pipe. 
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   pMaxNumInputBuffer: pointer (must be valid) 
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_GetMaxNumInterruptInputBuffer(HANDLE hDevice,
													PWORD pMaxNumInputBuffer);

//******************************************************************************
// STDevice_SetSuspendModeBehaviour: allow an application to prevent the system
//                                   going into stand-by.
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   Allow: True if the driver can ack a suspend request
//          False if the driver must nack a suspend request
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_SetSuspendModeBehaviour(HANDLE hDevice, BOOL Allow);

//******************************************************************************
// STDevice_EndPointControl: Controls the behaviour of pipes. The pipes must be 
//                           in open state for this function to success
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nEndPointIdx: number of the desired endpoint.
//   nOperation: constant indicating the operation to apply: 
//			     PIPE_RESET: resets a pipe
//               ABORT_TRANSFER: aborts a transfer (done by Read or write)
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_EndPointControl(HANDLE hDevice, 
									   UINT nEndPointIdx, 
									   UINT nOperation);

//******************************************************************************
// STDevice_Reset: device software resetting. The pipes must be in open state 
//                 for this function to success
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_Reset(HANDLE hDevice);

//******************************************************************************
// STDevice_ControlPipeRequest: issues a request on the Control Pipe (Endpoint0)
//                              The pipes must be in open state for this 
//                              function to success
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   Request: structure containing all the arguments for the request
//   pData: optional data for the request
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_ControlPipeRequest(HANDLE hDevice, PCNTRPIPE_RQ pRequest,
										 PBYTE pData);

//******************************************************************************
// STDevice_Read: issues a read operation on a given pipe. The pipes must be 
//                in open state for this function to success
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nEndPointIdx: index of the Endpoint to read from
//   pBuffer: Buffer where to put read bytes
//   pSize: pointer, on entry containing the size of the buffer, on exit 
//          containing the actual number of read bytes
//   nTimeOut: specific time out if needed. If zero, default timeout is used
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_Read(HANDLE hDevice, 
						    UINT nEndPointIdx,
							PBYTE pBuffer, 
							PUINT pSize, 
							DWORD nTimeOut);

//******************************************************************************
// STDevice_Write: issues a write operation on a given pipe. The pipes must be 
//                 in open state for this function to success
// Parameters:
//   hDevice: handle returned by the function STDevice_Open
//   nEndPointIdx: index of the Endpoint to write to
//   pBuffer: Buffer containing data to be sent
//   pSize: pointer, on entry containing the size of the buffer, on exit 
//          containing the actual number of written bytes
//   nTimeOut: specific time out if needed. If zero, default timeout is used
// Returned: STDEVICE_NOERROR = SUCCESS, Error otherwise (Error Code)
//******************************************************************************
DWORD WINAPI STDevice_Write(HANDLE hDevice, 
						    UINT nEndPointIdx,
 							PBYTE pBuffer, 
							PUINT pSize, 
							DWORD nTimeOut);

#ifdef __cplusplus
}
#endif
