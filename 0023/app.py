from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import sqlite3
import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
#初始化数据库
conn=sqlite3.connect('0023/mboard.db')
cursor=conn.cursor()
try:
    cursor.execute('create table message (id integer primary key,name varchar(64),mail varchar(64),word text,time_at datetime)')
except Exception as e:
    print('db has existed.')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/update',methods=['POST'])
def update():
    name=request.form['name']
    mail=request.form['mail']
    word=request.form['word']
    now=datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')

    if (name and mail and word):
        cursor.execute('insert into message (name,mail,word,time_at) values (?, ? ,? ,?)', [name, mail, word, now])
        conn.commit()
        return '提交成功'
    return '不能为空'


@app.route('/view', methods=['GET'])
def view():
    cursor.execute('select count(id) from message')
    num = cursor.fetchall()
    num = int(num[0][0])
    #最大页数
    all_p = num // 5 + 1

    p = int(request.args.get('p'))

    # 显示页数列表(5个)
    lis = ()
    if(all_p >= 5):
        if(p-2 >= 1 and p+2 <= all_p):
            lis = range(p-2, p+3)
        elif(p-2 >= 1 and p+2 > all_p):
            lis = range(all_p-4, all_p+1)
        else:
            lis = range(1, 6)
    else:
        lis = range(1, all_p+1)

    n = cursor.execute('select name,word,time_at from message where id BETWEEN ? and ?', [p*5-4, p*5])
    mess = cursor.fetchall()
    return render_template('view.html', p=p, mess=mess, all_p=all_p, lis=lis)


if __name__ == '__main__':
    app.run()
