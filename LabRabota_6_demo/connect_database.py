import sqlite3, random, root_dir


def connect():
    con = sqlite3.connect(root_dir.db)
    cur = con.cursor()
    return cur

def initial_data():
    r = []
    while len(r) <= 4:
        a = random.randint(0, 4)
        if a not in r:
            r.append(a)
    return r

def select():
    cur = connect()
    cur.execute('SELECT * FROM sound')
    db = cur.fetchall()
    r = initial_data()
    dict = {}
    for i in r:
        dial_1 = db[i][0]
        dial_2 = db[i][1]
        rang = db[i][2]
        raion = db[i][3]
        podraion = db[i][4]
        street = db[i][5]
        home = db[i][6]
        dict[i] = (dial_1, dial_2, rang, raion, podraion, street, home)
    cur.close()
    return dict

def ppr(street, home):
    cur = connect()
    sql = 'SELECT rang, raion, podraion FROM sound WHERE street=(?) AND home=(?)'
    v = (street, home,)
    cur.execute(sql, v)
    db = cur.fetchone()
    cur.close()
    return db

def select_street():
    cur = connect()
    sql = 'SELECT street FROM sound'
    cur.execute(sql)
    db = cur.fetchall()
    arr = []
    for i in db:
        arr.append(i[0])
    cur.close()
    return arr

