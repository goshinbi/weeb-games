
#!/usr/bin/Python3





import sqlite3

import os.path

from urllib.parse import urlparse

import time





def get_user(name):

    conn = sqlite3.connect('weebpoints.db')

    c = conn.cursor()

    # make sure the user exists

    c.execute("INSERT OR IGNORE INTO USERS (name, points) VALUES (?, ?)", (name, 0, ))

    conn.commit()

    c.execute('SELECT * FROM USERS WHERE name = (?) LIMIT 1', (name, ))

    user = c.fetchall()[0]

    uid = user[0]

    upoints = user[2]

    c.execute('SELECT * FROM STRINGS WHERE uid = (?)', (uid, ))

    strings = c.fetchall()

    conn.close()

    return (uid, upoints, sorted(strings, key=lambda string: string[4], reverse=True), )





def get_top(x):

    conn = sqlite3.connect('weebpoints.db')

    c = conn.cursor()

    c.execute('SELECT * FROM USERS')

    results = c.fetchall()

    return sorted(results, key=lambda res: res[2], reverse=True)[:x]

    conn.close()





def add_string(name, text, points, stime):

    start = time.time()

    conn = sqlite3.connect('weebpoints.db')

    c = conn.cursor()

    # get the user

    c.execute('SELECT * FROM USERS WHERE name = (?) LIMIT 1', (name, ))

    user = c.fetchall()[0]

    upoints = user[2]

    uid = user[0]

    # add the string

    c.execute('INSERT OR IGNORE INTO STRINGS (uid, text, points, time) VALUES (?, ?, ?, ?)', (uid, text, points, stime, ))

    # update the users points

    c.execute('UPDATE USERS SET points = (?) WHERE id = (?)', (int(upoints) + int(points), uid, ))

    conn.commit()

    conn.close()
