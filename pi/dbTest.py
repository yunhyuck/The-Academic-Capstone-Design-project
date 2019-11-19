import dbModule

paramDB = ('localhost', 'root', '1234', 'mysql', 'utf8')

db = dbModule.dbModule(paramDB[0], paramDB[1], paramDB[2], paramDB[3], paramDB[4])

db.dbSelect('*','RFID','')

db.dbInsert('RFID', '010293726')