#!/usr/bin/python3
"""takes in arguments and displays all values in the states table """

if __name__ == "__main__":
    """
    ake 4 arguments: mysql username, mysql password, database name
    and state name searched
    """
    from sys import argv
    import MySQLdb

    dtb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cursor = dtb.cursor()

    query = """SELECT * FROM states  WHERE name = '{}'
            ORDER BY states.id ASC""".format(argv[4])
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    dtb.close()
