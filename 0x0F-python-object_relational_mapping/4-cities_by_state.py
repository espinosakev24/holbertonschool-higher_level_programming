#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb as mysql
    from sys import argv

    a1, a2, a3 = argv[1], argv[2], argv[3]
    db = mysql.connect(host="localhost", db=a3, user=a1, passwd=a2, port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name"
                " FROM cities, states"
                " WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    for data in cur.fetchall():
        print(data)
