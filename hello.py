from flask import Flask,render_template,request,redirect,url_for
import re
App=Flask(__name__)
@App.route('/')
def first():
    return render_template('hadNone/first.html')
@App.route('/樊恩华_us')
def us():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('Fanenhua/us.html')
@App.route('/樊恩华_readmore')
def about():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('Fanenhua/about.html')
@App.route('/樊恩华')
def time():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('Fanenhua/time.html')
@App.route('/刘鹏',methods=['GET','POST'])
def Liupeng():
    if form.validate_on_submit():
        if form.name.data=='5201314':
            return redirect(url_for('Helang'))
    return render_template('Login/Login.html')
@App.route('/贺浪')
def Helang():
    return render_template('Helang/Helang.html')
if __name__=='__main__':
    App.run()