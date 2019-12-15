#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb as sql
    import re
    from sys import argv

    a1, a2, a3 = argv[1], argv[2], argv[3]

    db = sql.connect(host="localhost", db=a3, user=a1, passwd=a2, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    for data in cur.fetchall():
        if data[1] == argv[4]:
            print(data)
