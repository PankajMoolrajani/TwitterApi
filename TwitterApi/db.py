import MySQLdb

class DB:
    def connect(self):
        hostname = '198.199.107.31'
        dbname = 'twitter_follow'
        username = 'root'
        password = 'groove'

        connection = MySQLdb.connect(hostname, username, password, dbname)
        return connection


    def getCursor(self):
        db = DB()
        con = db.connect()
        cursor = con.cursor()
        return con, cursor

    def closeCursor(self, con, cursor):
        con.commit()
        id_row = str(cursor.lastrowid)
        cursor.close()
        return id_row


    def queryInsert(self, table, columns, values):
        query = "INSERT INTO "+table+"("+columns+") VALUES("+values+")"
        print query
        try:
            con, cursor = self.getCursor()
            cursor.execute(query)
            id_row = self.closeCursor(con, cursor)
        except:
            id_row = "0"

        return id_row


    def queryUpdate(self, table, column, value, condition):
        query = "UPDATE "+table+" SET "+column+" = "+value+" WHERE "+condition
        print query
        try:
            con, cursor = self.getCursor()
            cursor.execute(query)
            id_row = self.closeCursor(con, cursor)
        except:
            id_row = "0"

        return id_row


    def querySelect(self, table, columns, condition):
        query = "SELECT "+columns+" FROM "+table+" "+condition
        print query
        list_rows = []
        try:
            con, cursor = self.getCursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                list_rows.append(row)
            id_row = self.closeCursor(con, cursor)
        except:
            id_row = "0"
        return id_row, list_rows

if __name__ == "__main__":
    ob = DB()
    print ob.querySelect("profiles_groove", "*")[1]
