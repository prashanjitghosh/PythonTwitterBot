
class dictionary(dict):
     #constructor
    def __init__(self): 
        self = dict() 
        
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

    def CheckKey(self,key):
        if key in self.keys():
            return self[key]
        else:
            return None
    