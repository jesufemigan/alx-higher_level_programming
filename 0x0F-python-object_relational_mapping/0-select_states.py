#!/usr/bin/python3
'''lists all states from the database'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id')
    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")
    cur.close()
    db.close()
