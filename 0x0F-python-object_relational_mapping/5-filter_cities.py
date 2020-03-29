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
    cursor.execute("SELECT cities.name FROM cities "
                   "INNER JOIN states ON states.id = cities.state_id "
                   "WHERE states.name LIKE BINARY '%{}%' "
                   "ORDER BY cities.id ASC".format(argv[4]))

    """ shows rows of rhe query """
    res_query = cursor.fetchall()
    print(", ".join([i[0] for i in res_query]))

    """ Close connection and close cursor """
    cursor.close()
    connection.close()
