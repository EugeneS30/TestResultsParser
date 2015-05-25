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


resultsPerBuild = {}
#iterate over cucumber reports in their respective locations
for build in Generics.getDirsList():
    
    
    # !!!
    # Below line must be removed or commeted out before actual run!!!
    if build != "387":
        continue
       
    logging.info("Parsing BUILD: %s", build)
    logging.info("========================")
    
    jsonData = Generics.loadJsonData(Generics.buildPath(Configuration.buildsDirPath, build, "htmlreports\Functional_Test_Report", "cucumber.json"))
    logging.info("JSON Data loaded...")
    
    parser = Parser()
    parsedData = parser.parse(jsonData) #Returns list of FeatureFile objects
    logging.info("JSON data parsing complete")
    
    buildResults = parser.generateBuildResults(parsedData) #Returns a list of UniqueSceario objects 
    logging.info("Build results generated")
    
    resultsPerBuild[build] = buildResults #add (build, UniqueScearios list) pair to dictionary
        
    #logging.info("Going to write build results to file")
    #fileWriter = FileWriter()
    
    #fileWriter.init()
    #fileWriter.writeBuildResults(buildResults, build)


lst1 = []
for build, resultsString in resultsPerBuild.iteritems():
    for result in resultsString:
        lst1.append((build, result.getUniqueName(), result.getResult()))

allScenarios = []
for record in lst1:
    allScenarios.append(record[1])
    
uniqueList = list(set(allScenarios))

finalDict = {}

for item in uniqueList:
    finalDict[item] = []
   
for build, results in resultsPerBuild.iteritems():
    for result in results:
        
        finalDict[result.getUniqueName()].append((build, result.getResult()))

for key, value in finalDict.iteritems():
    print key, value