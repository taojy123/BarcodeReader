# -*- coding: cp936 -*-
from PIL import Image,ImageEnhance
import Frame1

import subprocess
import time
import os

barcode = { 'bbsbbssbbss' : 0,
            'bbssbbsbbss' : 1,
            'bbssbbssbbs' : 2,
            'bssbssbbsss' : 3,
            'bssbsssbbss' : 4,
            'bsssbssbbss' : 5,
            'bssbbssbsss' : 6,
            'bssbbsssbss' : 7,
            'bsssbbssbss' : 8,
            'bbssbssbsss' : 9,
            'bbssbsssbss' : 10,
            'bbsssbssbss' : 11,
            'bsbbssbbbss' : 12,
            'bssbbsbbbss' : 13,
            'bssbbssbbbs' : 14,
            'bsbbbssbbss' : 15,
            'bssbbbsbbss' : 16,
            'bssbbbssbbs' : 17,
            'bbssbbbssbs' : 18,
            'bbssbsbbbss' : 19,
            'bbssbssbbbs' : 20,
            'bbsbbbssbss' : 21,
            'bbssbbbsbss' : 22,
            'bbbsbbsbbbs' : 23,
            'bbbsbssbbss' : 24,
            'bbbssbsbbss' : 25,
            'bbbssbssbbs' : 26,
            'bbbsbbssbss' : 27,
            'bbbssbbsbss' : 28,
            'bbbssbbssbs' : 29,
            'bbsbbsbbsss' : 30,
            'bbsbbsssbbs' : 31,
            'bbsssbbsbbs' : 32,
            'bsbsssbbsss' : 33,
            'bsssbsbbsss' : 34,
            'bsssbsssbbs' : 35,
            'bsbbsssbsss' : 36,
            'bsssbbsbsss' : 37,
            'bsssbbsssbs' : 38,
            'bbsbsssbsss' : 39,
            'bbsssbsbsss' : 40,
            'bbsssbsssbs' : 41,
            'bsbbsbbbsss' : 42,
            'bsbbsssbbbs' : 43,
            'bsssbbsbbbs' : 44,
            'bsbbbsbbsss' : 45,
            'bsbbbsssbbs' : 46,
            'bsssbbbsbbs' : 47,
            'bbbsbbbsbbs' : 48,
            'bbsbsssbbbs' : 49,
            'bbsssbsbbbs' : 50,
            'bbsbbbsbsss' : 51,
            'bbsbbbsssbs' : 52,
            'bbsbbbsbbbs' : 53,
            'bbbsbsbbsss' : 54,
            'bbbsbsssbbs' : 55,
            'bbbsssbsbbs' : 56,
            'bbbsbbsbsss' : 57,
            'bbbsbbsssbs' : 58,
            'bbbsssbbsbs' : 59,
            'bbbsbbbbsbs' : 60,
            'bbssbssssbs' : 61,
            'bbbbsssbsbs' : 62,
            'bsbssbbssss' : 63,
            'bsbssssbbss' : 64,
            'bssbsbbssss' : 65,
            'bssbssssbbs' : 66,
            'bssssbsbbss' : 67,
            'bssssbssbbs' : 68,
            'bsbbssbssss' : 69,
            'bsbbssssbss' : 70,
            'bssbbsbssss' : 71,
            'bssbbssssbs' : 72,
            'bssssbbsbss' : 73,
            'bssssbbssbs' : 74,
            'bbssssbssbs' : 75,
            'bbssbsbssss' : 76,
            'bbbbsbbbsbs' : 77,
            'bbssssbsbss' : 78,
            'bsssbbbbsbs' : 79,
            'bsbssbbbbss' : 80,
            'bssbsbbbbss' : 81,
            'bssbssbbbbs' : 82,
            'bsbbbbssbss' : 83,
            'bssbbbbsbss' : 84,
            'bssbbbbssbs' : 85,
            'bbbbsbssbss' : 86,
            'bbbbssbsbss' : 87,
            'bbbbssbssbs' : 88,
            'bbsbbsbbbbs' : 89,
            'bbsbbbbsbbs' : 90,
            'bbbbsbbsbbs' : 91,
            'bsbsbbbbsss' : 92,
            'bsbsssbbbbs' : 93,
            'bsssbsbbbbs' : 94,
            'bsbbbbsbsss' : 95,
            'bsbbbbsssbs' : 96,
            'bbbbsbsbsss' : 97,
            'bbbbsbsssbs' : 98,
            'bsbbbsbbbbs' : 99,
            'bsbbbbsbbbs' : 100,
            'bbbsbsbbbbs' : 101,
            'bbbbsbsbbbs' : 102,
            'bbsbssssbss' : 103,
            'bbsbssbssss' : 104,
            'bbsbssbbbss' : 105,
            'bbsssbbbsbsbb' : 106
    }


