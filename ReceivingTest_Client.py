import SocketToReceiverTest_Client as Sock
import time
import MySQLdb
import subprocess

subprocess.Popen(["python", "Clock_project4.py"])

db = MySQLdb.connect('localhost','root','1234567890','TestDB')

cursor = db.cursor()
sql = ""

try:
    while True:
        Sock.connection()
        time.sleep(5)
        rowCount = str(Sock.sendingMsg()).split("'")
        rowCount = int(rowCount[1])
        print(rowCount)

        for i in range(0,rowCount):
            receiving = str(Sock.sendingMsg())
            receiving = receiving[2:-1]
            print(receiving)

            li = receiving.split(" ")
            if li[3]=="False":
                sql = "UPDATE TestTable SET Location = 'Moving' WHERE Pin = '%s';" % (li[0])
            else:
                sql = "UPDATE TestTable SET Location = '%s' WHERE Pin = '%s';" % (li[1],li[0]-1)
            print(sql)
            cursor.execute(sql)

        db.commit()

except:
    db.close()
