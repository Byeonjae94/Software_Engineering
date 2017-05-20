import socket
import time
#from apscheduler.schedulers.background import BackgroundScheduler

HOST = "52.78.114.210"
PORT = 8089
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#sched = BackgroundScheduler()
	
def sendingMsg():
    request = bytes('Request','utf-8')
    s.send(request)
    data = s.recv(1024)
    return data

def disconnectingSoc():
    s.close()
#while True:
#    time.sleep(5)
#    sendingMsg()

#sched.add_job(sendingMsg, 'interval', seconds=5)
#sched.start()
