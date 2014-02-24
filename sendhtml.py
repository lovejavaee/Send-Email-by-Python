#!/usr/bin/env python
# -*- coding=utf-8 -*-

import string
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "dog_clothes@126.com"

msg = MIMEMultipart('alternatvie')
msg['Subject'] = Header("宠物狗狗衣服",'utf-8')
msg['From'] = r"%s <dog_clothes@126.com>" % Header("宠物狗狗衣服",'utf-8') #使用国际化编码


html = open('html.tpl').read() #读取HTML模板
html_part = MIMEText(html,'html') #实例化为html部分
html_part.set_charset('utf-8')#设置编码
msg.attach(html_part) #绑定到message里

import MySQLdb
conn =   MySQLdb.Connection('127.0.0.1', 'root', '123456', 'mail')
cursor = conn.cursor()


import time

try:
    s = smtplib.SMTP('smtp.126.com') #登录SMTP服务器,发信
    s.login('dog_clothes','3330372')
    
    
    for i in range(421,20000):
        # 執行 SQL 語句
        index="%i" %i
        sql="select * from mail where id="+index
        
        cursor.execute(sql)
        result = cursor.fetchall()       
        msg['To'] = result[0][1]        
        try:
            s.sendmail(sender,result[0][1],msg.as_string())
            print(result[0][1]+"发送成功")
        except Exception,e:
            s.sendmail(sender,result[0][1],msg.as_string())
            print(result[0][1]+"发送成功")            
        time.sleep(10)
        
        
    s.close()
except Exception,e:
    print e
