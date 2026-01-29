# Ask the user to enter their favorite movies in one line, separated by commas
# (for example: "Inception, Titanic, Avatar").
# Use split(',') to turn the input into a list
# Remove extra spaces around each movie title
# Print the movie titles joined by " - " using join()

favorite_movies = input("Enter your favorite movies, separated by commas:")

movies = favorite_movies.split(",")

clean_movies = []
for movie in movies:
    clean_movies.append(movie.strip())

result = " | ".join(clean_movies)
print(result.title())
