from flask import Flask
App=Flask(__name__)
@App.route('/')
def index():
    return '<h1>hello world!</h1>'
if __name__=='__main__':
    App.run()