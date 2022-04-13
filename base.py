import sqlite3

def base():
    conn = sqlite3.connect('timetable_skytat.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS timetable(
                    id INT,
                    day TEXT,
                    time TEXT,
                    level TEXT,
                    teacher TEXT);""")
    conn.commit()

    more = [('1', 'вторник', '19:00', 'начальный уровень', 'Замира'),
            ('2', 'среда', '19:30', 'средний уровень', 'Расима'),
            ('3', 'среда', '20:00', 'средний уровень', 'Римма'),
            ('4', 'среда', '20:00', 'начальный уровень', 'Ильмир'),
            ('5', 'четверг', '19:00', 'начальный уровень', 'Замира'),
            ('6', 'пятница', '20:00', 'начальный уровень', 'Ильмир'),
            ('7', 'суббота', '10:30', 'средний уровень', 'Расима'),
            ('8', 'воскресенье', '20:00', 'средний уровень', 'Римма')]
    cur.executemany("INSERT INTO timetable VALUES(?, ?, ?, ?, ?);", more)
    conn.commit()

base()