import os, sys
lib_path = os.path.abspath('D:\\KestrelDrive\\KestrelShare\\PythonCode\\Genealogy\\classes')
sys.path.append(lib_path)
lib_path = os.path.abspath('D:\\KestrelDrive\\KestrelShare\\PythonCode\\Genealogy\\modules')
sys.path.append(lib_path)

from mySQLFunctions import *
from myGenFunctions import *
from personClass import *
from TkClasses import *


bill = person(1)
print bill.FormattedName('gL')

tuple_info = []
tuple_info.append(bill.Characteristic('Surname'))
tuple_info.append(bill.Characteristic('GivenName'))
tuple_info.append(bill.Characteristic('BirthYear'))
tuple_info.append(bill.Characteristic('DeathYear'))

tuple_info = tuple(tuple_info)

print type(tuple_info)
print tuple_info
print getFormattedName(tuple_info,'Lg')

