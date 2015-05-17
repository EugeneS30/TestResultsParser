'''
Created on 16 May 2015

@author: Polar
'''

class FeatureFile(object):
    
    def __init__(self, elements, name, keyword, tags, uri, line, id, description):
        self.featureFileElementsObjects = []
        self.name = name
        self.keyword = keyword
        self.tags = tags
        self.uri = uri
        self.line = line
        self.id = id
        self.description = description
        
        for element in elements:
            self.featureFileElementsObjects.append(FeatureFileElement(element))

    """
    def getElementsAsObjects(self):
        return self.featureFileElementsObjects
    
    def getElementsAsStrings(self):
        returnList = "" 
        for object in self.featureFileElementsObjects:
            returnList += object.__str__()
            
        return returnList
    """
    def getElementNames(self):
        elementNames = []
        
        for featureFileElementObject in self.featureFileElementsObjects:
            elementNames.append(featureFileElementObject.getName())
            
        return elementNames
    
    def getName(self):
        return self.name

    def getTags(self):
        return self.tags

    def getUri(self):
        return self.uri

    def getLine(self):
        return self.line

    def getDescription(self):
        return self.description
    
    def __str__(self):
        returnString = "FEATURE FILE : " + self.getUri() + "\n" + "Description: " + self.description + "\n"
        
        for featureFileElement in self.featureFileElementsObjects:
            returnString += featureFileElement.__str__() + "\n"
        
        
        return returnString
    
    
class FeatureFileElement(object):
    
    def __init__(self, elements):
        
        self.name = ""
        self.steps = []
        
        for key, value in elements.iteritems():
            if key == "name":
                self.name = value
            if key == "steps":
                for step in value:
                    self.steps.append(Step(step.get("name"), step.get("result")))
                    
    def __str__(self):
        returnString = "Element name: " + self.name + "\n"
        
        for step in self.steps:
            returnString += step.__str__() 
        
        return returnString 
    
    def getName(self):
        return self.name
    
    def getStepsAsObjects(self):
        return self.steps
    
    def getStepsAsString(self):
        str = ""
        for step in self.steps:
            str += step.__str__()
            
        return str + "\n"
    
class Step(object):
    
    def __init__(self, name, result):
        self.name = name
        self.result = result
    
    def getName(self):
        return self.name
    
    def getResult(self):
        return self.result.get("status")
    
    def __str__(self):
        returnString = ""
        returnString += "Step name: " + self.name + " - " + self.result.get("status") + "\n"
        return returnString