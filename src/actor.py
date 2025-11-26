'''
Movie Database Project

Description: This program implements an actor class with attributes for IMDB data

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    IMDB dataset
'''

from typing import Optional

class Actor:

    def __init__(self, 
                 name: str = "Unknown", 
                 birth_year: int = 0,
                 movies: str = "",
                 imdb_id: str = ""):

        # Private
        self.__name: str = name
        self.__imdb_id: str = imdb_id
        
        # Protected
        self._birth_year: int = birth_year
        self._movies: str = movies

        # Public Aliases
        self.name: str = name
        self.birth_year: int = birth_year
        self.movies: str = movies
        self.imdb_id: str = imdb_id

    ## Public Setters

    def set_name(self, name: str):
        self.__name = name
        self.name = name

    def set_imdb_id(self, imdb_id: str):
        self.__imdb_id = imdb_id
        self.imdb_id = imdb_id

    def set_birth_year(self, birth_year: int):
        self._birth_year = birth_year
        self.birth_year = birth_year
    
    def set_movies(self, movies: str):
        self._movies = movies
        self.movies = movies
    
    ## Public Getters 

    def get_name(self) -> str:
        return self.__name
    
    def get_imdb_id(self) -> str:
        return self.__imdb_id
    
    def get_birth_year(self) -> int:
        return self._birth_year
    
    def get_movies(self) -> str:
        return self._movies

    ## Protected Helper Methods

    def _normalize_string(self, s: str) -> str:
        return s.lower().strip()

    def _search_in_field(self, field: str, search_term: str) -> bool:
        normalized_field = self._normalize_string(field)
        normalized_term = self._normalize_string(search_term)
        return normalized_term in normalized_field

    ## Public Query Methods

    def in_movie(self, movie_title: str) -> bool:
        return self._search_in_field(self._movies, movie_title)