# -*- coding: cp936 -*-
import time
import uuid
import easygui

try:    
    easygui.msgbox("��ӭʹ�� ע����������".decode('gbk'))

    mac=easygui.enterbox('������ʶ����'.decode('gbk'))
    
    name=easygui.enterbox('�������û�����'.decode('gbk'))
    
    adddate = int(easygui.enterbox('�ӽ�����ʹ������'.decode('gbk')))
    nowdate = time.time()/86400
    limitdate = nowdate + adddate

    srccode=int(mac,16)+int(limitdate)
    checkcode=(srccode*67)%100
    code=str(srccode)+str('%02d' % checkcode)

    code=str(int(code)*987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321)

    easygui.msgbox('ע����Ϊ: '.decode('gbk') + code)

    f=file(name + "_reg.dat",'w')
    f.write(str(code))
    f.close()

    easygui.msgbox('����������reg.datע���ļ�,���ü��±��򿪲鿴���е�ע����'.decode('gbk'))
    
except:
    easygui.msgbox("����ȷ������Ϣ".decode('gbk'))
