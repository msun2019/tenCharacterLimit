# Author: Michael Sun
# Date: 3/4/16

lineNumber = 0 
f = open("input.txt", "r")
l = open("output.txt", "r+")
input = f.readlines()


	sentence = input[0 + lineNumber]
	cutSentence = sentence[:10]
	cutSentence += "\n"
	l.write(cutSentence)
	lineNumber += 1 