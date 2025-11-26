'''
Movie Database Project

Description: This program implements a movie class with attributes for IMDB data

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    IMDB dataset
'''

from typing import Optional

class Movie:

    def __init__(self, 
                 title: str = "Unknown Title", 
                 year: int = 0, 
                 runtime: int = 0,
                 genres: str = "",
                 director: str = "Unknown",
                 actors: str = "",
                 rating: float = 0.0,
                 revenue: float = 0.0,
                 imdb_id: str = ""):

        # Private
        self.__title: str = title
        self.__imdb_id: str = imdb_id
        
        # Protected
        self._year: int = year
        self._runtime: int = runtime
        self._genres: str = genres
        self._director: str = director
        self._actors: str = actors
        self._rating: float = rating
        self._revenue: float = revenue

        # Public Aliases
        self.title: str = title
        self.year: int = year
        self.runtime: int = runtime
        self.genres: str = genres
        self.director: str = director
        self.actors: str = actors
        self.rating: float = rating
        self.revenue: float = revenue
        self.imdb_id: str = imdb_id

    ## Public Setters

    def set_title(self, title: str):
        self.__title = title
        self.title = title

    def set_imdb_id(self, imdb_id: str):
        self.__imdb_id = imdb_id
        self.imdb_id = imdb_id

    def set_year(self, year: int):
        self._year = year
        self.year = year
    
    def set_runtime(self, runtime: int):
        self._runtime = runtime
        self.runtime = runtime

    def set_genres(self, genres: str):
        self._genres = genres
        self.genres = genres

    def set_director(self, director: str):
        self._director = director
        self.director = director

    def set_actors(self, actors: str):
        self._actors = actors
        self.actors = actors

    def set_rating(self, rating: float):
        self._rating = rating
        self.rating = rating

    def set_revenue(self, revenue: float):
        self._revenue = revenue
        self.revenue = revenue
    
    ## Public Getters 

    def get_title(self) -> str:
        return self.__title
    
    def get_imdb_id(self) -> str:
        return self.__imdb_id
    
    def get_year(self) -> int:
        return self._year
    
    def get_runtime(self) -> int:
        return self._runtime

    def get_genres(self) -> str:
        return self._genres
    
    def get_director(self) -> str:
        return self._director
    
    def get_actors(self) -> str:
        return self._actors
    
    def get_rating(self) -> float:
        return self._rating
    
    def get_revenue(self) -> float:
        return self._revenue

    ## Protected Helper Methods

    def _normalize_string(self, s: str) -> str:
        return s.lower().strip()

    def _search_in_field(self, field: str, search_term: str) -> bool:
        normalized_field = self._normalize_string(field)
        normalized_term = self._normalize_string(search_term)
        return normalized_term in normalized_field

    ## Public Query Methods

    def has_genre(self, genre: str) -> bool:
        return self._search_in_field(self._genres, genre)

    def has_actor(self, actor: str) -> bool:
        return self._search_in_field(self._actors, actor)