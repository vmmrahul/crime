from pymysql import *

def makeConnections():
    return connect(host='127.0.0.1', user='root', password='',port=3306, database='criminal')


