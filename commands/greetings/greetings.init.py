import os
import sys
import os
import imp
api = imp.load_source("api","../../api/ApplicationAPI.py")
apis = api.ApplicationAPI()
print("Hai "+sys.argv[1].replace("'", ""))
