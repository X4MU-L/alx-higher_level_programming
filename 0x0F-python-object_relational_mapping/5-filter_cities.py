#!/usr/bin/python3
"""print a tuple of all cities in hbtn_0e_0_usa if any"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3]
                             )
        state_name = argv[4]
    except Exception as e:
        if type(e) == IndexError:
            print(f"USAGE: {argv[0]} user passwd database state_name")
        else:
            print(e)
        exit(1)
    cur = db.cursor()
    cur.execute("SELECT c.name \
                 FROM cities AS c \
                 INNER JOIN states as s \
                 ON s.id = c.state_id \
                 WHERE s.name = (%s) \
                 ORDER BY c.id;", (state_name, ))
    print(", ".join([row[0] for row in cur.fetchall()]))
    db.close()
