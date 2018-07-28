###引入邮件内容的模板
from string import Template
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

message_template = read_template('123.txt')

import smtplib
from email.mime.text import MIMEText 
###模板中的关键点个人化修改
message = message_template.safe_substitute(PERSON_NAME='皮皮怪')
# print(message)习惯不好，用logging
mailto_list = ["821927872@qq.com", "3193642572@qq.com"]
mail_host = "smtp.163.com"
mail_port = 465
mail_user = 'ghfuidy@163.com'
mail_pass = 'zyq1996110163'

###----------------发送邮件
def send_mail(to_list, sub, content):
###to_list:接收人。sub：标题。content：内容。
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['to'] = ";".join(to_list)
    # print(msg['to'])有两个账号，账号之间以分号隔开，会自动群发
###列表分割的亮点，常用的还有split分割和strip格式规范化

    try:
        s= smtplib.SMTP_SSL(mail_host,mail_port)
        s.login(mail_user,mail_pass)
        s.send_message(msg)
        s.close
        return True
    except Exception as e:
        print(e)
        return False

if send_mail(mailto_list,"群发邮件定制邮件", message):
    print("发送成功")
else:
    print("发送失败")

###还缺少一个读取对象联系人文件的函数，暂时先空着吧，以后根据具体的情况再说