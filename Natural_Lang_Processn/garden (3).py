import spacy

garden_path_sentences = [
    "Mary gave the child the dog bit a Band-Aid." ,
    "The girl told the story cried.I convinced her children are noisy.",
    "Helen is expecting tomorrow to be a bad day.",
    "Fat people eat accumulates.",
    "I know the words to that song about the queen don’t rhyme."
]

garden_add = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

#merge both lists
garden_path_sentences.extend(garden_add)

#load module into spacy
nlp = spacy.load('en_core_web_sm')

print(" ".join(garden_path_sentences))

doc = nlp(" ".join(garden_path_sentences))

#named entity recog.
print([(entity,entity.label_,entity.label) for entity in doc.ents])


print([(i, i.label_, i.label) for i in doc.ents])

#getting meaning of unclear categ. term 'GPE'
print(spacy.explain('GPE'))
print(spacy.explain('PERSON'))

#Question:how does spacy catergories
#Ans: does so by using a contiguous spans of tokens. The default trained pipelines can identify 
#a variety of named and numeric entities, including companies, locations, organizations and products


#What was the entity and its explanation that you looked up?
# i looked up for entity 'GPE' and "PERSON"
 #GPE = 'Countries, cities, states'
 #"PERSON" = 'People, including fictional'

#Question: Did the entity make sense in terms of the word associated with it?
#ans: yes they make sense :)
