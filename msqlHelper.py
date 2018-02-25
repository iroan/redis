from mysql import connector

class MysqlHelper():
    def __init__(self,user,password):
        self.conn = connector.connect(user = user,
                                      password = password,
                                      host = '127.0.0.1',
                                      database = 'ex_redis'
                                      )
        cursor = self.conn.cursor()
        try:
            # cursor.execute('create table user(name varchar(20) primary key,password varchar(40))')
            pass
        except Exception as e:
            print(e.args)
        # cursor.execute('insert into table user(name,password) values(%s,%s)',[test,password])
        self.conn.commit()
        cursor.close()
    def __del__(self):
        self.conn.close()

    def __cud(self,sql,params):
        cs1 =self.conn.cursor()
        rows = cs1.execute(sql,params)
        self.conn.commit()
        cs1.close()
        self.conn.close()
        return rows

    def insert(self,sql,params):
        return self.__cud(sql,params)

    def update(self,sql,params):
        return self.__cud(sql,params)

    def delete(self,sql,params):
        return self.__cud(sql,params)

    def fetchone(self,sql,params=[]):
        csl = self.conn.cursor()
        csl.execute(sql,params)
        row = csl.fetchone()
        csl.close()
        self.conn.close()
        return row

    def fetchall(self,sql,params):
        csl = self.conn.cursor()
        csl.execute(sql,params)
        rows = csl.fetchall()
        csl.close()
        self.conn.close()
        return rows

if __name__ == '__main__':
    m = MysqlHelper('root','iroanMYS47')
    import hashlib
    sha1 = hashlib.sha1()
    sha1.update('iroan'.encode())
    pwd = sha1.hexdigest()
    m.insert('insert into user(name,password) values(%s,%s)',['iroan',pwd])
