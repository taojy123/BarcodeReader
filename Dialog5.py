# -*- coding: cp936 -*-
#Boa:Dialog:Dialog5

import wx
import Frame1

import os
import time
import datetime
import VideoCapture
import Image,ImageEnhance,ImageDraw,ImageFont,ImageFilter
import winsound
import traceback

from a import getbarcode
from a39_ST import getbarcodeST
from a39_ZT import getbarcodeZT
from a39_YT import getbarcodeYT
from a39_EMS import getbarcodeEMS

global mself
global cam
global zoom
zoom=5
global readname
readname=''
global font
font=''
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc',60)#宋体
except:
    pass
try:
    font = ImageFont.truetype('D:\\WINDOWS\\Fonts\\simsun.ttc',60)#宋体
except:
    pass
try:
    font = ImageFont.truetype('E:\\WINDOWS\\Fonts\\simsun.ttc',60)#宋体
except:
    pass
try:
    font = ImageFont.truetype('F:\\WINDOWS\\Fonts\\simsun.ttc',60)#宋体
except:
    pass
try:
    font = ImageFont.truetype('G:\\WINDOWS\\Fonts\\simsun.ttc',60)#宋体
except:
    pass
try:
    font = ImageFont.truetype('H:\\WINDOWS\\Fonts\\simsun.ttc',60)#宋体
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simhei.ttf',60)#黑体
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\STLITI.TTF',60)#隶书
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\MSYHBD.TTF',60)#雅黑粗
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\THUPO.TTF',60)#琥珀
except:
    pass

global wmfont
wmfont=''
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc',20)#宋体
except:
    pass
try:
    wmfont = ImageFont.truetype('D:\\WINDOWS\\Fonts\\simsun.ttc',20)#宋体
except:
    pass
try:
    wmfont = ImageFont.truetype('E:\\WINDOWS\\Fonts\\simsun.ttc',20)#宋体
except:
    pass
try:
    wmfont = ImageFont.truetype('F:\\WINDOWS\\Fonts\\simsun.ttc',20)#宋体
except:
    pass
try:
    wmfont = ImageFont.truetype('G:\\WINDOWS\\Fonts\\simsun.ttc',20)#宋体
except:
    pass
try:
    wmfont = ImageFont.truetype('H:\\WINDOWS\\Fonts\\simsun.ttc',20)#宋体
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simhei.ttf',20)#黑体
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\STLITI.TTF',20)#隶书
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\MSYHBD.TTF',20)#雅黑粗
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\THUPO.TTF',20)#琥珀
except:
    pass


def zip_image(im_path, max_size):
    max_size = max_size * 950
    while True:
        size = os.path.getsize(im_path)
        if size > max_size:
            print size
            im = Image.open(im_path)
            w, h = im.size
            im = im.resize((int(w*0.9), int(h*0.9)), 1)
            im.save(im_path)
        else:
            break





def create(parent):
    return Dialog5(parent)

[wxID_DIALOG5, wxID_DIALOG5BUTTON1, wxID_DIALOG5BUTTON2, wxID_DIALOG5BUTTON3, 
 wxID_DIALOG5BUTTON4, wxID_DIALOG5BUTTON5, wxID_DIALOG5RRECEIVE, 
 wxID_DIALOG5RSEND, wxID_DIALOG5SPINCTRL1, wxID_DIALOG5STATICBITMAP1, 
 wxID_DIALOG5STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(11)]

[wxID_DIALOG5TIMER1, wxID_DIALOG5TIMER2, 
] = [wx.NewId() for _init_utils in range(2)]

