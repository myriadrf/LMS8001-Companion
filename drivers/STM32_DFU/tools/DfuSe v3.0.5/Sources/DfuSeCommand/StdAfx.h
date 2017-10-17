// stdafx.h : include file for standard system include files,
//  or project specific include files that are used frequently, but
//      are changed infrequently
//

#if !defined(AFX_STDAFX_H__CEAF51BB_151A_4DB8_85D7_959F7819E9BB__INCLUDED_)
#define AFX_STDAFX_H__CEAF51BB_151A_4DB8_85D7_959F7819E9BB__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
#define WIN32_LEAN_AND_MEAN		// Exclude rarely-used stuff from Windows headers

#include <stdio.h>

#ifndef _AFX_NO_AFXCMN_SUPPORT
#include <afxcmn.h>			// MFC support for Windows Common Controls
#endif // _AFX_NO_AFXCMN_SUPPORT

#include <winuser.h>
#include "setupapi.h"
#include "..\Include\usb100.h"
#include "..\STDFU\STDFU.h"
#include "..\STDFUPRT\STDFUPRTINC.h"
#include "..\STDFUFILES\STDFUFILESINC.h"


// TODO: reference additional headers your program requires here

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_STDAFX_H__CEAF51BB_151A_4DB8_85D7_959F7819E9BB__INCLUDED_)
