import json

# initialize empty dictionary for storing movie data
movie_database = {}

# Function to add a new movie to the database
def add_movie():
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the name of the director: ")
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
    actors = input("Enter the names of the actors (separated by commas): ")
    actors_list = actors.split(", ")
    
    movie_database[title] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }
    
    print(f"{title} has been added to the database.")

# Function to edit an existing movie in the database
def edit_movie():
    title = input("Enter the movie title to edit: ")
    if title in movie_database:
        print(f"Current information for {title}:")
        print(json.dumps(movie_database[title], indent=4))
        
        # Prompt user for updated information
        genre = input("Enter the movie genre (or press Enter to keep current value): ")
        director = input("Enter the name of the director (or press Enter to keep current value): ")
        release_date = input("Enter the release date of the movie (YYYY-MM-DD) (or press Enter to keep current value): ")
        actors = input("Enter the names of the actors (separated by commas) (or press Enter to keep current value): ")
        actors_list = actors.split(", ")
        
        # Update the dictionary with the new information
        if genre:
            movie_database[title]["genre"] = genre
        if director:
            movie_database[title]["director"] = director
        if release_date:
            movie_database[title]["release_date"] = release_date
        if actors:
            movie_database[title]["actors"] = actors_list