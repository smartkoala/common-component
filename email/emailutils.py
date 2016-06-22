#! /usr/bin/python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os


#发送字符串
def send_string(host,username,password,sender,receiver,tilte,content):
    #创建发送对象
    msg = MIMEText(content,'plain','utf-8')
    #定义邮件标题
    msg['Subject'] = Header(tilte,'utf-8')
    server = smtplib.SMTP()
    server.connect(host)
    server.login(username,password)
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()

#发送附件
def send_attachment(host,username,password,sender,receiver,title,file_path):
    #创建发送对象
    msg = MIMEMultipart('related')
    #定义邮件标题
    msg['Subject'] = title
    #构造附件
    att = MIMEText(open(file_path, 'rb').read(),'base64', 'utf-8')  #注：windows路径用\\两个双斜杠
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s' % os.path.basename(file_path)
    #把附件放到发送对象中
    msg.attach(att)
    server = smtplib.SMTP()
    server.connect(host)
    server.login(username,password)
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()


if __name__ == '__main__':
    host = 'smtp.exmail.qq.com'
    username = 'xxx@ganji.com'
    password = 'xxxxxx'
    sender = 'xxx@ganji.com'
    receiver = 'xxxn@ganji.com'
    #receiver = ['xxx@ganji.com','xxx@ganji.com'] #群发邮件
    send_attachment(host,username,password,sender,receiver)
