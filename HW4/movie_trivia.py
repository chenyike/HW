#author - Yike Chen & Hao Liu

#Content Added...
#Chris Pratt, Guardians of the Galaxy, The Lego Movie
#Michael Emerson, Person of Interest, The Dark Knight Returns, Lost

import csv

def real_actor_name(string,lists):
    '''A function that search for similar names in the database and return the real actor's name'''
    n=0
    for item in lists:
        if item.lower() == string.lower():
            n+=1
            name = item
    if n>0:
        return name
    if n==0:
        return string

    
def real_movie_name(movielist,movieSets):
    '''A function that search for similar movielist in the database and return the real movielist'''
    movies = []
    for movie in movielist:
        search = False
        for movieSet in movieSets:
            for element in list(movieSet):
                if movie.lower() == element.lower():
                    real_name=element
                    search = True
        if search:
            movies.append(real_name)
        else:
            movies.append(movie)
    return movies


def real_movie_name2(movie,movieSets):
    '''A function that search for similar movie in the database and return the real movie name'''
    for movieSet in movieSets:
        for element in list(movieSet):
            if movie.lower() == element.lower():
                movie=element
    return movie
        

def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    #read in line by line
    for line in f:
        #remove beginning and trailing spaces
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        if actor not in movieInfo.keys():
            movieInfo[actor] = set([])
        movies = actorAndMovies[1:]
        cleaned_movies = []
        for movie in movies:
            cleaned_movies.append(movie.lstrip().rstrip())
        movieInfo[actor] = movieInfo.get(actor).union(set(cleaned_movies))
    f.close()
    return movieInfo


def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict


def insert_actor_info(actor, movies, movie_Db):
    '''insert/update actor's information'''
    actor = real_actor_name(actor,movie_Db.keys())
    movies = real_movie_name(movies,movie_Db.values())
    
    n=0
    for movie in movies:
        if actor in movie_Db.keys():
            if movie in movie_Db[actor]:
                n+=1

    if actor not in movie_Db.keys():
        movie_Db.keys().append(actor)
        movie_Db[actor]=[]
        for movie in movies:
            movie_Db[actor].append(movie)           
        return movie_Db
    
    elif actor in movie_Db.keys() and n==0:
        for movie in movies:
             if movie not in movie_Db[actor]:
                movie_Db[actor].add(movie)
        return movie_Db
    
    elif n>0:
        return movie_Db


def insert_rating(movie, ratings, ratings_Db):
    '''update ratings_Db'''
    movie = real_actor_name(movie,ratings_Db.keys())
    rating_list = []
    rating_list.append(str(ratings[0]))
    rating_list.append(str(ratings[1]))
    if movie not in ratings_Db.keys():
        ratings_Db[movie]=ratings_Db.get(movie, rating_list)
        return ratings_Db[movie]
    else:
        ratings_Db[movie]=rating_list
        return ratings_Db[movie]


def delete_movie(movie, movie_Db, ratings_Db):
    '''delete all information from the database that corresponds to the movie'''
    movie = real_movie_name2(movie,movie_Db.values())
    movie = real_actor_name(movie,ratings_Db.keys())
    if movie in ratings_Db.keys():
        del ratings_Db[movie]
    for item in movie_Db.values():
        if movie in item:
            item.remove(movie)
    return (movie_Db,ratings_Db)


def select_where_actor_is(actorName, movie_Db):
    '''give an actor, retun the list of all movies'''
    actorName = real_actor_name(actorName,movie_Db.keys())
    if actorName in movie_Db.keys():
        return list(movie_Db[actorName])
    else:
        return 'The actor is not in Database'
    

def select_where_movie_is(movieName, movie_Db):
    '''give a movie, return the list of all actors'''
    movieName = real_movie_name2(movieName,movie_Db.values())
    actorlist=[]
    for actor in movie_Db.keys():
        if movieName in movie_Db[actor]:
            actorlist.append(actor)
    return actorlist


