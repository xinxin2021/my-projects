# coding=utf-8
import pyperclip
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Common path to Python path', size=(500,150))
        panel = wx.Panel(parent=self)
        self.path2 = ''
        # on_click function needs 'path2' variable
        self.icon = wx.Icon('icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.st = wx.StaticText(panel,label='Path:')
        self.tc = wx.TextCtrl(panel)
        self.button = wx.Button(panel,label='Transformation',pos=(100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,self.button)
        self.path = wx.StaticText(panel,label='Python Path:?')
        self.button2 = wx.Button(panel,label='Copy to clipboard',pos=(100,50))
        self.button2.Bind(wx.EVT_BUTTON,self.copy,self.button2)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.st,flag=wx.EXPAND,border=10)
        vbox.Add(self.tc,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        vbox.Add(self.path,flag=wx.EXPAND,border=10)
        vbox.Add(self.button2,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_click(self,event):
        self.path2 = ''
        path = self.tc.GetValue()
        path_l = []
        if path != '':
            for i in range(len(path)):
                path_l.append(path[i])
            if path_l[0] == "'":
                del path_l[0]
            if path_l[-1] == "'":
                del path_l[-1]
            for i in range(len(path)):
                if path_l[i] == '\\':
                    path_l[i] = '\\\\'
            for i in range(len(path_l)):
                self.path2 += path_l[i]
            self.path.SetLabelText('Python path:' + self.path2)
        else:
            dhk = wx.MessageDialog(parent=self,message='Please enter the path!',caption='ERROR', style=wx.OK | wx.ICON_ERROR)
            if dhk.ShowModal() == wx.ID_OK:
                pass
    def copy(self,event):
        pyperclip.copy(self.path2)
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()