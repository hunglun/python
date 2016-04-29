# https://docs.python.org/2/library/xml.etree.elementtree.html

# Usage

# python  c:\Users\ao1\code\python\covMergeAnalysis.py sa_partTask B:\jenkins\workspace\unit_test_coverage\v\LogixTests\Safety\UnitTests\out_saPart.py\cut0\cut0.coverage.xml B:\jenkins\workspace\unit_test_coverage\v\LogixTests\Safety\UnitTests\out_saPart.py\cut1\cut1.coverage.xml 

# python  c:\Users\ao1\code\python\covMergeAnalysis.py sa_partInfoMake B:\jenkins\workspace\unit_test_coverage\v\LogixTests\Safety\UnitTests\out_saPart.py\cut2\cut2.coverage.xml B:\jenkins\workspace\unit_test_coverage\v\LogixTests\Safety\UnitTests\out_saPart.py\cut3\cut3.coverage.xml B:\jenkins\workspace\unit_test_coverage\v\LogixTests\Safety\UnitTests\out_saPart.py\cut4\cut4.coverage.xml B:\jenkins\workspace\unit_test_coverage\v\LogixTests\Safety\UnitTests\out_saPart.py\cut5\cut5.coverage.xml  


import sys
import xml.etree.ElementTree as ET

if len(sys.argv) <4 :
    print "Display coverage result."
    print "%s functionName xmlFilePath1 xmlFilePath2 .. " % sys.argv[0]
    exit(1)
functionName = sys.argv[1]
xmlFilePathList = sys.argv[2:]

def funcCovInfo(xmlFilePath):
    tree = ET.parse(xmlFilePath)
    root = tree.getroot()
    for m in root.iter('Method'):
        methodName = m.find('MethodName').text
        if methodName == functionName:
#            print methodName, m.find('LinesCovered').text, m.find('LinesPartiallyCovered').text,m.find('LinesNotCovered').text            
            lineInfoList = [(line.find('LnStart').text, line.find('Coverage').text) for line in m.iter('Lines')] 
#            print lineInfoList
            lineCount = int(lineInfoList[-1][0]) - int(lineInfoList[0][0])
#            print "Total lines in function", int(lineInfoList[-1][0]) - int(lineInfoList[0][0])
            return (methodName, 
                    lineCount,
                    lineInfoList)
def isEquivalent(covInfoList1, covInfoList2):
    if len(covInfoList1[2]) != len(covInfoList2[2]):
        return False
    lineDiff = abs(int(covInfoList1[2][0][0]) - int(covInfoList1[2][0][0]))
    for i in range(len(covInfoList1[2])):
        if lineDiff != abs(int(covInfoList1[2][i][0]) - int(covInfoList1[2][i][0])):
            return False
    return True
    
if __name__ == "__main__":
    funcCovInfoList = map(funcCovInfo,xmlFilePathList)
# [('sa_partInfoMake', 76, [('250', '0'), ('253', '0'), ('254', '0'), ('255', '0'), ('256', '0'), ('257', '0'), ('258', '0'), ('259', '0'), ('260', '0'), ('261', '0'), ('262', '0'), ('265', '0'), ('267', '0'), ('270', '1'), ('276', '2'), ('278', '2'), ('280', '2'), ('284', '0'), ('285', '0'), ('286', '0'), ('287', '0'), ('288', '0'), ('289', '0'), ('290', '0'), ('291', '0'), ('294', '0'), ('296', '2'), ('300', '2'), ('302', '2'), ('303', '2'), ('305', '2'), ('306', '2'), ('308', '2'), ('309', '2'), ('311', '2'), ('312', '2'), ('314', '2'), ('322', '0'), ('325', '0'), ('326', '0')]), ('sa_partInfoMake', 76, [('252', '0'), ('255', '0'), ('256', '0'), ('257', '0'), ('258', '0'), ('259', '0'), ('260', '0'), ('261', '0'), ('262', '0'), ('263', '0'), ('264', '0'), ('267', '0'), ('269', '0'), ('272', '1'), ('278', '2'), ('280', '2'), ('282', '2'), ('286', '0'), ('287', '0'), ('288', '0'), ('289', '0'), ('290', '0'), ('291', '0'), ('292', '0'), ('293', '0'), ('296', '0'), ('298', '0'), ('302', '0'), ('304', '0'), ('305', '0'), ('307', '0'), ('308', '0'), ('310', '0'), ('311', '0'), ('313', '0'), ('314', '0'), ('316', '1'), ('324', '0'), ('327', '0'), ('328', '0')])]
    maxLineCount = max (map(lambda x: x[1], funcCovInfoList))    
    print maxLineCount
    funcCovInfoListProper = filter(lambda x: x[1] == maxLineCount, funcCovInfoList)
    covInfoWithMostLines = sorted(funcCovInfoList,key = lambda x: x[1])[-1]
    covInfoWithMostLinesEqui = []
    for i in range(len(funcCovInfoListProper)):
        if isEquivalent(covInfoWithMostLines,funcCovInfoListProper[i]):
            covInfoWithMostLinesEqui.append(funcCovInfoListProper[i])

    #for each line, check the corresponding entry in each element of covInfoWithMostLinesEqui.
    print covInfoWithMostLinesEqui
    result = []
    for i in range(len(covInfoWithMostLines[2])):
        coverageInfoListLineI = map(lambda x: x[2][i][1], covInfoWithMostLinesEqui)
        #Coverage=0 means covered; 1 means partially covered, 2 means uncovered
        result.append( any (map (lambda x : x == '0',coverageInfoListLineI)))

    if result :
        print "Complete Code Coverage:", functionName
    else:
        print "Incomplete Code Coverage:", functionName
            
