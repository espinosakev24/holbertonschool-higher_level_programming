#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv

    a1, a2, a3 = argv[1], argv[2], argv[3]
    db = sql.connect(host="localhost", db=a3, user=a1, passwd=a2, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    cur.execute(query)
    for data in cur.fetchall():
        if data[1][0] == 'N':
            print(data)

    db.close()
