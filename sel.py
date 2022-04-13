import sqlite3


def sel(teacher):
    conn = sqlite3.connect('timetable_skytat.db')
    cur = conn.cursor()
    res = cur.execute("""SELECT day, time FROM timetable WHERE teacher = ?""", (teacher,))
    return res

