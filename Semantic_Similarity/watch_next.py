import spacy

def recommend_movie(movie_2_compare):
    movie_closest = ['None', 0] # creates a list to contain a movie and the similarity score.. see below
    with open("movies.txt", 'r') as movie_list:# open the file containing  movies
        nlp = spacy.load('en_core_web_md') #load spacy module
        movie_2_compare = nlp(movie_2_compare)
        print('Search for related movies begins...')
        for movie in movie_list: #get descrip of each movie
            movie = movie.split(":",1) #sepeartes the title from the description
            similarity = nlp(movie[1]).similarity(movie_2_compare)# check similar description
            if similarity > movie_closest[1]: #this stores the movie with the highest similarity per iteration
                movie_closest[1] = similarity
                movie_closest[0] = movie[0]
            
    print(f'Best Similar Movie : {movie_closest[0]}')#print them out to show order
  
    print('done!')

movie_review = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator'
recommend_movie(movie_review)