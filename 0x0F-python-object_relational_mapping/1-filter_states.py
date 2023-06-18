#!/usr/bin/python3
"""print a tuple of all states in hbtn_0e_0_usa if any"""
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
    except Exception as e:
        if type(e) == IndexError:
            print(f"USAGE: {argv[0]} user passwd database")

        print(e)
        exit(1)
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE 'N%' \
    ORDER BY states.id;")
    [print(row) for row in cur.fetchall()]
    db.close()
