from email.header import Header
from email.mime.text import MIMEText
import smtplib
class Send_Mail():
    def __init__(self,from_addr,password):
        self.from_addr=from_addr
        self.password=password
        self.smtp_server = "smtpdm.aliyun.com"
    def send(self,to_addr):
        msg = MIMEText('访问通知', 'plain', 'utf-8')
        msg['From'] =self.from_addr
        msg['To'] =to_addr
        msg['Subject'] = Header(u'有人访问你的专属天使了.', 'utf-8').encode()
        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [to_addr], msg.as_string())
        server.quit()
if __name__=='__main__':
    mail=Send_Mail('system@email.doforyou.gift','Aa741077081')
    mail.send('741077081@qq.com')