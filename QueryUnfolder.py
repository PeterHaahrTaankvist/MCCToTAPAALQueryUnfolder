import sys
import optparse
import os
import xml.etree.ElementTree as ET
def createPlaceDictionary(modelFile, unfoldedFile):
    placeDict = {}
    tree = ET.parse(modelFile)
    for child in tree.iter():
        if('place' in child.tag):
            placeDict[child.attrib['id']] = []

    tree = ET.parse(unfoldedFile)
    for child in tree.iter():
        if('place' in child.tag):
            print(child.attrib['id'])
            for key in placeDict:
                if child.attrib['id'].replace('_','').startswith(key.replace('-','')):
                    placeDict[key].append(child.attrib['id'])
    
    print(placeDict)
    
    


def createUnfoldedQueryFile(queryFile, outputfile):
    # Using readlines()
    file1 = open(queryFile, 'r', errors='ignore')
    fileString = file1.read()


    

def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--coloredModel", type="string", dest="modelFile", default="")
    optParser.add_option("--unfoldedModel", type="string", dest="unfoldedFile", default="")

    optParser.add_option("--queryFile", type="string", dest="queryFile", default="")
    optParser.add_option("--outputQuery", type="string", dest="outputfile", default="")

    options, args = optParser.parse_args()
    return options


                  
# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    outputfile = options.outputfile
    """
    if options.inputfile == "":
        print("we require an input file")
        sys.exit()
    if options.outputfile == "":
        print("no output file found.")
        sys.exit()
    if not options.modelFile.endswith(".pnml"):
        print("Model file must be pnml file")
    if not options.queryFile.endswith(".xml"):
        print("Query file must be xml file")
    if not outputfile.endswith(".xml"):
        print("Output file must be xml file")
        sys.exit()
    """
    print(options.modelFile)
    print("im am here: " + os.getcwd())
    createPlaceDictionary(options.modelFile, options.unfoldedFile)
    #cleanFile(options.queryFile,outputfile)
    