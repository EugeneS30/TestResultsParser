'''
Created on 15 May 2015

@author: Eugene Shragovich
'''
#import os

from conf.Conf import Configuration
from functional.parser import Parser
#from FileWriter import FileWriter
from generics.Generics import Generics
from generics.Logger import logging


resultsAllBuilds = {} # {buildNumber, [UniqueScenario, ...]}

#iterate over cucumber reports in their respective locations
for build in Generics.getDirsList():
    
    # !!!
    # Below line must be removed or commeted out before actual run!!!
#     if build != "387":
#         continue
       
    logging.info("========================")
    logging.info("Parsing BUILD: %s", build)
        
    jsonData = Generics.loadJsonData(Generics.buildPath(Configuration.buildsDirPath, build, "htmlreports\Functional_Test_Report", "cucumber.json"))
    logging.info("JSON Data loaded...")
    
    try:
        parsedData = Parser.parse(jsonData) #Returns list of FeatureFile objects
        logging.info("JSON data parsing complete")
    except TypeError:
        logging.error("Could not load the file. Skipping to next build...")
        continue
    
    buildResults = Parser.generateBuildResults(parsedData) #Returns a list of UniqueSceario objects 
    logging.info("Build results generated")
    
    resultsAllBuilds[build] = buildResults #add (build, UniqueScearios list) pair to dictionary


buildNameResultMap = [] # [buildNumber, uniqueName, result]
for build, resultsString in resultsAllBuilds.iteritems():
    for result in resultsString:
        buildNameResultMap.append((build, result.getUniqueName(), result.getResult()))

uniqueScenariosList = list(set(record[1] for record in buildNameResultMap))

finalResultDict = {}
for item in uniqueScenariosList:
    finalResultDict[item] = []
   
for build, results in resultsAllBuilds.iteritems():
    for result in results:
        finalResultDict[result.getUniqueName()].append((build, result.getResult()))

for key, value in finalResultDict.iteritems():
    print key, value
    
#logging.info("Going to write build results to file")
#fileWriter = FileWriter()
   
#fileWriter.init()
#fileWriter.writeBuildResults(buildResults, build)