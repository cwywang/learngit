from flask import Flask,render_template
from flask.ext.script import Manager
App=Flask(__name__,static_url_path='')
manager=Manager(App)
@App.route('/')
def first():
    return render_template('first.html')
@App.route('/樊恩华')
def index():
    return render_template('index.html')
if __name__=='__main__':
    manager.run()