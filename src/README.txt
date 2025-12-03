I have a question. How could we go about loading the data into different structures without creating duplicate entries?


🧱 Key idea: one “home” for each Movie

Make one primary place where movie objects live, e.g.:

class moviedatabase:
    def __init__(self):
        self._movies = []  # master list of ALL movie objects
        # indexes / structures:
        self._title_index = hashtable()   # title -> movie (or index)
        self._actor_index = hashtable()   # actor -> list of movies (or indices)
        self._genre_index = hashtable()   # genre -> list of movies
        self._rating_heap = maxheap()     # (rating, movie) pairs
        # graph, bloom filter, etc...


When you parse the CSV:

for row in csv_reader:
    m = movie(...parsed fields...)
    idx = len(self._movies)
    self._movies.append(m)

    # Now index it in other structures using the SAME object or its index:
    self._title_index.insert(m.get_title(), idx)          # or m
    for actor in m.get_actors():
        self._actor_index.add_to_list(actor, idx)         # or m
    for genre in m.get_genres():
        self._genre_index.add_to_list(genre, idx)         # or m

    self._rating_heap.push((m.get_rating(), idx))         # or (rating, m)


You’re not re-creating movies; you’re just reusing references or indices.