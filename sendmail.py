#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def send_email(from_addr, to_addr, subject, password):
    msg = MIMEText("开始查成绩了！",'html','utf-8')
    msg['From'] = u'<%s>' % from_addr
    msg['To'] = u'<%s>' % to_addr
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.163.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())

if __name__ == "__main__":
    send_email(u"163邮箱",u"接收邮箱",u"查成绩！",u"163授权码")