class Dialog5(wx.Dialog):
    def _init_utils(self):
        # generated method, don't edit
        self.timer1 = wx.Timer(id=wxID_DIALOG5TIMER1, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_DIALOG5TIMER1)

        self.timer2 = wx.Timer(id=wxID_DIALOG5TIMER2, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer2Timer, id=wxID_DIALOG5TIMER2)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG5, name='', parent=prnt,
              pos=wx.Point(413, 208), size=wx.Size(597, 491),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='\xca\xfd\xc2\xeb\xc9\xa8\xc3\xe8\xd2\xc7\xbb\xf1\xc8\xa1')
        self._init_utils()
        self.SetClientSize(wx.Size(581, 453))
        self.SetToolTipString('')
        self.Bind(wx.EVT_CLOSE, self.OnDialog5Close)

        self.button1 = wx.Button(id=wxID_DIALOG5BUTTON1,
              label='\xb5\xa5\xb4\xce\xc9\xa8\xc3\xe8', name='button1',
              parent=self, pos=wx.Point(168, 408), size=wx.Size(104, 32),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG5BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG5BUTTON2,
              label='\xc8\xa1\xcf\xfb', name='button2', parent=self,
              pos=wx.Point(464, 408), size=wx.Size(99, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG5BUTTON2)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_DIALOG5STATICBITMAP1, name='staticBitmap1', parent=self,
              pos=wx.Point(16, 32), size=wx.Size(550, 360), style=0)

        self.rsend = wx.RadioButton(id=wxID_DIALOG5RSEND,
              label='\xb7\xa2\xbc\xfe\xc9\xa8\xc3\xe8', name='rsend',
              parent=self, pos=wx.Point(96, 8), size=wx.Size(91, 14), style=0)
        self.rsend.SetValue(False)
        self.rsend.Show(False)

        self.rreceive = wx.RadioButton(id=wxID_DIALOG5RRECEIVE,
              label='\xc7\xa9\xb5\xa5\xc9\xa8\xc3\xe8', name='rreceive',
              parent=self, pos=wx.Point(240, 8), size=wx.Size(91, 14), style=0)
        self.rreceive.SetValue(False)
        self.rreceive.Show(False)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG5STATICTEXT1,
              label='-\xd7\xb4\xcc\xac-', name='staticText1', parent=self,
              pos=wx.Point(408, 8), size=wx.Size(104, 14), style=0)

        self.button3 = wx.Button(id=wxID_DIALOG5BUTTON3,
              label='\xc1\xac\xd0\xf8\xc9\xa8\xc3\xe8', name='button3',
              parent=self, pos=wx.Point(64, 408), size=wx.Size(104, 32),
              style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_DIALOG5BUTTON3)

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_DIALOG5SPINCTRL1, initial=3,
              max=10, min=1, name='spinCtrl1', parent=self, pos=wx.Point(19,
              414), size=wx.Size(40, 22), style=wx.SP_ARROW_KEYS)

        self.button4 = wx.Button(id=wxID_DIALOG5BUTTON4,
              label='\xb7\xc5\xb4\xf3', name='button4', parent=self,
              pos=wx.Point(272, 408), size=wx.Size(96, 32), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_DIALOG5BUTTON4)

        self.button5 = wx.Button(id=wxID_DIALOG5BUTTON5,
              label='\xcb\xf5\xd0\xa1', name='button5', parent=self,
              pos=wx.Point(368, 408), size=wx.Size(96, 32), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_DIALOG5BUTTON5)

    def __init__(self, parent):
        global mself
        global cam
        global zoom
        
        mself=self
        zoom=5
        
        self._init_ctrls(parent)


        try:
            cam = VideoCapture.Device(devnum=Frame1.devid)
            print 'cam init'
            time.sleep(2)
            im=cam.getImage()
            im=cam.getImage()
            im=cam.getImage()
            print 'cam start'
            self.timer1.Start(601)
        except:
            wx.MessageBox("视频设备连接失败，请确定正确连接和设置正确设备序号", "错误", wx.OK)
            #self.Destroy()


    def OnDialog5Close(self, event):
        global cam
        self.timer1.Stop()  
        self.timer2.Stop()
        cam=''
        self.Destroy()
        event.Skip()

    def OnButton1Button(self, event):#单次扫描
        global cam
        global zoom
        global readname
        global font
        global wmfont
        
        self.timer1.Stop()
        self.timer2.Stop()
        
        try:
            #cam.saveSnapshot('image.jpg')
            #im=Image.open('image.jpg')
            im=cam.getImage()
            w,h = im.size
            im=im.crop((zoom*w/32,zoom*h/24,w-(zoom*w/32),h-(zoom*h/24)))
            #im=im.crop((w/5,h/4,w-w/8,h-h/6))
            #1600*1200
            #320,300--1400,1000  1080*700
            #im=im.crop((300,290,1400,990))
            im.save('image.jpg')
        except:
            wx.MessageBox("视频设备扫描失败，请确定正确连接", "错误", wx.OK)
            #self.Destroy()
        
        try:
            w,h = self.staticBitmap1.GetSize()
            pic=wx.Image('image.jpg')
            self.staticBitmap1.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
        except:
            print 'pic show error'
        
        self.staticText1.SetLabel('-扫描中-')
        rescode=[]
        if Frame1.brmode==1:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcode(im,Frame1.step,Frame1.bs)
            if rescode == None:
                print 'plan 1'
                im=Image.open('image.jpg')
                im=ImageEnhance.Contrast(im).enhance(5.0)
                im=im.convert('L')
                rescode = getbarcode(im,Frame1.step,5)
        if Frame1.brmode==2:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeST(im,Frame1.step,150)
        if Frame1.brmode==3:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeZT(im,Frame1.step,150)
        if Frame1.brmode==4:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeYT(im,Frame1.step,140)
            if rescode == None:
                rescode = getbarcodeYT(im,Frame1.step,120)
        if Frame1.brmode==5:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeEMS(im,Frame1.step,150)
            if rescode == None:
                rescode = getbarcodeEMS(im,Frame1.step,130)
        if Frame1.brmode==6:
            rescode = None
            
        
        if os.path.exists('output\\' + str(datetime.date.today()))==False:
            os.makedirs('output\\' + str(datetime.date.today()))
        if os.path.exists('output\\'+ str(Frame1.mself.tuser.GetLabel()) +'\\' + str(datetime.date.today()))==False:
            os.makedirs('output\\' + Frame1.mself.tuser.GetLabel() +'\\'+ str(datetime.date.today()))

        srflag=''
        if self.rsend.GetValue()==True:
            srflag='H'
        if self.rreceive.GetValue()==True:
            srflag='E'
            
        im=Image.open('image.jpg')
        
        w,h=im.size
        wh=1
        #wh=int(h/800.0+0.5)
        if wh<1:
            wh=1
        im=im.resize((w/wh,h/wh),1)
        
        draw = ImageDraw.Draw(im)
        try:
            draw.text((10,10), open('wm.dat').read().decode('gb2312'), font=wmfont,fill='#ff0000')
        except:
            pass
        
        if Frame1.regflag==0:
            draw = ImageDraw.Draw(im)
            
            try:
                draw.text((50,80), u'运单管理专家 未注册版', font=font,fill='#0000ff')
                draw.text((50,160), u'服务热线:18915537743', font=font,fill='#00ff00')
            except:
                im = im.filter(ImageFilter.BLUR).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR)
                
        strtime ='-'
        if Frame1.gname/100==1:
            strtime = strtime + str(time.strftime('%Y%m%d',time.localtime(time.time())))
        if (Frame1.gname%100)/10==1:
            strtime = strtime + str(time.strftime('%H%M%S',time.localtime(time.time())))
        if Frame1.gname%10==1:
            strtime= strtime + str(mself.tuser.GetLabel())
        if strtime =='-':
            strtime =''
            
        if rescode <> None:
            readname=rescode
            #if Frame1.regflag==0:
            #    rescode=rescode[0:10]+'XX'
            print rescode,'ok'
            
            if Frame1.mself.tuser.GetLabel()=='-':
                if Frame1.regflag==1: 
                    im.save('output\\' + str(datetime.date.today())+'\\'+ srflag + rescode + strtime + '.jpg')
                Frame1.inputfile.append((rescode,  os.getcwd()+'\\output\\' + str(datetime.date.today())+'\\'+ srflag + rescode  + strtime + '.jpg'))
                w,h=im.size
                wh=h/500.0
                if wh<1:
                    wh=1
                im2=im
                #im=im.resize((int(w/wh),int(h/wh)),1)
                if Frame1.regflag==1:
                    if Frame1.backupflag == 1:
                        backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                        im.save(backupfile)
                        zip_image(backupfile, 100)
                    updatefile='output\\update\\'+ srflag + rescode + strtime + '.jpg'
                    im.save(updatefile)
                    max_size = 60
                    im_path = updatefile
                    zip_image(im_path, max_size)
            else:
                if Frame1.regflag==1: 
                    tfn='output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + rescode + strtime + '.jpg'
                    im.save(tfn)
                    f=open(tfn,'rb')
                    ta=f.read()
                    f.close()
                    #tb=struct.pack('30s',str(Frame1.mself.tuser.GetLabel()))
                    tb='[start]' + str(Frame1.mself.tuser.GetLabel()) + '[end]'
                    f=open(tfn,'wb')
                    f.write(tb+ta)
                    f.close()
                Frame1.inputfile.append((rescode,  os.getcwd()+'\\output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + rescode + strtime + '.jpg'))
                w,h=im.size
                wh=h/500.0
                if wh<1:
                    wh=1
                im2=im
                #im=im.resize((int(w/wh),int(h/wh)),1)
                if Frame1.regflag==1:
                    if Frame1.backupflag == 1:
                        backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                        im.save(backupfile)
                        zip_image(backupfile, 100)
                    updatefile='output\\update\\'+ srflag + rescode + strtime + '.jpg'
                    im.save(updatefile)
                    max_size = 60
                    im_path = updatefile
                    zip_image(im_path, max_size)
                
            self.staticText1.SetLabel('-'+str(rescode)+' 已储存-')
            winsound.MessageBeep(64)
            #wx.MessageBox("获取成功，已储存\n" + srflag + rescode, "完成", wx.OK)
            
        else:
            #wx.MessageBox("图片获取失败或未能识别", "获取失败", wx.OK)
            self.staticText1.SetLabel('-未能识别 手工输入-')
            dlgtext = wx.TextEntryDialog(self,'请手工填写条码序列','图片未能正缺识别', readname[:-3]) 
            if dlgtext.ShowModal() == wx.ID_OK:
                fileName = str(dlgtext.GetValue())

                #如果用户有输入数据则正常保存
                if fileName != readname[:-3]:

                    try:
                        readname=fileName
                        rescode = fileName
                        if Frame1.mself.tuser.GetLabel()=='-':
                            if Frame1.regflag==1:
                                im.save('output\\' + str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg')
                            Frame1.inputfile.append((fileName,  os.getcwd()+'\\output\\' + str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg'))
                            w,h=im.size
                            wh=h/500.0
                            if wh<1:
                                wh=1
                            im2=im
                            #im=im.resize((int(w/wh),int(h/wh)),1)
                            if Frame1.regflag==1:
                                if Frame1.backupflag == 1:
                                    backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                                    im.save(backupfile)
                                    zip_image(backupfile, 100)
                                updatefile='output\\update\\'+ srflag + fileName + strtime + '.jpg'
                                im.save(updatefile)
                                max_size = 60
                                im_path = updatefile
                                zip_image(im_path, max_size)
                        else:
                            if Frame1.regflag==1:
                                tfn='output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg'
                                im.save(tfn)
                                f=open(tfn,'rb')
                                ta=f.read()
                                f.close()
                                #tb=struct.pack('30s',str(Frame1.mself.tuser.GetLabel()))
                                tb='[start]' + str(Frame1.mself.tuser.GetLabel()) + '[end]'
                                f=open(tfn,'wb')
                                f.write(tb+ta)
                                f.close()
                            Frame1.inputfile.append((fileName,  os.getcwd()+'\\output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + fileName  + strtime + '.jpg'))
                            w,h=im.size
                            wh=h/500.0
                            if wh<1:
                                wh=1
                            im2=im
                            #im=im.resize((int(w/wh),int(h/wh)),1)
                            if Frame1.regflag==1:
                                if Frame1.backupflag == 1:
                                    backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                                    im.save(backupfile)
                                    zip_image(backupfile, 100)
                                updatefile='output\\update\\'+ srflag + fileName + strtime + '.jpg'
                                im.save(updatefile)
                                max_size = 60
                                im_path = updatefile
                                zip_image(im_path, max_size)

                        self.staticText1.SetLabel('-'+str(fileName)+' 已储存-')
                        winsound.MessageBeep(64)
                        #wx.MessageBox("手工录入完成，已储存\n" + srflag + str(fileName), "完成", wx.OK)
                    except:
                        pass

                #否则按无法识别处理
                else:
                    unreadfile='output\\unread\\'+  str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))  + '.jpg'
                    im.save(unreadfile)
                    self.staticText1.SetLabel('-'+str(fileName)+' 已添加到未识别-')
                    winsound.MessageBeep(64)


            dlgtext.Destroy() 
            
        self.timer1.Start(601)
        event.Skip()

    def OnButton2Button(self, event):
        global cam
        self.timer1.Stop()
        self.timer2.Stop()
        cam=''
        self.Destroy()
        event.Skip()

    def OnTimer1Timer(self, event):
        global cam
        global zoom

        self.timer1.Stop()
        
        try:
            #cam.saveSnapshot('image.jpg')
            #im=Image.open('image.jpg')
            im=cam.getImage()
            
            
            w,h = im.size
            im=im.crop((zoom*w/32,zoom*h/24,w-(zoom*w/32),h-(zoom*h/24)))
            #im=im.crop((w/5,h/4,w-w/8,h-h/6))
            #1600*1200
            #320,300--1400,1000
            #im=im.crop((300,290,1400,990))
            im.save('image.jpg')

            #加定位框
            im=Image.open('image.jpg')
            w,h = im.size
            draw = ImageDraw.Draw(im)
            draw.line(((int(w*0.6),int(h*0.03)),(int(w*0.96),int(h*0.03))),fill='#0000ff') 
            draw.line(((int(w*0.6),int(h*0.2)),(int(w*0.96),int(h*0.2))),fill='#0000ff') 
            draw.line(((int(w*0.6),int(h*0.03)),(int(w*0.6),int(h*0.2))),fill='#0000ff') 
            draw.line(((int(w*0.96),int(h*0.03)),(int(w*0.96),int(h*0.2))),fill='#0000ff') 
            draw.line(((int(w*0.6)-1,int(h*0.03)-1),(int(w*0.96)-1,int(h*0.03)-1)),fill='#0000ff') 
            draw.line(((int(w*0.6)-1,int(h*0.2)-1),(int(w*0.96)-1,int(h*0.2)-1)),fill='#0000ff') 
            draw.line(((int(w*0.6)-1,int(h*0.03)-1),(int(w*0.6)-1,int(h*0.2)-1)),fill='#0000ff') 
            draw.line(((int(w*0.96)-1,int(h*0.03)-1),(int(w*0.96)-1,int(h*0.2)-1)),fill='#0000ff')
            im.save('image.jpg')
            
        except:
            traceback.print_exc()
            wx.MessageBox("视频设备连接失败，请确定正确连接", "错误", wx.OK)
            self.Destroy()
        
        try:
            w,h = self.staticBitmap1.GetSize()
            pic=wx.Image('image.jpg')
            self.staticBitmap1.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
        except:
            print 'pic show error'

        self.timer1.Start(601)

        event.Skip()

    def OnButton3Button(self, event):#连续扫描

        self.timer2.Stop()
        timesec = self.spinCtrl1.Value *1000
        self.timer2.Start(timesec)
        
        event.Skip()

    def OnTimer2Timer(self, event):
        global cam
        global zoom
        global readname
        global font
        global wmfont
            
        
        self.timer1.Stop()
        self.timer2.Stop()
        
        try:
            #cam.saveSnapshot('image.jpg')
            #im=Image.open('image.jpg')
            im=cam.getImage()
            w,h = im.size
            im=im.crop((zoom*w/32,zoom*h/24,w-(zoom*w/32),h-(zoom*h/24)))
            #im=im.crop((w/5,h/4,w-w/8,h-h/6))
            #1600*1200
            #320,300--1400,1000
            #im=im.crop((300,290,1400,990))
            im.save('image.jpg')
        except:
            wx.MessageBox("视频设备扫描失败，请确定正确连接", "错误", wx.OK)
            self.Destroy()
        
        try:
            w,h = self.staticBitmap1.GetSize()
            pic=wx.Image('image.jpg')
            self.staticBitmap1.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
        except:
            print 'pic show error'
        
        self.staticText1.SetLabel('-扫描中-')
        rescode=[]
        if Frame1.brmode==1:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcode(im,Frame1.step,Frame1.bs)
            if rescode == None:
                print 'plan 1'
                im=Image.open('image.jpg')
                im=ImageEnhance.Contrast(im).enhance(5.0)
                im=im.convert('L')
                rescode = getbarcode(im,Frame1.step,5)
        if Frame1.brmode==2:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeST(im,Frame1.step,150)
        if Frame1.brmode==3:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeZT(im,Frame1.step,150)
        if Frame1.brmode==4:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeYT(im,Frame1.step,140)
            if rescode == None:
                rescode = getbarcodeYT(im,Frame1.step,120)
        if Frame1.brmode==5:
            im=Image.open('image.jpg')
            im=im.convert('L')
            rescode = getbarcodeEMS(im,Frame1.step,150)
            if rescode == None:
                rescode = getbarcodeEMS(im,Frame1.step,130)
        if Frame1.brmode==6:
            rescode = None
            
        
        if os.path.exists('output\\' + str(datetime.date.today()))==False:
            os.makedirs('output\\' + str(datetime.date.today()))
        if os.path.exists('output\\'+ str(Frame1.mself.tuser.GetLabel()) +'\\' + str(datetime.date.today()))==False:
            os.makedirs('output\\' + Frame1.mself.tuser.GetLabel() +'\\'+ str(datetime.date.today()))

        srflag=''
        if self.rsend.GetValue()==True:
            srflag='H'
        if self.rreceive.GetValue()==True:
            srflag='E'
            
        im=Image.open('image.jpg')
        w,h=im.size
        wh=1
        #wh=int(h/800.0+0.5)
        if wh<1:
            wh=1
        im=im.resize((w/wh,h/wh),1)

        draw = ImageDraw.Draw(im)
        try:
            draw.text((10,10), open('wm.dat').read().decode('gb2312'), font=wmfont,fill='#ff0000')
        except:
            pass  
            
        if Frame1.regflag==0:
            draw = ImageDraw.Draw(im)
            try:
                draw.text((50,80), u'运单管理专家 未注册版', font=font,fill='#0000ff')
                draw.text((50,160), u'服务热线:18915537743', font=font,fill='#00ff00')
            except:
                im = im.filter(ImageFilter.BLUR).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR)

        strtime ='-'
        if Frame1.gname/100==1:
            strtime = strtime + str(time.strftime('%Y%m%d',time.localtime(time.time())))
        if (Frame1.gname%100)/10==1:
            strtime = strtime + str(time.strftime('%H%M%S',time.localtime(time.time())))
        if Frame1.gname%10==1:
            strtime= strtime + str(mself.tuser.GetLabel())
        if strtime =='-':
            strtime =''
            
        if rescode <> None:
           
            readname=rescode
            #if Frame1.regflag==0:
            #    rescode=rescode[0:10]+'XX'
            print rescode,'ok'
            
            
            if Frame1.mself.tuser.GetLabel()=='-':
                if Frame1.regflag==1: 
                    im.save('output\\' + str(datetime.date.today())+'\\'+ srflag + rescode + strtime + '.jpg')
                Frame1.inputfile.append((rescode,  os.getcwd()+'\\output\\' + str(datetime.date.today())+'\\'+ srflag + rescode + strtime + '.jpg'))
                w,h=im.size
                wh=h/500.0
                if wh<1:
                    wh=1
                im2=im
                #im=im.resize((int(w/wh),int(h/wh)),1)
                if Frame1.regflag==1:
                    if Frame1.backupflag == 1:
                        backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                        im.save(backupfile)
                        zip_image(backupfile, 100)
                    updatefile='output\\update\\'+ srflag + rescode + strtime + '.jpg'
                    im.save(updatefile)
                    max_size = 60
                    im_path = updatefile
                    zip_image(im_path, max_size)
            else:
                if Frame1.regflag==1: 
                    tfn='output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + rescode  + strtime + '.jpg'
                    im.save(tfn)
                    f=open(tfn,'rb')
                    ta=f.read()
                    f.close()
                    #tb=struct.pack('30s',str(Frame1.mself.tuser.GetLabel()))
                    tb='[start]' + str(Frame1.mself.tuser.GetLabel()) + '[end]'
                    f=open(tfn,'wb')
                    f.write(tb+ta)
                    f.close()
                Frame1.inputfile.append((rescode,  os.getcwd()+'\\output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + rescode + strtime + '.jpg'))
                w,h=im.size
                wh=h/500.0
                if wh<1:
                    wh=1
                im2=im
                #im=im.resize((int(w/wh),int(h/wh)),1)
                if Frame1.regflag==1:
                    if Frame1.backupflag == 1:
                        backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                        im.save(backupfile)
                        zip_image(backupfile, 100)
                    updatefile='output\\update\\'+ srflag + rescode + strtime + '.jpg'
                    im.save(updatefile)
                    max_size = 60
                    im_path = updatefile
                    zip_image(im_path, max_size)
                
            self.staticText1.SetLabel('-'+str(rescode)+' 已储存-')
            winsound.MessageBeep(64)
            #wx.MessageBox("获取成功，已储存\n" + srflag + rescode, "完成", wx.OK)
            
        else:
            #wx.MessageBox("图片获取失败或未能识别", "获取失败", wx.OK)
            self.staticText1.SetLabel('-未能识别 手工输入-')
            dlgtext = wx.TextEntryDialog(self,'请手工填写条码序列','图片未能正缺识别', readname[:-3]) 
            if dlgtext.ShowModal() == wx.ID_OK:
                fileName = str(dlgtext.GetValue())

                #如果用户有输入数据则正常保存
                if fileName != readname[:-3]:

                    try:
                        readname=fileName
                        rescode = fileName
                        if Frame1.mself.tuser.GetLabel()=='-':
                            if Frame1.regflag==1:
                                im.save('output\\' + str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg')
                            Frame1.inputfile.append((fileName,  os.getcwd()+'\\output\\' + str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg'))
                            w,h=im.size
                            wh=h/500.0
                            if wh<1:
                                wh=1
                            im2=im
                            #im=im.resize((int(w/wh),int(h/wh)),1)
                            if Frame1.regflag==1:
                                if Frame1.backupflag == 1:
                                    backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                                    im.save(backupfile)
                                    zip_image(backupfile, 100)
                                updatefile='output\\update\\'+ srflag + fileName + strtime + '.jpg'
                                im.save(updatefile)
                                max_size = 60
                                im_path = updatefile
                                zip_image(im_path, max_size)
                        else:
                            if Frame1.regflag==1:
                                tfn='output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg'
                                im.save(tfn)
                                f=open(tfn,'rb')
                                ta=f.read()
                                f.close()
                                #tb=struct.pack('30s',str(Frame1.mself.tuser.GetLabel()))
                                tb='[start]' + str(Frame1.mself.tuser.GetLabel()) + '[end]'
                                f=open(tfn,'wb')
                                f.write(tb+ta)
                                f.close()
                            Frame1.inputfile.append((fileName,  os.getcwd()+'\\output\\' + str(Frame1.mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\'+ srflag + fileName + strtime + '.jpg'))
                            w,h=im.size
                            wh=h/500.0
                            if wh<1:
                                wh=1
                            im2=im
                            #im=im.resize((int(w/wh),int(h/wh)),1)
                            if Frame1.regflag==1:
                                if Frame1.backupflag == 1:
                                    backupfile='output\\backup\\'+ srflag + rescode + strtime + '.jpg'
                                    im.save(backupfile)
                                    zip_image(backupfile, 100)
                                updatefile='output\\update\\'+ srflag + fileName + strtime + '.jpg'
                                im.save(updatefile)
                                max_size = 60
                                im_path = updatefile
                                zip_image(im_path, max_size)

                        self.staticText1.SetLabel('-'+str(fileName)+' 已储存-')
                        winsound.MessageBeep(64)
                        #wx.MessageBox("手工录入完成，已储存\n" + srflag + str(fileName), "完成", wx.OK)
                    except:
                        traceback.print_exc()

                #否则按无法识别处理
                else:
                    unreadfile='output\\unread\\'+  str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))  + '.jpg'
                    im.save(unreadfile)
                    self.staticText1.SetLabel('-'+str(fileName)+' 已添加到未识别-')
                    winsound.MessageBeep(64)

            dlgtext.Destroy() 
            
        self.timer1.Start(601)
        timesec = self.spinCtrl1.Value *1000
        self.timer2.Start(timesec)
        
        event.Skip()

    def OnButton4Button(self, event):#放大
        global zoom
        if zoom<15:
            zoom=zoom+1
        event.Skip()
        

    def OnButton5Button(self, event):#缩小
        global zoom
        if zoom>0:
            zoom=zoom-1
        event.Skip()
        


