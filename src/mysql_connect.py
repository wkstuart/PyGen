#File: mysql_connect
#2014-08-27

import pymysql
import csv


def main():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='hondabay', db='genealogy')
    cur = conn.cursor()
    
    cur.execute("SHOW COLUMNS FROM tblpersons")
    field_names = ()
    for r in cur.fetchall():
        #print r
        field_names.append(r[0])
    print field_names
    
    
    cur.execute("SELECT * FROM tblpersons ")
    
    persons_file = open('../data/persons.csv', 'wb')
    persons_file_object = csv.writer(persons_file)
    persons_file_object.writerow(field_names)
    
    for r in cur.fetchall():
        #print r
        persons_file_object.writerow(r)
    
    persons_file.close()

    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()

