from flask import Flask,render_template,request
from flask.ext.script import Manager
import re
App=Flask(__name__)
@App.route('/')
def first():
    return render_template('hadNone/first.html')
@App.route('/樊恩华_Readmore')
def about():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('Fanenhua/about.html')
@App.route('/樊恩华')
def time():
    if(re.match(".*iPhone.*",request.headers.get('User-Agent')) or re.match(".*Android.*",request.headers.get('User-Agent'))):
        return "<h1>暂时无法登录凡恩华的个人网站 </br></h1><h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('Fanenhua/time.html')
@App.route('/刘鹏')
def love():
    return render_template('Liupeng/love.htm')
if __name__=='__main__':
	App.run()