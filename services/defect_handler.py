from services.generator import generate
from services.hook_identifier import checkForHook
import json

class DefectIdentifier:

    @staticmethod
    def identify(infile):
        outFiles = generate(infile=infile)
        #print(json.dumps(outFiles))
        retval = checkForHook(outFiles)
        return retval

