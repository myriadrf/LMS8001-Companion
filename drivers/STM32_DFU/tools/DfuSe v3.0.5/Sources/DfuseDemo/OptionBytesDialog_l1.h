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

#if !defined(AFX_OPTIONBYTESDIALOGL1_H__AAED8902_2401_40DA_9E0F_F15486707357__INCLUDED_)
#define AFX_OPTIONBYTESDIALOGL1_H__AAED8902_2401_40DA_9E0F_F15486707357__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// OptionBytesDialog.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// COptionBytesDialog_L1 dialog

class COptionBytesDialog_L1 : public CDialog
{
// Construction
public:

	HANDLE  m_phDevice;
    BYTE    * m_pBuffer;
    ULONG   m_nBytes;
    USHORT  m_nBlock;

	void* GetOptions(LPBYTE User, LPBYTE RDP, LPBYTE WRP0, LPBYTE WRP1, LPBYTE WRP2, LPBYTE WRP3, LPBYTE WRP4, LPBYTE WRP5, LPBYTE WRP6, LPBYTE WRP7, LPBYTE WRP8, LPBYTE WRP9, LPBYTE WRP10, LPBYTE WRP11 );
	void* SetOptions(BYTE User, BYTE RDP, BYTE WRP0, BYTE WRP1,BYTE WRP2, BYTE WRP3, BYTE WRP4, BYTE WRP5, BYTE WRP6, BYTE WRP7, BYTE WRP8, BYTE WRP9, BYTE WRP10, BYTE WRP11);

	COptionBytesDialog_L1(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(COptionBytesDialog_L1)
	enum { IDD = IDD_OPTION_BYTE_L1_DIALOG };
	CString	m_RDP_Value;
	CString	m_WRP0_Value;
	CString	m_WRP2_Value;
	CString	m_WRP4_Value;
	CString	m_WRP6_Value;
	CString	m_WRP8_Value;
	CString	m_WRP10_Value;
	CString	m_User_Value;

	BOOL	m_nRST_STDBY_Value;
	BOOL	m_nRST_STOP_Value;
	BOOL	m_WDG_SW_Value;
	BOOL	m_BF2_Value;
	BOOL	m_BOR_LEV0_Value;
	BOOL    m_BOR_LEV1_Value;
	BOOL	m_BOR_LEV2_Value;
	BOOL    m_BOR_LEV3_Value;

	BOOL	m_ReadOutProtectionEnabledValue;
	BOOL	m_ReadOutProtectionEnabledValue2;
	BOOL	m_ReadOutProtectionEnabledValue3;

	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(COptionBytesDialog_L1)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(COptionBytesDialog_L1)
	afx_msg void OnShowWindow(BOOL bShow, UINT nStatus);
	afx_msg void OnReadOutProtectionEnabledCheck();
	afx_msg void OnReadOutProtectionEnabledCheck2();
	afx_msg void OnReadOutProtectionEnabledCheck3();
	afx_msg void OnChangeUserEdit();
	afx_msg void OnWdgSw();
	afx_msg void OnBF2();
	afx_msg void OnNrstStopCheck2();
	afx_msg void OnNrstStdbyCheck();
    afx_msg void OnBor0Check();
	afx_msg void OnBor1Check();
	afx_msg void OnBor2Check();
	afx_msg void OnBor3Check();
	afx_msg void OnApply();
	virtual void OnCancel();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_OPTIONBYTESDIALOG_H__AAED8902_2401_40DA_9E0F_F15486707357__INCLUDED_)
