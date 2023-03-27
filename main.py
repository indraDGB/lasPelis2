import requests

# función para buscar películas por título
def search_movies_by_title(title, api_key):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={title}&type=movie"
    response = requests.get(url)
    return response.json()

# función para buscar películas por año
def search_movies_by_year(query, api_key):
    url = f"http://www.omdbapi.com/?apikey={api_key}&y={query}&type=movie"
    response = requests.get(url)
    return response.json()

# clave de API de OMDB
api_key = "ff6a6fc6"

# buscar películas por título
movie_title = input("Introduce el título de la película que deseas buscar: ")
movies_by_title = search_movies_by_title(movie_title, api_key)
print(movies_by_title)

# buscar películas por año
movie_year = input("Introduce el año de lanzamiento de la película que deseas buscar: ")
movies_year = search_movies_by_year(movie_year, api_key)
print(movies_year)
