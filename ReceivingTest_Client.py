import SocketToReceiverTest_Client as Sock
import time
import MySQLdb

db = MySQLdb.connect('localhost','root','1234567890','TestDB')

cursor = db.cursor()
sql = ""

while True:
    time.sleep(5)
    receiving = Sock.sendingMsg().split("'")
    for i in range(0,len(receiving)):
        if i%2==1:
            li = receiving[i].split(" ")
            sql = "INSERT INTO TestTable (Pin,Location) VALUES("+li[0]+","+li[1]+");"
            print(sql)
            cursor.execute(sql)

db.close()
