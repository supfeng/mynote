###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wxPythonFrame.wx_FrameSecret import FrameSecret


###########################################################################
## Class DialogSetInSucceed
###########################################################################

class DialogSetInSucceed(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(219, 138), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel11 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"登录成功", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer15.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button103 = wx.Button(self.m_panel11, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.m_button103, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button103.Bind(wx.EVT_BUTTON, self.check)

        self.m_panel11.SetSizer(bSizer15)
        self.m_panel11.Layout()
        bSizer15.Fit(self.m_panel11)
        bSizer14.Add(self.m_panel11, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer14)
        self.Layout()

        self.Centre(wx.BOTH)

    def check(self, event):
        """单击后出现加密事件界面"""
        frameS = FrameSecret(None)
        frameS.Show()
        self.Destroy()

    def __del__(self):
        pass








