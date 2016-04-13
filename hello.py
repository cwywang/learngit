from flask import Flask,render_template,request
from flask.ext.script import Manager
App=Flask(__name__)
manager=Manager(App)
@App.route('/')
def first():
    return render_template('first.html')
@App.route('/凡恩华')
def time():
	if(request.headers.get('User-Agent') =="Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"):
		return "<h1>hadNone团队正在修复手机端，请登录电脑查看网页！</h1>"
    return render_template('time.html')
if __name__=='__main__':
	manager.run()