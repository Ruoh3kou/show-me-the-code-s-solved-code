import redis
import string
import random


def getKeys(nums):
    res = []
    lists = string.ascii_letters + string.digits
    for x in range(nums):
        key = "-".join("".join(random.sample(lists, 4)) for i in range(4))
        res.append(key)
    return res


def saveRedis(keys):
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)  # 建立连接池
    r = redis.Redis(connection_pool=pool)
    for x, y in enumerate(keys):
        r.set(x + 1, y)
    return 0


if __name__ == '__main__':
    keys = getKeys(200)
    saveRedis(keys)
    print("It saved.")
