import pymysql
import csv

conn2 = pymysql.connect(host='localhost', port=3306, user='root', passwd='hondabay', db='genealogy')
cur2 = conn2.cursor()


persons_file = open('../data/persons.csv', 'wb')
persons_file_object = csv.writer(persons_file)

cur2.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'tblpersons'")
result = cur2.fetchall()
field_names = []
i = 0
for r in result:
    field_names.append(r[0])

persons_file_object.writerow(field_names)


cur2.execute("SELECT * FROM tblpersons WHERE pid < 50")
 
for r in cur2.fetchall():

    persons_file_object.writerow(r)

persons_file.close()

cur2.close()
conn2.close()
