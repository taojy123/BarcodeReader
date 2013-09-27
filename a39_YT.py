# -*- coding: cp936 -*-
from PIL import Image,ImageEnhance
import Frame1

barcode = { '000110100' : '0',
            '100100001' : '1',
            '001100001' : '2',
            '101100000' : '3',
            '000110001' : '4',
            '100110000' : '5',
            '001110000' : '6',
            '000100101' : '7',
            '100100100' : '8',
            '001100100' : '9',
            '010010100' : '',
            }

#bs 95
def getbarcodeYT(im,step,bs):
    w,h=im.size
    for i in range(0,h,step):
         im.putpixel((0,i),255)

    #for i in range(0,h,step):
    scanflag=step
    i=0
    while i<h-step:
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

        #if i==70:
        #    print a
        
        bflag=0
        scanflag=scanflag+1

        
        for k in range(1,len(a)-16,2):
            tlen = a[k]*1.0
            if a[k+1]/tlen>=1.5 and a[k+1]/tlen<=5 and a[k+4]/tlen>=1.5 and a[k+4]/tlen<=5 and a[k+6]/tlen>=1.5 and a[k+6]/tlen<=5:
                if a[k+2]/tlen<1.5 and a[k+3]/tlen<1.5 and a[k+5]/tlen<1.5 and a[k+7]/tlen<1.5 and a[k+8]/tlen<1.5: #start
                    for s in range (k+10,len(a)-6,2):
                        if a[s+1]/tlen>=1.5 and a[s+1]/tlen<=5 and a[s+4]/tlen>=1.5 and a[s+4]/tlen<=5 and a[s+6]/tlen>=1.5 and a[s+6]/tlen<=5: #stop
                            scanflag=0
                            r=a[k:s]

                            if len(r)==110:
                                n=0
                                rs=''
                                for m in r:
                                    if m>=tlen*1.5:
                                        n=n+1
                                        rs=rs+'1'
                                    else:
                                        rs=rs+'0'
                                try:
                                    if n==33:   #11*3
                                        rescode=''
                                        for rsi in range(0,len(rs),10):
                                            rescode=rescode+barcode[rs[rsi:rsi+9]]
                                        return rescode
                                except:
                                    print 'decode error'



