# -*- coding: cp936 -*-
import time
import uuid
import easygui

try:    
    easygui.msgbox("欢迎使用 注册码生成器".decode('gbk'))

    mac=easygui.enterbox('请输入识别码'.decode('gbk'))
    
    name=easygui.enterbox('请输入用户名称'.decode('gbk'))
    
    adddate = int(easygui.enterbox('从今日起使用天数'.decode('gbk')))
    nowdate = time.time()/86400
    limitdate = nowdate + adddate

    srccode=int(mac,16)+int(limitdate)
    checkcode=(srccode*67)%100
    code=str(srccode)+str('%02d' % checkcode)

    code=str(int(code)*987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321)

    easygui.msgbox('注册码为: '.decode('gbk') + code)

    f=file(name + "_reg.dat",'w')
    f.write(str(code))
    f.close()

    easygui.msgbox('已生成生成reg.dat注册文件,可用记事本打开查看其中的注册码'.decode('gbk'))
    
except:
    easygui.msgbox("请正确输入信息".decode('gbk'))
