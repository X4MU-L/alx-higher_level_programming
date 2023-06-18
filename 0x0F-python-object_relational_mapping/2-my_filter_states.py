#!/usr/bin/python3
"""print a tuple of a state passed in the command in hbtn_0e_0_usa if any"""
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
            print(f"USAGE: {argv[0]} user passwd database state")
        else:
            print(e)
        exit(1)
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name='{}' ORDER BY id;".format(
        argv[4]))
    [print(row) for row in cur.fetchall()]
    db.close()
