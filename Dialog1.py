# -*- coding: cp936 -*-
#Boa:Dialog:Dialog1

import wx
import Frame1

global mself

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, wxID_DIALOG1CDATE, 
 wxID_DIALOG1CHECKBOX1, wxID_DIALOG1CTIME, wxID_DIALOG1CUSER, wxID_DIALOG1LBS, 
 wxID_DIALOG1LSTEP, wxID_DIALOG1RADIOBUTTON1, wxID_DIALOG1RADIOBUTTON2, 
 wxID_DIALOG1RADIOBUTTON3, wxID_DIALOG1RADIOBUTTON4, wxID_DIALOG1RADIOBUTTON5, 
 wxID_DIALOG1RADIOBUTTON6, wxID_DIALOG1SBS, wxID_DIALOG1SSTEP, 
 wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT10, wxID_DIALOG1STATICTEXT11, 
 wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT4, 
 wxID_DIALOG1STATICTEXT5, wxID_DIALOG1STATICTEXT6, wxID_DIALOG1STATICTEXT7, 
 wxID_DIALOG1STATICTEXT8, wxID_DIALOG1STATICTEXT9, wxID_DIALOG1TDIR, 
 wxID_DIALOG1TFTP, wxID_DIALOG1TPASSWORD, wxID_DIALOG1TUSERNAME, 
] = [wx.NewId() for _init_ctrls in range(32)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(726, 45), size=wx.Size(414, 657),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xb2\xce\xca\xfd\xc9\xe8\xd6\xc3')
        self.SetClientSize(wx.Size(398, 619))
        self.SetToolTipString('')
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)

        self.sstep = wx.Slider(id=wxID_DIALOG1SSTEP, maxValue=50, minValue=1,
              name='sstep', parent=self, pos=wx.Point(128, 24),
              size=wx.Size(192, 24), style=wx.SL_HORIZONTAL, value=3)
        self.sstep.SetLabel('')
        self.sstep.SetToolTipString('\xb5\xf7\xd5\xfb\xc9\xa8\xc3\xe8\xbe\xab\xb6\xc8\xcf\xb5\xca\xfd(\xca\xfd\xd7\xd6\xd4\xbd\xd0\xa1\xbe\xab\xb6\xc8\xd4\xbd\xb8\xdf)')
        self.sstep.Bind(wx.EVT_SCROLL, self.OnSstepScroll)

        self.sbs = wx.Slider(id=wxID_DIALOG1SBS, maxValue=254, minValue=1,
              name='sbs', parent=self, pos=wx.Point(128, 56), size=wx.Size(192,
              24), style=wx.SL_HORIZONTAL, value=150)
        self.sbs.SetLabel('')
        self.sbs.SetToolTipString('\xb5\xf7\xd5\xfb\xca\xb6\xb1\xf0\xc1\xc1\xb6\xc8\xcf\xb5\xca\xfd(\xbb\xad\xc3\xe6\xd4\xbd\xc1\xc1\xc9\xe8\xd6\xc3\xd6\xb5\xd4\xbd\xb4\xf3)')
        self.sbs.Bind(wx.EVT_SCROLL, self.OnSbsScroll)

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1,
              label='\xc8\xb7\xb6\xa8', name='button1', parent=self,
              pos=wx.Point(96, 560), size=wx.Size(104, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2,
              label='\xc8\xa1\xcf\xfb', name='button2', parent=self,
              pos=wx.Point(200, 560), size=wx.Size(104, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG1BUTTON2)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='\xc9\xa8\xc3\xe8\xbd\xf8\xb6\xc8\xcf\xb5\xca\xfd',
              name='staticText1', parent=self, pos=wx.Point(40, 29),
              size=wx.Size(72, 14), style=0)
        self.staticText1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='\xca\xb6\xb1\xf0\xc1\xc1\xb6\xc8\xcf\xb5\xca\xfd',
              name='staticText2', parent=self, pos=wx.Point(40, 60),
              size=wx.Size(72, 14), style=0)
        self.staticText2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,
              label='\xd0\xde\xb8\xc4\xca\xb6\xb1\xf0\xb2\xce\xca\xfd\xbb\xe1\xd3\xb0\xcf\xec\xca\xb6\xb1\xf0\xd0\xa7\xc2\xca\xba\xcd\xca\xb6\xb1\xf0\xc2\xca\xa3\xac\xbd\xa8\xd2\xe9\xca\xb9\xd3\xc3\xc4\xac\xc8\xcf\xb2\xce\xca\xfd',
              name='staticText3', parent=self, pos=wx.Point(40, 88),
              size=wx.Size(312, 14), style=0)

        self.lstep = wx.StaticText(id=wxID_DIALOG1LSTEP, label='3',
              name='lstep', parent=self, pos=wx.Point(336, 29), size=wx.Size(7,
              14), style=0)

        self.lbs = wx.StaticText(id=wxID_DIALOG1LBS, label='145', name='lbs',
              parent=self, pos=wx.Point(336, 62), size=wx.Size(40, 14),
              style=0)

        self.radioButton1 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON1,
              label='\xd3\xc5\xcb\xd9\xbf\xec\xb5\xdd/\xc3\xf1\xba\xbd\xbf\xec\xb5\xdd',
              name='radioButton1', parent=self, pos=wx.Point(112, 160),
              size=wx.Size(216, 14), style=0)
        self.radioButton1.SetValue(False)

        self.radioButton2 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON2,
              label='\xc9\xea\xcd\xa8\xbf\xec\xb5\xdd', name='radioButton2',
              parent=self, pos=wx.Point(112, 184), size=wx.Size(224, 14),
              style=0)
        self.radioButton2.SetValue(False)

        self.radioButton3 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON3,
              label='\xd6\xd0\xcd\xa8\xbf\xec\xb5\xdd', name='radioButton3',
              parent=self, pos=wx.Point(112, 208), size=wx.Size(91, 14),
              style=0)
        self.radioButton3.SetValue(False)

        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4,
              label='\xd1\xa1\xd4\xf1\xcc\xf5\xc2\xeb\xca\xb6\xb1\xf0\xc4\xda\xba\xcb\xa3\xba',
              name='staticText4', parent=self, pos=wx.Point(40, 136),
              size=wx.Size(108, 14), style=0)

        self.radioButton4 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON4,
              label='\xd4\xb2\xcd\xa8\xbf\xec\xb5\xdd', name='radioButton4',
              parent=self, pos=wx.Point(112, 232), size=wx.Size(91, 14),
              style=0)
        self.radioButton4.SetValue(False)

        self.radioButton5 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON5,
              label='EMS\xcc\xd8\xbf\xec\xd7\xa8\xb5\xdd', name='radioButton5',
              parent=self, pos=wx.Point(112, 256), size=wx.Size(91, 14),
              style=0)
        self.radioButton5.SetValue(False)

        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5,
              label='\xc9\xcf\xb4\xab\xb7\xfe\xce\xf1\xc6\xf7\xb2\xce\xca\xfd\xa3\xba',
              name='staticText5', parent=self, pos=wx.Point(40, 408),
              size=wx.Size(96, 14), style=0)

        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6,
              label='FTP\xb5\xd8\xd6\xb7', name='staticText6', parent=self,
              pos=wx.Point(64, 432), size=wx.Size(45, 14), style=0)

        self.staticText7 = wx.StaticText(id=wxID_DIALOG1STATICTEXT7,
              label='\xd3\xc3\xbb\xa7\xc3\xfb', name='staticText7', parent=self,
              pos=wx.Point(72, 456), size=wx.Size(36, 14), style=0)

        self.staticText8 = wx.StaticText(id=wxID_DIALOG1STATICTEXT8,
              label='\xc3\xdc\xc2\xeb', name='staticText8', parent=self,
              pos=wx.Point(80, 480), size=wx.Size(24, 14), style=0)

        self.tftp = wx.TextCtrl(id=wxID_DIALOG1TFTP, name='tftp', parent=self,
              pos=wx.Point(120, 424), size=wx.Size(192, 22), style=0, value='')

        self.tusername = wx.TextCtrl(id=wxID_DIALOG1TUSERNAME, name='tusername',
              parent=self, pos=wx.Point(120, 448), size=wx.Size(192, 22),
              style=0, value='')

        self.tpassword = wx.TextCtrl(id=wxID_DIALOG1TPASSWORD, name='tpassword',
              parent=self, pos=wx.Point(120, 472), size=wx.Size(192, 22),
              style=wx.TE_PASSWORD, value='')

        self.staticText9 = wx.StaticText(id=wxID_DIALOG1STATICTEXT9,
              label='\xd7\xd3\xc4\xbf\xc2\xbc(\xbf\xc9\xc1\xf4\xbf\xd5)',
              name='staticText9', parent=self, pos=wx.Point(32, 504),
              size=wx.Size(82, 14), style=0)

        self.tdir = wx.TextCtrl(id=wxID_DIALOG1TDIR, name='tdir', parent=self,
              pos=wx.Point(120, 496), size=wx.Size(192, 22), style=0,
              value='wwwroot/yundan')

        self.radioButton6 = wx.RadioButton(id=wxID_DIALOG1RADIOBUTTON6,
              label='\xca\xd6\xb9\xa4\xca\xe4\xc8\xeb\xb5\xa5\xba\xc5(\xb2\xbb\xbd\xf8\xd0\xd0\xca\xb6\xb1\xf0)',
              name='radioButton6', parent=self, pos=wx.Point(112, 280),
              size=wx.Size(208, 14), style=0)
        self.radioButton6.SetValue(True)

        self.staticText10 = wx.StaticText(id=wxID_DIALOG1STATICTEXT10,
              label='\xb1\xb8\xb7\xdd\xcd\xbc\xc6\xac\xce\xc4\xbc\xfe\xa3\xba',
              name='staticText10', parent=self, pos=wx.Point(26, 374),
              size=wx.Size(84, 14), style=0)

        self.cdate = wx.CheckBox(id=wxID_DIALOG1CDATE, label='\xc8\xd5\xc6\xda',
              name='cdate', parent=self, pos=wx.Point(112, 336),
              size=wx.Size(48, 14), style=0)
        self.cdate.SetValue(False)
        self.cdate.Bind(wx.EVT_CHECKBOX, self.OnCdateCheckbox,
              id=wxID_DIALOG1CDATE)

        self.cuser = wx.CheckBox(id=wxID_DIALOG1CUSER,
              label='\xd3\xc3\xbb\xa7\xc3\xfb', name='cuser', parent=self,
              pos=wx.Point(224, 336), size=wx.Size(64, 14), style=0)
        self.cuser.SetValue(False)

        self.ctime = wx.CheckBox(id=wxID_DIALOG1CTIME, label='\xca\xb1\xbc\xe4',
              name='ctime', parent=self, pos=wx.Point(168, 336),
              size=wx.Size(48, 14), style=0)
        self.ctime.SetValue(False)

        self.checkBox1 = wx.CheckBox(id=wxID_DIALOG1CHECKBOX1,
              label='\xb1\xb8\xb7\xdd\xcd\xbc\xc6\xac\xce\xc4\xbc\xfe',
              name='checkBox1', parent=self, pos=wx.Point(112, 376),
              size=wx.Size(112, 14), style=0)
        self.checkBox1.SetValue(True)

        self.staticText11 = wx.StaticText(id=wxID_DIALOG1STATICTEXT11,
              label='\xc3\xfc\xc3\xfb\xb9\xe6\xd4\xf2\xa3\xba',
              name='staticText11', parent=self, pos=wx.Point(48, 312),
              size=wx.Size(60, 14), style=0)

    def __init__(self, parent):
        global mself
        self._init_ctrls(parent)
        mself=self
        self.sstep.Value=Frame1.step
        self.sbs.Value=Frame1.bs
        self.lstep.SetLabel(str(self.sstep.Value))
        self.lbs.SetLabel(str(self.sbs.Value))
        if Frame1.brmode==1:
            self.radioButton1.SetValue(True)
        if Frame1.brmode==2:
            self.radioButton2.SetValue(True)
        if Frame1.brmode==3:
            self.radioButton3.SetValue(True)
        if Frame1.brmode==4:
            self.radioButton4.SetValue(True)
        if Frame1.brmode==5:
            self.radioButton5.SetValue(True)
        if Frame1.brmode==6:
            self.radioButton6.SetValue(True)
            
        self.cdate.SetValue(False)
        self.ctime.SetValue(False)
        self.cuser.SetValue(False)
        if Frame1.gname/100==1:
            self.cdate.SetValue(True)
        if (Frame1.gname%100)/10==1:
            self.ctime.SetValue(True)
        if Frame1.gname%10==1:
            self.cuser.SetValue(True)     
            
        if Frame1.backupflag==1:
            self.checkBox1.SetValue(True)
        else:
            self.checkBox1.SetValue(False)
            
            
        self.tftp.SetValue(Frame1.gftp)
        self.tusername.SetValue(Frame1.gusername)
        self.tpassword.SetValue(Frame1.gpassword)
        self.tdir.SetValue(Frame1.gdir)

    def OnButton1Button(self, event):
        Frame1.step=self.sstep.Value
        Frame1.bs=self.sbs.Value
        
        if self.radioButton1.GetValue()==True:
            Frame1.brmode=1
        if self.radioButton2.GetValue()==True:
            Frame1.brmode=2  
        if self.radioButton3.GetValue()==True:
            Frame1.brmode=3
        if self.radioButton4.GetValue()==True:
            Frame1.brmode=4
        if self.radioButton5.GetValue()==True:
            Frame1.brmode=5
        if self.radioButton6.GetValue()==True:
            Frame1.brmode=6
            
        Frame1.gname=0
        if self.cdate.GetValue()==True:
            Frame1.gname=Frame1.gname+100
        if self.ctime.GetValue()==True:
            Frame1.gname=Frame1.gname+10
        if self.cuser.GetValue()==True:
            Frame1.gname=Frame1.gname+1
            
        if self.checkBox1.GetValue()==True:
            Frame1.backupflag=1
        else:
            Frame1.backupflag=0
            
                        
        Frame1.gftp = self.tftp.GetValue()
        Frame1.gusername=self.tusername.GetValue()
        Frame1.gpassword=self.tpassword.GetValue()
        Frame1.gdir=self.tdir.GetValue()
        
        
        try:
            f=file('config2.ini','w')
            f.write(str(Frame1.step)+'\n')
            f.write(str(Frame1.bs)+'\n')
            f.write(str(Frame1.brmode)+'\n')
            f.write(str(Frame1.gname)+'\n')
            f.write(str(Frame1.backupflag)+'\n')
            f.close()
            self.Destroy()
        except:
            print 'write error'
            f.close()
            
            self.Destroy()
        
        event.Skip()

    def OnButton2Button(self, event):
        self.Destroy()
        event.Skip()

    def OnSstepScroll(self, event):
        self.lstep.SetLabel(str(self.sstep.Value))
        event.Skip()

    def OnSbsScroll(self, event):
        self.lbs.SetLabel(str(self.sbs.Value))
        event.Skip() 

    def OnDialog1Close(self, event):
        self.Destroy()
        event.Skip()

    def OnCdateCheckbox(self, event):
        event.Skip()

