'''
Movie Database Project - Data Parser

Description: Handles loading and parsing of IMDB datasets into data structures

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    IMDB dataset (movies_metadata.csv, cleaned_actors.csv)
'''

import sys
sys.path.append('../src')

from hash_map import HashMap
from movie import Movie
from actor import Actor

class DataParser:
    
    def __init__(self):
        pass
    
    ## CSV Parsing Helpers
    
    def _parse_csv_line(self, line: str):
        # Parse a CSV line, handling commas within quotes
        # Returns array of fields
        fields = []
        current_field = ""
        in_quotes = False
        
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                fields.append(current_field.strip())
                current_field = ""
            else:
                current_field += char
        
        # Add last field
        if current_field:
            fields.append(current_field.strip())
        
        return fields
    
    def _read_file_lines(self, filepath: str):
        # Read all lines from a file
        # Returns array of lines
        lines = []
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    lines.append(line.strip())
        except FileNotFoundError:
            print(f"Error: File {filepath} not found")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
        
        return lines
    
    def _extract_genres(self, genres_field: str):
        # Extract genre names from the complex format
        # Input: "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}]"
        # Output: "Animation,Comedy"
        
        genres = []
        current = ""
        in_name = False
        
        i = 0
        while i < len(genres_field):
            if i + 6 < len(genres_field) and genres_field[i:i+6] == "'name'":
                # Found 'name', skip to the value
                i += 6
                while i < len(genres_field) and genres_field[i] != "'":
                    i += 1
                i += 1  # Skip opening quote
                
                # Extract genre name
                genre_name = ""
                while i < len(genres_field) and genres_field[i] != "'":
                    genre_name += genres_field[i]
                    i += 1
                
                if genre_name:
                    genres.append(genre_name)
            else:
                i += 1
        
        return ",".join(genres) if genres else ""
    
    def _extract_year(self, release_date: str):
        # Extract year from date string "1995-10-30"
        if not release_date or len(release_date) < 4:
            return 0
        
        year_str = ""
        for i in range(4):
            if i < len(release_date):
                year_str += release_date[i]
        
        try:
            return int(year_str)
        except:
            return 0
    
    ## Movie Loading
    
    def load_movies(self, filepath: str):
        # Load movies from metadata CSV
        # Returns HashMap: movie_id -> Movie object
        
        lines = self._read_file_lines(filepath)
        if lines is None:
            return None
        
        movies = HashMap()
        
        # Column indices based on the CSV header:
        # 0: adult, 1: belongs_to_collection, 2: budget, 3: genres, 4: homepage, 
        # 5: id, 6: imdb_id, 7: original_language, 8: original_title, 9: overview,
        # 10: popularity, 11: poster_path, 12: production_companies, 13: production_countries,
        # 14: release_date, 15: revenue, 16: runtime, 17: spoken_languages, 18: status,
        # 19: tagline, 20: title, 21: video, 22: vote_average, 23: vote_count
        
        # Skip header line
        for i in range(1, len(lines)):
            line = lines[i]
            if not line:
                continue
            
            fields = self._parse_csv_line(line)
            
            try:
                movie_id = fields[5] if len(fields) > 5 else ""  # id column
                imdb_id = fields[6] if len(fields) > 6 else ""   # imdb_id column
                title = fields[20] if len(fields) > 20 else "Unknown"  # title column
                release_date = fields[14] if len(fields) > 14 else ""  # release_date column
                year = self._extract_year(release_date)
                genres_raw = fields[3] if len(fields) > 3 else ""  # genres column
                genres = self._extract_genres(genres_raw)
                
                # Parse rating and revenue
                rating_str = fields[22] if len(fields) > 22 else "0"
                revenue_str = fields[15] if len(fields) > 15 else "0"
                
                try:
                    rating = float(rating_str) if rating_str else 0.0
                except:
                    rating = 0.0
                
                try:
                    revenue = float(revenue_str) if revenue_str else 0.0
                except:
                    revenue = 0.0
                
                # Create Movie object
                movie = Movie(
                    title=title,
                    year=year,
                    runtime=0,  # Ignoring runtime
                    genres=genres,
                    director="",  # Not in this dataset
                    actors="",  # Will be populated later
                    rating=rating,
                    revenue=revenue,
                    imdb_id=imdb_id
                )
                
                # Use the numeric id as key
                movies.put(movie_id, movie)
                
            except Exception as e:
                print(f"Error parsing movie line {i}: {e}")
                continue
        
        print(f"Loaded {movies.size()} movies")
        return movies
    
    ## Actor Loading
    
    def load_actors(self, filepath: str):
        # Load actors from cleaned_actors CSV
        # Returns HashMap: movie_id -> comma-separated actor names
        
        lines = self._read_file_lines(filepath)
        if lines is None:
            return None
        
        movie_to_actors = HashMap()
        
        # Skip header line
        for i in range(1, len(lines)):
            line = lines[i]
            if not line:
                continue
            
            fields = self._parse_csv_line(line)
            
            # Parse actor fields: movie_id, actor_id, actor_name, character_name
            try:
                movie_id = fields[0] if len(fields) > 0 else ""
                actor_name = fields[2] if len(fields) > 2 else ""
                
                if not movie_id or not actor_name:
                    continue
                
                # Add actor to movie's actor list
                if movie_to_actors.contains(movie_id):
                    existing = movie_to_actors.get(movie_id)
                    movie_to_actors.put(movie_id, existing + "," + actor_name)
                else:
                    movie_to_actors.put(movie_id, actor_name)
                    
            except Exception as e:
                print(f"Error parsing actor line {i}: {e}")
                continue
        
        print(f"Loaded actors for {movie_to_actors.size()} movies")
        return movie_to_actors
    
    ## Update Movie Objects with Actors
    
    def add_actors_to_movies(self, movies: HashMap, movie_to_actors: HashMap):
        # Update Movie objects with their actors string
        
        all_movie_ids = movies.get_all_keys()
        
        for i in range(len(all_movie_ids)):
            movie_id = all_movie_ids[i]
            
            if movie_to_actors.contains(movie_id):
                actors_string = movie_to_actors.get(movie_id)
                movie = movies.get(movie_id)
                movie.set_actors(actors_string)
        
        print("Updated movies with actor information")
    
    ## Title Index Builder
    
    def build_title_index(self, movies: HashMap):
        # Build a title -> movie_id HashMap for quick title lookups
        
        title_to_id = HashMap()
        all_movie_ids = movies.get_all_keys()
        
        for i in range(len(all_movie_ids)):
            movie_id = all_movie_ids[i]
            movie = movies.get(movie_id)
            title = movie.get_title()
            title_to_id.put(title, movie_id)
        
        print(f"Built title index with {title_to_id.size()} entries")
        return title_to_id