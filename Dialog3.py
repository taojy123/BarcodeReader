# -*- coding: cp936 -*-
#Boa:Dialog:Dialog3

import wx

global mself


def create(parent):
    return Dialog3(parent)

[wxID_DIALOG3, wxID_DIALOG3BUTTON1, wxID_DIALOG3BUTTON2, 
 wxID_DIALOG3STATICTEXT1, wxID_DIALOG3STATICTEXT2, wxID_DIALOG3STATICTEXT3, 
 wxID_DIALOG3TEXTCTRL1, wxID_DIALOG3TEXTCTRL2, wxID_DIALOG3TEXTCTRL3, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Dialog3(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG3, name='', parent=prnt,
              pos=wx.Point(534, 254), size=wx.Size(305, 177),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xd0\xc2\xd4\xf6\xd3\xc3\xbb\xa7')
        self.SetClientSize(wx.Size(297, 143))
        self.Bind(wx.EVT_CLOSE, self.OnDialog3Close)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG3STATICTEXT1,
              label='\xc7\xeb\xca\xe4\xc8\xeb\xd0\xc2\xd4\xf6\xb5\xc4\xd3\xc3\xbb\xa7\xc3\xfb',
              name='staticText1', parent=self, pos=wx.Point(34, 21),
              size=wx.Size(108, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG3STATICTEXT2,
              label='\xc7\xeb\xca\xe4\xc8\xeb\xc3\xdc\xc2\xeb',
              name='staticText2', parent=self, pos=wx.Point(82, 45),
              size=wx.Size(60, 14), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG3STATICTEXT3,
              label='\xc7\xeb\xd4\xd9\xb4\xce\xca\xe4\xc8\xeb\xc3\xdc\xc2\xeb',
              name='staticText3', parent=self, pos=wx.Point(58, 69),
              size=wx.Size(84, 14), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG3TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(152, 16), size=wx.Size(100, 22),
              style=0, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG3TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(152, 40), size=wx.Size(100, 22),
              style=wx.TE_PASSWORD, value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG3TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(152, 64), size=wx.Size(100, 22),
              style=wx.TE_PASSWORD, value='')

        self.button1 = wx.Button(id=wxID_DIALOG3BUTTON1,
              label='\xc8\xb7\xb6\xa8', name='button1', parent=self,
              pos=wx.Point(64, 104), size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG3BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG3BUTTON2,
              label='\xc8\xa1\xcf\xfb', name='button2', parent=self,
              pos=wx.Point(160, 104), size=wx.Size(75, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG3BUTTON2)

    def __init__(self, parent):
        global mself
        mself=self
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        rc = wx.MessageBox("请确定此用户名已在查询网站注册过,否则可能造成您上传的图片被其他人浏览", "新增用户", wx.YES_NO | wx.ICON_QUESTION) #2/yes : 8/no
        if rc == 2:
            username = self.textCtrl1.GetValue()
            code1 = self.textCtrl2.GetValue()
            code2 = self.textCtrl3.GetValue()
            if code1 <> code2 or len(code1)<1 or len(username)<1:
                wx.MessageBox("两次输入的密码不一致或输入为空", "新增用户", wx.OK)
                return
            f=file('cod.dat','a')
            f.close()
            f=file('cod.dat','r')
            s=f.read()
            f.close()
            c=''
            for n in s:
                c=c+chr((ord(n)+12))
            if '{'+ username + '}' in c:
                wx.MessageBox("该用户已存在", "新增用户", wx.OK)
                return
            c='{'+ username + '}' + code1 + '{'
            s=''
            for n in c:
                if ord(n)>126 or ord(n)<48:
                    wx.MessageBox("输入的用户名和密码不符合规范请使用字母或数字", "新增用户", wx.OK)
                    return
                s=s+chr((ord(n)-12))
            f=file('cod.dat','a')
            f.write(s)
            f.close()
            wx.MessageBox("新增用户成功", "新增用户", wx.OK)
            
        self.Destroy()
        event.Skip()

    def OnButton2Button(self, event):
        self.Destroy()
        event.Skip()

    def OnDialog3Close(self, event):
        self.Destroy()
        event.Skip()
