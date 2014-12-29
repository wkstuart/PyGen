import os, sys, datetime
lib_path = os.path.abspath('D:/KestrelDrive/KestrelShare/PythonCode/Genealogy/classes')
sys.path.append(lib_path)

import mySQLFunctions
reload(mySQLFunctions)

import myGenFunctions
reload(myGenFunctions)

class person:
    
    def __init__(self, PID):
        self.result_tuple = mySQLFunctions.getGenTableStructure('tblpersons')
        self.field_names = self.result_tuple[0]
        self.field_types = self.result_tuple[1]
        self.data = mySQLFunctions.getGenTableRecord('tblpersons','PID',PID)
        self.inconsistency_list = self.runConsistencyChecks()
            
    def hasInconsistencies(self):
        if self.inconsistency_list == None:
            return False
        else:
            return True
    def runConsistencyChecks(self):
        self.inconsistency_list = []
        if self.data['Living'] == 'Y' and self.data['DeathYear'] <> None:
            self.inconsistency_list.append('Living is Y and Death Year has value.')

    def ActivityCount(self):
        self.filter = "PIDFK = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tbljoinactivitiespersons',self.filter)
    
    def Characteristic(self, strFieldName):
        return self.data[strFieldName]
    
    def CalculatedAge(self):            
        if self.data['Living'] == 'N' and self.data['DeathYear'] == None:
            return None
        else:
            if self.data['BirthYear'] == None:
                return 'n/a'
            else:
                age = datetime.datetime.now().year - self.data['BirthYear']
                return age
    
    def ChildrenNames(self, strFormatType):
        children_PID_list = mySQLFunctions.getChildren(self.data['PID'],self.data['Gender'][0])
        result = []
        for c in children_PID_list:
            name_info = mySQLFunctions.getNameInfo(c[0])
            result.append(myGenFunctions.getFormattedName(name_info[0], strFormatType))
        return result

    def DocumentCount(self):
        self.filter = "PIDFK = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tbljoindocumentspersons',self.filter)
        
    def FactCount(self):
        self.filter = "PIDFK_Person = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tblfacts',self.filter)
        
    def FormattedName(self, strFormatType):
        ''' types are Lg, Ng, Lgb, '''
        if strFormatType == 'Lgb':
            formatted_name = self.data['Surname'].upper() + ', ' + self.data['GivenName'] + ' (b ' + str(self.data['BirthYear']) + ')'
        elif strFormatType == 'Lg':
            formatted_name = self.data['Surname'].upper() + ', ' + self.data['GivenName']
        elif strFormatType == 'Ng':
            formatted_name = self.data['Surname'] + ', ' + self.data['GivenName']
        return formatted_name
        
    def GraphicsCount(self):
        self.filter = "PIDFK = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tbljoingraphicspersons',self.filter)

    def GraphicsDescriptions(self):
        '''returns a result with tag, description, graphic type and year'''
        graphics_list = mySQLFunctions.getGraphics(self.data['PID'])
        result = []
        for g in graphics_list:
            graphics_info = mySQLFunctions.getGraphicDescriptionInfo(g[0])
            result.append(graphics_info[0])
        return result
    def NoteCount(self):
        self.filter = "PID = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tblnotes',self.filter)
        
    def SpouseCount(self):
        if self.data['Gender'] == 'Male':
            self.filter = "FactType = 'Marriage' AND PIDFK_Person = " + str(self.data['PID'])
        else:
            self.filter = "FactType = 'Marriage' AND PIDFK_Relation = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tblfacts',self.filter)

    def TaskCount(self):
        self.filter = "PIDFK = " + str(self.data['PID'])
        return mySQLFunctions.generalCount('tbljoinpersonstasks',self.filter)

Bill = person(1)
print Bill.Characteristic('Surname')
print Bill.CalculatedAge()
print Bill.FormattedName('Lgb')
print Bill.FormattedName('Lg')
print Bill.FormattedName('Ng')
Jane = person(2)
print Jane.FormattedName('Lgb')
print Jane.CalculatedAge()
print Jane.ChildrenNames('Lgb')
print Jane.hasInconsistencies()
print Jane.SpouseCount()
Charlie = person(62)
print Charlie.SpouseCount()
print Charlie.FactCount()
print Charlie.DocumentCount()
print Charlie.NoteCount()
William = person(44)
print William.ActivityCount()
print William.TaskCount()
print William.DocumentCount()
print William.GraphicsCount()
for d in William.GraphicsDescriptions():
    print d[3], d[1]
    
for c in William.ChildrenNames('Lgb'):
    print c