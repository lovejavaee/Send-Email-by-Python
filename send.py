#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText

import MySQLdb
conn =   MySQLdb.Connection('127.0.0.1', 'root', '123456', 'mail')
cursor = conn.cursor()
# 執行 SQL 語句
cursor.execute("SELECT * FROM mail")
result = cursor.fetchall()


#要发给谁
mail_to="xiepan1990929@126.com"

def send_mail(to_list,sub,content):
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.126.com"
    mail_user="xiepan1990929"
    mail_pass="3330372"
    mail_postfix="126.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        #print '1'
        return True
    except Exception, e:
        #print '2'
        print str(e)
        return False
if __name__ == '__main__':
    # 輸出結果
    i=0;
    for record in result:        
        if send_mail(record[1],"hello","this is python sent"):
            print "发送成功"
            i=i+1;
            if i>10:
                exit
        else:
            print "发送失败"
