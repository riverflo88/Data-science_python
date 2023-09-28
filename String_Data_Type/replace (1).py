sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
#replace all the "!" with " " using the replace function
sentence = sentence.replace("!"," ")
print(sentence)
#create sentence to be in upper case
sentence_upper = sentence.upper()
print(sentence.upper())
#print the string in reverse order
#string are like list of characters
print(sentence_upper[::-1])