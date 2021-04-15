import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''create table if not exists MyRecivedData(
                        ID INTEGER PRIMARY KEY,
                        data TEXT,
                        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        session INTEGER,
                        FOREIGN KEY(session) REFERENCES Session(id)
                        );''')
        self.cur.execute('''create table if not exists Session(
                        ID INTEGER PRIMARY KEY,
                        location TEXT,
                        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        );''')
        self.conn.commit()

    def fetch_record(self):
        self.cur.execute('select * from MyRecivedData')
        rows = self.cur.fetchall()
        return rows

    def fetch_current_data(self, session):
        self.cur.execute(
            'select * from MyRecivedData where session ='+str(session)+';')
        rows = self.cur.fetchall()
        return rows

    def insert_session(self, location):
        # saving data
        self.cur.execute(
            'insert into Session (location) values(?)', (location,))
        self.conn.commit()

        # getting its id
        self.cur.execute(
            'SELECT id  FROM  Session WHERE   ID = (SELECT MAX(ID)  FROM Session);')
        rows = self.cur.fetchone()[0]
        return rows

    def insert_data(self, data, session):
        # adding data at given session
        self.cur.execute('insert into MyRecivedData (data , session) values(?,?)',
                         (data, session))
        self.conn.commit()

    def __de__(self):
        self.conn.close()


# db = Database('store.sqlite3')
# db.insert_session('firts')
# db.insert_data('xyz77', 6)
# print(db.fetch_record())
# print(db.fetch_current_data(6))


# import sqlite3

# conn = sqlite3.connect('test.sqlite3')
# cursor = conn.cursor()

# # creating data table
# try:

#     command = """CREATE TABLE MyRecivedData(
#         ID INTEGER PRIMARY KEY,
#         data TEXT,
#         Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#         session INTEGER,
#         FOREIGN KEY(session) REFERENCES Session(id)
#         );"""
#     conn.execute(command)

# except:
#     pass

# # creating session table
# try:
#     command = """CREATE TABLE Session(
#     ID INTEGER PRIMARY KEY,
#     location TEXT,
#     Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#     );"""
#     conn.execute(command)
# except:
#     pass


# def AddSession():
#     command = """INSERT INTO Session (location) VALUES ('mumbai'); """
#     conn.execute(command)
#     conn.commit()

#     command = """SELECT id FROM Session ORDER BY id DESC LIMIT 1;"""
#     val = conn.execute(command)
#     print(val)

#     # command = """SELECT id  from Session (location) VALUES ('mumbai');"""
#     # conn.execute(command)
#     # conn.commit()


# AddSession()

# command = """INSERT INTO MyRecivedData (data,session) VALUES ('jsj',9);"""
# conn.execute(command)
# conn.commit()

# conn.close()