def select_where_rating_is(targeted_rating, comparison, is_critic,ratings_Db):
    '''returns a list of movies that satisfies an inequality or equality based on the comparison argument
    and the targeted rating argument'''
    # choose critic or audience
    movielist=[] 
    if is_critic:
        column=0
    else:
        column=1
    if comparison=='>':
        for movie in ratings_Db.keys():
            if int(ratings_Db[movie][column]) > int(targeted_rating):
                movielist.append(movie)
    if comparison=='=':
        for movie in ratings_Db.keys():
            if int(ratings_Db[movie][column]) == int(targeted_rating):
                movielist.append(movie)
    if comparison=='<':
        for movie in ratings_Db.keys():
            if int(ratings_Db[movie][column]) < int(targeted_rating):
                movielist.append(movie)
    return movielist


def get_co_actors(actorName,moviedb):
    '''returns list of all actors that the actor has ever worked with in any movie'''
    actorName= real_actor_name(actorName,moviedb.keys())
    actorlist = []
    for actor in moviedb.keys():
        for movie in moviedb[actor]:
            if actorName in moviedb.keys():
                if movie in moviedb[actorName]:
                    actorlist.append(actor)
    actorset = set(actorlist)
    if actorName in moviedb.keys():
        actorset.remove(actorName)
    actorlist = list(actorset)
    return actorlist
            

def get_common_movie(actor1,actor2,moviedb):
    '''goes through the database and return the movies where both actors were cast.'''
    actor1 = real_actor_name(actor1,moviedb.keys())
    actor2 = real_actor_name(actor2,moviedb.keys())
    movielist=[]
    if actor1 in moviedb.keys() and actor2 in moviedb.keys():
        for movie in moviedb[actor2]:
            if movie in moviedb[actor1]:
                movielist.append(movie)
    movielist=list(set(movielist))
    return movielist


def critics_darling(movie_Db,ratings_Db):
    '''given the two dictionaries, we are interested in finding the actor whose movies have the highest average critics rating'''
    actorlist = []
    number = 0
    total = 0
    dic={}
    index = 0  # get the critics column
    for actor in movie_Db.keys():
        for movie in movie_Db[actor]:
            if movie in ratings_Db.keys():
                number += 1
                total += float(ratings_Db[movie][index])
        average = total/number
        total = 0
        number = 0
        # create a new dictionary containing actor and average score
        dic[actor] = dic.get(actor,average)
    for actor in dic.keys():
        if dic[actor] == max(dic.values()):
            actorlist.append(actor)           
    return actorlist


def audience_darling(movie_Db,ratings_Db):
    '''given the two dictionaries, we are interested in finding the actor whose movies have the highest average audience rating'''
    actorlist = []
    number = 0
    total = 0
    dic={}
    index = 1  # get the audience column
    for actor in movie_Db.keys():
        for movie in movie_Db[actor]:
            if movie in ratings_Db.keys():
                number += 1
                total += float(ratings_Db[movie][index])
        average = total/number
        total = 0
        number = 0
        dic[actor] = dic.get(actor,average)
    for actor in dic.keys():
        if dic[actor] == max(dic.values()):
            actorlist.append(actor)           
    return actorlist

    
def good_movies(ratings_Db):
    '''this function returns the set of movies that both critics and the audience have rated above 85'''
    good_critic_movies = select_where_rating_is(85, '>', True,ratings_Db)+select_where_rating_is(85, '=', True,ratings_Db)
    good_audience_movies = select_where_rating_is(85, '>', False,ratings_Db)+select_where_rating_is(85, '=', False,ratings_Db)
    good_movies = good_critic_movies + good_audience_movies
    return set(good_movies)


def get_common_actors(movie1,movie2,movies_Db):
    '''given a pair of movies, return a list of actors that acted in both'''
    movie1 = real_movie_name2(movie1,movies_Db.values())
    movie2 = real_movie_name2(movie2,movies_Db.values())
    search1=False
    search2=False
    movie1actor=[]
    movie2actor=[]
    actorlist=[]
    for item in movies_Db.values():
        if movie1 in item:
            search1=True
    for item in movies_Db.values():
        if movie2 in item:
            search2=True
    if search1 and search2:
        for actor in movies_Db.keys():
            if movie1 in movies_Db[actor]:
                movie1actor.append(actor)
            if movie2 in movies_Db[actor]:
                movie2actor.append(actor)
        actorlist = list (set(movie1actor).intersection( set(movie1actor) ))
    else:
        actorlist=[]
    return actorlist


