Semantic.py
Create a file called semantic.py and run all the code extracts above.
● Write a note about what you found interesting about the similarities
between cat, monkey and banana and think of an example of your own.
● Run the example file with the simpler language model ‘en_core_web_sm’ and
write a note on what you notice is different from the model 'en_core_web_md'.


watch_next.py
Let us build a system that will tell you what to watch next based on the word
vector similarity of the description of movies.
● Create a file called watch_next.py
● Read in the movies.txt file. Each separate line is a description of a different
movie.
● Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
● The function should take in the description as a parameter and return the
title of the most similar movie.