#!/usr/bin/python3
# Displays all the values in the state table of the database
# Whose name matches that supplied as argument
# Usage: ./2-my_filter_states.py <mysql username>\
#                                 <mysql password>\
#                                 <database name>\
#                                 <state name searched>

import sys 
import MYSQLdb

if __name__ == "__main__":
    db = MYSQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
