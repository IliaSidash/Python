import sqlite3
import os

PATH = os.path.join(os.path.dirname(__file__), 'dataBase.db')

con = sqlite3.connect(PATH)
if not con:
    print('Error')
else:
    print('Connected to DB')
    cur = con.cursor()

def add_name(data):
    sql = '''INSERT INTO Name (number, name, id_kategory, id_group, id_conformity)
        VALUES(?, ?, ?, ?, ?)'''
    try:
        cur.execute(sql, data[:5])
    except sqlite3.IntegrityError:
        update_name(data)
    finally:
        con.commit()

def update_name(data):
    cur.execute("""SELECT id_name FROM Name WHERE name=?""", (data[1],))
    id_name = cur.fetchone()
    list = []
    for i in data:
        list.append(i)
    list.append(id_name[0])
    var = tuple(list)
    sql = """UPDATE Name SET number=?, name=?, id_kategory=?, id_group=?, id_conformity=?, id_lecturer=?, id_position=?, id_rank=?, date=?, id_rezult=? WHERE id_name=?"""
    cur.execute(sql, var)
    con.commit()

def get_group():
    cur.execute("""SELECT * FROM Groups""")
    return cur.fetchall()

def get_conformity():
    cur.execute("""SELECT conformity FROM Conformity""")
    return cur.fetchall()

def get_kategory():
    cur.execute("""SELECT * FROM kategory""")
    return cur.fetchall()

def get_name():
    cur.execute("""SELECT lecturer_name FROM Lecturer_name""")
    return cur.fetchall()

def get_position():
    cur.execute("""SELECT position FROM Position""")
    return cur.fetchall()

def get_rank():
    cur.execute("""SELECT rank FROM Rank""")
    return cur.fetchall()

def get_rezult():
    cur.execute("""SELECT rezult FROM Rezult""")
    return cur.fetchall()

def get_lecturer_name():
    cur.execute("""SELECT lecturer_name FROM Lecturer_name""")
    return cur.fetchall()

def get_rezult():
    cur.execute("""SELECT rezult FROM Rezult""")
    return cur.fetchall()

def get_id_group(group):
    var = (group,)
    sql = """SELECT id_group FROM Groups WHERE group_groups=(?)"""
    cur.execute(sql, var)
    return cur.fetchone()[0]

def get_id_kategory(kategory):
    var = (kategory,)
    sql = """SELECT id_kategory FROM kategory WHERE kategory=(?)"""
    cur.execute(sql, var)
    return cur.fetchone()[0]

def get_id_conformity(conformity):
    var = (conformity,)
    sql ="""SELECT id_conformity FROM Conformity WHERE conformity=(?)"""
    cur.execute(sql, var)
    return cur.fetchone()[0]

def get_id_lecturer(lecturer):
    var = (lecturer,)
    sql = """SELECT id_lecturer_name FROM Lecturer_name WHERE lecturer_name=(?)"""
    cur.execute(sql, var)
    if len(lecturer) > 0:
        return cur.fetchone()[0]

def get_id_position(position):
    var = (position,)
    sql = """SELECT id_position FROM Position WHERE position=(?)"""
    cur.execute(sql, var)
    if len(position) > 0:
        return cur.fetchone()[0]

def get_id_rank(rank):
    var = (rank,)
    sql = """SELECT id_rank FROM Rank WHERE rank=(?)"""
    cur.execute(sql, var)
    if len(rank) > 0:
        return cur.fetchone()[0]

def get_id_rezult(rezult):
    var = (rezult,)
    sql = """SELECT id_rezult FROM Rezult WHERE rezult=(?)"""
    cur.execute(sql, var)
    if len(rezult) > 0:
        return cur.fetchone()[0]

def view_db():
    sql = """SELECT Name.number, Name.name, Rezult.rezult, Name.date, Groups.group_groups, kategory.kategory, Lecturer_name.lecturer_name
            FROM Name, Groups, kategory, Lecturer_name, Rezult
            WHERE Groups.id_group=Name.id_group AND kategory.id_kategory=Name.id_kategory AND Lecturer_name.id_lecturer_name=Name.id_lecturer AND Rezult.id_rezult=Name.id_rezult"""
    cur.execute(sql)
    return cur.fetchall()

