'''
Created on 15 May 2015

@author: Eugene Shragovich
'''
#import os
import sys
from datetime import *

from conf.Conf import Configuration
from functional.parser import Parser
from functional.ExcelWriter import ExcelWriter
from generics.Generics import Generics
from generics.Logger import logging
from __builtin__ import str

builds = []
resultsAllBuilds = {} # {buildNumber, [UniqueScenario, ...]}

#iterate over cucumber reports in their respective locations
for build in Generics.getDirsList():
    logging.info("========================")
    logging.debug("Processing build: %s", build)
    
    if int(build) < Configuration.startBuildNumber:
        logging.debug("Skipping build: %s", build)
        continue
    
    builds.append(build) #Creating a builds list
    
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

wb = ExcelWriter("TestResults")
wb.writeLine("Filename", 0, 0, "heading")
wb.writeLine("Scenario", 0, 1, "heading")

startBuildsFromCol = 2
for build in reversed(builds):
    wb.writeLine(int(build), 0, startBuildsFromCol, "heading")
    startBuildsFromCol += 1

rowToStartFrom = 1
for key, values in finalResultDict.iteritems():
    splitString = key.split(",") #Split the key,value string by ","
    wb.writeLine(splitString[0], rowToStartFrom, 0) # write feature file name
    wb.writeLine(splitString[1], rowToStartFrom, 1) # write scenario name
    
        
    colToStartFrom = 2
    for build in reversed(builds):
        for value in values:
            if value[0] == build:
                wb.writeLine(str(value[1]), rowToStartFrom, colToStartFrom)
                colToStartFrom += 1

    rowToStartFrom += 1
    


    
wb.saveFile()
exit(0)




"""
csvSeparator = ","

sys.stdout.write("Filename")
sys.stdout.write(csvSeparator)
sys.stdout.write("scenario")
sys.stdout.write(csvSeparator)


for build in reversed(builds):
    sys.stdout.write(build)
    sys.stdout.write(csvSeparator)
  
print

for key, values in finalResultDict.iteritems():
    sys.stdout.write(key)
    sys.stdout.write(csvSeparator)
    
    for build in reversed(builds):
        for value in values:
            if value[0] == build:
                sys.stdout.write("" + str(value[1]))
                #print value[1]
        sys.stdout.write(csvSeparator)
    print
"""

#logging.info("Going to write build results to file")
#fileWriter = FileWriter()
   
#fileWriter.init()
#fileWriter.writeBuildResults(buildResults, build)