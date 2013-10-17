# -*- coding: cp936 -*-
#Boa:Frame:Frame1


import wx
from wx.lib.anchors import LayoutAnchors
import wx.media
import sys
import os
import uuid
import time
import datetime
import threading
from PIL import Image,ImageEnhance,ImageDraw,ImageFont,ImageFilter
import struct
import win32com.client
import ftplib
import httplib
import Dialog1
import Dialog2
import Dialog3
import Dialog4
import Dialog5
import Dialog6
from a import getbarcode
from a39_ST import getbarcodeST
from a39_ZT import getbarcodeZT
from a39_YT import getbarcodeYT
from a39_EMS import getbarcodeEMS
from Dialog5 import zip_image


global mself
global step
step=3
global bs
bs=150
global path
path=''
global dir
dir=''
global fileCannot
fileCannot=[]
global runflag
runflag=0
global stopflag
stopflag=0
global srflag
srflag=''
global regflag
regflag=0
global devid
devid=0
global fsearch
fsearch=[]
global brmode
brmode=1 #������1����ͨ2����ͨ3��Բͨ4��EMS 5
global tw
global th
tw=673
th=353
global tcfg
tcfg=[]
global inputfile
inputfile=[]
global gftp
gftp='118.123.17.17'
global gusername
gusername='cnhohai'
global gpassword
gpassword='333666'
global gdir
gdir='yundan'
global gname
gname=0   #����/ʱ��/�û���
global readname
readname=''
global font
font=''
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc',60)#����
except:
    pass
try:
    font = ImageFont.truetype('D:\\WINDOWS\\Fonts\\simsun.ttc',60)#����
except:
    pass
try:
    font = ImageFont.truetype('E:\\WINDOWS\\Fonts\\simsun.ttc',60)#����
except:
    pass
try:
    font = ImageFont.truetype('F:\\WINDOWS\\Fonts\\simsun.ttc',60)#����
except:
    pass
try:
    font = ImageFont.truetype('G:\\WINDOWS\\Fonts\\simsun.ttc',60)#����
except:
    pass
try:
    font = ImageFont.truetype('H:\\WINDOWS\\Fonts\\simsun.ttc',60)#����
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simhei.ttf',60)#����
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\STLITI.TTF',60)#����
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\MSYHBD.TTF',60)#�źڴ�
except:
    pass
try:
    font = ImageFont.truetype('C:\\WINDOWS\\Fonts\\THUPO.TTF',60)#����
except:
    pass

