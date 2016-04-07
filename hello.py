from flask import Flask,request,render_template,session,redirect,url_for,flash
from flask.ext.bootstrap import Bootstrap #模板渲染
from flask.ext.wtf import Form #表单类
from wtforms import StringField,SubmitField #
from wtforms.validators import Required #表单验证器 的required函数。用来验证 字段中有数据
from flask.ext.sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))#os.path.dirname返回当前的执行目录
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')#os.path.join(a,b)将a,b合成一个规范路径
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='my life'#跨站请求的保护
bootstrap=Bootstrap(app)#Bootstrap模板
db=SQLAlchemy(app)#SQLAlchemy数据库
class NameForm(Form):
    name=StringField('登录名:',validators=[Required()])#validators 验证器
    submit=SubmitField('Submit')
@app.route('/index',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():#如果提交的为空那么，这个为false
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            db.session.add(User(username=form.name.data))
            db.session.commit()
            session['know']=False
        else:
            session['know']=True
        old_name=session.get('name')#先取出留在上次会话的数据
        if old_name!=None and old_name==form.name.data:#如果上次会话有数据，且不与本次会话的数据相等，我们就认为用户没有重复输入
            flash('你重复输入了哦')#flash消息
        session['name']=form.name.data#然后将提交的消息保存到会话中
        return redirect(url_for('index'))
    return render_template('extends.html',name=session.get('name'),form=form,know=session.get('know',False))
class Role(db.Model):
    __tablename__='roles'#为这个表命名
    id=db.Column(db.Integer,primary_key=True)#设定这个表的主键，primary_key缺省为False，表示此列不做主键
    #unique设为True,不允许出现重复值；index为此列建立索引值，提高查找效率；
    #nullable允许出现空值；default为这列设定初始值
    name=db.Column(db.String(64),unique=True)
    #为User表中的role_id作为一个反向引用，返回的好像是一个列表。记录着所有在User中与之关联的行
    #backref向User模型中添加一个role属性,从而定义反向关系
    #lazy='dynamic' 阻止自动查询。这样就能对query对象进行过滤，然后返回更加精确的对象。
    users=db.relationship('User',backref='role',lazy='dynamic')
    def __repr__(self):
        return '<Role %r>'%self.name
class User(db.Model):
    __tablename__='users'#为这个表命名
    id=db.Column(db.Integer,primary_key=True)#设定这个表的主键
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))#ForeignKey将role_id与另一个表相关联，即为这列添加外键
    def __repr__():
        return '<User %r>'% self.username
if __name__=='__main__':
    app.run(debug=True)

