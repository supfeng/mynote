import wx
from wxPythonFrame.wx_FrameMain import FrameMain


# 下面是使用 wxPython 的固定用法：启动 wxPython 框架
app = wx.App()
main = FrameMain(None)
main.Show()
app.MainLoop()





