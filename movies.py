import requests
import json

# Problem 1
def list_of_popular_movies_by_vote_average():
  # get API and make request (no year parametr in API documentation)
  popular_movie_api = 'https://api.themoviedb.org/3/movie/popular?api_key=e2ebf69d07d1c0ac3760bf3aa16b2cd6&language=en-US'
  data = requests.get(popular_movie_api)
  data = data.json()

  vote_average_list = []
  for i in range(20):
    # Parse JSON for all vote_average values
    vote_average = data['results'][i]['vote_average']
    # append each value to a list
    vote_average_list.append(vote_average)

  # sort list by high -> low vote_average
  vote_average_list.sort()
  vote_average_list.reverse()

  popular_movies = []

  # get movie title for each corresponding vote average
  for num in vote_average_list:
    for i in range(20):
      if (data['results'][i]['vote_average'] == num):
        popular_movies.append(data['results'][i]['title'])

  # print the top 5 movies (first 5 in the list)
  print("The 5 most popular movies right now are: ", popular_movies[:5])



def most_successful_actor_by_revenue():
  # get all data (100 movies/5 pages)
  page_1_data = requests.get('https://api.themoviedb.org/3/discover/movie',
                        params = {
                            'api_key':'e2ebf69d07d1c0ac3760bf3aa16b2cd6',
                            'language':'en-US',
                            'sort_by':'revenue.desc',
                            'include_adult':'false',
                            'include_video':'false',
                            'page': 1}).json()
  
  page_2_data = requests.get('https://api.themoviedb.org/3/discover/movie',
                        params = {
                            'api_key':'e2ebf69d07d1c0ac3760bf3aa16b2cd6',
                            'language':'en-US',
                            'sort_by':'revenue.desc',
                            'include_adult':'false',
                            'include_video':'false',
                            'page': 2}).json()
  
  page_3_data = requests.get('https://api.themoviedb.org/3/discover/movie',
                        params = {
                            'api_key':'e2ebf69d07d1c0ac3760bf3aa16b2cd6',
                            'language':'en-US',
                            'sort_by':'revenue.desc',
                            'include_adult':'false',
                            'include_video':'false',
                            'page': 3}).json()
  
  page_4_data = requests.get('https://api.themoviedb.org/3/discover/movie',
                        params = {
                            'api_key':'e2ebf69d07d1c0ac3760bf3aa16b2cd6',
                            'language':'en-US',
                            'sort_by':'revenue.desc',
                            'include_adult':'false',
                            'include_video':'false',
                            'page': 4}).json()
  
  page_5_data = requests.get('https://api.themoviedb.org/3/discover/movie',
                        params = {
                            'api_key':'e2ebf69d07d1c0ac3760bf3aa16b2cd6',
                            'language':'en-US',
                            'sort_by':'revenue.desc',
                            'include_adult':'false',
                            'include_video':'false',
                            'page': 5}).json()

  data = page_1_data, page_2_data, page_3_data, page_4_data, page_5_data
  
  # create list of actor names
  actor_names = []
  # append top 5 stars of each movie to actor_names
  for page_num in range(4):
    for movie in data[page_num]['results']:
      id = movie['id']
      try:
        movie_credits = requests.get('https://api.themoviedb.org/3/movie/{}/credits?api_key=e2ebf69d07d1c0ac3760bf3aa16b2cd6&language=en-US'.format(id)).json()
        actor_names.append(movie_credits['cast'][0]['name'])
        actor_names.append(movie_credits['cast'][1]['name'])
        actor_names.append(movie_credits['cast'][2]['name'])
        actor_names.append(movie_credits['cast'][3]['name'])
        actor_names.append(movie_credits['cast'][4]['name'])
      except IndexError:
        actor_names = actor_names

  # identify actor in greatest number of films. 
  most_successful_actor = max(set(actor_names), key = actor_names.count)
  num_of_films = actor_names.count(most_successful_actor)
  print("Most successful actor by revenue is:", most_successful_actor, "and he/she has acted in", num_of_films, "top 100 films.")

list_of_popular_movies_by_vote_average()
most_successful_actor_by_revenue()
