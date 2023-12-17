#!/usr/bin/python3
"""
import the sys module
imports the MySQLdb used below
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    """
    ensures that the this module cannot be
    called by other modules indirectly
    """
    usr = sys.argv[1]
    psw = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=psw, db=db)

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
