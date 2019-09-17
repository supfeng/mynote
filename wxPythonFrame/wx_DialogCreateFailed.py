###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class DialogCreateFailed
###########################################################################

class DialogCreateFailed(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(247, 135), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel12 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_panel12, wx.ID_ANY, u"创建失败：已存在该账号", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer17.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button105 = wx.Button(self.m_panel12, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_button105, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button105.Bind(wx.EVT_BUTTON, self.check)

        self.m_panel12.SetSizer(bSizer17)
        self.m_panel12.Layout()
        bSizer17.Fit(self.m_panel12)
        bSizer16.Add(self.m_panel12, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer16)
        self.Layout()

        self.Centre(wx.BOTH)

    def check(self, event):
        """点击按钮后的动作"""
        self.Destroy()

    def __del__(self):
        pass




