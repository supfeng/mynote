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


###########################################################################
## Class DialogCreateSecretThing
###########################################################################

class DialogCreateSecretThing(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(594, 402), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.db = myDB.DBop()
        self.setbool = 0    # 该值为窗口间通信的布尔值
        self.secretUsername = opNum.OpUsername().readUser()

        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel13 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel14 = wx.Panel(self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText15 = wx.StaticText(self.m_panel14, wx.ID_ANY, u"加密事件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        gSizer2.Add(self.m_staticText15, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.getThing = self.m_textCtrl7



        self.m_staticText16 = wx.StaticText(self.m_panel14, wx.ID_ANY, u"时间", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gSizer2.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl8, 0, wx.ALL, 5)

        self.getTime = self.m_textCtrl8

        self.m_panel14.SetSizer(gSizer2)
        self.m_panel14.Layout()
        gSizer2.Fit(self.m_panel14)
        bSizer23.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel13.SetSizer(bSizer23)
        self.m_panel13.Layout()
        bSizer23.Fit(self.m_panel13)
        bSizer22.Add(self.m_panel13, 1, wx.EXPAND | wx.ALL, 5)

        self.m_button20 = wx.Button(self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer22.Add(self.m_button20, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button20.Bind(wx.EVT_BUTTON, self.addThing)

        self.m_button21 = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer22.Add(self.m_button21, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button21.Bind(wx.EVT_BUTTON, self.cancelThing)

        self.SetSizer(bSizer22)
        self.Layout()

        self.Centre(wx.BOTH)

    def addThing(self, event):
        """添加事件"""
        """ 第一步：获取text中文本；
            第二步：连接数据库；
            第三步：插入数据库中；
            第四步：添加到ListBox中"""
        thingName = self.getThing.GetValue()    # 获取内容
        thingTime = self.getTime.GetValue()
        self.db.insertSecretThing(self.secretUsername, thingTime, thingName)
        # 更新 listbox
        self.setbool = 1
        self.Destroy()

    def cancelThing(self, event):
        """取消"""
        self.Destroy()

    def __del__(self):
        pass



