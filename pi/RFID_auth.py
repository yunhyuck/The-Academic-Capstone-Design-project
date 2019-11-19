import socket
import dbModule

paramDB = ('localhost', 'root', '1234', 'mysql', 'utf8')

db = dbModule.dbModule(paramDB[0], paramDB[1], paramDB[2], paramDB[3], paramDB[4])
 
s = socket.socket()         
 
s.bind(('0.0.0.0', 8090 ))
s.listen(2)

con = []
f = ""

while True:
 
    client, addr = s.accept()
    
    while True:
        content = client.recv(32)
        
        if len(content) ==0:
           break
 
        else:
           con = content
           f = int(con[:])
           result = db.dbSelect('*', 'RFID', f)

    print(result)

    msg = '안녕'
    client.send(msg.encode('utf-8'))


    client.close()
