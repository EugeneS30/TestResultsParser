'''
Created on 17 May 2015

@author: Polar
'''
import os
import csv

from conf.Conf import Configuration
from generics.Generics import Generics

class FileWriter(object):
    '''
    classdocs
    '''
    path = Configuration.CSVFilePath
    
    @staticmethod
    def writeObject(featureFileObject):
        """ Write CSV data for one Object.
        
        """
        reader = Generics.getCSVReaDer()
        writer = Generics.getCSVWriter()

        writer.writerow("sd")
         
    
    @staticmethod
    def dumpToCSV(featureFileObject):
        
        for object in featureFileObject:
            print object
            continue
            FileWriter.writeObject(object)
    
    