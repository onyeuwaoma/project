# -*- coding: utf-8 -*-
"""

@author: Nnaemeka Onyeuwaoma (UKZN)
"""

# exercise 
import pandas as pd
movie = pd.read_csv("movie_dataset.csv")
movie2 = pd.read_csv("movie_dataset.csv")
print(movie)
print(movie.info())
print(movie.describe())

##### replacing the NAN with the average value of the column average
x= movie["Revenue (Millions)"].mean()
x1= movie["Metascore"].mean()
movie["Revenue (Millions)"].fillna(x, inplace = True)
movie["Metascore"].fillna(x1, inplace = True)
print(movie)
###### droping NAN and reseting the data

movie2.dropna(inplace = True)
movie2 = movie2.reset_index(drop= True)
print(movie2)

"""
Assumption: I replaced the NAN with the mean of the respective cloumns where the appeared.
""" 

############# 1. What is the highest rated movie in the dataset?
movie['Rating'].max()
movie2['Rating'].max()
print(movie2.info())
print(movie.describe())

############# gives the row with the highest in a particular column
movie .nlargest(1,'Rating')

############### 2. What is the average revenue of all movies in the dataset?
x= movie["Revenue (Millions)"].mean()


############# 3. What is the average revenue of movies from 2015 to 2017 in the datase
rows_2015 = movie.loc[movie["Year"] == 2015]
rows_2016 = movie.loc[movie["Year"] == 2016]
rows_2017 = movie.loc[movie["Year"] == 2017]
print(rows_2017)
concate = pd.concat([rows_2015, rows_2016, rows_2017])
print(concate)
print(concate.describe())
aver_2015_2017 = concate['Revenue (Millions)'].mean()
print(aver_2015_2017)

################### 4. How many movies were released in the year 2016?
length_2016 = rows_2016['Year'].count()
print(length_2016)

############ 5. How many movies were directed by Christopher Nolan?
Christopher_Nolan = movie[movie["Director"] == "Christopher Nolan"]
length_Christopher_Nolan = Christopher_Nolan['Director'].count()
print(length_Christopher_Nolan)

############# 6. How many movies in the dataset have a rating of at least 8.0?
rating_8 = movie.loc[movie["Rating"] >= 8.0]
rate_count= rating_8['Rating'].count()
print(rate_count) 

############## 7. What is the median rating of movies directed by Christopher Nolan?
median_CN= Christopher_Nolan["Rating"].median()
print(median_CN)

################### 8. Find the year with the highest average rating?
year_rating= movie .nlargest(1,'Rating')
print(year_rating)

################### 9. What is the percentage increase in number of movies made between 2006 and 2016?
movie_2006 = movie.loc[movie["Year"] == 2006]
movie_2006_count = movie_2006['Year'].count()
movie_2016 = movie.loc[movie["Year"] == 2016]
movie_2016_count = movie_2016['Year'].count()
print(movie_2006_count)
print(movie_2016_count)
percentage_increase = (((movie_2016_count - movie_2006_count)/movie_2006_count)*100)
print(percentage_increase)


################### 10. Find the most common actor in all the movies?

actors = movie["Actors"].str.split(',') # split strings 
actors_sep1 = movie.explode("Actors") # Convert list into multiple rows
print(actors_sep1)
# Get count of duplicates in a single column using dataframe.pivot_table()
actors_count = actors_sep1.pivot_table(index = ['Actors'], aggfunc ='size')
print("Get count of duplicate values in a single column:\n", actors_count)
print("Get count of duplicate values in a single column:\n", actors_count)

##################### method 2

import pandas as pd
movie = pd.read_csv("movie_dataset.csv")

##### replacing the NAN with the average value of the column average
x= movie["Revenue (Millions)"].mean()
x1= movie["Metascore"].mean()
movie["Revenue (Millions)"].fillna(x, inplace = True)
movie["Metascore"].fillna(x1, inplace = True)
print(movie)
all_actors = [actors.split(',') for actors in movie['Actors']]
actors_sublist = [item.strip() for sublist in all_actors for item in sublist]

# Get the most common actor
most_common_actor = max(set(actors_sublist), key=actors_sublist.count)

# Display the most common actor
print("Most Common Actor:", most_common_actor)


##################### 11. How many unique genres are there in the dataset?
# Split the 'Genre' column by commas and create a list of all genres
all_genres = [genre.split(',') for genre in movie['Genre']]
genres_sublist = [item.strip() for sublist in all_genres for item in sublist]

# Get unique genres and count them
unique_genres = set(genres_sublist)
num_unique_genres = len(unique_genres)

# Display the unique genres and the count
print("Unique Genres:", unique_genres)
print("Number of Unique Genres:", num_unique_genres)



##################### 12. Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

from ydata_profiling import ProfileReport
profile=ProfileReport(movie,title="Rrofiling Report")
profile.to_file("correlation.html")















