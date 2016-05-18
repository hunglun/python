# https://docs.python.org/2/library/xml.etree.elementtree.html
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) !=3 :
    print "Display coverage result."
    print "%s xmlFilePath functionName" % sys.argv[0]
    exit(1)
xmlFilePath = sys.argv[1]
functionName = sys.argv[2]

tree = ET.parse(xmlFilePath)
root = tree.getroot()
for m in root.iter('Method'):
    methodName = m.find('MethodName').text
    methodFullName = m.find('MethodFullName').text
    if methodName == functionName:
        lineInfoList = [(int(line.find('LnStart').text), int(line.find('Coverage').text)) for line in m.iter('Lines')] 
        lineCount = int(lineInfoList[-1][0]) - int(lineInfoList[0][0])
        linesCovered =  m.find('LinesCovered').text
        linesPartiallyCovered = m.find('LinesPartiallyCovered').text
        linesUncovered = m.find('LinesNotCovered').text
        print methodFullName
        print lineCount
        print linesCovered
        print linesPartiallyCovered
        print linesCovered 
        print lineInfoList

