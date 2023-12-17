#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    """
    take 3 arguments: mysql username,
    mysql password and database name
    """
    import MySQLdb
    from sys import argv

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
        )
    cursor = database.cursor()
    search = argv[4].split(";")
    query = """SELECT c.name FROM cities AS c
    INNER JOIN states AS s
    ON c.state_id = s.id
    WHERE s.name = '{}'
    ORDER BY c.id ASC""".format(search[0])
    cursor.execute(query)
    results = cursor.fetchall()

    # print("{:s}".format(results))
    x = len(results)
    for city in results:
        for i in city:
            if x != 1:
                print("{:s}".format(i), end=", ")
            else:
                print("{:s}".format(i), end="")
        x -= 1
    print()

    cursor.close()
    database.close()
