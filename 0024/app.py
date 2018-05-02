from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import sqlite3
import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
#初始化数据库
conn = sqlite3.connect('0024/todolist.db')
cursor = conn.cursor()
try:
    cursor.execute(
        'create table tdlist (id integer primary key,title varchar(64),word text,time_at datetime,done integer)')
except Exception as e:
    print('db has existed.')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
    title = request.form['title']
    word = request.form['word']
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    done=0

    if (title):
        cursor.execute('insert into tdlist (title,word,time_at,done) values (?, ? ,? ,?)', [
                       title, word,now, done])
        # conn.commit()
        return render_template('index.html', judge=1)
    return render_template('index.html', judge=0)



if __name__ == '__main__':
    app.run()
