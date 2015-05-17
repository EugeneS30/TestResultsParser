'''
Created on 15 May 2015

@author: Polar
'''
import os

from generics.Generics import Generics
from conf.Conf import Configuration
from functional.Parser import Parser
from functional.FileWriter import FileWriter

#iterate over cucumber reports in their respective locations
for build in Generics.getDirsList(): 
    jsonData = Generics.loadJsonData(Generics.buildPath(Configuration.buildsDirPath, build, "cucumber.json"))
    
    parser = Parser()
    parsedData = parser.parse(jsonData) #Returns list of FeatureFile objects 
    
    for featureFileObject in parsedData:
        FileWriter.writeObject(featureFileObject)