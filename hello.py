from flask import Flask,render_template
from flask.ext.script import Manager
App=Flask(__name__)
manager=Manager(App)
@App.route('/')
def index():
    return render_template('first.html')
if __name__=='__main__':
    manager.run()