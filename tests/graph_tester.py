'''
Movie Database Project - Graph Testing Script

Description: Test actor graph building and BFS with small dataset

@Author: Ian MacCabe
@Contact: ian.maccabe@temple.edu    
@Date: [Your Date]

Sources: 
    Small test datasets
'''

import sys
sys.path.append('../src')

from parse_data import DataParser
from graph import ActorGraph

def setup_complete_graph():
    '''Helper function to set up a complete graph with all data'''
    
    # Load data
    parser = DataParser()
    movies = parser.load_movies("../data/movie_data_small.csv")
    movie_to_actors = parser.load_actors("../data/actor_data_small.csv")
    
    if movies is None or movie_to_actors is None:
        return None, None, None
    
    # Update movies with actors
    parser.add_actors_to_movies(movies, movie_to_actors)
    
    # Build title index
    title_to_id = parser.build_title_index(movies)
    
    # Create graph
    graph = ActorGraph()
    
    # Add movies to graph
    all_movie_ids = movies.get_all_keys()
    for i in range(len(all_movie_ids)):
        movie_id = all_movie_ids[i]
        movie = movies.get(movie_id)
        graph.add_movie(movie)
    
    # Set the internal data structures that graph needs
    graph._movies = movies
    graph._title_to_id = title_to_id
    graph._ActorGraph__movie_to_actors = movie_to_actors
    
    # Build the actor graph
    all_movie_ids = movie_to_actors.get_all_keys()
    for i in range(len(all_movie_ids)):
        movie_id = all_movie_ids[i]
        actors_string = movie_to_actors.get(movie_id)
        movie = movies.get(movie_id)
        if movie:
            movie_title = movie.get_title()
            graph._connect_actors_in_movie(movie_title, actors_string)
    
    return graph, movies, movie_to_actors

def test_graph_building():
    '''Test building the actor graph from small dataset'''
    
    print("=" * 60)
    print("TEST 1: Building Actor Graph")
    print("=" * 60)
    
    graph, movies, movie_to_actors = setup_complete_graph()
    
    if graph is None:
        print("FAILED: Could not build graph")
        return None, None
    
    print(f"\nAdded {movies.size()} movies to graph")
    print("Actor graph built successfully!")
    
    return graph, movies

def test_actor_connections():
    '''Test finding connections between actors'''
    
    print("\n" + "=" * 60)
    print("TEST 2: Actor Connections")
    print("=" * 60)
    
    graph, movies = test_graph_building()
    
    if graph is None:
        print("FAILED: Could not build graph")
        return
    
    # Test with actors from Toy Story (if it's in your dataset)
    actor1 = "Tom Hanks"
    actor2 = "Tim Allen"
    
    print(f"\nFinding connection between '{actor1}' and '{actor2}'...")
    
    movies_connection = graph.get_connection_movies(actor1, actor2)
    
    if movies_connection:
        print(f"Direct connection found!")
        print(f"  Shared movies: {movies_connection}")
    else:
        print(f"No direct connection found")

def test_shortest_path():
    '''Test BFS shortest path between actors'''
    
    print("\n" + "=" * 60)
    print("TEST 3: Shortest Path (BFS)")
    print("=" * 60)
    
    graph, movies = test_graph_building()
    
    if graph is None:
        print("FAILED: Could not build graph")
        return
    
    # Test actors - adjust these based on what's in your small dataset
    actor1 = "Tom Hanks"
    actor2 = "Tim Allen"
    
    print(f"\nFinding shortest path from '{actor1}' to '{actor2}'...")
    
    path = graph.find_shortest_path(actor1, actor2)
    
    if path:
        graph.display_path(path)
    else:
        print("No path found between these actors")
    
    # Try another pair if you have more movies
    print("\n" + "-" * 60)
    actor3 = "Tom Hanks"
    actor4 = "Don Rickles"
    
    print(f"\nFinding shortest path from '{actor3}' to '{actor4}'...")
    
    path2 = graph.find_shortest_path(actor3, actor4)
    
    if path2:
        graph.display_path(path2)
    else:
        print("No path found between these actors")

def test_find_movie_by_title():
    '''Test Query 1: Find movie by title'''
    
    print("\n" + "=" * 60)
    print("TEST 4: Find Movie by Title")
    print("=" * 60)
    
    graph, movies, movie_to_actors = setup_complete_graph()
    
    if graph is None:
        print("FAILED: Could not build graph")
        return
    
    test_title = "Toy Story"
    print(f"\nSearching for: '{test_title}'")
    
    movie = graph.find_movie_by_title(test_title)
    
    if movie:
        print(f"\nFound movie:")
        print(f"  Title: {movie.get_title()}")
        print(f"  Year: {movie.get_year()}")
        print(f"  Genres: {movie.get_genres()}")
        print(f"  Rating: {movie.get_rating()}")
        print(f"  Actors: {movie.get_actors()[:100]}...")  # Truncate long actor lists
    else:
        print(f"Movie '{test_title}' not found")

def test_find_movies_by_actor():
    '''Test Query 2: Find movies by actor'''
    
    print("\n" + "=" * 60)
    print("TEST 5: Find Movies by Actor")
    print("=" * 60)
    
    graph, movies, movie_to_actors = setup_complete_graph()
    
    if graph is None:
        print("FAILED: Could not build graph")
        return
    
    actor_name = "Tom Hanks"
    print(f"\nSearching for movies with: '{actor_name}'")
    
    actor_movies = graph.find_movies_by_actor(actor_name)
    
    if actor_movies and len(actor_movies) > 0:
        print(f"\nFound {len(actor_movies)} movie(s):")
        for i in range(len(actor_movies)):
            movie = actor_movies[i]
            print(f"\n  {i+1}. {movie.get_title()} ({movie.get_year()})")
            print(f"     Rating: {movie.get_rating()}")
            print(f"     Genres: {movie.get_genres()}")
    else:
        print(f"No movies found for '{actor_name}'")

def run_all_tests():
    '''Run all graph tests'''
    
    print("\n" + "=" * 60)
    print("ACTOR GRAPH - TESTING SUITE")
    print("=" * 60)
    
    test_graph_building()
    test_actor_connections()
    test_shortest_path()
    test_find_movie_by_title()
    test_find_movies_by_actor()
    
    print("\n" + "=" * 60)
    print("ALL GRAPH TESTS COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tests()