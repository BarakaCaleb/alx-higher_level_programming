#!/usr/bin/python3
# Displays all the values in the states table of the database
# Whose name matches the supplied argument
# Safe from SQL injection

import sys
import MYSQLdb

if __name__ == "__main__":
    db = MYSQLdb.connec(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECY * FROM `states`")
    [print(state) for state in c.fetchall() if state [1] == sys.argv[4]]