global wmfont
wmfont=''
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('D:\\WINDOWS\\Fonts\\simsun.ttc',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('E:\\WINDOWS\\Fonts\\simsun.ttc',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('F:\\WINDOWS\\Fonts\\simsun.ttc',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('G:\\WINDOWS\\Fonts\\simsun.ttc',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('H:\\WINDOWS\\Fonts\\simsun.ttc',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simhei.ttf',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\STLITI.TTF',20)#����
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\MSYHBD.TTF',20)#�źڴ�
except:
    pass
try:
    wmfont = ImageFont.truetype('C:\\WINDOWS\\Fonts\\THUPO.TTF',20)#����
except:
    pass

global backupflag
backupflag = 1

if not os.path.exists('output\\update'):
    os.makedirs('output\\update')


if not os.path.exists('output\\backup'):
    os.makedirs('output\\backup')


if not os.path.exists('output\\unread'):
    os.makedirs('output\\unread')

if not os.path.exists('D:\\������¼'):
    os.makedirs('D:\\������¼')

if not os.path.exists('D:\\ǩ�ռ�¼'):
    os.makedirs('D:\\ǩ�ռ�¼')

class ThreadClass1(threading.Thread):
    def run(self):

        
        global mself
        global step
        global bs
        global path
        global runflag
        global stopflag
        global fileName
        global brmode
        
        runflag=1
        stopflag=0
        mself.gauge1.SetValue(0)
        
        tf=path[path.rfind('.'):].lower()
        if tf=='.jpg' or tf=='.bmp' or tf=='.png' or tf=='.gif':
            fileName=path
            w,h = mself.spic.GetSize()
            pic=wx.Image(path)
            mself.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
            mself.gauge1.SetRange(10)

            mself.gauge1.SetValue(1)
            rescode=[]
            if brmode==1:
                im=Image.open(path)
                im=ImageEnhance.Contrast(im).enhance(5.0)
                im=im.convert('L')
                mself.gauge1.SetValue(2)
                rescode = getbarcode(im,step,5)
                mself.gauge1.SetValue(6)
                if rescode == None:
                    print 'plan 2'
                    im=Image.open(path)
                    im=im.convert('L')
                    rescode = getbarcode(im,step,bs)
                    mself.gauge1.SetValue(9)
            if brmode==2:
                im=Image.open(path)
                im=im.convert('L')
                mself.gauge1.SetValue(3)
                rescode = getbarcodeST(im,step,150)
                mself.gauge1.SetValue(8)
            if brmode==3:
                im=Image.open(path)
                im=im.convert('L')
                mself.gauge1.SetValue(3)
                rescode = getbarcodeZT(im,step,150)
                mself.gauge1.SetValue(8)
            if brmode==4:
                im=Image.open(path)
                im=im.convert('L')
                mself.gauge1.SetValue(3)
                rescode = getbarcodeYT(im,step,140)
                if rescode == None:
                    rescode = getbarcodeYT(im,step,120)
                mself.gauge1.SetValue(8)
            if brmode==5:
                im=Image.open(path)
                im=im.convert('L')
                mself.gauge1.SetValue(3)
                rescode = getbarcodeEMS(im,step,150)
                if rescode == None:
                    rescode = getbarcodeEMS(im,step,130)
                mself.gauge1.SetValue(8)
            if brmode==6:
                rescode=None
                
            if rescode <> None:
                print rescode,'ok'
                mself.textCtrl1.SetValue(mself.textCtrl1.GetValue() + '\nCode:\n  ' + rescode + '\n- - - - - - - - - - - - -')  
                
                
        mself.textCtrl1.SetValue(mself.textCtrl1.GetValue() + '\nFinished' + '\n===========================')
        mself.textCtrl1.SetSelection(len(mself.textCtrl1.GetValue())-3, len(mself.textCtrl1.GetValue())-3)
        runflag=0
        mself.gauge1.SetValue(mself.gauge1.GetRange())
        
        
class ThreadClass2(threading.Thread):
    def run(self):
        global mself
        global step
        global bs
        global dir
        global fileCannot
        global runflag
        global stopflag
        global fileName
        global srflag
        global regflag
        global brmode
        global inputfile
        global readname
        global font
        global wmfont
        
        #im=Image.open("d:\\1.jpg")
        #im.save('output\\' + str(datetime.date.today())+'\\'+  '-.jpg')

        runflag=1
        stopflag=0
        mself.gauge1.SetValue(0)

        while not stopflag:
            print "Begin auto"
            runflag=0
            fileNames = os.listdir(dir)
            runflag=1
            fileCannot=[]
            fileCan=[]
            mself.gauge1.SetRange(len(fileNames))
            tg=0
            mself.gauge1.SetValue(tg)
            for file in fileNames:
                if stopflag == 1:
                    break

                tg=tg+1
                mself.gauge1.SetValue(tg)

                dotIx = file.rfind('.')

                fileBegin = file[:dotIx ]
                fileType = file[dotIx:]
                fileName = dir + '\\' + file
                if os.path.exists('output\\' + str(datetime.date.today()))==False:
                    os.makedirs('output\\' + str(datetime.date.today()))
                if os.path.exists('output\\'+ str(mself.tuser.GetLabel()) +'\\' + str(datetime.date.today()))==False:
                    os.makedirs('output\\' + mself.tuser.GetLabel() +'\\'+ str(datetime.date.today()))

                if fileType.lower()=='.jpg' or fileType.lower()=='.bmp' or fileType.lower()=='.png' or fileType.lower()=='.gif':
                    w,h = mself.spic.GetSize()
                    pic=wx.Image(fileName)
                    mself.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())

                    rescode=[]
                    if brmode==1:
                        im=Image.open(fileName)
                        im=ImageEnhance.Contrast(im).enhance(5.0)
                        im=im.convert('L')
                        rescode = getbarcode(im,step,5)
                        if rescode == None:
                            print 'plan 2'
                            im=Image.open(fileName)
                            im=im.convert('L')
                            rescode = getbarcode(im,step,bs)
                    if brmode==2:
                        im=Image.open(fileName)
                        im=im.convert('L')
                        rescode = getbarcodeST(im,step,150)
                    if brmode==3:
                        im=Image.open(fileName)
                        im=im.convert('L')
                        rescode = getbarcodeZT(im,step,150)
                    if brmode==4:
                        im=Image.open(fileName)
                        im=im.convert('L')
                        rescode = getbarcodeYT(im,step,140)
                        if rescode == None:
                            rescode = getbarcodeYT(im,step,120)
                    if brmode==5:
                        im=Image.open(fileName)
                        im=im.convert('L')
                        rescode = getbarcodeEMS(im,step,150)
                        if rescode == None:
                            rescode = getbarcodeEMS(im,step,130)
                    if brmode==6:
                        rescode = None

                    #��ʶ���
                    if rescode <> None:
                        readname=rescode
                        #if regflag==0:
                        #    rescode=rescode[0:10]+'XX'
                        print rescode,'ok'
                        mself.textCtrl1.SetValue( 'Code:\n  ' + rescode +'\n- - - - - - - - - - - - -\n' +mself.textCtrl1.GetValue())

                        im=Image.open(fileName)
                        w,h=im.size
                        wh=1
                        #wh=int(h/800.0+0.5)
                        if wh<1:
                            wh=1
                        im=im.resize((w/wh,h/wh),3)
                        draw = ImageDraw.Draw(im)
                        try:
                            draw.text((10,10), open('wm.dat').read().decode('gb2312'), font=wmfont,fill='#ff0000')
                        except:
                            pass

                        #���δע��
                        if regflag==0:
                            draw = ImageDraw.Draw(im)
                            try:
                                draw.text((50,80), u'�˵�����ר�� δע���', font=font,fill='#0000ff')
                                draw.text((50,160), u'��������:18915537743', font=font,fill='#00ff00')
                            except:
                                im = im.filter(ImageFilter.BLUR).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR)

                            im.save('Temp.jpg')

                        #��ע��
                        else:
                            strtime ='-'
                            if gname/100==1:
                                strtime = strtime + str(time.strftime('%Y%m%d',time.localtime(time.time())))
                            if (gname%100)/10==1:
                                strtime = strtime + str(time.strftime('%H%M%S',time.localtime(time.time())))
                            if gname%10==1:
                                strtime= strtime + str(mself.tuser.GetLabel())
                            if strtime =='-':
                                strtime=''

                            #ע�ᵫδ��¼�û�(���ձ����)
                            if mself.tuser.GetLabel()=='-':
                                savefile = 'output\\' + str(datetime.date.today()) + '\\' + rescode + strtime +  str(fileType)
                                savefile1 = os.getcwd() + '\\' + savefile
                                im.save(savefile1)
                                inputfile.append((rescode, savefile1))

                                if srflag == "H":
                                    savefile2 = savefile.replace('output\\' + str(datetime.date.today()), "D:\\������¼")
                                    im.save(savefile2)
                                    zip_image(savefile2, 95)
                                if srflag == "E":
                                    savefile2 = savefile.replace('output\\' + str(datetime.date.today()), "D:\\ǩ�ռ�¼")
                                    im.save(savefile2)
                                    zip_image(savefile2, 95)

                                updatefile='output\\update\\' + rescode + strtime + str(fileType)
                                im.save(updatefile)
                                zip_image(updatefile, 60)


                            #ע���ҵ�¼�û�
                            else:
                                tfn='output\\' + str(mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\' + rescode + strtime + str(fileType)
                                im.save(tfn)
                                f=open(tfn,'rb')
                                ta=f.read()
                                f.close()
                                #tb=struct.pack('30s',str(mself.tuser.GetLabel()))
                                tb='[start]' + str(mself.tuser.GetLabel()) + '[end]'
                                f=open(tfn,'wb')
                                f.write(tb+ta)
                                f.close()
                                inputfile.append((rescode, os.getcwd()+'\\output\\' + str(mself.tuser.GetLabel()) +'\\'+str(datetime.date.today())+'\\' + rescode  + strtime + str(fileType)))
                                w,h=im.size
                                wh=h/500.0
                                if wh<1:
                                    wh=1
                                im2=im
                                im=im.resize((int(w/wh),int(h/wh)),3)
                                updatefile='output\\update\\' + rescode + strtime + str(fileType)
                                im.save(updatefile)
                                while os.path.getsize(updatefile)>95000:
                                    print os.path.getsize(updatefile)
                                    w,h=im.size
                                    im=im2.resize((int(w/1.1),int(h/1.1)),3)
                                    im.save(updatefile)

                        fileCan.append(fileName)
                        #mself.textCtrl1.SetValue(mself.textCtrl1.GetValue() + '\n- - - - - - - - - - - - -')


                    #��δʶ���
                    else:
                        #ֱ�ӷ���unread�ļ��У��������ֹ�ʶ������
                        #fileCannot.append(fileName)
                        im=Image.open(fileName)
                        im.save( os.getcwd() + '\\output\\unread\\' + file )

                        mself.textCtrl1.SetValue( 'Can not read\n- - - - - - - - - - - - -\n' + mself.textCtrl1.GetValue())

                    #mself.textCtrl1.SetSelection(len(mself.textCtrl1.GetValue())+1000, len(mself.textCtrl1.GetValue())+1000)

                    #ʶ�����ɾ��ʶ�����ԭ�ļ�
                    try:
                        os.remove(fileName)
                    except:
                        pass

            mself.textCtrl1.SetValue('Finished\nRead:'+str(len(fileCan))+',Cannot Read:'+ str(len(fileCannot)) + '\n= = = = = = = = = = =\n' + mself.textCtrl1.GetValue())
            #mself.textCtrl1.SetSelection(len(mself.textCtrl1.GetValue())+1000, len(mself.textCtrl1.GetValue())+1000)
            runflag=0

            time.sleep(600)



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GAUGE1, wxID_FRAME1PANEL1, wxID_FRAME1SPIC, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TUSER, 
] = [wx.NewId() for _init_ctrls in range(8)]

[wxID_FRAME1TIMER1] = [wx.NewId() for _init_utils in range(1)]

class Frame1(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        self.timer1 = wx.Timer(id=wxID_FRAME1TIMER1, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_FRAME1TIMER1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(479, 237), size=wx.Size(689, 411),
              style=wx.DEFAULT_FRAME_STYLE,
              title='\xd4\xcb\xb5\xa5\xb9\xdc\xc0\xed\xd7\xa8\xbc\xd2')
        self._init_utils()
        self.SetClientSize(wx.Size(673, 373))
        self.SetBackgroundColour(wx.Colour(254, 244, 209))
        self.SetIcon(wx.Icon('C:\\ReaderPlugin\\icon.ico',
              wx.BITMAP_TYPE_ICO))
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(673, 373),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('')
        self.panel1.SetBackgroundColour(wx.Colour(255, 196, 136))
        self.panel1.Bind(wx.EVT_SIZE, self.OnPanel1Size)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(456, 24), size=wx.Size(176, 312),
              style=wx.VSCROLL | wx.TE_MULTILINE, value='')
        self.textCtrl1.SetEditable(False)
        self.textCtrl1.SetBackgroundColour(wx.Colour(238, 255, 247))

        self.spic = wx.StaticBitmap(bitmap=wx.NullBitmap, id=wxID_FRAME1SPIC,
              name='spic', parent=self.panel1, pos=wx.Point(40, 24),
              size=wx.Size(400, 280), style=0)
        self.spic.SetToolTipString('-')
        self.spic.Bind(wx.EVT_LEFT_DOWN, self.OnSpicLeftDown)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='\xc6\xf3\xd2\xb5\xb0\xe6', name='staticText1',
              parent=self.panel1, pos=wx.Point(280, 200), size=wx.Size(147, 56),
              style=0)
        self.staticText1.SetFont(wx.Font(36, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, ''))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='\xd4\xcb\xb5\xa5\xb9\xdc\xc0\xed\xd7\xa8\xbc\xd2',
              name='staticText2', parent=self.panel1, pos=wx.Point(48, 128),
              size=wx.Size(336, 75), style=0)
        self.staticText2.SetFont(wx.Font(42, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, '\xce\xa2\xc8\xed\xd1\xc5\xba\xda'))

        self.gauge1 = wx.Gauge(id=wxID_FRAME1GAUGE1, name='gauge1',
              parent=self.panel1, pos=wx.Point(32, 312), range=100,
              size=wx.Size(408, 24), style=wx.GA_HORIZONTAL)
        self.gauge1.SetToolTipString('\xc8\xce\xce\xf1\xbd\xf8\xb6\xc8')
        self.gauge1.SetValue(0)
        self.gauge1.SetLabel('')

        self.tuser = wx.StaticText(id=wxID_FRAME1TUSER, label='-', name='tuser',
              parent=self.panel1, pos=wx.Point(8, 3), size=wx.Size(4, 14),
              style=0)

    def __init__(self, parent):
        global mself
        global regflag
        global tcfg
        global step
        global bs
        global brmode
        global gname
        global devid
        global dir
        global srflag
        
        mself=self
        self._init_ctrls(parent)
        
        tcfg.append('config')
        tcfg.append('')
        tcfg.append('��������')
        tcfg.append('')
        tcfg.append('1')
        tcfg.append('0.1')
        tcfg.append('�½�')
        tcfg.append('20')
        tcfg.append('0')
        tcfg.append('')
        tcfg.append('')
        tcfg.append('��������')
        tcfg.append('')
        tcfg.append('����')
        tcfg.append('����')
        tcfg.append('0.1')
        tcfg.append('')
        tcfg.append('')
        tcfg.append('')
        tcfg.append('')
        tcfg.append('')
        tcfg.append('')
        tcfg.append('0')
        tcfg.append('')
        tcfg.append('0')
        tcfg.append('�����')


        try:
            f=file('config.ini','r')
            for i in range(1,26):
                tcfg[i]=f.readline().replace('\n','')
            f.close()
        except:
            print 'read tcfg error'

        try:
            f=file('config2.ini','r')
            step=int(f.readline().replace('\n',''))
            bs=int(f.readline().replace('\n',''))
            brmode=int(f.readline().replace('\n',''))
            gname=int(f.readline().replace('\n',''))
            backupflag=int(f.readline().replace('\n',''))
            f.close()
        except:
            print 'read set error'

        try:
            f=file('config3.ini','r')
            devid=int(f.readline().replace('\n',''))
            f.close()
        except:
            print 'read dev error'
        
        menubar = wx.MenuBar()
        mfile = wx.Menu()
        mfile.Append(11, '����Ƭʶ��', '')
        mfile.Append(12, '�ļ���ʶ��', '')
        mfile.Append(13, '��������ʶ��', '')
        mfile.Append(14, 'ǩ������ʶ��', '')
        mfile.Append(15, '����ɨ���ǻ�ȡ', '')
        mfile.Append(16, '�˳�', '')
        mopera = wx.Menu()
        mopera.Append(21, '��ֹʶ��', '')
        mopera.Append(22, '��¼δʶ���浥', '')
        mopera.Append(23, '�����˵�¼����Ϣ', '')
        mopera.Append(24, '�ϴ��Ѵ���ͼƬ', '')
        moptions = wx.Menu()
        moptions.Append(31, '��������', '')
        moptions.Append(32, 'ɨ���豸�������', '')
        moptions.Append(33, '�˵�¼����Ϣ����', '')
        moptions.Append(34, '���ˮӡ����', '')
        musers = wx.Menu()
        musers.Append(41, '�û���¼', '')
        musers.Append(42, '�����û�', '')
        musers.Append(43, 'ɾ���û�', '')
        musers.Append(44, '����ͼƬ����', '')
        msearch = wx.Menu()
        msearch.Append(51, '�����Ų�ѯ', '')
        msearch.Append(52, '�����ڲ�ѯ', '')
        mhelp = wx.Menu()
        mhelp.Append(61, '����', '')
        mhelp.Append(62, '����', '')
        mhelp.Append(63, 'ע��', '')
        
        menubar.Append(mfile, '�ļ�')
        menubar.Append(mopera, '����')
        menubar.Append(moptions, 'ѡ��')
        menubar.Append(musers, '�û�')
        menubar.Append(msearch, '��ѯ')
        menubar.Append(mhelp, '����')
        
        self.Bind(wx.EVT_MENU, self.Onpath, id=11)
        self.Bind(wx.EVT_MENU, self.Ondir, id=12)
        self.Bind(wx.EVT_MENU, self.Onsend, id=13)
        self.Bind(wx.EVT_MENU, self.Onreceive, id=14)
        self.Bind(wx.EVT_MENU, self.Onscan, id=15)
        self.Bind(wx.EVT_MENU, self.Onquit, id=16)
        self.Bind(wx.EVT_MENU, self.Onstop, id=21)
        self.Bind(wx.EVT_MENU, self.Onrefill, id=22)
        self.Bind(wx.EVT_MENU, self.Onoutinput, id=23)
        self.Bind(wx.EVT_MENU, self.Onupdatepic, id=24)
        self.Bind(wx.EVT_MENU, self.Onset, id=31)
        self.Bind(wx.EVT_MENU, self.Ondev, id=32)
        self.Bind(wx.EVT_MENU, self.Oninput, id=33)
        self.Bind(wx.EVT_MENU, self.Onwatermark, id=34)
        self.Bind(wx.EVT_MENU, self.Onlogin, id=41)
        self.Bind(wx.EVT_MENU, self.Onadd, id=42)
        self.Bind(wx.EVT_MENU, self.Ondel, id=43)
        self.Bind(wx.EVT_MENU, self.Ondecode, id=44)
        self.Bind(wx.EVT_MENU, self.Onsearchname, id=51)
        self.Bind(wx.EVT_MENU, self.Onsearchdate, id=52)
        self.Bind(wx.EVT_MENU, self.Onhelp, id=61)
        self.Bind(wx.EVT_MENU, self.Onabout, id=62)
        self.Bind(wx.EVT_MENU, self.Onreg, id=63)
        self.SetMenuBar(menubar)
        
        try:
            conn=httplib.HTTPConnection('www.baidu.com')
            conn.request("GET", "/")
            r=conn.getresponse()
            #r.getheaders() #��ȡ���е�httpͷ
            ts=  r.getheader('date') #��ȡhttpͷdate����
            #print ts
            structtime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
            #print structtime
            numtime=int(time.mktime(structtime))
            #print numtime

            f=file("reg.dat",'a')
            f.close()
            f=file("reg.dat",'r')
            code=int(f.read())
            code=int(code/987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321)
            mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
            f.close()
            if (int(code/100)*67 - int(code%100)) % 100 == 0:
                limitdate = int(code//100)-int(mac,16)
                #nowdate = int(time.time()//86400)
                nowdate = int(numtime //86400)
                
                if limitdate>=nowdate:
                    regflag=1
                else:
                    dlg=wx.MessageDialog(self,'ע��ʧ�ܣ�ע�����ѹ���','ע�Ṧ��λ�ڰ����˵�',wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy
                    regflag=0
            else:
                dlg=wx.MessageDialog(self,'�����δע�ᣬ�����ò��ֹ���','ע�Ṧ��λ�ڰ����˵�',wx.OK)
                dlg.ShowModal()
                dlg.Destroy
                regflag=0

        except:
            try:
                regflag=0
                print "no wlan"
                numtime = int(time.time())
                f=file("reg.dat",'a')
                f.close()
                f=file("reg.dat",'r')
                code=int(f.read())
                code=int(code/987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321)
                mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
                f.close()
                if (int(code/100)*67 - int(code%100)) % 100 == 0:
                    limitdate = int(code//100)-int(mac,16)
                    #nowdate = int(time.time()//86400)
                    nowdate = int(numtime //86400)
                    if limitdate>=nowdate:
                        regflag=1
            except:
                pass

            if not regflag:
                dlg=wx.MessageDialog(self,'�����δע�ᣬ�����ò��ֹ��ܡ�\n��ע���û������������ʹ�á�','ע�Ṧ��λ�ڰ����˵�',wx.OK)
                dlg.ShowModal()
                dlg.Destroy
                regflag=0


        try:
            conf = open("config_dir.ini").read()
            dir = conf.split(",")[0]
            srflag = conf.split(",")[1]
            self.textCtrl1.SetValue('ʶ����\n')
            self.staticText1.SetLabel('')
            self.staticText2.SetLabel('')
            t = ThreadClass2()
            t.start()
        except:
            print "has no auto dir"
        
        #print gbStr

        #self.dirPickerCtrl1.GetPath()
        #im=Image.open(r'E:\1.bmp')
        #im.show()
        #self.picbox.SetBitmap(im)


    def OnPanel1Size(self, event):

        mw,mh = self.panel1.GetSize()

        if mw>650 and mh>320 :
            
            try:
                #main s(673 353)  
                

                #gauge1 p(32,312) s(408, 24)
                self.gauge1.SetPosition((32,mh-41))
                self.gauge1.SetSize((mw-265,24))
                
                #textCtrl1 p(465,24) s(176, 312)
                self.textCtrl1.SetPosition((mw-208,24))
                self.textCtrl1.SetSize((176,mh-41))
                
                '''
                #b2(32, 352) b3(152, 352) b4(272, 352) b5(392, 352) b1(512, 352)
                self.button2.SetPosition((32,mh-51))
                self.button3.SetPosition((152,mh-51))
                self.button4.SetPosition((272,mh-51))
                self.button5.SetPosition((392,mh-51))
                self.button1.SetPosition((512,mh-51))
                '''
                
                #spic p(40,24) s(400,280)
                self.spic.SetSize((mw-273,mh-73))
                
                self.timer1.Start(500)
                
            except:
                pass
            
        event.Skip()

    def OnFrame1Close(self, event):

        try:
            os.remove('temp.jpg')
        except:
            pass
        try:
            os.remove('image.jpg')
        except:
            pass

        try:
            Dialog1.mself.Destroy()
        except:
            pass
        try:
            Dialog2.mself.Destroy()
        except:
            pass
        try:
            Dialog3.mself.Destroy()
        except:
            pass
        try:
            Dialog4.mself.Destroy()
        except:
            pass
        try:
            Dialog5.mself.Destroy()
        except:
            pass
        try:
            Dialog6.mself.Destroy()
        except:
            pass
        
        self.Destroy()
        event.Skip()

    def OnTimer1Timer(self, event):
        global fileName
        global tw
        global th
        
        try:
            w,h = self.spic.GetSize()
            if (w<>tw or h<>th) and fileName<>'':
                self.timer1.Stop()
                w,h = self.spic.GetSize()
                pic=wx.Image(fileName)
                self.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
                tw=w
                th=h
        except:
            pass
        event.Skip()
        


    def Onpath(self, event):
        
        global path
        global runflag
        
        if runflag==1:
            dlg=wx.MessageDialog(self,'ʶ�����ڽ����У����Ժ�','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy
        else:
            wildcard = "JPG (*.jpg)|*.jpg|"   \
                       "GIF (*.gif)|*.gif|"   \
                       "BMP (*.bmp)|*.bmp|"   \
                       "PNG (*.png)|*.png|"   \
                       "All files (*.*)|*.*"
            dlg = wx.FileDialog(
                self, message="��ѡ��һ����Ƭ",
                defaultDir=os.getcwd(), 
                defaultFile="",
                wildcard=wildcard,
                style=wx.OPEN
                )
            if dlg.ShowModal() == wx.ID_OK:
                paths = dlg.GetPaths()
                for path in paths:
                    self.textCtrl1.SetValue('ʶ����\n')
                    self.staticText1.SetLabel('')
                    self.staticText2.SetLabel('')
                    t = ThreadClass1()
                    t.start()
            dlg.Destroy()
                
        
    def Ondir(self, event):

        global dir
        global runflag
        global srflag
        global stopflag
        global fileCannot
        
        if runflag==1:
            dlg=wx.MessageDialog(self,'ʶ�����ڽ����У����Ժ�','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.DirDialog(self, "Choose a directory:",style=wx.DD_DEFAULT_STYLE)
            if dlg.ShowModal() == wx.ID_OK:
                dir=dlg.GetPath()
                open("config_dir.ini", "w").write(dir.encode('gbk') + ",")
                dlg=wx.MessageDialog(self,'ϵͳ��ÿ��10�����Զ�ɨ��һ�Σ����ȷ����ʼ..','��ʾ',wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                #ѭ���Զ�ɨ��
                self.textCtrl1.SetValue('ʶ����\n')
                self.staticText1.SetLabel('')
                self.staticText2.SetLabel('')
                srflag=''
                t = ThreadClass2()
                t.start()
            dlg.Destroy()


    def Onsend(self, event):

        global dir
        global runflag
        global srflag
        global fileCannot
        
        if runflag==1:
            dlg=wx.MessageDialog(self,'ʶ�����ڽ����У����Ժ�','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy
        else:
            dlg = wx.DirDialog(self, "Choose a directory:",style=wx.DD_DEFAULT_STYLE)
            if dlg.ShowModal() == wx.ID_OK:
                dir=dlg.GetPath()
                open("config_dir.ini", "w").write(dir.encode('gbk') + ",H")
                dlg=wx.MessageDialog(self,'ϵͳ��ÿ��10�����Զ�ɨ��һ�Σ����ȷ����ʼ..','��ʾ',wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                #ѭ���Զ�ɨ��
                self.textCtrl1.SetValue('ʶ����\n')
                self.staticText1.SetLabel('')
                self.staticText2.SetLabel('')
                srflag='H'
                t = ThreadClass2()
                t.start()

            dlg.Destroy()
            
    def Onreceive(self, event):

        global dir
        global runflag
        global srflag
        global fileCannot
        
        if runflag==1:
            dlg=wx.MessageDialog(self,'ʶ�����ڽ����У����Ժ�','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            dlg = wx.DirDialog(self, "Choose a directory:",style=wx.DD_DEFAULT_STYLE)
            if dlg.ShowModal() == wx.ID_OK:
                dir=dlg.GetPath()
                open("config_dir.ini", "w").write(dir.encode('gbk') + ",E")
                dlg=wx.MessageDialog(self,'ϵͳ��ÿ��10�����Զ�ɨ��һ�Σ����ȷ����ʼ..','��ʾ',wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
                #ѭ���Զ�ɨ��
                self.textCtrl1.SetValue('ʶ����\n')
                self.staticText1.SetLabel('')
                self.staticText2.SetLabel('')
                srflag='E'
                t = ThreadClass2()
                t.start()
            dlg.Destroy()
            
    def Onscan(self, event): 
        Dialog5.create(None).Show() 

    def Onquit(self, event): 
        self.Close()

    def Onstop(self, event):   #��ֹʶ��
        global stopflag
        global runflag
        stopflag = 1
        runflag = 0
        dlg=wx.MessageDialog(self,'����ֹʶ��','��ʾ',wx.OK)
        dlg.ShowModal()
        dlg.Destroy
        
        ts=self.textCtrl1.GetValue()
        self.textCtrl1.SetValue(self.textCtrl1.GetValue()+'\nSTOP')


    def Onrefill(self, event):   #��¼
        global fileCannot
        global srflag
        global inputfile

        if len(fileCannot)<1:
            dlg=wx.MessageDialog(self,'�ļ���ʶ�������û��δ��ʶ�����Ƭ','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
                         
        for file in fileCannot:
            global readname
            
            dotIx = file.rfind('.')
            dirIx = file.rfind('\\')
            fileDir = file[:dirIx+1 ]
            fileName = file[dirIx+1:dotIx]
            fileType = file[dotIx:]
            
            w,h = mself.spic.GetSize()
            mself.spic.SetBitmap(wx.Image(file).Rescale(w,h).ConvertToBitmap())
            dlgtext = wx.TextEntryDialog(self,'����д����ʾͼƬ�е���������','δʶ���ļ���¼', readname[:-3]) 
            if dlgtext.ShowModal() == wx.ID_OK:
                fileName = str(dlgtext.GetValue())
                readname=fileName
                
                try:
                    im=Image.open(file)
                    w,h=im.size
                    wh=1
                    #wh=int(h/800.0+0.5)
                    if wh<1:
                        wh=1
                    im=im.resize((w/wh,h/wh),3)
                    
                    strtime ='-'
                    if gname/100==1:
                        strtime = strtime + str(time.strftime('%Y%m%d',time.localtime(time.time())))
                    if (gname%100)/10==1:
                        strtime = strtime + str(time.strftime('%H%M%S',time.localtime(time.time())))
                    if gname%10==1:
                        strtime= strtime + str(mself.tuser.GetLabel())
                    if strtime =='-':
                        strtime=''
                        
                    if mself.tuser.GetLabel()=='-':
                        im.save('output\\' + str(datetime.date.today())+'\\' + fileName + strtime + fileType)
                        inputfile.append((fileName, os.getcwd()+'\\output\\' + str(datetime.date.today())+'\\' + fileName  + strtime + fileType))
                        w,h=im.size
                        wh=h/500.0
                        if wh<1:
                            wh=1
                        im2=im
                        im=im.resize((int(w/wh),int(h/wh)),3)
                        updatefile='output\\update\\' + fileName + strtime + str(fileType)
                        im.save(updatefile)
                        while os.path.getsize(updatefile)>95000:
                            print os.path.getsize(updatefile)
                            w,h=im.size
                            im=im2.resize((int(w/1.1),int(h/1.1)),3)
                            im.save(updatefile)
                    else:
                        tfn='output\\' + str(mself.tuser.GetLabel()) +'\\'+ str(datetime.date.today())+'\\' + fileName  + strtime + fileType
                        im.save(tfn)
                        f=open(tfn,'rb')
                        ta=f.read()
                        f.close()
                        #tb=struct.pack('30s',str(mself.tuser.GetLabel()))
                        tb='[start]' + str(mself.tuser.GetLabel()) + '[end]'
                        f=open(tfn,'wb')
                        f.write(tb+ta)
                        f.close()
                        inputfile.append((fileName, os.getcwd()+'\\output\\' + str(mself.tuser.GetLabel()) +'\\'+ str(datetime.date.today())+'\\' + fileName  + strtime + fileType))
                        w,h=im.size
                        wh=h/500.0
                        if wh<1:
                            wh=1
                        im2=im
                        im=im.resize((int(w/wh),int(h/wh)),3)
                        updatefile='output\\update\\' + fileName + strtime + str(fileType)
                        im.save(updatefile)
                        while os.path.getsize(updatefile)>95000:
                            print os.path.getsize(updatefile)
                            w,h=im.size
                            im=im2.resize((int(w/1.1),int(h/1.1)),3)
                            im.save(updatefile)
                except:
                    pass
            dlgtext.Destroy() 
            
        fileCannot=[]
        dlg=wx.MessageDialog(self,'������в�¼','��ʾ',wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    
    def Onoutinput(self, event): 
        global inputfile
        global tcfg
        
        inputfile=list(set(inputfile))
        
        if len(inputfile)>0:
            xlApp = win32com.client.Dispatch('Excel.Application')
            try:
                xlBook = xlApp.Workbooks.Open(os.getcwd()+'\\output\\'+str(time.localtime(time.time())[0])+'��'+str(time.localtime(time.time())[1])+'��' + '������¼.xls') 
            except:
                xlBook = xlApp.Workbooks.Add()
                xlBook.SaveAs(os.getcwd()+'\\output\\'+str(time.localtime(time.time())[0])+'��'+str(time.localtime(time.time())[1])+'��' + '������¼.xls')
                
            try:
                xlSht = xlBook.Worksheets(str(time.localtime(time.time())[2]))
            except:
                xlSht = xlApp.sheets.Add()
                xlSht.Cells(1,1).Value='�˵����'
                xlSht.Cells(1,2).Value='�ļ�����'
                xlSht.Cells(1,3).Value='�ļ�����'
                xlSht.Cells(1,4).Value='Ŀ�ĵ�'
                xlSht.Cells(1,5).Value='����'
                xlSht.Cells(1,6).Value='ʵ��'
                xlSht.Cells(1,7).Value='���ʽ'
                xlSht.Cells(1,8).Value='�˷�'
                xlSht.Cells(1,9).Value='���ջ���'
                xlSht.Cells(1,10).Value='ȡ��Ա'
                xlSht.Cells(1,11).Value='�ļ���˾'
                xlSht.Cells(1,12).Value='�Ա�������'
                xlSht.Cells(1,13).Value='ԭ�ĵ�'
                xlSht.Cells(1,14).Value='Ŀ������'
                xlSht.Cells(1,15).Value='��Ʒ���'
                xlSht.Cells(1,16).Value='�������'
                xlSht.Cells(1,17).Value='�Ʒ�����'
                xlSht.Cells(1,18).Value='���տ�������'
                xlSht.Cells(1,19).Value='�ɷ�������������'
                xlSht.Cells(1,20).Value='��ע'
                xlSht.Cells(1,21).Value='ת�뵥��'
                xlSht.Cells(1,22).Value='�ӵ���'
                xlSht.Cells(1,23).Value='��ǩ����'
                xlSht.Cells(1,24).Value='�ص����'
                xlSht.Cells(1,25).Value='�ͻ����'
                xlSht.Cells(1,26).Value='�ļ��绰'
                xlSht.Cells(1,27).Value='����֪ͨ'
                xlSht.Cells(1,28).Value='�ļ���'
                xlSht.Cells(1,29).Value='�ļ���ַ'
                xlSht.Cells(1,30).Value='�ռ��绰'
                xlSht.Cells(1,31).Value='�ռ���'
                xlSht.Cells(1,32).Value='�ռ���˾'
                xlSht.Cells(1,33).Value='�ռ���ַ'
                xlSht.Cells(1,34).Value='����ʽ'
                xlSht.Cells(1,35).Value='�����'
                xlSht.Cells(1,36).Value='��Ʒ����'
                xlSht.Cells(1,37).Value='������������'
                xlSht.Cells(1,38).Value='�������ý��'
                xlSht.Cells(1,39).Value='�˷ѱұ�'
                xlSht.name = str(time.localtime(time.time())[2])
                
            rowi=2
            while str(xlSht.Cells(rowi,1))<>'None' and str(xlSht.Cells(rowi,1))<>'':
                rowi=rowi+1
                
            print inputfile
            
            try:
                for rescdoe,hlink in inputfile:
                    xlSht.Cells(rowi,1).Value = "'"+rescdoe
                    xlSht.Cells(rowi,1).Hyperlinks.Add(xlSht.Cells(rowi,1),hlink)
                    xlSht.Cells(rowi,2).Value = tcfg[1]
                    xlSht.Cells(rowi,3).Value = tcfg[2]
                    xlSht.Cells(rowi,4).Value = tcfg[3]
                    xlSht.Cells(rowi,5).Value = tcfg[4]
                    xlSht.Cells(rowi,6).Value = tcfg[5]
                    xlSht.Cells(rowi,7).Value = tcfg[6]
                    xlSht.Cells(rowi,8).Value = tcfg[7]
                    xlSht.Cells(rowi,9).Value = tcfg[8]
                    xlSht.Cells(rowi,10).Value = tcfg[9]
                    xlSht.Cells(rowi,11).Value = tcfg[10]
                    xlSht.Cells(rowi,13).Value = tcfg[11]
                    xlSht.Cells(rowi,14).Value = tcfg[12]
                    xlSht.Cells(rowi,15).Value = tcfg[13]
                    xlSht.Cells(rowi,16).Value = tcfg[14]
                    xlSht.Cells(rowi,17).Value = tcfg[15]
                    xlSht.Cells(rowi,18).Value = tcfg[16]
                    xlSht.Cells(rowi,20).Value = tcfg[17]
                    xlSht.Cells(rowi,26).Value = tcfg[18]
                    xlSht.Cells(rowi,28).Value = tcfg[19]
                    xlSht.Cells(rowi,29).Value = tcfg[20]
                    xlSht.Cells(rowi,34).Value = tcfg[21]
                    xlSht.Cells(rowi,35).Value = tcfg[22]
                    xlSht.Cells(rowi,36).Value = tcfg[23]
                    xlSht.Cells(rowi,38).Value = tcfg[24]
                    xlSht.Cells(rowi,39).Value = tcfg[25]
                    rowi=rowi+1
                wx.MessageBox("�����,���ε���"+str(len(inputfile))+"����ʶ����˵�¼����Ϣ", "�����˵�¼����Ϣ", wx.OK)
                inputfile=[]
            except:
                print 'outinput error'
            
            xlBook.Close(SaveChanges=1)
            del xlApp
            
        else:
            wx.MessageBox("����û��δ�������˵���Ϣ,��������ʶ�����д˲���", "�����˵�¼����Ϣ", wx.OK)
        
    
    def Onupdatepic(self, event):
        global gftp
        global gusername
        global gpassword
        global gdir
        
        updatepics = os.listdir('output\\update')
        if len(updatepics)>0:
            try:
                f=ftplib.FTP(gftp,gusername,gpassword)
                hostdir='wwwroot/yundan'
                if gdir <> '':
                    hostdir=hostdir+'/'+gdir
                if mself.tuser.GetLabel()=='-':
                    f.cwd(hostdir)
                else:
                    try:
                        f.mkd(hostdir+ '/' + mself.tuser.GetLabel())
                    except:
                        pass
                    f.cwd(hostdir+ '/' + mself.tuser.GetLabel())
                    
                wx.MessageBox("�ϴ��ٶ����������Ӱ�죬�����ĵȴ������ϴ����ɹ�֧��������\n  ���ȷ����ʼ�ϴ�", "�ϴ��Ѵ���ͼƬ", wx.OK)
            except:
                wx.MessageBox("��������������ʧ��", "�ϴ��Ѵ���ͼƬ", wx.OK)
                updatepics=[]
        else:
            wx.MessageBox("Ŀǰû�д��ϴ���ͼƬ", "�ϴ��Ѵ���ͼƬ", wx.OK)
            
        unsuc=0
        mself.gauge1.SetRange(len(updatepics))
        i=0
        for picname in updatepics:
            i=i+1
            mself.gauge1.SetValue(i)
            try:
                f.storbinary('STOR '+picname,open('output\\update\\'+picname,'rb'))
                os.remove('output\\update\\'+picname)
                print picname + 'seccessed'
            except:
                unsuc=unsuc+1
                print 'ftp update error'
                
        try:
            f.quit()
        except:
            pass
        wx.MessageBox("�ϴ���ɣ�"+str(unsuc)+"��ͼƬ�ϴ����ɹ�", "�ϴ��Ѵ���ͼƬ", wx.OK)

        
    def Onset(self, event):
        Dialog1.create(None).Show() 

    def Ondev(self, event):
        global devid
        
        dlgtext = wx.TextEntryDialog(self,'����д��ʹ�õ�ɨ���豸����ţ���0��1��2..','ɨ���豸�������', str(devid)) 
        if dlgtext.ShowModal() == wx.ID_OK:
            try:
                devid = int(dlgtext.GetValue())
                open("config3.ini","w").write(str(devid)+"\n")
            except:
                pass
        dlgtext.Destroy() 
        
    def Oninput(self, event):
        Dialog6.create(None).Show() 
        
    def Onwatermark(self, event):
        dlgtext = wx.TextEntryDialog(self,'�������������') 
        if dlgtext.ShowModal() == wx.ID_OK:
            if dlgtext.GetValue() == "abc123":
                dlgtext2 = wx.TextEntryDialog(self,'������ˮӡ����') 
                if dlgtext2.ShowModal() == wx.ID_OK:
                    wm = dlgtext2.GetValue().encode('gb2312')
                    open("wm.dat","w").write(wm)
                dlgtext2.Destroy() 
        dlgtext.Destroy()
        
        
        
    def Onlogin(self, event):
        return
        Dialog4.create(None).Show() 
        
    def Onadd(self, event):
        Dialog3.create(None).Show() 

    def Ondel(self, event):
        rc = wx.MessageBox("ȷ��Ҫɾ�����û�", "ɾ���û�", wx.YES_NO | wx.ICON_QUESTION) #2/yes : 8/no
        if rc==2 or self.tuser.GetLabel()<>'-':
            f=file('cod.dat','a')
            f.close()
            f=file('cod.dat','r')
            s=f.read()
            f.close()
            su=''
            try:
                for n in self.tuser.GetLabel():
                    su=su+chr((ord(n)-12))
                s=s.replace(su,'')
                f=file('cod.dat','w')
                f.write(s)
                f.close()
                self.tuser.SetLabel('-')
                wx.MessageBox("�û���ɾ��", "ɾ���û�", wx.OK)
            except:
                pass
                
    def Ondecode(self, event):
        
        dlg = wx.DirDialog(self, "��ѡ��������ͼƬĿ¼",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            dir=dlg.GetPath()
            
            if os.path.exists(dir+'\\decode')==False:
                os.makedirs(dir+'\\decode')
                
            fileNames = os.listdir(dir)
            for file in fileNames:
                dotIx = file.rfind('.')
                fileBegin = file[:dotIx ]
                fileType = file[dotIx:]
                fileName = dir + '\\' + file
                fileOut = dir + '\\decode\\' + file
                
                if fileType.lower()=='.jpg' or fileType.lower()=='.bmp' or fileType.lower()=='.png' or fileType.lower()=='.gif':
                    try:
                        f=open(fileName,'rb')
                        ta=f.read()
                        f.close()
                        ta=ta.replace('[start]' + str(mself.tuser.GetLabel()) + '[end]','')
                        f=open(fileOut,'wb')
                        f.write(ta)
                        f.close()
                    except:
                        pass
                    
            wx.MessageBox("��ɽ��룬����ԭͼƬĿ¼�µ�decode�ļ��в鿴", "ͼƬ����", wx.OK)
                    
        dlg.Destroy()
        
        
        
    def Onsearchname(self, event):
        global fileName
        global fsearch
        
        dlgtext = wx.TextEntryDialog(self,'�������˵���ţ��磺666907994815','�����Ų�ѯ', '') 
        if dlgtext.ShowModal() == wx.ID_OK: 
            if mself.tuser.GetLabel()=='-':
                dirs=os.listdir('output')
                fsearch=[]
                for dirName in dirs:
                    try:
                        fileNames = os.listdir('output\\' + dirName)
                        for file in fileNames:
                            if file.rfind(dlgtext.GetValue()) > -1:
                                fsearch.append('output\\' + dirName + '\\' + file)
                    except:
                        pass
                try:
                    w,h = self.spic.GetSize()
                    fileName=fsearch[0]
                    pic=wx.Image(fileName)
                    self.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
                    dlgtext.Destroy()
                    self.spic.SetToolTipString('���ͼƬ��ʾ��һ��')
                    fsearch.remove(fsearch[0])
                    return
                except:
                    self.spic.SetToolTipString('-')

            else:
                dirs=os.listdir('output\\'+ str(mself.tuser.GetLabel()))
                fsearch=[]
                for dirName in dirs:
                    try:
                        fileNames = os.listdir('output\\' + str(mself.tuser.GetLabel()) +'\\'+ dirName)
                        for file in fileNames:
                            if file.rfind(dlgtext.GetValue()) > -1:
                                fsearch.append('output\\' + str(mself.tuser.GetLabel()) +'\\'+ dirName + '\\' + file)
                    except:
                        pass
                try:
                    w,h = self.spic.GetSize()
                    fileName = fsearch[0]
                    f=open(fileName,'rb')
                    ta=f.read()
                    f.close()
                    ta=ta.replace('[start]' + str(mself.tuser.GetLabel()) + '[end]','')
                    f=open('temp.jpg','wb')
                    f.write(ta)
                    f.close()
                    fileName = 'temp.jpg'
                    pic=wx.Image(fileName)
                    self.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
                    dlgtext.Destroy()
                    self.spic.SetToolTipString('���ͼƬ��ʾ��һ��')
                    fsearch.remove(fsearch[0])
                    return
                except:
                    self.spic.SetToolTipString('-')
        
                    
            dlg=wx.MessageDialog(self,'δ�ҵ���Ӧ�˵���Ϣ','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy
        dlgtext.Destroy()
        
                
        
    def Onsearchdate(self, event):
        dlgtext = wx.TextEntryDialog(self,'����������','�����ڲ�ѯ', str(datetime.date.today()))
        if dlgtext.ShowModal() == wx.ID_OK:
            if mself.tuser.GetLabel()=='-':
                tempdir='output'
            else:
                tempdir='output\\'+ str(mself.tuser.GetLabel())
            dirs=os.listdir(tempdir)
            
            for dirName in dirs:
                if dirName.rfind(str(dlgtext.GetValue())) > -1:
                    fileNames = os.listdir(tempdir+ '\\' + dirName)
                    tn = 0
                    for file in fileNames:
                        tf=file[file.rfind('.'):].lower()
                        if tf=='.jpg' or tf=='.bmp' or tf=='.png' or tf=='.gif':
                            tn=tn+1
                    dlg=wx.MessageDialog(self,'��������'+str(tn)+'���˵���Ϣ','��ʾ',wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()
                    dlgtext.Destroy()
                    return
            dlg=wx.MessageDialog(self,'δ�ҵ���Ӧ������Ϣ','��ʾ',wx.OK)
            dlg.ShowModal()
            dlg.Destroy
        dlgtext.Destroy()

              
    def Onhelp(self, event):
        Dialog2.create(None).Show() 

                
    def Onabout(self, event):
        dlg=wx.MessageDialog(self,'\n   �˵�����ר��\n\n      �汾��v4.57','���� ������ʶ��ϵͳ',wx.OK)
        dlg.ShowModal()
        dlg.Destroy

    def Onreg(self, event):
        global regflag
        
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
        dlgtext = wx.TextEntryDialog(self,'����ʶ����Ϊ��'+ mac +'��������ע����','���ע��', mac) 
        try:
            if dlgtext.ShowModal() == wx.ID_OK:
                    
                conn=httplib.HTTPConnection('www.baidu.com')
                conn.request("GET", "/")
                r=conn.getresponse()
                #r.getheaders() #��ȡ���е�httpͷ
                ts=  r.getheader('date') #��ȡhttpͷdate����
                #print ts
                structtime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
                #print structtime
                numtime=int(time.mktime(structtime))
                #print numtime
            
                code0 = int(dlgtext.GetValue())
                code = int(code0/987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321)
                #startdate=15339 #20120101
                if (int(code/100)*67 - int(code%100)) % 100 == 0:
                    limitdate = int(code//100)-int(mac,16)
                    #nowdate = int(time.time()//86400)
                    nowdate = int(numtime//86400)
                    
                    if limitdate>=nowdate:
                        regflag=1
                        f=file("reg.dat",'w')
                        f.write(str(code0))
                        f.close()
                        dlg=wx.MessageDialog(self,'ע��ɹ�!','���ע��',wx.OK)
                        dlg.ShowModal()
                        dlg.Destroy
                    else:
                        dlg=wx.MessageDialog(self,'ע��ʧ�ܣ�ע�����ѹ���','���ע��',wx.OK)
                        dlg.ShowModal()
                        dlg.Destroy
                        regflag=0
                else:
                    dlg=wx.MessageDialog(self,'ע��ʧ�ܣ�ע�������','���ע��',wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy
                    regflag=0
                
            dlgtext.Destroy() 
        except:
            dlg=wx.MessageDialog(self,'ע��ʧ�ܣ�������Ϣ����\nע��ʱ���������硣','���ע��',wx.OK)
            dlg.ShowModal()
            dlg.Destroy
            regflag=0
            dlgtext.Destroy() 

    def OnSpicLeftDown(self, event):
        global fsearch
        
        if mself.tuser.GetLabel()=='-':
            try:
                w,h = self.spic.GetSize()
                fileName=fsearch[0]
                pic=wx.Image(fileName)
                self.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
                self.spic.SetToolTipString('���ͼƬ��ʾ��һ��')
                fsearch.remove(fsearch[0])
                return
            except:
                self.spic.SetToolTipString('-')

        else:
            try:
                w,h = self.spic.GetSize()
                fileName = fsearch[0]
                f=open(fileName,'rb')
                ta=f.read()
                f.close()
                ta=ta.replace('[start]' + str(mself.tuser.GetLabel()) + '[end]','')
                f=open('temp.jpg','wb')
                f.write(ta)
                f.close()
                fileName = 'temp.jpg'
                pic=wx.Image(fileName)
                self.spic.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
                self.spic.SetToolTipString('���ͼƬ��ʾ��һ��')
                fsearch.remove(fsearch[0])
                return
            except:
                self.spic.SetToolTipString('-')

        event.Skip()


        

        
