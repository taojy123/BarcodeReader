# -*- coding: cp936 -*-
#Boa:Dialog:Dialog4

import wx
import Frame1

global mself


def create(parent):
    return Dialog4(parent)

[wxID_DIALOG4, wxID_DIALOG4BUTTON1, wxID_DIALOG4BUTTON2, 
 wxID_DIALOG4STATICTEXT1, wxID_DIALOG4STATICTEXT2, wxID_DIALOG4TEXTCTRL1, 
 wxID_DIALOG4TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog4(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG4, name='', parent=prnt,
              pos=wx.Point(530, 270), size=wx.Size(278, 166),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xd3\xc3\xbb\xa7\xb5\xc7\xc2\xbc')
        self.SetClientSize(wx.Size(270, 132))
        self.Bind(wx.EVT_CLOSE, self.OnDialog4Close)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG4STATICTEXT1,
              label='\xd3\xc3\xbb\xa7\xc3\xfb', name='staticText1', parent=self,
              pos=wx.Point(50, 27), size=wx.Size(36, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG4STATICTEXT2,
              label='\xc3\xdc\xc2\xeb', name='staticText2', parent=self,
              pos=wx.Point(58, 51), size=wx.Size(24, 14), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG4TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(96, 24), size=wx.Size(112, 22), style=0,
              value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG4TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(96, 48), size=wx.Size(112, 22),
              style=wx.TE_PASSWORD, value='')

        self.button1 = wx.Button(id=wxID_DIALOG4BUTTON1,
              label='\xb5\xc7\xc2\xbc', name='button1', parent=self,
              pos=wx.Point(48, 88), size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG4BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG4BUTTON2,
              label='\xc8\xa1\xcf\xfb', name='button2', parent=self,
              pos=wx.Point(152, 88), size=wx.Size(75, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG4BUTTON2)

    def __init__(self, parent):
        global mself
        mself=self
        self._init_ctrls(parent)

    def OnDialog4Close(self, event):
        self.Destroy()
        event.Skip()

    def OnButton1Button(self, event):
        username = self.textCtrl1.GetValue()
        code = self.textCtrl2.GetValue()

        f=file('cod.dat','a')
        f.close()
        f=file('cod.dat','r')
        s=f.read()
        f.close()
        c=''
        for n in s:
            c=c+chr((ord(n)+12))
        
        if '{'+ username + '}'+ code +'{' in c:
            wx.MessageBox("登录成功", "用户登录", wx.OK)
            Frame1.mself.tuser.SetLabel(username)
        else:
            wx.MessageBox("用户名不存在或密码输入错误", "用户登录", wx.OK)
            
        self.Destroy()
        event.Skip()

    def OnButton2Button(self, event):
        self.Destroy()
        event.Skip()
