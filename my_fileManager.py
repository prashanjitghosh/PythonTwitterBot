
def GetConfigurationValue(File_name,configuration):
     l_config = open(File_name,"r")
     ReadLines = l_config.readlines()
     for line in ReadLines:
         configpair = [ ]
         configpair = (line.strip()).split(':')
         if (configpair[0].lower()) == (str(configuration).lower()):
             l_config.close()
             return configpair[1]
     l_config.close()
     return None 

def GetConfigurationValueList(File_name,configuration):
     l_config = open(File_name,"r")
     ReadLines = l_config.readlines()
     for line in ReadLines:
         configpair = [ ]
         configpair = (line.strip()).split(':')
         if (configpair[0].lower()) == (str(configuration).lower()):
              l_config.close()
              return configpair[1:]

def GetLastProcessedId(File_name):
     l_readFile  = open(File_name,"r")
     l_lastProcessedid  = int((l_readFile.read().strip() ) )
     l_readFile.close()
     return l_lastProcessedid

def UpdateLastProcessedId(File_name,l_lastProcessedid):
      l_writeFile  = open(File_name,"w")
      l_writeFile.write(str(l_lastProcessedid))
      l_writeFile.close()
 

