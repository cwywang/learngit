#邮件库
from email.header import Header
from email.mime.text import MIMEText
import smtplib

#短信库
import httplib2
from urllib import parse
import json
import http.client
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
class Send_Message():
    def __init__(self,apikey):
        self.apikey=apikey
        self.sms_host = "sms.yunpian.com"
        self.port = 443
        #版本号
        version = "v2"
        #查账户信息的URI
        self.user_get_uri = "/" + version + "/user/get.json"
        #智能匹配模版短信接口的URI
        self.sms_send_uri = "/" + version + "/sms/single_send.json"
        #模板短信接口的URI
        self.sms_tpl_send_uri = "/" + version + "/sms/tpl_single_send.json"
    def tpl_send_sms(self,mobile):
        tpl_id = 2 #对应的模板内容为：您的验证码是#code#【#company#】
        tpl_value = {'#code#':'1688','#company#':'唯旎网'}
        params = parse.urlencode({'apikey':self.apikey, 'tpl_id':tpl_id, 'tpl_value': parse.urlencode(tpl_value), 'mobile':mobile})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPSConnection(self.sms_host, port=self.port, timeout=30)
        conn.request("POST", self.sms_tpl_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str
if __name__=='__main__':
    send=Send_Message("fc320bf08d260174d73a7aa9d6ee3dfb")
    send.tpl_send_sms('15909347775')