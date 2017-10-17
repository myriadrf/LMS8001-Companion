// stdafx.h : include file for standard system include files,
//  or project specific include files that are used frequently, but
//      are changed infrequently
//

#if !defined(AFX_STDAFX_H__8AF8AF98_54E9_427C_A7B0_AE3C7B2ADDE5__INCLUDED_)
#define AFX_STDAFX_H__8AF8AF98_54E9_427C_A7B0_AE3C7B2ADDE5__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#define WINVER 0x040A

// Insert your headers here
#define WIN32_LEAN_AND_MEAN		// Exclude rarely-used stuff from Windows headers

#include <windows.h>
#include "..\Include\usb100.h"
#include "..\Include\STTubeDeviceTyp30.h"
#include "..\Include\STTubeDeviceFun30.h"
#include "..\Include\STTubeDeviceErr30.h"

// TODO: reference additional headers your program requires here

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_STDAFX_H__8AF8AF98_54E9_427C_A7B0_AE3C7B2ADDE5__INCLUDED_)
