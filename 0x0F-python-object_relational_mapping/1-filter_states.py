#!/usr/bin/python3
"""List all data into DB"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Connection to DB """
    connection = MySQLdb.connect(host="localhost",
                                port=3306,
                                charset="utf8",
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3])
    """ Cursor that exec SQL query """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id ASC")

    """ shows rows of rhe query """
    res_query = cursor.fetchall()

    for i in res_query:
        print(i)

    """ Close connection and close cursor """
    cursor.close()
    connection.close()
