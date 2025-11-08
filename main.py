# Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Fix file path issues when running as .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Folder used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

csv_path = resource_path('rotten_tomatoes_movies.csv')
movieData = pd.read_csv(csv_path)


pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

favMovie = "Little Shop of Horrors"

print("My favorite movie is " + favMovie)

# Part 3 Investigate the data
# print(movieData.head())
# print(movieData["movie_title"])

# Part 4 Filter data
print("\nThe data for my favorite movie is:\n")

# Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
favMovieData = movieData.loc[favMovieBooleanList]

print(favMovieData)
print("\n\n")

# Create a new variable to store a new data set with a certain genre
horrorMovieBooleanList = movieData["genres"].str.contains("Horror", case=False, na=False)
horrorMovieData = movieData.loc[horrorMovieBooleanList]

numOfMovies = horrorMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Horror in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Horror.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Part 5 Describe data
# find min
min = horrorMovieData['audience_rating'].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 68 points higher than the lowest rated movie.")
print()

# find max
max = horrorMovieData['audience_rating'].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 10 points lower than the highest rated movie.")
print()

# find mean
mean = horrorMovieData['audience_rating'].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

# find median
median = horrorMovieData['audience_rating'].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Part 6 Create graphs
# Create histogram
plt.hist(horrorMovieData["audience_rating"], range=(0, 120), bins=20)

# Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Horror Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Horror Movies")

# Prints interpretation of histogram
print("According to the histogram, most horror movies had an audience rating between 70 and 80.")
print("Close the graph by pressing the 'X' in the top right corner.\n")

# Show histogram
plt.show()

# Create scatterplot
plt.scatter(data=horrorMovieData, x="audience_rating", y="critic_rating")

# Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 110)
plt.ylim(0, 110)

# Prints interpretation of scatterplot
print("According to the scatter plot, Critic Ratings increase as Audience Ratings increase.\n")
print("Close the graph by pressing the 'X' in the top right corner.")

# Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
