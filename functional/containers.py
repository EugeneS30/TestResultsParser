'''
Created on 16 May 2015

@author: Polar
'''

class FeatureFile(object):
    
    def __init__(self, elements, name, keyword, tags, uri, line, ID, description):
        self.featureFileElementsObjects = [] #List of Scenarios in single .feature file
        self.name = name
        self.keyword = keyword
        self.tags = tags
        self.uri = uri
        self.line = line
        self.ID = ID
        self.description = description
        
        
        for element in elements:
            self.featureFileElementsObjects.append(FeatureFileElement(element))

    def getElementNames(self):
        elementNames = []
        
        for featureFileElementObject in self.featureFileElementsObjects:
            elementNames.append(featureFileElementObject.getName())
            
        return elementNames
    
    def getElementsReferences(self):
        elementReferences = []
        
        for featureFileElementObject in self.featureFileElementsObjects:
            elementReferences.append(featureFileElementObject)
            
        return elementReferences
    
    def generateUniqueScenarios(self):
        uniqueScenariosList = []
        
        for featureFileElementsObject in self.featureFileElementsObjects:
            if featureFileElementsObject.getType() == "background":
                continue
            uniqueScenariosList.append(UniqueScenario(self.uri, featureFileElementsObject.getName(), featureFileElementsObject.getType(), featureFileElementsObject.failedStepsExist()))
            
        return uniqueScenariosList
    
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
        self.type = ""
        self.steps = []
        
        for key, value in elements.iteritems():
            if key == "name":
                self.name = value
            if key == "type":
                self.type = value
            if key == "steps":
                for step in value:
                    self.steps.append(Step(step.get("name"), step.get("result")))
                    
    def __str__(self):
        returnString = "Element name: " + self.name + " " + self.type + "\n"
        
        for step in self.steps:
            returnString += step.__str__() 
        
        return returnString
    
    def failedStepsExist(self):
        """ Returns scenario result
        
        Iterates over scenario steps and checks results of each step
        If "skipped" comes as a first step, the whole scenario will be marked as N/A
        In other cases, the scenario will be marked:
        "True"  - for passed
        "False" - for failed  
        """ 
        for step in self.steps:
            result = step.getResult()
            if result == "skipped":
                return "N/A"
            if result == "failed":
                return False

        return True
        
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getStepsAsObjects(self):
        return self.steps
    
    def getStepsAsString(self):
        returnString = ""
        for step in self.steps:
            returnString += step.__str__()
            
        return returnString + "\n"
    

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
    

class UniqueScenario(object):
    
    def __init__(self, uri, elementName, elementType, result):
        self.uri = uri
        self.elementName = elementName
        self.elementType = elementType
        self.result = result
        self.uniqueName = self.getURI() + "," + self.getName()# + "," + self.getType()
        
    def getURI(self):
        return self.uri
    
    def getResult(self):
        return self.result
    
    def getName(self):
        return self.elementName
    
    def getType(self):
        return self.elementType
    
    def getUniqueName(self):
        return self.uniqueName
        
    def __str__(self):
        return str(self.uri) + "," + str(self.elementName) + "," + str(self.getType) + "," + str(self.result)