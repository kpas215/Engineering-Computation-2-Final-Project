'''
Movie Database Project - Testing Script

Description: Test data loading and parsing with small dataset

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    Small test datasets
'''

import sys
sys.path.append('../src')

from parse_data import DataParser
from hash_map import HashMap

def test_movie_loading():
    '''Test loading movies from small dataset'''
    
    print("=" * 60)
    print("TEST 1: Loading Movies")
    print("=" * 60)
    
    parser = DataParser()
    movies = parser.load_movies("../data/movie_data_small.csv")
    
    if movies is None:
        print("FAILED: Could not load movies")
        return None
    
    print(f"\nSuccess! Loaded {movies.size()} movies")
    print("\nSample movies:")
    
    # Display first few movies
    all_ids = movies.get_all_keys()
    for i in range(min(5, len(all_ids))):
        movie_id = all_ids[i]
        movie = movies.get(movie_id)
        print(f"\nMovie ID: {movie_id}")
        print(f"  Title: {movie.get_title()}")
        print(f"  Year: {movie.get_year()}")
        print(f"  Genres: {movie.get_genres()}")
        print(f"  Rating: {movie.get_rating()}")
        print(f"  Revenue: {movie.get_revenue()}")
    
    return movies

def test_actor_loading():
    '''Test loading actors from small dataset'''
    
    print("\n" + "=" * 60)
    print("TEST 2: Loading Actors")
    print("=" * 60)
    
    parser = DataParser()
    movie_to_actors = parser.load_actors("../data/actor_data_small.csv")
    
    if movie_to_actors is None:
        print("FAILED: Could not load actors")
        return None
    
    print(f"\nSuccess! Loaded actors for {movie_to_actors.size()} movies")
    print("\nSample actor listings:")
    
    # Display first few movie-actor mappings
    all_movie_ids = movie_to_actors.get_all_keys()
    for i in range(min(3, len(all_movie_ids))):
        movie_id = all_movie_ids[i]
        actors = movie_to_actors.get(movie_id)
        print(f"\nMovie ID: {movie_id}")
        print(f"  Actors: {actors}")
    
    return movie_to_actors

def test_integration():
    '''Test integrating movies with actors'''
    
    print("\n" + "=" * 60)
    print("TEST 3: Integration - Adding Actors to Movies")
    print("=" * 60)
    
    parser = DataParser()
    
    # Load both datasets
    movies = parser.load_movies("../data/movie_data_small.csv")
    movie_to_actors = parser.load_actors("../data/actor_data_small.csv")
    
    if movies is None or movie_to_actors is None:
        print("FAILED: Could not load data")
        return
    
    # Add actors to movies
    parser.add_actors_to_movies(movies, movie_to_actors)
    
    print("\nVerifying integration:")
    all_ids = movies.get_all_keys()
    for i in range(min(3, len(all_ids))):
        movie_id = all_ids[i]
        movie = movies.get(movie_id)
        print(f"\nMovie: {movie.get_title()}")
        print(f"  Actors: {movie.get_actors()}")

def test_title_index():
    '''Test building title index'''
    
    print("\n" + "=" * 60)
    print("TEST 4: Building Title Index")
    print("=" * 60)
    
    parser = DataParser()
    movies = parser.load_movies("../data/movie_data_small.csv")
    
    if movies is None:
        print("FAILED: Could not load movies")
        return
    
    # Build title index
    title_to_id = parser.build_title_index(movies)
    
    print("\nTesting title lookups:")
    
    # Try to find "Toy Story"
    test_title = "Toy Story"
    if title_to_id.contains(test_title):
        movie_id = title_to_id.get(test_title)
        movie = movies.get(movie_id)
        print(f"\nFound '{test_title}':")
        print(f"  ID: {movie_id}")
        print(f"  Year: {movie.get_year()}")
        print(f"  Rating: {movie.get_rating()}")
    else:
        print(f"\n'{test_title}' not found in index")

def test_hashmap_basic():
    '''Test basic HashMap functionality'''
    
    print("\n" + "=" * 60)
    print("TEST 5: HashMap Basic Operations")
    print("=" * 60)
    
    hash_map = HashMap()
    
    # Test put
    print("\nTesting put()...")
    hash_map.put("key1", "value1")
    hash_map.put("key2", "value2")
    hash_map.put("key3", "value3")
    print(f"Added 3 items. Size: {hash_map.size()}")
    
    # Test get
    print("\nTesting get()...")
    val = hash_map.get("key1")
    print(f"Get 'key1': {val}")
    
    # Test contains
    print("\nTesting contains()...")
    print(f"Contains 'key1': {hash_map.contains('key1')}")
    print(f"Contains 'key999': {hash_map.contains('key999')}")
    
    # Test get_all_keys
    print("\nTesting get_all_keys()...")
    keys = hash_map.get_all_keys()
    print(f"All keys: {keys}")
    
    # Test update
    print("\nTesting update (put existing key)...")
    hash_map.put("key1", "new_value1")
    val = hash_map.get("key1")
    print(f"Updated 'key1': {val}")

def run_all_tests():
    '''Run all tests'''
    
    print("\n" + "=" * 60)
    print("MOVIE DATABASE - TESTING SUITE")
    print("=" * 60)
    
    # Test HashMap basics first
    test_hashmap_basic()
    
    # Test data loading
    test_movie_loading()
    test_actor_loading()
    test_integration()
    test_title_index()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tests()