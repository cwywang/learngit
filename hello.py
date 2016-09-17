from flask import Flask,render_template,request,redirect,url_for
from flask.ext.wtf import Form
import re
#from send_mail import Send_Mail
App=Flask(__name__)
#mail=Send_Mail('system@email.doforyou.gift','Aa741077081')
@App.route('/樊恩华_us')
def us():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('mb5_blacksea/us.html')
@App.route('/樊恩华_readmore')
def about():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('mb5_blacksea/about.html')
@App.route('/mb2',methods=['GET','POST'])
def mb2():
    if request.method == 'POST':
        if request.form['password']=='5201314':
            return render_template('mb2_heart/mb2_heart.html')
    return render_template('mb4_login/mb4_login.html',password='password')
@App.route('/mb3',methods=['GET','POST'])
def mb3():
    if request.method == 'POST':
        if request.form['password']=='20131006':
            return render_template('mb3_tree/mb3_tree.html')
    return render_template('mb4_login/mb4_login.html',password='简简单单,平平淡淡')
@App.route('/mb5',methods=['GET','POST'])
def mb5():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    if request.method == 'POST':
        if request.form['password']=='5201314':
            return render_template('mb5_blacksea/time.html')
    return render_template('mb4_login/mb4_login.html',password='password')
@App.route('/mb6')
def mb6():
    return render_template('mb6_liupianyezi/mb6_liupianyezi.html')
@App.route('/mb7')
def mb7():
    return render_template('mb7_heisedexue/mb7_heisedexue.html')
@App.route('/mb8')
def mb8():
    return render_template('mb8_xiaomingxiaohong/mb8_xiaomingxiaohong.html')
@App.route('/mb9')
def mb9():
    return render_template('mb9_woaini/mb9_woaini.html')
@App.route('/mb9_1')
def mb9_1():
    return render_template('mb9_woaini/love.html')
if __name__=='__main__':
    App.run()