def bacon_function(movieDb,index,dic):
    '''A function that helps expand the bacon search,
    and return the overall dictionary containing the bacon number and the movielist'''
    dicx={}
    for previous_actor in dic[index-1].keys():
        for current_actor in movieDb.keys():
            for current_movie in movieDb[current_actor]:
                if current_movie in movieDb[previous_actor]:
                    dicx[current_actor]=dicx.get(current_actor,index)
    for i in range (1,index):
        for actor in dic[i].keys():
            if actor in dicx.keys():
                del dicx[actor]
    dic[index]=dic.get(index,dicx)
    return dic


def get_bacon(actor,movieDb):
    '''Get an actor's Bacon number, aka, the number of links that have to be followed to get to Kevin Bacon'''
    actor = real_actor_name(actor,movieDb.keys())
    index = 2
    dic = {}
    dic[0]=dic.get(0,'Kevin Bacon')
    
    dic1={}
    for movie in movieDb['Kevin Bacon']:
        for actors in movieDb.keys():
            if movie in movieDb[actors]:
                dic1[actors]=dic1.get(actors , 1)
    del dic1['Kevin Bacon']

    dic[1]=dic.get(1,dic1)
    length = len(dic[1])

    while not ( len(dic[index-1])==0):
        dic = bacon_function(movieDb,index,dic)
        length += len(dic[index])
        index += 1

    search = False
    for i in range(1,index):
        if actor in dic[i].keys():
            search = True
            return i
    if search == False:
        return 'Due to the limitation of our database, we are unable to tell you the bacon number' 