def select_for_edit(name):
    name = (name,)
    sql = """SELECT Name.number, Rezult.rezult, Name.date, Groups.group_groups, kategory.kategory, Lecturer_name.lecturer_name,
            Conformity.conformity, Position.position, Rank.rank
            FROM Name, Groups, kategory, Lecturer_name, Rezult, Conformity, Position, Rank
            WHERE Groups.id_group=Name.id_group AND kategory.id_kategory=Name.id_kategory AND Lecturer_name.id_lecturer_name=Name.id_lecturer AND Rezult.id_rezult=Name.id_rezult
            AND Conformity.id_conformity=Name.id_conformity AND Position.id_position=Name.id_position AND Rank.id_rank=Name.id_rank AND Name.name=?"""
    cur.execute(sql, name)
    return cur.fetchone()

def search(par):
    sql = """SELECT Name.id_name, Name.name, kategory.kategory, Groups.group_groups
        FROM Name, Groups, kategory WHERE Groups.group_groups='1' AND kategory.id_kategory=Name.id_kategory"""
    cur.execute(sql)
    print(cur.fetchall())


def get_errors(sql):
    cur.execute(sql)
    return cur.fetchall()

def view_error(name, sql2, sql3):
    sql = """SELECT Name.id_name FROM Name WHERE Name.name=(?)"""
    var = (name,)
    cur.execute(sql, var)
    id_name = cur.fetchall()
    var = (id_name[0][0],)
    cur.execute(sql2, var)
    data = cur.fetchall()
    list_errors = []
    for i in data:
        cur.execute(sql3, i)
        list_errors.append(cur.fetchall()[0][0])
    return list_errors



def add_commend(sql, sql2, commend, name):
    var = (commend, name)
    cur.execute(sql, var)
    data = cur.fetchall()
    var2 = (data[0][0], data[0][1])
    cur.execute(sql2, var2)
    con.commit()

def del_name(name):
    name = (name,)
    cur.execute("""SELECT id_name FROM Name WHERE name=?""", name)
    id_name = cur.fetchone()
    table_sql = ('commend_zeropart', 'commend_firstpart', 'commend_secondpart', 'commend_thirdpart', 'commend_fourthpart')
    for i in table_sql:
            sql = """DELETE FROM """ + i + """ WHERE id_name=?"""
            cur.execute(sql, id_name)
    cur.execute("""DELETE FROM Name WHERE name=?""", name)
    con.commit()


def del_commend(commend, index):
    table_sql = ('zero_part', 'first_part', 'second_part', 'third_part', 'fourth_part')
    var = (commend,)
    sql = """SELECT id_error FROM """ + table_sql[index] + """ WHERE error=(?)"""
    cur.execute(sql, var)
    id_error = (cur.fetchone()[0],)
    table_sql = ('commend_zeropart', 'commend_firstpart', 'commend_secondpart', 'commend_thirdpart', 'commend_fourthpart')
    sql = """SELECT id FROM """ + table_sql[index] + """ WHERE id_error=(?)"""
    cur.execute(sql, id_error)
    all_id = cur.fetchall()
    var = all_id[(len(all_id)-1)]
    sql = """DELETE FROM """ + table_sql[index] + """ WHERE id=(?)"""
    cur.execute(sql, var)
    con.commit()

def del_commend_firstpart(commend):
    var = (commend,)
    sql = """SELECT id_error FROM first_part WHERE error=(?)"""
    cur.execute(sql, var)
    id_error = (cur.fetchone()[0],)
    sql = """SELECT id FROM commend_firstpart WHERE id_error=(?)"""
    cur.execute(sql, id_error)
    all_id = cur.fetchall()
    var = all_id[(len(all_id)-1)]
    sql = """DELETE FROM commend_firstpart WHERE id=(?)"""
    cur.execute(sql, var)
    con.commit()


def view_dicts(table):
    sql = """SELECT * FROM """ + table
    cur.execute(sql)
    return cur.fetchall()

def add_param_in_dict(table, par, text):
    var = (text,)
    sql = """INSERT INTO """ + table + """ (""" + par +""") VALUES (?)"""
    cur.execute(sql, var)
    con.commit()

def edit_param_in_dict(id_par, par, table, text, new_text):
    var = (text,)
    sql = 'SELECT ' + id_par +' FROM ' + table + ' WHERE '+ par + '=?'
    cur.execute(sql, var)
    var = (new_text, cur.fetchone()[0])
    sql = 'UPDATE ' + table + ' SET ' + par + '=? WHERE ' + id_par + '=?'
    cur.execute(sql, var)
    con.commit()

def disconnect_db():
    cur.close()
    con.close()

