'''
Created on 17 May 2015

@author: Polar
'''

class Test(object):
    
    def __init__(self, name, result):
        self.name = name
        self.result = result
    
    def __str__(self):
        returnString = ""
        returnString += "Step name: " + self.name + " - " + self.result.get("status")
        return returnString
    


name = "test1"
results = {"duration": 2323, "status": "passed"}


t = Test(name, results)
print t