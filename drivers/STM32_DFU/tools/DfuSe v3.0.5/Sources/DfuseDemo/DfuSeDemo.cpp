/******************** (C) COPYRIGHT 2015 STMicroelectronics ********************
* Company            : STMicroelectronics
* Author             : MCD Application Team
* Description        : STMicroelectronics Device Firmware Upgrade Extension Demo
* Version            : V3.0.5
* Date               : 01-September-2015
********************************************************************************
* THE PRESENT SOFTWARE WHICH IS FOR GUIDANCE ONLY AIMS AT PROVIDING CUSTOMERS
* WITH CODING INFORMATION REGARDING THEIR PRODUCTS IN ORDER FOR THEM TO SAVE TIME.
* AS A RESULT, STMICROELECTRONICS SHALL NOT BE HELD LIABLE FOR ANY DIRECT,
* INDIRECT OR CONSEQUENTIAL DAMAGES WITH RESPECT TO ANY CLAIMS ARISING FROM THE
* CONTENT OF SUCH SOFTWARE AND/OR THE USE MADE BY CUSTOMERS OF THE CODING
* INFORMATION CONTAINED HEREIN IN CONNECTION WITH THEIR PRODUCTS.
********************************************************************************
* FOR MORE INFORMATION PLEASE CAREFULLY READ THE LICENSE AGREEMENT FILE
* "MCD-ST Liberty SW License Agreement V2.pdf"
*******************************************************************************/

// DfuSeDemo.cpp : Defines the class behaviors for the application.
//

#include "stdafx.h"
#include "DfuSeDemo.h"
#include "DfuSeDemoDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CDfuSeDemoApp

BEGIN_MESSAGE_MAP(CDfuSeDemoApp, CWinApp)
	//{{AFX_MSG_MAP(CDfuSeDemoApp)
	//}}AFX_MSG
	ON_COMMAND(ID_HELP, CWinApp::OnHelp)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CDfuSeDemoApp construction

CDfuSeDemoApp::CDfuSeDemoApp()
{
}

/////////////////////////////////////////////////////////////////////////////
// The one and only CDfuSeDemoApp object

CDfuSeDemoApp theApp;

/////////////////////////////////////////////////////////////////////////////
// CDfuSeDemoApp initialization

BOOL CDfuSeDemoApp::InitInstance()
{
	AfxEnableControlContainer();

	// Standard initialization
	CDfuSeDemoDlg dlg;
	m_pMainWnd = &dlg;
	int nResponse = dlg.DoModal();
	if (nResponse == IDOK)
	{
	}
	else if (nResponse == IDCANCEL)
	{
	}

	// Since the dialog has been closed, return FALSE so that we exit the
	//  application, rather than start the application's message pump.
	return FALSE;
}
