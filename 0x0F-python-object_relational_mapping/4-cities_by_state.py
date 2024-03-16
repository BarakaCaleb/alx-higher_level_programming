#!/usr/bin/python3
# Lists all the cities of the database ordered by city_id

import sys
import MYSQLdb

if __name__ == "__main__":
    db = MYSQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                    ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
