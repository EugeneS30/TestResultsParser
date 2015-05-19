'''
Created on 15 May 2015

@author: Eugene Shragovich
'''
import os

from conf.Conf import Configuration
from Parser import Parser
from FileWriter import FileWriter
from generics.Generics import Generics

exit(0)

#iterate over cucumber reports in their respective locations
for build in Generics.getDirsList(): 
    jsonData = Generics.loadJsonData(Generics.buildPath(Configuration.buildsDirPath, build, "cucumber.json"))
    
    parser = Parser()
    parsedData = parser.parse(jsonData) #Returns list of FeatureFile objects 
    
    for featureFileObject in parsedData:
        #FileWriter.writeObject(featureFileObject)
        print featureFileObject.getName()
        print featureFileObject.getElementNames()
