import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# cat and monkey are both animals
# for monkey and banana , the similarity could be because Monkeys like to eat banana
# a similar one is banana and apple , they are both fruits and have good similaritiy score

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# using "en_core_web_sm" 
nlp_ = spacy.load('en_core_web_sm')
word1 = nlp_("cat")
word2 = nlp_("monkey")
word3 = nlp_("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp_('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# cat and monkey are both animals
# for monkey and banana , the similarity could be because Monkeys like to eat banana
# a similar one is banana and apple , they are both fruits and have good similaritiy score

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp_(sentence_to_compare)
for sentence in sentences:
    similarity = nlp_(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#`en_core_web_sm` uses a small model, 
#it has no word vectors loaded and Similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 

