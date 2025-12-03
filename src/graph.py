'''
Movie Database Project - Graph Class

Description: Implements an actor connection graph for finding shortest paths between actors

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    IMDB dataset
'''

from hash_map import HashMap
from queue import Queue
from movie import Movie
from actor import Actor

class ActorGraph:

    def __init__(self):
        # Private
        self.__graph = HashMap()  # actor_name -> HashMap of connected actors
        self.__movie_to_actors = HashMap()  # movie_id -> actors string
        
        # Protected
        self._movies = HashMap()  # movie_id -> Movie object
        self._title_to_id = HashMap()  # title -> movie_id (for title lookups)
        
    ## Phase 1: Data Loading
    
    def load_movies(self, dataset_path: str):
        # Read movie metadata dataset
        # For each row, create Movie object
        # Store in self._movies using movie_id as key
        # Also store in self._title_to_id for title lookups
        pass
    
    def add_movie(self, movie: Movie):
        movie_id = movie.get_imdb_id()
        title = movie.get_title()
        self._movies.put(movie_id, movie)
        self._title_to_id.put(title, movie_id)
    
    def load_actors(self, dataset_path: str):
        # Read cleaned_actors dataset
        # Build movie_id -> actors mapping
        pass
    
    ## Phase 2: Build Movie-to-Actors Index
    
    def build_movie_index(self):
        # Read through cleaned_actors dataset
        # Group actors by movie_id
        # Store as movie_id -> "actor1,actor2,actor3" in self.__movie_to_actors
        pass
    
    def add_actor_to_movie(self, movie_id: str, actor_name: str):
        # Add actor to the movie_id entry in __movie_to_actors
        if self.__movie_to_actors.contains(movie_id):
            existing = self.__movie_to_actors.get(movie_id)
            self.__movie_to_actors.put(movie_id, existing + "," + actor_name)
        else:
            self.__movie_to_actors.put(movie_id, actor_name)
    
    ## Phase 3: Build Actor-to-Actor Graph
    
    def build_actor_graph(self):
        # Iterate through self.__movie_to_actors
        # For each movie_id, get the actors string
        # Connect all pairs of actors who appear in that movie
        all_movie_ids = self.__movie_to_actors.get_all_keys()
        
        for i in range(len(all_movie_ids)):
            movie_id = all_movie_ids[i]
            actors_string = self.__movie_to_actors.get(movie_id)
            movie = self._movies.get(movie_id)
            movie_title = movie.get_title() if movie else movie_id
            self._connect_actors_in_movie(movie_title, actors_string)
    
    def _parse_actors(self, actors_string: str):
        # Split actors string by comma
        # Return array of actor names
        actors = []
        current = ""
        for char in actors_string:
            if char == ',':
                actors.append(current.strip())
                current = ""
            else:
                current += char
        if current:
            actors.append(current.strip())
        return actors
    
    def _connect_actors_in_movie(self, movie_title: str, actors_string: str):
        # Parse actors string into individual names
        actors = self._parse_actors(actors_string)
        
        # Connect every pair of actors
        for i in range(len(actors)):
            for j in range(i + 1, len(actors)):
                actor1 = actors[i]
                actor2 = actors[j]
                self.add_edge(actor1, actor2, movie_title)
                self.add_edge(actor2, actor1, movie_title)
    
    def add_edge(self, actor1: str, actor2: str, movie_title: str):
        # Get or create HashMap for actor1
        if not self.__graph.contains(actor1):
            self.__graph.put(actor1, HashMap())
        
        connections = self.__graph.get(actor1)
        
        # Add or append to existing connection
        if connections.contains(actor2):
            # Append movie to existing connection string
            existing_movies = connections.get(actor2)
            connections.put(actor2, existing_movies + "," + movie_title)
        else:
            # Create new connection
            connections.put(actor2, movie_title)
    
    ## Query Methods
    
    def find_movie_by_title(self, title: str):
        # Query 1: Find movie by title
        if self._title_to_id.contains(title):
            movie_id = self._title_to_id.get(title)
            return self._movies.get(movie_id)
        return None
    
    def find_movies_by_actor(self, actor_name: str):
        # Query 2: Find all movies by a given actor
        # Iterate through __movie_to_actors and check if actor appears
        results = []
        all_movie_ids = self.__movie_to_actors.get_all_keys()
        
        for i in range(len(all_movie_ids)):
            movie_id = all_movie_ids[i]
            actors_string = self.__movie_to_actors.get(movie_id)
            if self._actor_in_string(actor_name, actors_string):
                movie = self._movies.get(movie_id)
                if movie:
                    results.append(movie)
        
        return results
    
    def _actor_in_string(self, actor_name: str, actors_string: str) -> bool:
        # Check if actor name appears in the actors string
        return actor_name.lower() in actors_string.lower()
    
    ## Query 6: Shortest Path (BFS)
    
    def find_shortest_path(self, actor_a: str, actor_b: str):
        # BFS implementation
        # Returns path or None if no connection
        
        if not self.__graph.contains(actor_a) or not self.__graph.contains(actor_b):
            return None
        
        # Initialize BFS structures
        queue = Queue()
        visited = HashMap()  # actor_name -> True
        parent = HashMap()   # actor_name -> parent_actor_name
        
        # Start BFS
        queue.enqueue(actor_a)
        visited.put(actor_a, True)
        parent.put(actor_a, None)
        
        while not queue.is_empty():
            current_actor = queue.dequeue()
            
            # Found target
            if current_actor == actor_b:
                return self._reconstruct_path(parent, actor_a, actor_b)
            
            # Explore neighbors
            if self.__graph.contains(current_actor):
                connections = self.__graph.get(current_actor)
                neighbors = connections.get_all_keys()  # Get all connected actors
                
                for i in range(len(neighbors)):
                    neighbor = neighbors[i]
                    if not visited.contains(neighbor):
                        visited.put(neighbor, True)
                        parent.put(neighbor, current_actor)
                        queue.enqueue(neighbor)
        
        return None  # No path found
    
    def _reconstruct_path(self, parent: HashMap, start: str, end: str):
        # Build path from end to start using parent tracking
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = parent.get(current) if parent.contains(current) else None
        
        # Reverse path
        return self._reverse_path(path)
    
    def _reverse_path(self, path):
        # Reverse the path array manually
        reversed_path = []
        for i in range(len(path) - 1, -1, -1):
            reversed_path.append(path[i])
        return reversed_path
    
    ## Helper Methods
    
    def get_connection_movies(self, actor1: str, actor2: str):
        # Get the movies that connect two actors
        if self.__graph.contains(actor1):
            connections = self.__graph.get(actor1)
            if connections.contains(actor2):
                return connections.get(actor2)
        return None
    
    def display_path(self, path):
        # Display the shortest path between two actors
        if path is None or len(path) == 0:
            print("No connection found")
            return
        
        print(f"Connection path ({len(path)} actors, {len(path)-1} degrees):")
        for i in range(len(path) - 1):
            actor1 = path[i]
            actor2 = path[i + 1]
            movies = self.get_connection_movies(actor1, actor2)
            print(f"  {actor1} -> {actor2}")
            print(f"    via: {movies}")