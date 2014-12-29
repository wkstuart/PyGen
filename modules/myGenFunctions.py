def getFormattedName(tupInfo, strFormatType=None):
    '''tuple must contain Surname, GivenName, BirthYear, DeathYear
    types are Lg, lg, Lgb, gL, gl'''
    formatted_name = tupInfo[0].upper() + ', ' + tupInfo[1] + ' (b ' + str(tupInfo[2]) + ')'
    if strFormatType == 'None':
        pass
    elif strFormatType == 'Lgb':
        pass
    elif strFormatType == 'Lg':
        formatted_name = tupInfo[0].upper() + ', ' + tupInfo[1]
    elif strFormatType == 'Ng':
        formatted_name = tupInfo[0] + ', ' + tupInfo[1]
    elif strFormatType == 'gl':
        formatted_name = tupInfo[1] + ' ' + tupInfo[0]
    elif strFormatType == 'gL':
        formatted_name = tupInfo[1] + ' ' + tupInfo[0].upper()
    return formatted_name    
 
def booleanToYesNo(blnValue):
    if blnValue:
        return 'Yes'
    else:
        return 'No'