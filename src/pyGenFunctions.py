import pymysql

def getMySQLCursor():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='hondabay', db='genealogy')
    cur = conn.cursor()
    return cur
    
def getGenTableStructure(strTableName): 
    ''' Takes a Genealogy table name and returns a list of field names '''
    cur = getMySQLCursor()
    cur.execute("SHOW COLUMNS FROM " + strTableName)
    field_names = ()
    for r in cur.fetchall():
        #print r
        field_names.append(r[0])
    print field_names
    
    