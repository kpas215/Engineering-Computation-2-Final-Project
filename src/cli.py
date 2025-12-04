"""
cli.py
Command Line Interface for the Movie Database Project

Author: [Killian Slattery]
Date: [12/4/2025]

This CLI acts as the frontend for the Movie Database System.
It interacts with:
    - moviedatabase.py 
    - graph.py
    - sorting.py and heap.py for sorting and top-N queries


"""

from moviedatabase import moviedatabase       # Main database class
from graph import ActorGraph                  # BFS actor connection graph


def print_menu():
    
    # Display the list of available user commands
    # keep the CLI simple and readable
    print("============================================================")
    print("\n MOVIE DATABASE CLI\n")
    print("1.  Find movie by title")
    print("2.  Find movies by actor")
    print("3.  Top N movies by rating")
    print("4.  Top N movies by revenue")
    print("5.  Sort all movies by genre (Hybrid Sort)")
    print("6.  Find connection between two actors (Graph BFS)")
    print("7.  Suggest similar movies (skeleton)")
    print("8.  Quit")
    print("============================================================")


def load_all_data(db, graph):
    """
    Load all data required for this CLI to function.

    NOTE:
    - The MOVIEDATABASE loaddata() MUST populate:
        self.__movies
        title index
        heaps for rating + revenue
    - The GRAPH needs movie + actor CSVs to build connections.
      Since these are not implemented yet, we use skeleton hooks.
    """

    print("\n[1/2] Loading movie database...")
    try:
        db.loaddata()               # TODO: teammates implement CSV parsing here
        print("Movie database loaded successfully.")
    except Exception as e:
        print("Error loading movie database:", e)

    print("\n[2/2] Loading actor graph (optional if data not ready)...")
    try:
        # TODO: teammates must implement these graph functions
        # graph.load_movies("movies.csv")
        # graph.load_actors("cleaned_actors.csv")
        # graph.build_movie_index()
        # graph.build_actor_graph()

        print("Actor graph loaded successfully (or placeholder used).")
    except Exception as e:
        print("Graph loading skipped or failed:", e)

    # Attach graph to database for unified access
    db.link_actor_graph(graph)


def cli_loop():
    """
    The main loop of the CLI.
    Repeatedly asks the user for a choice and calls the appropriate
    MovieDatabase or ActorGraph function.
    """

    # Create core objects
    db = moviedatabase()    # main movie database
    graph = ActorGraph()    # actor BFS graph

    # Load all data (db + graph)
    load_all_data(db, graph)

    # Begin user interaction loop
    while True:
        print_menu()                            # Show commands
        choice = input("Enter your choice: ")    # Read user input

        # ---------------------------------------------
        # OPTION 1: FIND MOVIE BY TITLE
        # ---------------------------------------------
        if choice == "1":
            title = input("Enter the movie title: ")

            movie = db.find_movie_by_title(title)

            if movie is None:
                print("Movie not found.")
            else:
                print("\nTitle:", movie.get_title())
                print("Year:", movie.get_year())
                print("Genres:", movie.get_genres())
                print("Rating:", movie.get_rating())
                print("Revenue:", movie.get_revenue())

        # ---------------------------------------------
        # OPTION 2: FIND MOVIES BY ACTOR
        # ---------------------------------------------
        elif choice == "2":
            actor = input("Enter actor name: ")

            # This depends on your team's actor index.
            try:
                results = db.find_movies_by_actor(actor)
            except NotImplementedError:
                print("Actor search not implemented by team yet.")
                continue

            if not results:
                print("No movies found for this actor.")
            else:
                print("\nMovies with", actor + ":")
                for m in results:
                    print(" -", m.get_title())

        # ---------------------------------------------
        # OPTION 3: TOP N MOVIES BY RATING (max heap)
        # ---------------------------------------------
        elif choice == "3":
            try:
                n = int(input("How many top movies? "))
            except ValueError:
                print("Invalid number.")
                continue

            try:
                results = db.top_n_by_rating(n)
            except Exception as e:
                print("Top N by rating not available yet:", e)
                continue

            print("\nTop", n, "Movies by Rating:")
            for m in results:
                print(f"{m.get_rating():.1f} - {m.get_title()}")

        # ---------------------------------------------
        # OPTION 4: TOP N MOVIES BY REVENUE (max heap)
        # ---------------------------------------------
        elif choice == "4":
            try:
                n = int(input("How many top movies? "))
            except ValueError:
                print("Invalid number.")
                continue

            try:
                results = db.top_n_by_revenue(n)
            except Exception as e:
                print("Top N by revenue not available yet:", e)
                continue

            print("\nTop", n, "Movies by Revenue:")
            for m in results:
                print(f"${m.get_revenue():,.0f} - {m.get_title()}")

        # ---------------------------------------------
        # OPTION 5: SORT MOVIES BY GENRE (Hybrid Sort)
        # ---------------------------------------------
        elif choice == "5":
            print("\nSorting movies by genre using hybrid merge/insertion sort...")

            try:
                sorted_movies = db.sort_movies_by_genre()
            except Exception as e:
                print("Genre sorting not available yet:", e)
                continue

            print("\nFirst 50 Genre-Sorted Movies:")
            for m in sorted_movies[:50]:
                print(m.get_genres(), "-", m.get_title())

        # ---------------------------------------------
        # OPTION 6: ACTOR CONNECTION PATH (Graph BFS)
        # ---------------------------------------------
        elif choice == "6":
            a1 = input("Actor A: ")
            a2 = input("Actor B: ")

            try:
                path = db.find_actor_connection(a1, a2)
            except Exception as e:
                print("Graph search unavailable:", e)
                continue

            if path is None:
                print("No connection found.")
            else:
                print("\nConnection Path:")
                for i in range(len(path) - 1):
                    print("  ", path[i], "→", path[i+1])
                print("\nDegrees of separation:", len(path) - 1)

        # ---------------------------------------------
        # OPTION 7: SIMILAR MOVIES (Skeleton)
        # ---------------------------------------------
        elif choice == "7":
            title = input("Enter a movie title: ")

            # Teammates will implement logic later. 
            # Your placeholder prevents CLI from crashing.
            similar = db.suggest_similar_movies(title)

            if not similar:
                print("No similar movie suggestions implemented yet.")
            else:
                print("\nSuggested Similar Movies:")
                for m in similar:
                    print(" -", m.get_title())

        # ---------------------------------------------
        # OPTION 8: QUIT
        # ---------------------------------------------
        elif choice == "8":
            print("Exiting Movie Database. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# =============================================
# Run CLI if file executed directly.
# =============================================
if __name__ == "__main__":
    cli_loop()