import socket
import MySQLdb
from geopy.distance import vincenty
import time

HOST=''
PORT=8089
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr=s.accept()
print('Connected by',addr)

db = MySQLdb.connect('localhost','root','0893','traccardb1')
cursor = db.cursor()

while True:
    data=conn.recv(1024)
    if not data:
         break
    print('Client requested by entering ',data)
    
    cursor.execute("select * from positions where deviceid=1 order by devicetime DESC limit 1")
    lastdata = cursor.fetchone()
    usr_pos = (lastdata[7],lastdata[8])

    cursor.execute("select * from locations")
    for i in xrange(cursor.rowcount):
        place,loc_lati,loc_longi,scope = cursor.fetchone()
        loc_pos = (loc_lati,loc_longi)
        distance = vincenty(usr_pos,loc_pos).meters
	if i==0:
	    nearest = (place,distance,distance<scope)
	elif(distance<nearest[1]):
	    nearest = (place,distance,distance<scope)	

    msg = nearest[0]+" "+str(nearest[1])+" "+str(nearest[2])
    conn.send(msg)

conn.close()
db.close()
