###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wxPythonFrame.wx_FrameSetIn import FrameSetIn
from wxPythonFrame.wx_FrameCreateUser import FrameCreateUser


###########################################################################
## Class DialogSecret
###########################################################################

class DialogSecret(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(734, 376), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"加密事件"), wx.VERTICAL)

        self.m_button99 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"登录已有账户", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        sbSizer2.Add(self.m_button99, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button99.Bind(wx.EVT_BUTTON, self.setInHavedAccount)

        self.m_button100 = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"创建新账户", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        sbSizer2.Add(self.m_button100, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button100.Bind(wx.EVT_BUTTON, self.createNewAccount)

        bSizer10.Add(sbSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer10)
        self.Layout()

        self.Centre(wx.BOTH)

    def setInHavedAccount(self, event):
        """登录到已有账户，弹出对话框"""
        frameSI = FrameSetIn(None)
        frameSI.Show()
        self.Destroy()

    def createNewAccount(self, event):
        """创建新用户，弹出对话框"""
        frameCU = FrameCreateUser(None)
        frameCU.Show()
        self.Destroy()

    def __del__(self):
        pass





