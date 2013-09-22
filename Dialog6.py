# -*- coding: cp936 -*-
#Boa:Dialog:Dialog6

import wx
import struct
import Frame1

global mself


def create(parent):
    return Dialog6(parent)

[wxID_DIALOG6, wxID_DIALOG6BUTTON1, wxID_DIALOG6BUTTON2, wxID_DIALOG6BUTTON3, 
 wxID_DIALOG6STATICTEXT1, wxID_DIALOG6STATICTEXT10, wxID_DIALOG6STATICTEXT11, 
 wxID_DIALOG6STATICTEXT12, wxID_DIALOG6STATICTEXT13, wxID_DIALOG6STATICTEXT14, 
 wxID_DIALOG6STATICTEXT15, wxID_DIALOG6STATICTEXT16, wxID_DIALOG6STATICTEXT17, 
 wxID_DIALOG6STATICTEXT18, wxID_DIALOG6STATICTEXT19, wxID_DIALOG6STATICTEXT2, 
 wxID_DIALOG6STATICTEXT20, wxID_DIALOG6STATICTEXT21, wxID_DIALOG6STATICTEXT22, 
 wxID_DIALOG6STATICTEXT23, wxID_DIALOG6STATICTEXT24, wxID_DIALOG6STATICTEXT25, 
 wxID_DIALOG6STATICTEXT3, wxID_DIALOG6STATICTEXT4, wxID_DIALOG6STATICTEXT5, 
 wxID_DIALOG6STATICTEXT6, wxID_DIALOG6STATICTEXT7, wxID_DIALOG6STATICTEXT8, 
 wxID_DIALOG6STATICTEXT9, wxID_DIALOG6TEXTCTRL1, wxID_DIALOG6TEXTCTRL10, 
 wxID_DIALOG6TEXTCTRL11, wxID_DIALOG6TEXTCTRL12, wxID_DIALOG6TEXTCTRL13, 
 wxID_DIALOG6TEXTCTRL14, wxID_DIALOG6TEXTCTRL15, wxID_DIALOG6TEXTCTRL16, 
 wxID_DIALOG6TEXTCTRL17, wxID_DIALOG6TEXTCTRL18, wxID_DIALOG6TEXTCTRL19, 
 wxID_DIALOG6TEXTCTRL2, wxID_DIALOG6TEXTCTRL20, wxID_DIALOG6TEXTCTRL21, 
 wxID_DIALOG6TEXTCTRL22, wxID_DIALOG6TEXTCTRL23, wxID_DIALOG6TEXTCTRL24, 
 wxID_DIALOG6TEXTCTRL25, wxID_DIALOG6TEXTCTRL3, wxID_DIALOG6TEXTCTRL4, 
 wxID_DIALOG6TEXTCTRL5, wxID_DIALOG6TEXTCTRL6, wxID_DIALOG6TEXTCTRL7, 
 wxID_DIALOG6TEXTCTRL8, wxID_DIALOG6TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(54)]

