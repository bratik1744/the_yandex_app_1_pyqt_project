import datetime as dt
import pickle
import classes_tasks
import os
import classes_UI
import sqlite3


def data(year, month, day):
    try:
        d = dt.datetime(year, month, day).date()
    except ValueError:
        d = None
    finally:
        return d


def save(object):
    way = r'current_tasks' + f'\{object.name}.bin'
    with open(way, "wb") as output:
        pickle.dump(object, output, pickle.HIGHEST_PROTOCOL)


def read(name):
    way = r'current_tasks\\'
    with open(way + name, "rb") as inp:
        obj = pickle.load(inp)  # protocol version is auto detected
    return obj


def name_file_list():
    return os.listdir(path=r'current_tasks')


def full_read():
    list_name = name_file_list()
    lst_obj = [read(name) for name in list_name]
    return lst_obj


def information_panel_UI(obj):
    if type(obj) == classes_tasks.PermanentTasks:
        return classes_UI.InformationAboutAPermanentTask(obj)
    elif type(obj) == classes_tasks.OneTimeTasks:
        return classes_UI.InformationAboutAOneTimeTask(obj)
    elif type(obj) == classes_tasks.Homework:
        return classes_UI.HomeworkInformation(obj)
    elif type(obj) == classes_tasks.Ideas:
        return classes_UI.IdeasInformation(obj)
    elif type(obj) == classes_tasks.Rules:
        return classes_UI.InformationAboutTheRules(obj)


def wr_inf(money, exp):
    f = open(r'inf\exp.txt', 'r+')
    ff = open(r'inf\money.txt', 'r+')
    e = f.readline()
    m = ff.readline()
    f.close()
    ff.close()
    f = open(r'inf\exp.txt', 'w')
    ff = open(r'inf\money.txt', 'w')
    f.write(str(int(e) + int(exp)))
    ff.write(str(int(m) + int(money)))
    f.close()
    ff.close()


def read_saving():
    f = open(r'inf\exp.txt', 'r')
    ff = open(r'inf\money.txt', 'r')
    return ff.readline(), f.readline()


def delete(obj):
    os.remove(r'current_tasks\\' + f'{obj.name}.bin')


def read_history():
    con = sqlite3.connect("statistik.db")
    cur = con.cursor()
    lst = list(
        map(lambda x: str(x[0]) + ' ' + x[1] + ' ' + str(x[2]), cur.execute("""SELECT * FROM hist_buy""").fetchall()))
    con.commit()
    cur.close()
    return lst


def write_history(name, price):
    con = sqlite3.connect("statistik.db")
    cur = con.cursor()
    ss = cur.execute("""SELECT * FROM hist_buy""").fetchall()
    ss_2 = cur.execute("""SELECT * FROM stat""").fetchall()
    cur.execute(
        f"INSERT INTO hist_buy('id', 'name', 'price', 'id_stat') VALUES('{len(ss)}', '{name}', '{price}', {len(ss_2) - 1});")
    con.commit()
    cur.close()


def read_sql_statistik():
    con = sqlite3.connect("statistik.db")
    cur = con.cursor()
    vip = cur.execute("""SELECT * FROM stat
            WHERE действие = 'выполнил'""").fetchall()
    prs = cur.execute("""SELECT * FROM stat
            WHERE действие = 'просрочил'""").fetchall()
    nr = cur.execute("""SELECT * FROM stat
            WHERE действие = 'нарушил'""").fetchall()
    con.close()
    return len(vip), len(prs), len(nr)


def write_sql_statistik(name, deyst):
    con = sqlite3.connect("statistik.db")
    cur = con.cursor()
    ss = cur.execute("""SELECT * FROM stat""").fetchall()
    cur.execute(f"INSERT INTO stat('id', 'задача', 'действие') VALUES('{len(ss)}', '{name}', '{deyst}');")
    con.commit()
    cur.close()


def del_sql_statistik():
    try:
        con = sqlite3.connect("statistik.db")
        cur = con.cursor()
        ss = cur.execute("""SELECT * FROM stat""").fetchall()
        cur.execute(f"DELETE FROM stat WHERE id = '{len(ss) - 1}'")
        con.commit()
        cur.close()
    except BaseException:
        pass


if __name__ == "__main__":
    write_history('efwe', 5)
