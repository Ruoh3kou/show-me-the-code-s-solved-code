import string
import random


def getKeys(nums):
    res = []
    lists = string.ascii_letters + string.digits
    for x in range(nums):
        key = "-".join("".join(random.sample(lists, 4)) for i in range(4))
        res.append(key)
    return res


if __name__ == '__main__':
    keys = getKeys(200)
    print(keys)
