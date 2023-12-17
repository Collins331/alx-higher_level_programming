#!/usr/bin/python3

"""import sys module and MySQLdb module"""

if __name__ == "__main__":
    """
    take 3 arguments: mysql username, mysql password and database name
    """
    import MySQLdb
    import sys

    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    dtb = MySQLdb.connect(host="localhost", user=user, password=pswd,
                          port=3306, database=db)

    cursor = dtb.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    dtb.close()
