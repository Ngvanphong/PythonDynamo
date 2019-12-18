import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

#import libraby left of dynamo to use in python
clr.AddReference('RevitNodes')
import Revit
from Revit.Elements import * # import namspace element in Revit Dynamo
clr.ImportExtensions(Revit.Elements) # use wrap elemnt dynamo with revit (.ToDSType(False))
clr.ImportExtensions(Revit.GeometryConversion) #Convert XYZ double to Point in Revit and Covert dynamo to Revit

#import Revit Api(C#)
clr.AddReference('RevitApi')
from Autodesk.Revit.DB import *

#iImport library to use Transaction update and create elment in revit Api
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from math import *

#Import a module to file python
import sys
sys.path.append(r"C:\Users\Windows 10\Documents\LearnPython")
import lesson5

#The inputs to this node will be stored as a list in the IN variables.
inputValue1 = IN[0]

valueRevit= UnwrapElement(IN[0]) # Get Elment Python use from Dynamo
family = UnwrapElement(IN[1])

lines = IN[0].ToRevitType() # Convert dynamo to revit type of element.

#Create document
doc= DocumentManager.Instance.CurrentDBDocument

#start Transaction Api
TransactionManager.Instance.EnsureInTransaction(doc)

#Do some thing

wrappedCol= columnCreate.ToDSType(False) ; #False if want control Revit from Dynamo, True then not control

#stop Transaction Api
TransactionManager.Instance.TransactionTaskDone()

#Filter Element in RevitApi
collector = FilteredElementCollector(doc,doc.ActiveView.Id) # collecion in revit api
filter= ElementCategoryFilter(BuiltInCategory.OST_Doors) # filter in revit api
doors= collector.WherePasses(filter).ToElements() # where in revit api

#Filter elemnent Instance of Family
instanceFilter= FamilyInstanceFilter(doc,family.Id)
doorInstance= collector.OfCategory(BuiltInCategory.OST_Doors).WherePasses(instanceFilter).ToElements()

#get parameter.
parameters= doorInstance.FirstElement().GetOrderedParameters()
nameParameter=[]
for par in paramters:
	namParameter.append(par.Definition.Name)
	
# assign parameter in python
doorMat= doorInstance.FirstElement().get_Parameter(BuiltInParameter.DOOR_FRAME_MATERIAL)
paraStorageType= doorMat.StorageType()
#Open Transaction before set value parameter
doorMat.Set('Wood')
level = floor.LookupParameter('Level').AsElementId() # get Parameter follow name para
	
xyzPy =XYZ(1,2,0) #Create a Coordinate.
xyzRe= xyzPy.ToPoint(xyzPy) #Auto multi with 304.8

#Libraby python script
docS = sys.builtin_module_names

#Namspace Revit Elements have module
revitElement= Revit.Elements

#How to use funtion
s= sin.__doc__

#Assign your output to the OUT variable.
OUT = doors