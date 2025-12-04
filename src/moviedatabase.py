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
from methodlibrary.heap import maxheap
from methodlibrary.sorting import hybrid_merge_sort
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



# this is just some skeleton code outlining some things we might need, feel free to change it i just wanted to build an outline
# its chat generated - killian

class moviedatabase:

    def __init__(self):
        self.__movies = []
        self.__titleindex = indexhash()
        self.__ratingheap = maxheap()
        self.__revenueheap = maxheap()

        self.__actorindex = None   # actor -> list of indices
        self.__genreindex = None   # genre -> list of indices

        self.__loaded = False

    def loaddata(self):
         for i in range(len(self.__movies)):
            movie = self.__movies[i]

            # 1) Title -> index (hash table)
            self.__titleindex.add(movie.get_title(), i)

            # 2) Rating heap (for top-N by rating)
            self.__ratingheap.push((movie.get_rating(), i))

            # 3) Revenue heap (for top-N by revenue)
            self.__revenueheap.push((movie.get_revenue(), i))

            """
            ADD METHODS TO LOAD ADDITIONAL INDEXES (actor index, genre index, etc.)
            """

        # sanity checks
        if self.__titleindex.isempty():
            raise ImportError("moviedatabase: loaddata(self), loaded empty titleindex")

        if self.__ratingheap.isempty():
            raise ImportError("moviedatabase: loaddata(self), loaded empty ratingheap ")

        # We could also check revenue heap if needed

        self.__loaded = True

    ##########################################################
    # YOUR QUERY SKELETONS (Killian’s responsibility)
    ##########################################################

    def find_movie_by_title(self, title):
        idx = self.__titleindex.get(title)
        return self.__movies[idx] if idx is not None else None

    def top_n_by_rating(self, n):
        temp = maxheap()
        for item in self.__ratingheap._data:
            temp.push(item)

        result = []
        for _ in range(min(n, len(temp))):
            rating, idx = temp.pop()
            result.append(self.__movies[idx])

        return result

    def top_n_by_revenue(self, n):
        temp = maxheap()
        for item in self.__revenueheap._data:
            temp.push(item)

        result = []
        for _ in range(min(n, len(temp))):
            revenue, idx = temp.pop()
            result.append(self.__movies[idx])

        return result

    def find_movies_by_actor(self, actor):
        # Depends on Mason building actorindex
        pass

    def find_movies_in_genre_between_years(self, genre, start, end):
        pass

    def suggest_similar_movies(self, title):
        # Depends on Mason building genreindex or bloom filter
        pass

    ##########################################################
    # GRAPH INTEGRATION (Killian responsibility)
    ##########################################################

    def link_actor_graph(self, graph):
        self.__actor_graph = graph

    def find_actor_connection(self, actor1, actor2):
        return self.__actor_graph.find_shortest_path(actor1, actor2)




# this is some code to work with sorting.py 
class moviedatabase:
    def __init__(self):
        self.__movies: List[Movie] = []  # an array of all movies

        # Index: title -> index in __movies
        self.__titleindex = indexhash()

        # Heaps for top-N queries
        self.__ratingheap = maxheap()    # (rating, index)
        self.__revenueheap = maxheap()   # (revenue, index)

        # Optional: we can build a genre-index array when sorting
        # so we don't store a permanent index here.

        """
        ADD ADDITIONAL INDICES FOR EACH QUERY YOU WANT THE MOVIE DATABASE TO DO
        """

        self.__loaded = False



    def sort_movies_by_genre(self):

"""
        Use the hybrid_merge_sort algorithm to sort movies by genre.

        We build a list of (genre_key, index) tuples, where:
            genre_key = a normalized primary genre string
            index     = index into self.__movies

        Then we apply hybrid_merge_sort on that list.
        Finally, we map back to Movie objects in genre-sorted order.

        RETURN:
            List[Movie] sorted by genre (primary genre key).
        """

        if not self.__loaded:
            raise RuntimeError("moviedatabase: sort_movies_by_genre called before data loaded.")

        # 1) Build (genre_key, index) list
        genre_index_pairs = []

        for i, movie in enumerate(self.__movies):
            raw_genres = movie.get_genres()

            # Defensive: handle None or empty strings
            if raw_genres is None:
                primary_genre = ""
            else:
                # Datasets sometimes separate genres with ',' or '|'
                # We normalize by treating both as separators.
                temp = raw_genres.replace("|", ",")
                parts = [g.strip() for g in temp.split(",") if g.strip() != ""]
                primary_genre = parts[0] if parts else ""

            # Store (genre_key, index)
            genre_index_pairs.append((primary_genre.lower(), i))

        # 2) Sort that list using hybrid_merge_sort.
        # We sort by the first element of each tuple (the genre_key).
        sorted_pairs = hybrid_merge_sort(
            genre_index_pairs,
            threshold=16,
            key=lambda pair: pair[0]  # sort by genre_key
        )

        # 3) Map sorted indices back to Movie objects
        sorted_movies = [self.__movies[idx] for (_, idx) in sorted_pairs]

        return sorted_movies
