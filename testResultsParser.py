'''
Created on 15 May 2015

@author: Eugene Shragovich
'''
import os

from conf.Conf import Configuration
from functional.parser import Parser
from FileWriter import FileWriter
from generics.Generics import Generics
from generics.Logger import logging


#iterate over cucumber reports in their respective locations
for build in Generics.getDirsList():
    #print Generics.buildPath(Configuration.buildsDirPath, build, "htmlreports\Functional_Test_Report", "cucumber.json")
    logging.info("Parsing BUILD: %s", build)
    logging.info("========================")
    
    jsonData = Generics.loadJsonData(Generics.buildPath(Configuration.buildsDirPath, build, "htmlreports\Functional_Test_Report", "cucumber.json"))
    logging.info("JSON Data loaded...")
    
    parser = Parser()
    parsedData = parser.parse(jsonData) #Returns list of FeatureFile objects
    logging.info("JSON data parsing complete")
    
    buildResults = parser.generateBuildResults(parsedData)
    logging.info("Build results generated")
    
    logging.info("Going to write build results to file")
    fileWriter = FileWriter()
    
    fileWriter.init()
    fileWriter.writeBuildResults(buildResults, build)
    
    exit(0)