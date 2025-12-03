'''
Movie Database Project

Description: This program implements a movie database class with attributes for IMDB data

@Author: Mason Ahner
@Contact: mtabud12@gmail.com   
@Date: 11/28/2025

Sources: ChatGPT. Used to research how to format a database without creating multiple duplicates.
The actual implementations are my own
'''

from methodlibrary.hashtable import indexhash #used for index based hashtables
from methodlibrary.queue import priorityqueue #used to get the movie title by rating (also used to sort entries by highest rating)
from movie import Movie #import Movie Struct/Class
from actor import Actor #import Actor Struct/Class
from typing import List
class moviedatabase:
    def __init__(self):
        self.__movies: List[Movie] = [] #an array of all movies
        self.__titleindex = indexhash() #an index based hash. call the movie name to get its index location inside the movieDB array
        self.__ratingindex = priorityqueue() #a priority-queue that is sorted by rating. when popping, you get a rating,index pair sorted by highest rating
        """
        ADD ADDITIONAL INDICES FOR EACH QUEREY YOU WANT THE MOVIE DATABASE TO DO
        """
        
        
        
        self.__loaded = False # a boolean to see if the file has been loaded

    def loaddata(self):
        #used to load the CSV data via CSV parsing
        
        """
        CALL CSV PARSING FUNCTION, CREATE MOVIES, AND DUMP EACH MOVIE INTO MOVIE ARRAY (self.__movies[])
        
        """

        #index through the movie array, fill remaining hashindexes
        for i in range(len(self.__movies)):
            self.__titleindex.add(self.__movies[i].get_title(),i) #add all movie titles with its corresponding index to titleindex
            self.__ratingindex.enqueue((self.__movies[i].get_rating(), i)) #uses a tuple, since first entry in tupple is rating, it will sort by rating first
            """
            ADD METHODS TO LOAD ADDITIONAL INDEXES
            
            """
        #run quick checks to see if each index/based entry is
        if self.__titleindex.isempty():
            raise ImportError("moviedatabase: loaddata(self), loaded empty titleindex")
        
        if self.__ratingindex.isempty():
            raise ImportError("moviedatabase: loaddata(self), loaded empty ratingindex ")
        
        """ 
        ADD ADDITIONAL CHECKS FOR EACH INDEX IMPLEMENTED
        """
        
        self.__loaded = True #set loaded to true if no issue have arised



