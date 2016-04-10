from flask import Flask
from flask.ext.script import Manager
App=Flask(__name__)
manager=Manager(App)
@App.route('/')
def index():
    return '<h1>hello world!</h1>'
if __name__=='__main__':
    manager.run()