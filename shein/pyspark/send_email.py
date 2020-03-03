#coding:utf-8
import os 
import sys
import time
import smtplib
from email.mime.text import MIMEText
import unicodedata as ud
import pyarrow.parquet as pq
from inspect import getsourcefile
DIR='./'
path=os.path.join(DIR, 'send_email_data.txt')
#indicator
indicators=open(path,'r').readlines()
send_message=''
sign,length=0,[0]
for line in indicators:
    if '###########' in line:
        send_message+=line
        continue
    lis=line.split('\t')[3:]
    if sign==0:
        length=[len(w) if w not in 'search_word' else len(w)+20 for w in lis ]
        sign=1
    res=[]
    for w,lg in zip(lis,length):
        if '\n' in w:
            res.append(w)
            continue
        if len(w)<lg:
            w+=(lg-len(w))*' '
        elif len(w)>lg:
            w=w[:lg]
        else:
            pass
        res.append(w)
    send_message+='\t'.join(res)
#clear send_email_data.txt
# with open(path,'w') as f:
#     pass
#time
to_time=str(time.strftime("%Y-%m-%d", time.localtime()))
#email configuration
mail_host='smtp.exmail.qq.com'
mail_user='aiapp-search@shein.com'
mail_pass='Aiapp123'
sender='aiapp-search@shein.com'
receivers=['tujialiang@shein.com']#,'xuheng@shein.com','xingzeliang@shein.com','hujianyu@shein.com','wangyajun@shein.com']
receivers=', '.join(receivers)

message=MIMEText(send_message,'plain','utf-8')
message['Subject']=to_time+'shein iosshus en 的搜索词信息统计 '
message['From']=sender
message['To']=receivers
smtpObj=smtplib.SMTP()
smtpObj.connect(mail_host,25)
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender,receivers.split(','),message.as_string())
smtpObj.quit()

