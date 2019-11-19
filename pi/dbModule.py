import pymysql

class dbModule:
    def __init__(self, host, user, pswd, dbNm, char):
        self.host = host
        self.user = user
        self.pswd = pswd
        self.dbNm = dbNm
        self.char = char

    def dbConnect(self):
        # Set up DB Connection Environment
        conn = pymysql.connect(host = self.host,     # IP
                               user = self.user,     # User ID
                               password = self.pswd, # User Password
                               db = self.dbNm,        # DB Name
                               charset = self.char)  # Encoding Character

        curs = conn.cursor()

        return conn, curs

    def dbClose(self, curs, conn):
        curs.close()
        conn.close()

    def dbSelect(self, cols, tabs, cond):
        try:
            # DB Connect
            conn, curs = self.dbConnect()
            # Write Query: Select Data
            sql = "SELECT %s FROM %s where num = '%s';" % (cols, tabs, cond)
            print(sql)
            # Execute Query
            curs.execute(sql)
            # Fetch
            selectData = curs.fetchall()
            # 'selectData' return
            return selectData
        except:
            print('Error: Select Failed')
        finally:
            # DB Close
            self.dbClose(curs, conn)

    def dbInsert(self, tableNm, value):
        try:
            # DB Connect
            conn, curs = self.dbConnect()
            # Write Query: Select Data / Execute Query
            sql = 'INSERT INTO ' + tableNm
            # Execute Query
            sql += ' VALUES(%s);' 
            curs.execute(sql, (value))
            # Apply Query
            conn.commit()
        except:
            print('Error: Insert Failed')
        finally:
            # DB Close
            self.dbClose(curs, conn)

