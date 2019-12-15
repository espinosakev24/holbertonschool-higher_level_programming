#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb as sql
    from sys import argv

    a1, a2, a3 = argv[1], argv[2], argv[3]
    n = 0
    db = sql.connect(host="localhost", db=a3, user=a1, passwd=a2, port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities"
                " INNER JOIN states ON states.id = cities.state_id"
                " WHERE states.name LIKE BINARY %s"
                " ORDER BY cities.id ASC", (argv[4],))

    result = cur.fetchall()
    it = ''
    for data in result:
        it += data[0] + ', '
    print(it[:-2])
    db.close()
