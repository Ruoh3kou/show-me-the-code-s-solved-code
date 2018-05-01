import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(pwd,salt=None):
    if salt is None:
        salt=os.urandom(8)
    if isinstance(pwd,str):
        pwd=pwd.encode('UTF-8')
    result=pwd
    for i  in range(10):
        result=HMAC(result,salt,sha256).digest()
    return result

if __name__ == '__main__':
    encrypt_password('ruohua3kou')