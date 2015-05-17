'''
Created on 15 May 2015

@author: Polar
'''

import json
from pprint import pprint

from containers import FeatureFile
from generics.generics import Generics

class Parser(object):
    
    def __init__(self, path):
        # "C:\\Users\\Polar\\Google Drive\\374\\cucumber.json"
        
        json_data = Generics.loadJsonData(path)
        
        featureFileObjects = []
        elementKeysExpected = [u'elements', u'name', u'keyword', u'tags', u'uri', u'line', u'id', u'description']
        
        ## Create feature file objects
        
        #Iterate over list elements
        for featureFile in json_data:
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
        
        
        for feature in featureFileObjects:
            print feature
            
        exit()
        
        c = 1
        for feature in featureFileObjects:
            print "Feature file: ", c
            c += 1
            print feature
            print "=============="
                
        exit(0)
            
        c = 0
        for feature in featureFileObjects:
            if feature.getDescription() == "":
                c += 1
                print feature.getElements()
            
            feature.getElements()
            
        print c
        exit(0)
        for featureFile in json_data:
            for element in featureFile['elements']:
                for key, value in element.iteritems():
                    print key
                    print value
                exit(0)
            exit(0)
            
        
        """
        for element in json_data:
            featureFileElements = []
            keys = []
            values = []
        
            for key, value in element.iteritems():
                keys.append(key)
                values.append(value)
                featureFileElements.append(value)
                
            l = len(featureFileElements)
            if l != 8:
                featureFileElements.insert(3, None)
                    
        
            elementObjects.append(FeatureFileObject(*featureFileElements))
        """    
            