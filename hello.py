from flask import Flask,render_template
from flask.ext.script import Manager
App=Flask(__name__)
manager=Manager(App)
@App.route('/')
def first():
    return render_template('first.html')
@App.route('/凡恩华')
def time():
    return render_template('time.html')
if __name__=='__main__':
    manager.run()