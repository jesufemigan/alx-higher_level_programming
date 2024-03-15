#!/usr/bin/python3

'''lists all cities in database'''

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT c.id, c.name, s.name
                 FROM cities c INNER JOIN states s
                 ON c.state_id = s.id
                 ORDER BY c.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
