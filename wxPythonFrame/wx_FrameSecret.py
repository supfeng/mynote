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
from wxPythonFrame.wx_DialogCreateSecretThing import DialogCreateSecretThing


###########################################################################
## Class FrameSecret
###########################################################################

class FrameSecret(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(917, 686), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.secretUsername = ''

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        self.m_panel6.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)  # 更换 Panel 背景

        self.m_staticText1 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"加密事件待完成", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer6.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_staticText1.SetBackgroundColour((245, 245, 245))  # 设置文本框背景色

        self.m_staticline3 = wx.StaticLine(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        # 将数据库数据显示到主界面
        self.db = myDB.DBop()  # 数据库接口
        self.secretUsername = opNum.OpUsername().readUser()
        self.todoSecretThing, self.todoSecretThingIndex = self.db.getSecretThing(self.secretUsername)
        self.m_listBox6 = wx.ListBox(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.todoSecretThing, 0)
        bSizer9.Add(self.m_listBox6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button71 = wx.Button(self.m_panel6, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_button71, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button71.Bind(wx.EVT_BUTTON, self.deleteThing)

        self.m_button72 = wx.Button(self.m_panel6, wx.ID_ANY, u"已完成", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_button72, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button72.Bind(wx.EVT_BUTTON, self.todoToDone)

        self.m_button73 = wx.Button(self.m_panel6, wx.ID_ANY, u"添加事件", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_button73, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button73.Bind(wx.EVT_BUTTON, self.creatThing)  # 给 button 绑定事件

        bSizer6.Add(bSizer9, 1, wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"加密事件已完成", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer6.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_staticText4.SetBackgroundColour((245, 245, 245))  # 设置文本框背景色

        self.m_staticline4 = wx.StaticLine(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer6.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)



        self.doneSecretThing, self.doneSecretThingIndex = self.db.getSecretDone(self.secretUsername)
        self.m_listBox1 = wx.ListBox(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.doneSecretThing, 0)
        bSizer6.Add(self.m_listBox1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button68 = wx.Button(self.m_panel6, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button68, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_button68.Bind(wx.EVT_BUTTON, self.deleteSecretDone)

        self.m_panel6.SetSizer(bSizer6)
        self.m_panel6.Layout()
        bSizer6.Fit(self.m_panel6)
        bSizer4.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

    def deleteThing(self, event):
        """删除事件"""
        sel = self.m_listBox6.GetSelection()
        if sel != -1:
            todoSecretThing, todoSecretThingIndex = self.db.getSecretThing(self.secretUsername)    # 再获取一遍，以防下标不对称
            self.db.delTodoThing(todoSecretThingIndex[sel])
            self.m_listBox6.Delete(sel)
        else:
            pass

    def deleteSecretDone(self, event):
        """删除已做过的事件"""
        sel = self.m_listBox1.GetSelection()
        if sel != -1:
            doneSecretThing, doneSecretThingIndex = self.db.getSecretDone(self.secretUsername)  # 再获取一遍，以防下标不对称
            self.db.delDoneThing(doneSecretThingIndex[sel])
            self.m_listBox1.Delete(sel)
        else:
            pass

    def todoToDone(self, event):
        """将 todo 表中的事件转移到 done 表中"""
        sel = self.m_listBox6.GetSelection()
        if sel != -1:
            todoSecretThing, todoSecretThingIndex = self.db.getSecretThing(self.secretUsername) # 再获取todo一遍，以防下标不对称
            self.db.doToDone(todoSecretThingIndex[sel])     # 数据库更新事件
            doneSecretThing, doneSecretThingIndex = self.db.getSecretDone(self.secretUsername) # 再次获取 done 一遍
            todoSecretThing, todoSecretThingIndex = self.db.getSecretThing(self.secretUsername) # 需要更新第二遍
            self.m_listBox6.Set(todoSecretThing)       # 桌面更新事件
            self.m_listBox1.Set(doneSecretThing)
        else:
            pass

    def creatThing(self, event):
        """打开创建事件对话框"""
        dialogCT = DialogCreateSecretThing(None)
        dialogCT.ShowModal()
        if dialogCT.setbool == 1:   # 刷新 listbox
            todoSecretThing, todoSecretThingIndex = self.db.getSecretThing(self.secretUsername)
            self.m_listBox6.Set(todoSecretThing)


    def __del__(self):
        pass

    def OnEraseBack(self,event):
        """更换 Panel 背景"""
        dc = event.GetDC()      # 返回 Panel 上的内容并将背景扣去
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("background.jpg")
        dc.DrawBitmap(bmp, 0, 0)


