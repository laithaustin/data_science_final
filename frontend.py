# Frontend:
# 1. Survey + (backend stuff), what genres you like, how are you feeling, etc
# 2. X Suggestions
# 3. User either redoes suggestions or picks a movie to watch
# 4. Prompt user for feedback on the movie + (backend stuff)
# 5. x Suggestions
# 6. back to 3

# the goal here is to create a frontend that asks the user a series of questions and then iteratively gives them movie suggestions
# the user can then give feedback on the suggestions and the frontend will give them new suggestions based on their feedback
# our base set of questions will be: what genres do you like, how are you feeling, what are your 3 favorite movies, what 3 movies have you seen
# recently, get users to rate 3 random movies, favorite actor/actress, favorite director, runtime preference, favorite decade

# frontend is going to just be in command line for now, we can make it a web app later

import os
import sys
import random
import pandas as pd
import numpy as np

class User:
    def __init__(self, name):
        self.name = name
        self.genre_preferences = []
        self.mood = ""
        self.favorite_movies = []
        self.recent_movies = []
        self.ratings = []
        self.favorite_actor = ""
        self.favorite_director = ""
        self.runtime_preference = ""
        self.favorite_decade = ""

    def add_genre_preference(self, genre):
        self.genre_preferences.append(genre)

    def add_favorite_movie(self, movie):
        self.favorite_movies.append(movie)

    def add_recent_movie(self, movie):
        self.recent_movies.append(movie)

    def add_rating(self, rating):
        self.ratings.append(rating)

    def set_favorite_actor(self, actor):
        self.favorite_actor = actor

    def set_favorite_director(self, director):
        self.favorite_director = director

    def set_runtime_preference(self, runtime):
        self.runtime_preference = runtime

    def set_favorite_decade(self, decade):
        self.favorite_decade = decade

    def get_name(self):
        return self.name

    def get_genre_preferences(self):
        return self.genre_preferences

    def get_mood(self):
        return self.mood

    def get_favorite_movies(self):
        return self.favorite_movies

    def get_recent_movies(self):
        return self.recent_movies

    def get_ratings(self):
        return self.ratings

    def get_favorite_actor(self):
        return self.favorite_actor

    def get_favorite_director(self):
        return self.favorite_director

    def get_runtime_preference(self):
        return self.runtime_preference

    def get_favorite_decade(self):
        return self.favorite_decade

def random_sample():
    # load in the movie data and randomly sample 3 movies
    # load data from filtered_data.csv
    df = pd.read_csv("filtered_data.csv")
    movies = df["title"].tolist()
    release_date = df["release_date"].tolist()
    random_samples = random.sample(list(zip(movies, release_date)), 3)
    random_movies = [movie[0] for movie in random_samples]
    random_release_date = [movie[1] for movie in random_samples]
    return random_movies, random_release_date

def get_suggestions(user):
    # TODO: for now just print out random movies
    return [movie for movie in random_sample()[0]]
    

def main():
    print("Welcome to the Movie Recommender System!")
    print("To get started, please enter your name: ")
    name = input()
    print("Hello " + name + "!")
    # create a user object here
    user = User(name)

    print("To start. What are your favorite genres? (Separate each genre with a comma)")
    genres = input().split(",")
    for genre in genres:
        user.add_genre_preference(genre)


    print("How are you feeling today?")
    mood = input()
    user.mood = mood

    print("What are your 3 favorite movies? (Separate each movie with a comma)")
    favorite_movies = input()
    favorite_movies = favorite_movies.split(",")
    for movie in favorite_movies:
        user.add_favorite_movie(movie)
    
    print("What are 3 movies you've seen recently? (Separate each movie with a comma, in ascending order of recency)")
    recent_movies = input()
    recent_movies = recent_movies.split(",")
    for movie in recent_movies:
        user.add_recent_movie(movie)
    
    print("Please rate the following movies on a scale of 1-5 (1 being the worst, 5 being the best)")
    movies, release_date = random_sample()
    for movie, release_date in zip(movies, release_date):
        print(movie + " (" + release_date + ")")
        rating = input()
        user.add_rating([movie, release_date, rating])
    
    print("Who is your favorite actor?")
    actor = input()
    user.set_favorite_actor(actor)

    print("Who is your favorite director?")
    director = input()
    user.set_favorite_director(director)

    print("What is your preferred runtime? (Enter 'short', 'medium', or 'long')")
    runtime = input()
    user.set_runtime_preference(runtime)

    print("What is your favorite decade? (Enter '60s' - '10s')")
    decade = input()
    user.set_favorite_decade(decade)

    print("Thank you for your input! Here are some movie suggestions based on your preferences:")
    suggestions = get_suggestions(user)
    for suggestion in suggestions:
        print(suggestion)
    
    print("Would you like to update your movie ratings? (Enter 'yes' or 'no')")
    update = input()
    while update == "yes":
        print("What movie did you watch and how did you like it? (Enter 'movie, rating' and 'done' when finished)")
        movie, rating = input().split(",")
        user.add_rating([movie, rating])

        print("New suggestions:")
        suggestions = get_suggestions(user)
        for suggestion in suggestions:
            print(suggestion)
        
        print("Would you like to update your movie ratings? (Enter 'yes' or 'no')")
        update = input()
        if update == "no":
            break
    
    print("Thank you for using the Movie Recommender System!")

if __name__ == "__main__":
    main()







    
