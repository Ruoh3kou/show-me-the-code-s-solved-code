import pymysql
import string
import random


def getKeys(nums):
    res = []
    lists = string.ascii_letters + string.digits
    for x in range(nums):
        key = "-".join("".join(random.sample(lists, 4)) for i in range(4))
        res.append(key)
    return res


def saveDB(keys):
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='ruohua3kou',
        db='test'
    )
    cur = db.cursor()

    newTableSql = """create table t(id INT,_keys VARCHAR(30))"""
    try:
        cur.execute(newTableSql)
        db.commit()
    except:
        print("建表失败")
        db.rollback()

    for ID, KEY in enumerate(keys):
        insertSql = "insert into t(id,_keys) VALUES('%d','%s')" % (
            ID + 1, KEY)
        try:
            cur.execute(insertSql)
            db.commit()
        except:
            print("插入失败")
            db.rollback()

    cur.close()
    db.close()


if __name__ == '__main__':
    keys = getKeys(200)
    saveDB(keys)
    print("It saved.")
