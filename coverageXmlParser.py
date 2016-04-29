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
    if methodName == functionName:
        print methodName
        print "Lines covered:", m.find('LinesCovered').text
        print "Lines partially covered",m.find('LinesPartiallyCovered').text
        print "Lines not covered:",m.find('LinesNotCovered').text

