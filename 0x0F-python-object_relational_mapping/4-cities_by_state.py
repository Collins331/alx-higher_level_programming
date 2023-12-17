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
    query = """SELECT c.id, c.name, s.name FROM cities AS c
    INNER JOIN states AS s
    ON c.state_id = s.id
    ORDER BY c.id ASC"""
    cursor.execute(query)
    results = cursor.fetchall()

    for city in results:
        print(city)

    cursor.close()
    database.close()
