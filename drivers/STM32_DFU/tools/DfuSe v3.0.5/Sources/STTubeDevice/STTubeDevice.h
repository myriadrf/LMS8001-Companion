// STTubeDevice.h : main header file for the STTUBEDEVICE DLL
//

#if !defined(AFX_STTUBEDEVICE_H__3C699C04_5F0F_11D5_9645_0050041B1E9F__INCLUDED_)
#define AFX_STTUBEDEVICE_H__3C699C04_5F0F_11D5_9645_0050041B1E9F__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CSTTubeDeviceApp
// See STTubeDevice.cpp for the implementation of this class
//
class CSTDevicesManager;

class CSTTubeDeviceApp : public CWinApp
{
private:
	CSTDevicesManager *m_pMgr;
public:
	CSTDevicesManager *GetMgr() { return m_pMgr; }
	CSTTubeDeviceApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CSTTubeDeviceApp)
	public:
	virtual BOOL InitInstance();
	virtual int ExitInstance();
	//}}AFX_VIRTUAL

	//{{AFX_MSG(CSTTubeDeviceApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_STTUBEDEVICE_H__3C699C04_5F0F_11D5_9645_0050041B1E9F__INCLUDED_)