class Dialog6(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG6, name='', parent=prnt,
              pos=wx.Point(596, 247), size=wx.Size(692, 440),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xd4\xcb\xb5\xa5\xc2\xbc\xc8\xeb\xd0\xc5\xcf\xa2\xc9\xe8\xd6\xc3')
        self.SetClientSize(wx.Size(676, 402))
        self.SetToolTipString('')
        self.Bind(wx.EVT_CLOSE, self.OnDialog6Close)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG6STATICTEXT1,
              label='\xbc\xc4\xbc\xfe\xc8\xd5\xc6\xda', name='staticText1',
              parent=self, pos=wx.Point(24, 32), size=wx.Size(48, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG6STATICTEXT2,
              label='\xbc\xc4\xbc\xfe\xcd\xf8\xb5\xe3', name='staticText2',
              parent=self, pos=wx.Point(24, 56), size=wx.Size(48, 14), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG6STATICTEXT3,
              label='\xc4\xbf\xb5\xc4\xb5\xd8', name='staticText3', parent=self,
              pos=wx.Point(24, 80), size=wx.Size(36, 14), style=0)

        self.staticText4 = wx.StaticText(id=wxID_DIALOG6STATICTEXT4,
              label='\xbc\xfe\xca\xfd', name='staticText4', parent=self,
              pos=wx.Point(24, 104), size=wx.Size(24, 14), style=0)

        self.staticText5 = wx.StaticText(id=wxID_DIALOG6STATICTEXT5,
              label='\xca\xb5\xd6\xd8', name='staticText5', parent=self,
              pos=wx.Point(24, 128), size=wx.Size(24, 14), style=0)

        self.staticText6 = wx.StaticText(id=wxID_DIALOG6STATICTEXT6,
              label='\xb8\xb6\xbf\xee\xb7\xbd\xca\xbd', name='staticText6',
              parent=self, pos=wx.Point(24, 152), size=wx.Size(48, 14),
              style=0)

        self.staticText7 = wx.StaticText(id=wxID_DIALOG6STATICTEXT7,
              label='\xd4\xcb\xb7\xd1', name='staticText7', parent=self,
              pos=wx.Point(24, 176), size=wx.Size(24, 14), style=0)

        self.staticText8 = wx.StaticText(id=wxID_DIALOG6STATICTEXT8,
              label='\xb4\xfa\xca\xd5\xbb\xf5\xbf\xee', name='staticText8',
              parent=self, pos=wx.Point(24, 200), size=wx.Size(48, 14),
              style=0)

        self.staticText9 = wx.StaticText(id=wxID_DIALOG6STATICTEXT9,
              label='\xc8\xa1\xbc\xfe\xd4\xb1', name='staticText9', parent=self,
              pos=wx.Point(24, 224), size=wx.Size(36, 14), style=0)

        self.staticText10 = wx.StaticText(id=wxID_DIALOG6STATICTEXT10,
              label='\xbc\xc4\xbc\xfe\xb9\xab\xcb\xbe', name='staticText10',
              parent=self, pos=wx.Point(24, 248), size=wx.Size(48, 14),
              style=0)

        self.staticText11 = wx.StaticText(id=wxID_DIALOG6STATICTEXT11,
              label='\xd4\xad\xbc\xc4\xb5\xd8', name='staticText11',
              parent=self, pos=wx.Point(24, 272), size=wx.Size(36, 14),
              style=0)

        self.staticText12 = wx.StaticText(id=wxID_DIALOG6STATICTEXT12,
              label='\xc4\xbf\xb5\xc4\xcd\xf8\xb5\xe3', name='staticText12',
              parent=self, pos=wx.Point(24, 296), size=wx.Size(48, 14),
              style=0)

        self.staticText13 = wx.StaticText(id=wxID_DIALOG6STATICTEXT13,
              label='\xce\xef\xc6\xb7\xc0\xe0\xb1\xf0', name='staticText13',
              parent=self, pos=wx.Point(24, 320), size=wx.Size(48, 14),
              style=0)

        self.staticText14 = wx.StaticText(id=wxID_DIALOG6STATICTEXT14,
              label='\xbf\xec\xbc\xfe\xc0\xe0\xd0\xcd', name='staticText14',
              parent=self, pos=wx.Point(312, 32), size=wx.Size(48, 14),
              style=0)

        self.staticText15 = wx.StaticText(id=wxID_DIALOG6STATICTEXT15,
              label='\xbc\xc6\xb7\xd1\xd6\xd8\xc1\xbf', name='staticText15',
              parent=self, pos=wx.Point(312, 56), size=wx.Size(48, 14),
              style=0)

        self.staticText16 = wx.StaticText(id=wxID_DIALOG6STATICTEXT16,
              label='\xb4\xfa\xca\xd5\xca\xd6\xd0\xf8\xb7\xd1',
              name='staticText16', parent=self, pos=wx.Point(312, 80),
              size=wx.Size(60, 14), style=0)

        self.staticText17 = wx.StaticText(id=wxID_DIALOG6STATICTEXT17,
              label='\xb1\xb8\xd7\xa2', name='staticText17', parent=self,
              pos=wx.Point(312, 104), size=wx.Size(24, 14), style=0)

        self.staticText18 = wx.StaticText(id=wxID_DIALOG6STATICTEXT18,
              label='\xbc\xc4\xbc\xfe\xb5\xe7\xbb\xb0', name='staticText18',
              parent=self, pos=wx.Point(312, 128), size=wx.Size(48, 14),
              style=0)

        self.staticText19 = wx.StaticText(id=wxID_DIALOG6STATICTEXT19,
              label='\xbc\xc4\xbc\xfe\xc8\xcb', name='staticText19',
              parent=self, pos=wx.Point(312, 152), size=wx.Size(36, 14),
              style=0)

        self.staticText20 = wx.StaticText(id=wxID_DIALOG6STATICTEXT20,
              label='\xbc\xc4\xbc\xfe\xb5\xd8\xd6\xb7', name='staticText20',
              parent=self, pos=wx.Point(312, 176), size=wx.Size(48, 14),
              style=0)

        self.staticText21 = wx.StaticText(id=wxID_DIALOG6STATICTEXT21,
              label='\xb7\xfe\xce\xf1\xb7\xbd\xca\xbd', name='staticText21',
              parent=self, pos=wx.Point(312, 200), size=wx.Size(48, 14),
              style=0)

        self.staticText22 = wx.StaticText(id=wxID_DIALOG6STATICTEXT22,
              label='\xcc\xe5\xbb\xfd\xd6\xd8', name='staticText22',
              parent=self, pos=wx.Point(312, 224), size=wx.Size(36, 14),
              style=0)

        self.staticText23 = wx.StaticText(id=wxID_DIALOG6STATICTEXT23,
              label='\xce\xef\xc6\xb7\xc3\xfb\xb3\xc6', name='staticText23',
              parent=self, pos=wx.Point(312, 248), size=wx.Size(48, 14),
              style=0)

        self.staticText24 = wx.StaticText(id=wxID_DIALOG6STATICTEXT24,
              label='\xc6\xe4\xcb\xfb\xb7\xd1\xd3\xc3\xbd\xf0\xb6\xee',
              name='staticText24', parent=self, pos=wx.Point(312, 272),
              size=wx.Size(72, 14), style=0)

        self.staticText25 = wx.StaticText(id=wxID_DIALOG6STATICTEXT25,
              label='\xd4\xcb\xb7\xd1\xb1\xd2\xb1\xf0', name='staticText25',
              parent=self, pos=wx.Point(312, 296), size=wx.Size(48, 14),
              style=0)

        self.button1 = wx.Button(id=wxID_DIALOG6BUTTON1,
              label='\xb1\xa3\xb4\xe6\xc9\xe8\xd6\xc3', name='button1',
              parent=self, pos=wx.Point(128, 360), size=wx.Size(136, 24),
              style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG6BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG6BUTTON2,
              label='\xbb\xd6\xb8\xb4\xc4\xac\xc8\xcf', name='button2',
              parent=self, pos=wx.Point(280, 360), size=wx.Size(136, 24),
              style=0)
        self.button2.SetToolTipString('')
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG6BUTTON2)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(80, 32), size=wx.Size(216, 22), style=0,
              value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(80, 56), size=wx.Size(216, 22), style=0,
              value='\xce\xe2\xd6\xd0\xc1\xf9\xb2\xbf')
        self.textCtrl2.SetToolTipString('')

        self.textCtrl3 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(80, 80), size=wx.Size(216, 22), style=0,
              value='')

        self.textCtrl4 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(80, 104), size=wx.Size(216, 22),
              style=0, value='1')

        self.textCtrl5 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(80, 128), size=wx.Size(216, 22),
              style=0, value='0.1')

        self.textCtrl6 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(80, 152), size=wx.Size(216, 22),
              style=0, value='\xd4\xc2\xbd\xe1')

        self.textCtrl7 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(80, 176), size=wx.Size(216, 22),
              style=0, value='20')

        self.textCtrl8 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(80, 200), size=wx.Size(216, 22),
              style=0, value='0')

        self.textCtrl9 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(80, 224), size=wx.Size(216, 22),
              style=0, value='')

        self.textCtrl10 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(80, 248),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl11 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL11,
              name='textCtrl11', parent=self, pos=wx.Point(80, 272),
              size=wx.Size(216, 22), style=0,
              value='\xce\xe2\xd6\xd0\xc1\xf9\xb2\xbf')

        self.textCtrl12 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL12,
              name='textCtrl12', parent=self, pos=wx.Point(80, 296),
              size=wx.Size(216, 22), style=0, value='')
        self.textCtrl12.SetToolTipString('')

        self.textCtrl13 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL13,
              name='textCtrl13', parent=self, pos=wx.Point(80, 320),
              size=wx.Size(216, 22), style=0, value='\xbb\xf5\xd1\xf9')
        self.textCtrl13.SetToolTipString('')

        self.textCtrl14 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL14,
              name='textCtrl14', parent=self, pos=wx.Point(392, 32),
              size=wx.Size(216, 22), style=0, value='\xc6\xfb\xd4\xcb')

        self.textCtrl15 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL15,
              name='textCtrl15', parent=self, pos=wx.Point(392, 56),
              size=wx.Size(216, 22), style=0, value='0.1')

        self.textCtrl16 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL16,
              name='textCtrl16', parent=self, pos=wx.Point(392, 80),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl17 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL17,
              name='textCtrl17', parent=self, pos=wx.Point(392, 104),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl18 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL18,
              name='textCtrl18', parent=self, pos=wx.Point(392, 128),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl19 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL19,
              name='textCtrl19', parent=self, pos=wx.Point(392, 152),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl20 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL20,
              name='textCtrl20', parent=self, pos=wx.Point(392, 176),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl21 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL21,
              name='textCtrl21', parent=self, pos=wx.Point(392, 200),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl22 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL22,
              name='textCtrl22', parent=self, pos=wx.Point(392, 224),
              size=wx.Size(216, 22), style=0, value='0')

        self.textCtrl23 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL23,
              name='textCtrl23', parent=self, pos=wx.Point(392, 248),
              size=wx.Size(216, 22), style=0, value='')

        self.textCtrl24 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL24,
              name='textCtrl24', parent=self, pos=wx.Point(392, 272),
              size=wx.Size(216, 22), style=0, value='0')

        self.textCtrl25 = wx.TextCtrl(id=wxID_DIALOG6TEXTCTRL25,
              name='textCtrl25', parent=self, pos=wx.Point(392, 296),
              size=wx.Size(216, 22), style=0, value='\xc8\xcb\xc3\xf1\xb1\xd2')

        self.button3 = wx.Button(id=wxID_DIALOG6BUTTON3,
              label='\xc8\xa1\xcf\xfb', name='button3', parent=self,
              pos=wx.Point(424, 360), size=wx.Size(136, 24), style=0)
        self.button3.SetToolTipString('')
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_DIALOG6BUTTON3)

    def __init__(self, parent):
        global mself
        mself=self
        
        self._init_ctrls(parent)
        
        try:
            self.textCtrl1.SetValue(Frame1.tcfg[1])
            self.textCtrl2.SetValue(Frame1.tcfg[2])
            self.textCtrl3.SetValue(Frame1.tcfg[3])
            self.textCtrl4.SetValue(Frame1.tcfg[4])
            self.textCtrl5.SetValue(Frame1.tcfg[5])
            self.textCtrl6.SetValue(Frame1.tcfg[6])
            self.textCtrl7.SetValue(Frame1.tcfg[7])
            self.textCtrl8.SetValue(Frame1.tcfg[8])
            self.textCtrl9.SetValue(Frame1.tcfg[9])
            self.textCtrl10.SetValue(Frame1.tcfg[10])
            self.textCtrl11.SetValue(Frame1.tcfg[11])
            self.textCtrl12.SetValue(Frame1.tcfg[12])
            self.textCtrl13.SetValue(Frame1.tcfg[13])
            self.textCtrl14.SetValue(Frame1.tcfg[14])
            self.textCtrl15.SetValue(Frame1.tcfg[15])
            self.textCtrl16.SetValue(Frame1.tcfg[16])
            self.textCtrl17.SetValue(Frame1.tcfg[17])
            self.textCtrl18.SetValue(Frame1.tcfg[18])
            self.textCtrl19.SetValue(Frame1.tcfg[19])
            self.textCtrl20.SetValue(Frame1.tcfg[20])
            self.textCtrl21.SetValue(Frame1.tcfg[21])
            self.textCtrl22.SetValue(Frame1.tcfg[22])
            self.textCtrl23.SetValue(Frame1.tcfg[23])
            self.textCtrl24.SetValue(Frame1.tcfg[24])
            self.textCtrl25.SetValue(Frame1.tcfg[25])
        except:
            print 'Dialog6 init error'
        
        
    def OnButton3Button(self, event):
        self.Destroy()
        event.Skip()

    def OnDialog6Close(self, event):
        self.Destroy()
        event.Skip()

    def OnButton2Button(self, event):
        self.textCtrl1.SetValue('')
        self.textCtrl2.SetValue('吴中六部')
        self.textCtrl3.SetValue('')
        self.textCtrl4.SetValue('1')
        self.textCtrl5.SetValue('0.1')
        self.textCtrl6.SetValue('月结')
        self.textCtrl7.SetValue('20')
        self.textCtrl8.SetValue('0')
        self.textCtrl9.SetValue('')
        self.textCtrl10.SetValue('')
        self.textCtrl11.SetValue('吴中六部')
        self.textCtrl12.SetValue('')
        self.textCtrl13.SetValue('货样')
        self.textCtrl14.SetValue('汽运')
        self.textCtrl15.SetValue('0.1')
        self.textCtrl16.SetValue('')
        self.textCtrl17.SetValue('')
        self.textCtrl18.SetValue('')
        self.textCtrl19.SetValue('')
        self.textCtrl20.SetValue('')
        self.textCtrl21.SetValue('')
        self.textCtrl22.SetValue('0')
        self.textCtrl23.SetValue('')
        self.textCtrl24.SetValue('0')
        self.textCtrl25.SetValue('人民币')

        event.Skip()

    def OnButton1Button(self, event):
        
        try:
            f=file('config.ini','w')
            f.write(self.textCtrl1.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[1]=self.textCtrl1.GetValue().encode('gb2312')
            f.write(self.textCtrl2.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[2]=self.textCtrl2.GetValue().encode('gb2312')
            f.write(self.textCtrl3.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[3]=self.textCtrl3.GetValue().encode('gb2312')
            f.write(self.textCtrl4.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[4]=self.textCtrl4.GetValue().encode('gb2312')
            f.write(self.textCtrl5.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[5]=self.textCtrl5.GetValue().encode('gb2312')
            f.write(self.textCtrl6.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[6]=self.textCtrl6.GetValue().encode('gb2312')
            f.write(self.textCtrl7.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[7]=self.textCtrl7.GetValue().encode('gb2312')
            f.write(self.textCtrl8.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[8]=self.textCtrl8.GetValue().encode('gb2312')
            f.write(self.textCtrl9.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[9]=self.textCtrl9.GetValue().encode('gb2312')
            f.write(self.textCtrl10.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[10]=self.textCtrl10.GetValue().encode('gb2312')
            f.write(self.textCtrl11.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[11]=self.textCtrl11.GetValue().encode('gb2312')
            f.write(self.textCtrl12.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[12]=self.textCtrl12.GetValue().encode('gb2312')
            f.write(self.textCtrl13.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[13]=self.textCtrl13.GetValue().encode('gb2312')
            f.write(self.textCtrl14.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[14]=self.textCtrl14.GetValue().encode('gb2312')
            f.write(self.textCtrl15.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[15]=self.textCtrl15.GetValue().encode('gb2312')
            f.write(self.textCtrl16.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[16]=self.textCtrl16.GetValue().encode('gb2312')
            f.write(self.textCtrl17.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[17]=self.textCtrl17.GetValue().encode('gb2312')
            f.write(self.textCtrl18.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[18]=self.textCtrl18.GetValue().encode('gb2312')
            f.write(self.textCtrl19.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[19]=self.textCtrl19.GetValue().encode('gb2312')
            f.write(self.textCtrl20.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[20]=self.textCtrl20.GetValue().encode('gb2312')
            f.write(self.textCtrl21.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[21]=self.textCtrl21.GetValue().encode('gb2312')
            f.write(self.textCtrl22.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[22]=self.textCtrl22.GetValue().encode('gb2312')
            f.write(self.textCtrl23.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[23]=self.textCtrl23.GetValue().encode('gb2312')
            f.write(self.textCtrl24.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[24]=self.textCtrl24.GetValue().encode('gb2312')
            f.write(self.textCtrl25.GetValue().encode('gb2312')+'\n')
            Frame1.tcfg[25]=self.textCtrl25.GetValue().encode('gb2312')
            f.close()
            self.Destroy()
        except:
            print 'write error'
            f.close()
        #print Frame1.tcfg
        
        event.Skip()
