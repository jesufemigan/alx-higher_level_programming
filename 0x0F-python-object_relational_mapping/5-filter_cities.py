#!/usr/bin/python3

'''lists all in cities'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name
                FROM cities c INNER JOIN states s
                ON s.id = c.state_id
                WHERE s.name = %s
                ORDER BY c.id""", [sys.argv[4]])

    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
