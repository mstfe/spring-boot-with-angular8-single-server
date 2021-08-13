import psycopg2


class DbHelper:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="jQrApplication", user='jQrApplication', password='QrAppAa123!', host='139.162.246.130', port='5432')
        self.conn.autocommit = False

    def cursor(self):
        self.dbCursor = self.conn.cursor()
        return self.dbCursor

    def insert(self, sqlInsert):
        self.dbCursor.execute(sqlInsert)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def count(self,sqlSelect):
        return self.dbCursor.execute(sqlSelect)