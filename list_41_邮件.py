# import smtplib
# from email.mime.text import MIMEText

# server = smtplib.SMTP('smtp.163.com', 25)
# server.starttls()
# server.login('ghfuidy@163.com', 'zyq1996110163')

# content = 'Your Message!'
# msg = MIMEText(content)
# msg['From'] = 'ghfuidy@163.com'
# msg['To'] = '821927872@qq.com'
# msg['Subject'] = "Python发送邮件测试"

# server.sendmail('ghfuidy@163.com', '821927872@qq.com', msg.as_string())
# server.quit()
###163邮箱拒绝访问，错误代码“554, b'DT:SPM 163”，垃圾邮件遭到拒绝，推测是缺失发件人，主题，和寄件人等信息，导致被拒绝。修改内容后，发送成功，证明推断正确。


# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

# sender = "ghfuidy@163.com"
# mypass = "zyq1996110163"
# toAddr = "821927872@qq.com"

# body = '''
# <p>Python 邮件发送测试...</p>
# <p><a href="https://www.baidu.com/">百度</a></p>
# <p>图片演示：</p>
# <p><img src="cid:image1"></p>
# '''

# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = toAddr
# msg['Subject'] = "Python发送邮件测试"

# server = smtplib.SMTP_SSL('smtp.163.com',465)
# server.ehlo()
# # server.starttls()
# # ssl连接不能使用starttls函数？？？
# server.login(sender, mypass)

# msg.attach(MIMEText(body, 'HTML', 'utf-8'))
# with open('girl.jpg', 'rb') as fp:
#     img = MIMEImage(fp.read())
#     img.add_header('Content-ID','<image1>')

# msg.attach(img)

# try:
#     server.send_message(msg)
#     print('successfully')
# except server.SMTPException as e:
#     print(e)
#     print('fail')
# finally:
#     server.quit()

###将图片嵌入HTMl页面中可以完美实现，不过qq会提醒是否显示图片
###最后验证一下将图片作为附件的邮件

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# from email.mime.base import MIMEBase

sender = "ghfuidy@163.com"
mypass = "zyq1996110163"
toAddr = "821927872@qq.com"

body = '''
python邮件发送PS信息
ghfuidy@163.com
PSzyq1996110
'''

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = toAddr
msg['Subject'] = "Python发送PS信息"

server = smtplib.SMTP_SSL('smtp.163.com',465)
server.ehlo()
server.login(sender, mypass)

msg.attach(MIMEText(body, 'plain', 'utf-8'))

with open(r'D:\用户目录\我的图片\美莉\156649_201611091239450326371557.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())

img.add_header('Content-Disposition', 'attachment',filename='girl.jpg')
###上面的add_header为附件命名，不然传上去的文件变为（.bin）文件，需要修改后缀名才能正常打开
msg.attach(img)

try:
    server.sendmail(sender, toAddr, msg.as_string())
    print('successfully')
except server.SMTPException as e:
    print(e)
    print('fail')
finally:
    server.quit()