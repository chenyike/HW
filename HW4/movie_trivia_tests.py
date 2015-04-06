#author - Yike Chen & Hao Liu

from movie_trivia import *
import unittest

class TestMovies(unittest.TestCase):

    movieDb = {}
    ratingDb = {}
    movieDb_small = {}
    ratingDb_small = {}


    def setUp(self):
        self.movieDb = create_actors_DB('movies.txt')
        self.ratingDb = create_ratings_DB('moviescores.csv')
        self.movieDb_small = create_actors_DB('movies_small.txt')
        self.ratingDb_small = create_ratings_DB('moviescores_small.csv')


    def testreal_actor_name(self):
        # input an actor's name in low case, should return real name in Database
        actor = real_actor_name('will smith',self.movieDb.keys())
        self.assertEquals(actor, 'Will Smith', ' check real actor name')

        
    def testreal_movie_name(self):
        # input an movie's namemixed with low case and upper case, should return real movie's name in Database
        movies = real_movie_name(['lost','titAnic'],self.movieDb.values())
        self.assertEqual(movies, ['Lost','Titanic'], ' check real movie name')


    def testreal_movie_name2(self):
        # input an movie's namemixed with low case, should return real movie's name in Database
        movie = real_movie_name2('lost', self.movieDb.values())
        self.assertEqual(movie, 'Lost', ' check real movie name2')

        
    def testinsert_actor_info(self):
        # Input an actor who already exist but his movie does not exist
        movielist = insert_actor_info('Tom HaNks',['I\'m great','am i'], self.movieDb)
        self.assertTrue('Tom Hanks' in movielist.keys() )
        for movie in ['I\'m great','am i']:
            self.assertTrue(movie in movielist['Tom Hanks'])
        # Input an actor and a movie that already exist in the database
        movielist = insert_actor_info('Tom HaNks', ['You\'ve got Mail'], self.movieDb)
        self.assertEqual(movielist, self.movieDb, 'Scenario where actor and movie both already exist testing failed')
        # Choose an actor that is not in the list and test it
        movielist = insert_actor_info('E',['I\'m great','am i'], self.movieDb)
        self.assertTrue('E' in movielist.keys() )
        for movie in ['I\'m great','am i']:
            self.assertTrue(movie in movielist['E'])

        
    def testinsert_rating(self):
        # Choose a random movie and test it
        ratings = insert_rating('Lost', (87,88), self.ratingDb)
        self.assertEqual(ratings, ['87', '88'], 'Desired functionality testing failed.')
        # Input a non-exist movie and test it, should return the newly input information. If not, then failed.
        ratings = insert_rating('What', ('44','66'), self.ratingDb)
        self.assertEqual(ratings, ['44','66'], 'Non-exist movie scenario testing failed')


    def testdelete_movie(self):
        # Choose a movie that is not in the database and test it
        movieDB = delete_movie('Errr', self.movieDb, self.ratingDb)
        self.assertTrue('Errr' not in movieDB[0].values())
        self.assertTrue('Errr' not in movieDB[1].keys())
        # Choose a movie that is in the database and test it
        movieDB = delete_movie('tHE godfather', self.movieDb, self.ratingDb)
        self.assertTrue('The Godfather' not in movieDB[0].values())
        self.assertTrue('The Godfather' not in movieDB[1].keys())


    def testselect_where_actor_is(self):
        # Choose a random actor and test it
        movielist = select_where_actor_is('MichAEl EmERson', self.movieDb)
        self.assertEqual(movielist, ['The Dark Knight Returns', 'Person of Interest', 'Lost'] , 'Desired functionality testing failed. ')
        # Input a non-exist actor and test it, should return an empty list. If not, then failed.
        movielist = select_where_actor_is('idk', self.movieDb)
        self.assertEqual(movielist,'The actor is not in Database','Non-exist movie scenario testing failed')


    def testselect_where_movie_is(self):
        # Choose a random movie and test it
        actors = select_where_movie_is('The GODFather', self.movieDb)
        self.assertEqual(actors, ['Diane Keaton', 'Marlon Brando', 'Al Pacino'],'Desired functionality testing failed. ')
        # Input a non-exist movie and test it, should return an empty list. If not, then failed.
        actors = select_where_movie_is('God', self.movieDb)
        self.assertEqual(actors,[],'Non-exist movie scenario testing failed')


    def testselect_where_rating_is(self):
        # Choose a random number and test critic library
        movielist = select_where_rating_is(100,'=', True, self.ratingDb_small)
        self.assertEqual(movielist, ['Maltese Falcon', 'Lilies of the Field'] , 'Critic functionality testing failed. ')
        # Input >0 , should return the entire library. 
        movielist = select_where_rating_is(0,'>',True, self.ratingDb)
        self.assertEqual(movielist, self.ratingDb.keys() , 'Desired functionality testing failed, check critic. ')
        # Choose a random number and test audience library
        movielist = select_where_rating_is(97,'>',False, self.ratingDb)
        self.assertEqual(movielist, ['The Avengers', 'Seven', 'Mission Impossible', 'Ted', 'The Godfather'] , 'Audience functionality testing failed. ')
        # input 0, should return nothing
        movielist = select_where_rating_is(0,'=',False, self.ratingDb)
        self.assertEqual(movielist, [] , 'Desired functionality testing failed, check audience. ')

        
    def testget_co_actors(self):
        # Choose a random actor and test
        actorlist = get_co_actors('Diane KEAton',self.movieDb)
        self.assertEqual(actorlist,['Al Pacino', 'Woody Allen', 'Marlon Brando', 'Robert DeNiro']  , 'Critic functionality testing failed. ')
        # Choose a non-exist actor and test, should return an empty list
        actorlist = get_co_actors('idk',self.movieDb)
        self.assertEqual(actorlist,[], 'non-exist actor testing failed. ')

        
    def testget_common_movie(self):
        # Choose 2 random actors and test
        movielist = get_common_movie('Diane Keaton','Al pAcino',self.movieDb)
        self.assertEqual(movielist,['The Godfather', 'The Godfather Part II'] , 'Critic functionality testing failed. ')
        # Choose non-exist actors and test, should return an empty list
        movielist = get_common_movie('idk', 'Errr',self.movieDb)
        self.assertEqual(movielist,[], 'Check two non existing actors testing failed. ')


    def testcritics_darling(self):
        # test if it can return a critics favourite movie, use the original datadase
        actorlist=critics_darling(self.movieDb,self.ratingDb)
        self.assertEqual(actorlist, ['Joan Fontaine'], 'Critic functionality testing failed. ')
        # test if it can return multiple favourite, use a different test database
        actorlist=critics_darling(self.movieDb_small,self.ratingDb_small)
        self.assertEqual(set(actorlist),set(['critic_medium_audience','critic_least_audience']) , 'Critic functionality testing failed. ')
        

    def testaudience_darling(self):
        # test if it can return an audience favourite movie, use the original datadase
        actorlist=audience_darling(self.movieDb,self.ratingDb)
        self.assertEqual(actorlist, ['Diane Keaton'], 'Critic functionality testing failed. ')
        # test if it can return multiple audience favourite movies, use a different test database
        actorlist=audience_darling(self.movieDb_small,self.ratingDb_small)
        self.assertEqual(set(actorlist),set(['critic_most_audience','critic_least_audience']) , 'Critic functionality testing failed. ')
        

    def testgood_movies(self):
        # simply test it with a small database
        movieset=good_movies(self.ratingDb_small)
        self.assertEqual(movieset, set(['Maltese Falcon', 'Rear Window', 'Lilies of the Field']), 'Critic functionality testing failed. ')

    
    def testget_common_actors(self):
        # test if shared actors can be found given two movie names
        actorlist=get_common_actors('Superman','speed',self.movieDb)
        self.assertEqual(actorlist,[], 'Critic functionality testing failed. ')
        # test if movie is not in database, should return an empty list
        actorlist=get_common_actors('Godfather','Godfather Part II',self.movieDb)
        self.assertEqual(actorlist,[], 'Check movies not in database. ')


    def testbacon_function(self):
        # Test if the bacon function that we wrote is correct
        dic=bacon_function(self.movieDb,2,{0: 'Kevin Bacon', 1: {'Tom Cruise': 1, 'Brad Pitt': 1, 'Jennifer Lawrence': 1, 'Julianne Moore': 1, 'Tom Hanks': 1, 'Kevin Costner': 1, 'Jack Nicholson': 1, 'Ryan Gosling': 1, 'Dustin Hoffman': 1, 'Sean Penn': 1, 'January Jones': 1}})
        self.assertEqual(dic[2],{'Rachel McAdams': 2, 'Sylvester Stallone': 2, 'Angelina Jolie': 2, 'Leonardo Di Caprio': 2, 'Meg Ryan': 2, 'Julia Roberts': 2, 'Kevin Bacon': 2, 'Morgan Freeman': 2, 'Mark Wahlberg': 2, 'George Clooney': 2, 'Bradley Cooper': 2, 'Anthony Hopkins': 2, 'Eric Bana': 2, 'Meryl Streep': 2, 'Josh Brolin': 2, 'Renee Zellweger': 2, 'Amy Adams': 2, 'Diane Kruger': 2, 'James Earl Jones': 2, 'John Goodman': 2, 'Shirley Maclaine': 2, 'Ray Liotta': 2},'Failed')


    def testget_bacon(self):
        # Test and see if bacon number makes sense
        bacon_number=get_bacon('Shirley Maclaine',self.movieDb)
        self.assertEqual(bacon_number,2,'Bacon function is problematic')
        
unittest.main() 
