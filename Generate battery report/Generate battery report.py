# coding=utf-8
import os
import wx

def isi(path,name):
    file = os.listdir(path)
    if name in file:
        return True
    else:
        return False
def isib(l,dx):
    for i in range(len(l)):
        if l[i] in dx:
            return False
    return True
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Generate battery report',size=(350,90))
        panel = wx.Panel(parent=self)
        self.icon = wx.Icon('battery icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.path = wx.StaticText(panel,label='Sava Path:C:\\')
        self.path2 = wx.StaticText(panel,label='.html')
        self.path3 = wx.TextCtrl(panel)
        self.path3.SetValue('batteryreport')
        self.button = wx.Button(panel,label='Save',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,self.button)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.path,flag=wx.LEFT)
        hbox.Add(self.path3,flag=wx.LEFT)
        hbox.Add(self.path2,flag=wx.LEFT)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox,flag=wx.LEFT)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_click(self,event):
        name = self.path3.GetValue()
        name += '.html'
        if name == 'CON':
            message = wx.MessageDialog(None,"You can't use CON as the file name!",'WARNING',wx.OK | wx.ICON_WARNING)
            if message.ShowModel() == wx.ID_OK:
                pass
        elif isi('C:\\',name):
            message = wx.MessageDialog(None,'This HTML file already exists in disk C!','ERROR',wx.OK | wx.ICON_ERROR)
            if message.ShowModal() == wx.ID_OK:
                pass
        elif isib([' ', '/', '\\', '?', ':', '*', '"', '<', '>', '|'],self.path3.GetValue()):
            command = 'powercfg /batteryreport /output C:\\'
            command += self.path3.GetValue()
            command += '.html'
            os.popen(command)
            message = wx.MessageDialog(None,'Saved successfully!','INFORMATION',wx.OK | wx.ICON_INFORMATION)
            if message.ShowModal() == wx.ID_OK:
                pass
        else:
            message = wx.MessageDialog(None,"Can't contain any of the following characters: (spaces),/,\\,?,:,*,<,> and |.Otherwise,an exception is thrown.",'WARNING',wx.OK | wx.ICON_WARNING)
            if message.ShowModal() == wx.ID_OK:
                pass
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()
