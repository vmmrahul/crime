from pymysql import *

def makeConnections():
    return connect(host='127.0.0.1', user='root', password='1234',port=3306, database='criminal')


