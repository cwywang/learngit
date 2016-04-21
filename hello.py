from flask import Flask,render_template,request,redirect,url_for
from flask.ext.wtf import Form
#from flask.ext.mail import Message,Mail
import re
App=Flask(__name__)

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
@App.route('/樊恩华')
def time():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('mb5_blacksea/time.html')
@App.route('/刘鹏',methods=['GET','POST'])
def Liupeng():
    if request.method == 'POST':
        if request.form['password']=='5201314':
            return redirect(url_for('Liupeng_'))
    return render_template('mb4_login/mb4_login.html',password='password')
@App.route('/刘鹏_',methods=['GET','POST'])
def Liupeng_():
    return render_template('mb2_heart/mb2_heart.html')
@App.route('/鸽子',methods=['GET','POST'])
def Gezi():
    if request.method == 'POST':
        if request.form['password']=='20131006':
            return redirect(url_for('Gezi_'))
    return render_template('mb4_login/mb4_login.html',password='简简单单,平平淡淡')
@App.route('/鸽子_')
def Gezi_():
    return render_template('mb3_tree/mb3_tree.html')
@App.route('/mb1')
def mb1():
    return render_template('mb1_image/mb1_image.html')
if __name__=='__main__':
    App.run()