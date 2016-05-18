import os
def createHtmlTable(listOfWords,width,height):
    rows = 6
    cols = 4
    print "<table border='1' style='width:100%'>"
    for r in range(rows):  
        print "<tr>"
        for c in range(cols):
            word = listOfWords[rows*r+c]
            print "<th><figure><img src='%s.svg' alt='%s' height='%s' width='%s' align=top><figcaption>%s</figcaption></figure></th>" % (word,word,height,width,word)
        print "</tr>"
    print "</table>"

prefix="http://bcserver-1142.appspot.com/redirect/"
words =[ "alligator","ant","bear","bee","bird","camel","cat","cheetah","chicken","chimpanzee","cow","crocodile","deer","dog","dolphin","duck","eagle","elephant","fish","fly","fox","frog","giraffe","goat","goldfish","hamster","hippopotamus","horse","kangaroo","kitten","lion","lobster","monkey","octopus","owl","panda","pig","puppy","rabbit","rat","scorpion","seal","shark","sheep","snail","snake","spider","squirrel","tiger","turtle","wolf","zebra"]

for w in words:
#    os.system("qr --factory=svg-path %s > %s.svg" % (prefix + w,w))
#    print("qr --factory=svg-path %s > %s.svg" % (prefix + w,w))
    pass

print createHtmlTable(words,150,200)
