'''
Created on 17 May 2015

@author: Eugene Shragovich
'''
import os
import csv

from conf.Conf import Configuration
from generics.Generics import Generics
from generics.Logger import logging

class FileWriter(object):
    
    def __init__(self):
        
        self.reader = self._getCSVReaDer()
        self.writer = self._getCSVWriter()
        self.path = Configuration.CSVFilePath
    
    def _getCSVReaDer(self):
        try:
            logging.debug("Trying to open existing results CSV file...")
            inputFile = open(os.path.join(self.path, Configuration.resultsCSV), 'rb') #If file exists Open existing CSV file for reading only
        except IOError:
            logging.debug("CSV file does not exist in defined pathL %s", self.path)
            logging.debug("Creating new CSV file...")
            inputFile = open(os.path.join(self.path, Configuration.resultsCSV), 'w+') #If file does not exist! Open file for reading and writing 
        finally:
            return csv.reader(inputFile) 
    
    def _getCSVWriter(self):
        tempFile = open(os.path.join(self.path, Configuration.resultsCSVTemp), 'wb') #Open temp CSV file for writing. Overwrites if already existed    
        return csv.writer(tempFile)
    
    def init(self):
        """ Initi
        """
        pass
    
    def finalize(self):
        raise NotImplementedError("This method has not yet been implemented")
    
    def writeBuildResults(self, buildResults, buildNumber):
        
        for item in buildResults:
            self.writer(str(item )+ "\n")
            #fd.write(str(item )+ "\n")
        #fd.close()
    
    
    def writeObject(self, featureFileObject):
        """ Write CSV data for one Object.
        
        """
        self.writer.writerow("sd")
         
    
    @staticmethod
    def dumpToCSV(featureFileObject):
        
        for object in featureFileObject:
            print object
            continue
            FileWriter.writeObject(object)
            

    
    