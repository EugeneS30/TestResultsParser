'''
Created on 15 May 2015

@author: Polar
'''

import csv
import json
import os

from conf.Conf import Configuration

class Generics(object):
    
    @staticmethod
    def buildPath(*args):
        return os.path.join(*args)
    
    @staticmethod
    def loadJsonData(path):
        with open(path) as json_file:
            return json.load(json_file)
        
    @staticmethod
    def getDirsList():
        buildsDirPath = Configuration.buildsDirPath
        buildsDirListAll = os.listdir(buildsDirPath)
        buildsDirNames = []

        for directory in buildsDirListAll:
            if directory.isdigit():
                buildsDirNames.append(directory)
                
        return buildsDirNames
    
    @staticmethod
    def getCSVReaDer():
        try:
            inputFile = open(os.path.join(FileWriter.path, Configuration.resultsCSV), 'rb') #Open existing CSV file 
        except IOError:
            inputFile = open(os.path.join(FileWriter.path, Configuration.resultsCSV), 'w+') #Open existing CSV file
        finally:
            return csv.reader(inputFile) 
    
    @staticmethod
    def getCSVWriter():
        try:
            tempFile = open(os.path.join(FileWriter.path, Configuration.resultsCSVTemp), 'wb') #Open temp CSV file 
        except IOError:
            tempFile = open(os.path.join(FileWriter.path, Configuration.resultsCSVTemp), 'w+') #Open temp CSV file
        finally:
            return csv.writer(tempFile)