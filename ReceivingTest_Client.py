import SocketToReceiverTest_Client as Sock
import time
import MySQLdb

db = MySQLdb.connect('localhost','root','1234567890','TestDB')

cursor = db.cursor()
sql = ""

try:
    while True:
        time.sleep(5)
        rowCount = str(Sock.sendingMsg()).split("'")
        print("sended")
        rowCount = int(rowCount[1])

        for i in range(0,rowCount):
            receiving = str(Sock.sendingMsg())
            receiving = receiving[2:-1]
            print(receiving)

            li = receiving.split(" ")
            sql = "UPDATE TestTable SET Location = '%s' WHERE Pin = '%s';" % (li[1],li[0])
            print(sql)
            cursor.execute(sql)

        db.commit()

except:
    db.close()
