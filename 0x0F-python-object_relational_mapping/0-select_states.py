#!/usr/bin/python3
"""import sys module and MySQLdb module"""


if __name__ == "__main__":
    """ensures that the module can be only called directly"""
    import sys
    import MySQLdb
    """accepts three inputs"""
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
