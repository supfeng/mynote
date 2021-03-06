###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import myDB
import opNum
from wxPythonFrame.wx_DialogSetInSucceed import DialogSetInSucceed
from wxPythonFrame.wx_DialogPWFailed import DialogPWFailed


###########################################################################
## Class FrameSetIn
###########################################################################

class FrameSetIn(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.db = myDB.DBop()

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel9 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel9, wx.ID_ANY, u"登录"), wx.VERTICAL)

        self.m_panel10 = wx.Panel(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer13.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl17 = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        0)
        bSizer13.Add(self.m_textCtrl17, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.getUsername = self.m_textCtrl17

        self.m_staticText4 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer13.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl18 = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PASSWORD)
        bSizer13.Add(self.m_textCtrl18, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.getPassword = self.m_textCtrl18

        self.m_panel10.SetSizer(bSizer13)
        self.m_panel10.Layout()
        bSizer13.Fit(self.m_panel10)
        sbSizer3.Add(self.m_panel10, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button102 = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.m_button102, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button102.Bind(wx.EVT_BUTTON, self.check)


        self.m_panel9.SetSizer(sbSizer3)
        self.m_panel9.Layout()
        sbSizer3.Fit(self.m_panel9)
        bSizer12.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def check(self, event):
        """点击登录按钮"""
        username = self.getUsername.GetValue()
        password = self.getPassword.GetValue()
        boolValue = self.db.checkUser(username, password)
        if boolValue == 1:
            saveUsername = opNum.OpUsername()   # 记录当前登录的用户名
            saveUsername.writeUser(username)
            dialogSIS = DialogSetInSucceed(None)
            dialogSIS.ShowModal()

        else:
            dialogPWF = DialogPWFailed(None)
            dialogPWF.ShowModal()

        self.Destroy()

    def __del__(self):
        pass




