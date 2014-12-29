def generalCount(strTableName, strFilter=None):  
    ''' returns a tuple with the number found'''
    conn = getConnection()
    cur = conn.cursor()
    if strFilter==None:
        command = 'SELECT Count(*) FROM ' + strTableName
    else:
        command = 'SELECT Count(*) FROM ' + strTableName +  ' WHERE ' + strFilter;
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    intResult = result[0][0]
    return intResult
    
def getChildren(intPID, strGenderAbbr):
    '''Returns a list with the identifiers of all children of the py with PID'''
    conn = getConnection()
    cur = conn.cursor()
    if strGenderAbbr == 'F':
        command = "SELECT PID FROM tblpersons WHERE PIDFK_Mother = " + str(intPID) + ";"
    else:
        command = "SELECT PID FROM tblpersons WHERE PIDFK_Father = " + str(intPID) + ";"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getConfidenceOptions():
    '''returns a tuple containing tuple pairs of numeric code value and text for Confidence'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT ConfidenceCode as Code, Confidence as Text FROM lookupconfidencecode ORDER BY ConfidenceCode;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getConnection():
    import pymysql
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='hondabay', db='genealogy')
    return conn

def getDateQualifierOptions():
    '''returns a tuple containing allowable values for DateQualifier'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT DateQualifier as Text FROM lookupdatequalifier ORDER BY DateQualifier;"
    cur.execute(command)
    result = cur.fetchall()
    options = []
    for c in result:
        options.append(c[0])
    cur.close()
    conn.close()
    return options

def getFactTypeOptions(blnIncludeAll):
    '''returns a tuple containing allowable values for Fact Type'''
    conn = getConnection()
    cur = conn.cursor()
    if blnIncludeAll:
        command = "SELECT Event as Text FROM lu_facttype ORDER BY Event;"
    else:
        command = "SELECT Event as Text FROM lu_facttype WHERE IncludeInAssignmentList = 'Yes' ORDER BY Event;"
    cur.execute(command)
    result = cur.fetchall()
    options = []
    for c in result:
        options.append(c[0])
    cur.close()
    conn.close()
    return options
    
def getGenTableRecord(strTableName,strIdentifierName, intIdentifier):
    '''Returns contents of a single record in the genealogy database as a dictionary'''
    table_info = getGenTableStructure(strTableName)
    field_list = table_info[0]
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT * FROM " + strTableName + " WHERE " + strIdentifierName + " = " + str(intIdentifier) + ";"
    cur.execute(command)
    x = cur.fetchall()
    record_content = {}
    i = 0
    for r in x[0]:
        #print "i = ", i, "r = ", r
        #print "field_list[i] = " , field_list[i], "  r = ", r
        record_content[field_list[i]] = r
        i += 1
    cur.close()
    conn.close()
    return record_content

def getGenTableStructure(strTableName): 
    ''' Takes a Genealogy table name and returns a tuple of FieldNames, 
        FieldTypes, FieldAllowNull, or FieldKey from SHOW COLUMN'''
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SHOW COLUMNS FROM " + strTableName)
    field_names = []
    field_types = []
    field_can_be_null = []
    field_key = []
    for r in cur.fetchall():
        field_names.append(r[0])
        field_types.append(r[1])
        field_can_be_null.append(r[2])
        field_key.append(r[3])
    cur.close()
    conn.close()
    return (field_names, field_types, field_can_be_null, field_key)

def getGraphicDescriptionInfo(intGID):
    '''returns tuple with fields necessary for creating a graphic descriptor'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT Tag, Description, GraphicType, Year FROM tblgraphics WHERE GID = " + str(intGID) + ';'
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
    
def getGraphics(intPID):
    '''Returns a list with the identifiers of all graphics for the identified py'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT GIDFK as GID FROM tbljoingraphicspersons WHERE PIDFK = " + str(intPID) + ";"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
    
def getGraphicTypeOptions():
    '''returns a tuple containing allowable values for Graphic Type'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT GraphicType as Text FROM lookupgraphictype ORDER BY GraphicType;"
    cur.execute(command)
    result = cur.fetchall()
    options = []
    for c in result:
        options.append(c[0])
    cur.close()
    conn.close()
    return options

def getLocationTypeOptions():
    '''returns a tuple containing allowable values for Location'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT TypeCode as Code, Type as Text FROM lookuplocationtype ORDER BY Type;"
    cur.execute(command)
    options = cur.fetchall()
    cur.close()
    conn.close()
    return options

