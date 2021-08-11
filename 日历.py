import wx
import calendar
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='日历', size=(100,100))
        panel = wx.Panel(parent=self)
        b1 = wx.Button(parent=panel, id=1, label='输出当年日历', pos=(100,50))
        b2 = wx.Button(parent=panel, id=2, label='输出当月日历', pos=(100,50))
        self.Bind(wx.EVT_BUTTON, self.on_Button, id=1, id2=2)
        s1 = wx.StaticText(parent=panel, label='输出某年某月日历')
        s2 = wx.StaticText(parent=panel, label='年：')
        t1 = wx.TextCtrl(panel)
        s3 = wx.StaticText(parent=panel, label='月：')
        t2 = wx.TextCtrl(panel)
        b3 = wx.Button(parent=panel, id=3, label='输出该年日历', pos=(100,50))
        b4 = wx.Button(parent=panel, id=4, label='输出该月日历', pos=(100,50))
        self.Bind(wx.EVT.BUTTON, self.on_click, id=3, id2=4)

        hbox = wx.BoxzSizer(wx.HORIZONTAL)
        hbox.Add(b1,
