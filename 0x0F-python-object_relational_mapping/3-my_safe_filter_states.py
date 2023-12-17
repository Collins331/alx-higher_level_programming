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
    search = argv[4].split(';')

    query = f"SELECT * FROM states  WHERE name = '{search[0]}'\
            ORDER BY states.id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    dtb.close()