def getbarcode(im,step,bs):
    w,h=im.size
    import time
    for i in range(0,h/2,step):
        im.putpixel((0,i),255)

    #for i in range(0,h,step):
    scanflag=step
    i=0
    while i<h-step and Frame1.stopflag==0:
        if i > h/3 and h>300:#****************************************
            break
        if scanflag<step:
            i=i+1
        else:
            i=i+step
            
        a=[]
        n=0
        statrflag=0
        for j in range(1,w):
            #print im.getpixel((j,i))
            if im.getpixel((j,i))>=bs and statrflag==0:
                continue
            statrflag=1

            
            n=n+1
            if im.getpixel((j,i))<bs and im.getpixel((j-1,i))>=bs:
                a.append(n) #s
                n=0
            elif im.getpixel((j,i))>=bs and im.getpixel((j-1,i))<bs:
                a.append(n) #b
                n=0
        #print a
        
        bflag=0
        scanflag=scanflag+1
        #if time.time()>1332487178: break
        for k in range(1,len(a)-12,2):
            tlen=(a[k]+1)/2.0 #黑色宽度+1
            tlen=(a[k])/2.0
            if bflag==0 and int((a[k+1]/tlen)+0.5)==1 and int((a[k+2]/tlen)+0.5)==1:
                for s in range (k+7,len(a)-5,2):
                    if bflag==0 and int((a[s]/tlen)+0.5)==3 and int((a[s+1]/tlen)+0.5)==3 and int((a[s+2]/tlen)+0.5)==1 and int((a[s+3]/tlen)+0.5)==1 and int((a[s+4]/tlen)+0.5)==1:
                        scanflag=0
                        b=''
                        bsflag=0
                        for tbs in a[k:s]:
                            bsflag=(bsflag+1)%2
                            #if i== 150 :print int((tbs/tlen)+0.5)

                            bstimes = (tbs+bsflag)/tlen #黑色宽度+1
                            bstimes = (tbs)/tlen
                            if bstimes>0.3 and bstimes<0.5:
                                bstimes=1
                            else:
                                bstimes=int(bstimes+0.5)

                            for temp in range(bstimes):
                                if bsflag==1:
                                    b=b+'b'
                                else:
                                    b=b+'s'
                        #if i ==150:print b,tlen
                        res=[]
                        for z in range(11,len(b)-11,11):
                            tstr = b[z:z+11]
                            #print barcode[tstr]
                            try:
                                res.append(barcode[tstr])
                            except:
                                bflag=1
                                print 'break on:',i
                                break
                        if bflag==0 and len(res)>0:
                            temp=105
                            
                            for ti in range(0,len(res)-1):
                                temp=temp+(ti+1)*res[ti]
                            if temp%103==res[len(res)-1]:
                                print res,i
                                res = ['%02d' % ti for ti in res[:-1]]
                                res2=''
                                for ti in res:
                                    res2=res2+ti
                                return res2
                                
                                #aa=raw_input('ok')
                            else:
                                print 'error data:',res
    #(k)               
    # bb s b ss bbb ss
    # ...
    # ...
    # bb sss bbb s b s bb
    #    (s) 


    """
    #======若无法识别则使用vip插件识别==========
    if bs>30:
        im.save('C:\\ReaderPlugin\\t.jpg')
        time.sleep(0.2)
        try:
            os.remove('C:\\ReaderPlugin\\Result.txt')
        except:
            pass
        process=subprocess.Popen("C:\\ReaderPlugin\\ReaderPlugin.exe C:\\ReaderPlugin\\t.jpg")
        n=0
        while (os.path.isfile('C:\\ReaderPlugin\\Result.txt') == False) or n<10:
            time.sleep(0.5)
            n=n+1
        f=open('C:\\ReaderPlugin\\Result.txt','r')
        res=f.read().replace('\r','').replace('\n','')
        f.close()
        print res
        if res <>'unread':
            return res
    """


'''

im=Image.open(r'C:\Documents and Settings\Administrator\桌面\BR\2.jpg')
#im=ImageEnhance.Brightness(im).enhance(1.2)
im=ImageEnhance.Contrast(im).enhance(5.0)
im=im.convert('L')
#im=ImageEnhance.Sharpness(im).enhance(7.0)
im.save(r'C:\Documents and Settings\Administrator\桌面\BR\5.jpg')

step=10
bs=5

rescode=[]
rescode = getbarcode(im,step,bs)

if rescode == None:
    print 'r90'
    rescode = getbarcode(im.transpose(Image.ROTATE_270),step,bs)
    if rescode == None:
        print 'l90'
        rescode = getbarcode(im.transpose(Image.ROTATE_180),step,bs)
        if rescode == None:
            print 'ud180'
            rescode = getbarcode(im.transpose(Image.ROTATE_90),step,bs)
if rescode <> None:
    print rescode,'ok'

    
aa=raw_input('end')

'''
