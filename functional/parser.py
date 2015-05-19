'''
Created on 15 May 2015

@author: Polar
'''

from containers import FeatureFile
#from generics.Generics import Generics

class Parser(object):
    
    @staticmethod
    def parse(jsonData):
        
        featureFileObjects = []                
                
        ## Create feature file objects
        
        #Iterate over list elements
        for featureFile in jsonData:
                
            featureFileElements = []
            keys = []
            values = []
            
            #Extract feature files as dictionaries
            for key, element in featureFile.iteritems():
                keys.append(key)
                values.append(element)
                featureFileElements.append(element)
                
            #Some feature files don't have "tags". Below code is to add None
            #value in these cases to keep constant number of variables to
            #create a FeatireFileObject 
            l = len(featureFileElements)
            if l != 8:
                featureFileElements.insert(3, None)
            
            #Store feature file as FeatureFile class in featureFileObjects list   
            featureFileObjects.append(FeatureFile(*featureFileElements))

        return featureFileObjects
    
    @staticmethod
    def printParsedData(featureFileObjects):
        for feature in featureFileObjects:
            print feature
            
    @staticmethod
    def generateBuildResults(parsedData):
        uniqueScenarioObjects = []
        buildResultData = []
    
        for featureFile in parsedData: #Iterate over 
            uniqueScenarioObjects.append(featureFile.generateUniqueScenarios())        
        
        for uniqueScenarioList in uniqueScenarioObjects:
            for uniqueScenario in uniqueScenarioList:
                buildResultData.append(uniqueScenario)
                
        return buildResultData