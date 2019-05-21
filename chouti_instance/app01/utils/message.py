import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(email_list, content, subject="抽屉新热榜-用户注册"):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["抽屉新热榜",'wptawy@126.com'])
    msg['Subject'] = subject
    # SMTP服务
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login("825644691@qq.com", "ywpiwtukjsvjbejh")
    server.sendmail('825644691@qq.com', email_list, msg.as_string())
    server.quit()