def getMonthOptions():
    '''returns a tuple containing allowable values for DateQualifier'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT Mo as Text FROM lookupmonth ORDER BY MonthNumber;"
    cur.execute(command)
    result = cur.fetchall()
    options = []
    for c in result:
        options.append(c[0])
    cur.close()
    conn.close()
    return options

def getNameInfo(intPID):
    '''returns tuple with fields necessary for creating a formatted name'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT Surname, GivenName, BirthYear, DeathYear FROM tblpersons WHERE PID = " + str(intPID) + ';'
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getNatureOfOriginalOptions():
    '''returns a tuple containing tuple pairs of numeric code value and text for Nature of Original'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT NatureOfOriginalCode as Code, NatureOfOriginalText as Text "
    command = command + "FROM lu_natureoforiginalcodes ORDER BY NatureOfOriginalText;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getPlaceOptions():
    '''returns a tuple containing tuple pairs of numeric code value and text for Places'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT LID as Code, PlaceName as Text FROM tbllocations ORDER BY PlaceName;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getRelationToOriginalOptions():
    '''returns a tuple containing tuple pairs of numeric code value and text for Nature of Original'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT RelationToOriginalCode as Code, RelationToOriginalText as Text "
    command = command + "FROM lu_relationtooriginalcodes ORDER BY RelationToOriginalText;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getSourceCategoryOptions():
    '''returns a tuple containing allowable values for Fact Type'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT source_category_code as Code, source_category as Text "
    command = command + "FROM lu_sourcecategory ORDER BY source_category;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getSourceContentOptions():
    '''returns a tuple containing allowable values for Fact Type'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT source_content_type_code as Code, source_content_type as Text "
    command = command + "FROM lu_sourcecontenttype ORDER BY source_content_type;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getSourceOptions(intWidth=None):
    '''returns a tuple containing tuple pairs of numeric code value and text for Source'''
    conn = getConnection()
    cur = conn.cursor()
    if intWidth == None:
        command = "SELECT SID as Code, SUBSTR(Name,1,255) as Text FROM tblsources ORDER BY Name;"
    else:
        command = "SELECT SID as Code, SUBSTR(Name,1," + str(intWidth) + ") as Text FROM tblsources ORDER BY Name;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getSourceTypeOptions():
    '''returns a tuple containing tuple pairs of numeric code value and text for Source Type'''
    conn = getConnection()
    cur = conn.cursor()
    command = "SELECT source_content_type_code as Code, source_content_type as Text FROM lu_sourcecontenttype ORDER BY source_content_type;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getSpouses(intPID, strGenderAbbr):
    '''Returns a list with the identifiers of all children of the py with PID'''
    conn = getConnection()
    cur = conn.cursor()
    if strGenderAbbr == 'F':
        command = "SELECT PID FROM tblpersons WHERE PIDFK_Mother = " + str(intPID) + ";"
    else:
        command = "SELECT PID FROM tblpersons WHERE PIDFK_Father = " + str(intPID) + ";"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def getTaskOptions(intWidth=None):
    '''returns a tuple containing tuple pairs of numeric code value and text for Task'''
    conn = getConnection()
    cur = conn.cursor()
    if intWidth == None:
        command = "SELECT TID as Code, SUBSTR(TaskName,1,255) as Text FROM tblTasks ORDER BY TaskName;"
    else:
        command = "SELECT TID as Code, SUBSTR(TaskName,1," + str(intWidth) + ") as Text FROM tblTasks ORDER BY TaskName;"
    cur.execute(command)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def putGenTableItem(strTableName,strIdentifierName, intIdentifier, strFieldName, strFieldType, strFieldValue):
    '''Sets any value other than identifier in the genealogy database to specified value'''
    '''Recognized types are string, number and date'''
    if (strIdentifierName == strFieldName):
        pass
    else: 
        conn = getConnection()
        cur = conn.cursor()
        command = "UPDATE " + strTableName
        command = command + " SET " + strFieldName + ' = ' 
        if (strFieldType == 'string'):
            command = command + "'" + strFieldValue + "'"
        elif (strFieldType == 'number'):
            command = command + strFieldValue
        elif (strFieldType == 'date'):
            # not sure how this should be handled
            command = command + "'" + strFieldValue + "'"
        else:
            # default to number
            command = command + strFieldValue
        command = command + " WHERE " + strIdentifierName + " = " + str(intIdentifier) + ";"
        cur.execute(command)
        conn.commit()
        cur.close()
        conn.close()
 
   