import sys
import optparse
import os
import xml.etree.ElementTree as ET
import re
def createPlaceDictionary(modelFile, unfoldedFile):
    placeDict = {}
    tree = ET.parse(modelFile)
    for child in tree.iter():
        if('place' in child.tag):
            placeDict[child.attrib['id']] = []

    tree = ET.parse(unfoldedFile)
    for child in tree.iter():
        if('place' in child.tag):
            for key in placeDict:
                if child.attrib['id'].replace('_','').replace('-','').startswith(key.replace('-','').replace('_','')):
                    placeDict[key].append(child.attrib['id'])
    return placeDict
    
def addPlacesToIntegerSum(placeList, sumNode):
    for place in placeList:
        tokensCountNode = ET.SubElement(sumNode,"tokens-count")
        placeNode = ET.SubElement(tokensCountNode, "place")
        placeNode.text = place

def constructUnfoldedQuery(placeDict, options):
    tree = ET.parse(options.queryFile)
    for parent in tree.iter():
        toRemove = []
        for child in parent:
            if 'tokens-count' in child.tag:
                #remove this if we run into problems
                if not child[0].text in placeDict:
                    continue
                sumNode = ET.SubElement(parent,"integer-sum")
                addPlacesToIntegerSum(placeDict[child[0].text], sumNode)
                toRemove.append(child)
                
        for child in toRemove:
            parent.remove(child)

    ET.register_namespace('', "http://mcc.lip6.fr/")
    with open(options.outputFile, 'w') as f:
        tree.write(f, encoding='unicode')

    

def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--coloredModel", type="string", dest="modelFile", default="")
    optParser.add_option("--unfoldedModel", type="string", dest="unfoldedFile", default="")

    optParser.add_option("--queryFile", type="string", dest="queryFile", default="")
    optParser.add_option("--outputQuery", type="string", dest="outputFile", default="")

    options, args = optParser.parse_args()
    return options


                  
# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    #outputfile = options.outputfile
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
    placeDict = createPlaceDictionary(options.modelFile, options.unfoldedFile)
    constructUnfoldedQuery(placeDict, options)
    #cleanFile(options.queryFile,outputfile)
    