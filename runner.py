import os, sys
from imutils import paths
from services.defect_handler import DefectIdentifier
import json


folder = sys.argv[1]
files = paths.list_files(folder)

for file in files:
    isHook = DefectIdentifier.identify(file)
    #print(json.dumps(isHook))