def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')

    #copy the original database for future use
    actor_list = actor_DB.copy()
    ratings_list = ratings_DB.copy()

    #welcome paragraph
    print '''Welcome to the Movie Trivia!
    Have you ever wondered how do the audience like your favorite movie?
    How about critics?
    Do you wanna know more about your favorite actors masterpieces?
    Has any other actors worked with him/her in one movie?
    Here in Movie Trivia, you are able to find all the answers of actors, movies and ratings by critics or audience...\n\n'''

    #provide the information that we can process with this program
    choose =raw_input('''Please enter 1 if you would like to add in any actor and his/her movies;
    Please enter 2 if you would like to add in ratings for any movies;
    Please enter 3 if you would like to delete all information corresponds to the movie;
    Please enter 4 if you would like to know all the movies one actor has acted;
    Please enter 5 if you would like to know all the actors acted in given movie;
    Please enter 6 if you would like to compare the ratings of two movies;
    Please enter 7 if you would like to know all the actors who have worked with one given actor;
    Please enter 8 if you would like to know the movie which two given actors have been acted in;
    Please enter 9 if you would like to know the top rated actor's name by audience;
    Please enter 10 if you would like to know the top rated actor's name by critics;
    Please enter 11 if you would like to know the top rated movie;
    Please enter 12 if you would like to know the actor which acted two given movies;
    Please enter 13 if you would like to know the Bacon number of a given actor;
    Please press 0 if you want to exit''')

    while int(choose) > 0:
        if int(choose) == 1:
            movielist = []
            actor = raw_input('''which actor would you like to add? ''') 
            movie = raw_input('What movie was he in? ')
            movielist.append(movie)
            choice = raw_input('Do you want to add another movie? Input Y if you would like to add: ')
            while choice in 'Yy':
                movie = raw_input('What movie was he in? ')
                movielist.append(movie)
                choice = raw_input('Do you want to add another movie? Input Y if you would like to add: ')
            insert_actor_info(actor, movielist, actor_DB)
            print 'Information Updated: ', actor, ':', list(actor_DB[actor])
            print 

        if int(choose) == 2:
            ratings = []
            movie = raw_input ('Which movie\'s rating would you like to update?')
            critic_rating = raw_input ('what is the critic rating of the movie?')
            ratings.append(critic_rating)
            audience_rating = raw_input ('what is the audience rating of the movie?')
            ratings.append(audience_rating)
            insert_rating(movie,ratings,ratings_DB)
            print 'Informatin updated: ', movie, ':', ratings_DB[movie]
            print

        if int(choose)==3:
            movie = raw_input('which movie do you want to delete?')
            delete_movie(movie,actor_DB,ratings_DB)
            print 'Deleted! '
            print
                
        if int(choose)==4:
            actor = raw_input('Which actor would you like to know? ')
            movielist=select_where_actor_is(actor, actor_DB)
            print 'The movies that ', actor, 'was in are: ', movielist
            print
            
        if int(choose)==5:
            movie = raw_input ('Which movie would you like to know?')
            actorlist = select_where_movie_is(movie, actor_DB)
            print actorlist, 'was in this movie. '
            print

        if int(choose)==6:
            number = raw_input ('what range of movies would you like to know. please input rate score first')
            is_great = raw_input('''input > if you like to know movies that are above that score;
        input = if you want to know movies that are equal to that one;
        input < if you want to know movies that are less than that score''') 
            choice = raw_input ('Input y if you want to critic score, input n if you want to know audience score')
            if choice in 'Yy':
                is_critic = True
            else:
                is_critic = False
            movielist = select_where_rating_is(number,is_great,choice, ratings_DB)
            print 'movies that ' , is_great, number, 'are ', movielist
            print

        if int(choose)==7:
            actor = raw_input('Which actor would you like to know? ')
            actorlist=get_co_actors(actor, actor_DB)
            print 'The actors that ', actor, 'co-acted are: ', actorlist
            print
            
        if int(choose)==8:
            actor1 = raw_input('Which actor would you like to know? ')
            actor2 = raw_input('Which actor would you like to know next? ')
            movielist=get_common_movie(actor1, actor2, actor_DB)
            print 'The movies that ', actor1, 'and',actor2,  'were in together are: ', movielist
            print
            
        if int(choose)==9:
            actorlist=critics_darling(actor_DB,ratings_DB)
            print 'Critics_darlings are', actorlist
            print

        if int(choose)==10:
            actorlist=audience_darling(actor_DB,ratings_DB)
            print 'Audience_darlings are', actorlist
            print

        if int(choose)==11:
            movielist=good_movies(ratings_DB)
            print 'Good movies are', movielist
            print

        if int(choose)==12:
            movie1 = raw_input('Which movie would you like to know? ')
            movie2 = raw_input('Which movie would you like to know next? ')
            actorlist=get_common_actors(movie1, movie2, actor_DB)
            print actorlist, 'are all in', movie1, 'and', movie2, 'together.'
            print
           
        if int(choose)==13:
            actor = raw_input('Which actor would you like to know? ')
            number=get_bacon(actor,actor_DB)
            print actor, 'has a Bacon number of ', number
            print

        #revert all the changes that has been made to the database
        actor_Db = actor_list 
        ratings_Db = ratings_list
                
        print   
        choose =raw_input('''Please enter 1 if you would like to add in any actor and his/her movies;
        Please enter 2 if you would like to add in ratings for any movies;
        Please enter 3 if you would like to delete all information corresponds to the movie;
        Please enter 4 if you would like to know all the movies one actor has acted;
        Please enter 5 if you would like to know all the actors acted in given movie;
        Please enter 6 if you would like to compare the ratings of two movies;
        Please enter 7 if you would like to know all the actors who have worked with one given actor;
        Please enter 8 if you would like to know the movie which two given actors have been acted in;
        Please enter 9 if you would like to know the top rated actor's name by audience;
        Please enter 10 if you would like to know the top rated actor's name by critics;
        Please enter 11 if you would like to know the top rated movie;
        Please enter 12 if you would like to know the actor which acted two given movies;
        Please enter 13 if you would like to know the Bacon number of a given actor;
        Please press 0 if you want to exit.''')
    
if __name__ == '__main__':
    main()
