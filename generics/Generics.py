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