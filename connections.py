from pymysql import *
import re
def makeConnections():
    return connect(host='127.0.0.1', user='root', password='',port=3306, database='criminal')


def checkNumber(number):
    number = number
    if re.match(r'[6789]\d{9}$', number):
        return True
    elif re.match(r'(91)?[6789]\d{9}$', number):
        return True
    elif re.match(r'^([0])?[6789]\d{9}$', number):
        return True
    else:
        return False


def checkEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False