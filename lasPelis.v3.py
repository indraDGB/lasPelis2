import requests
from io import BytesIO
from PIL import Image
from rich import print
from rich.table import Table
from rich.console import Console

# función para buscar películas por título
def search_movies_by_title(title, api_key, param, type):
    url = f"http://www.omdbapi.com/?apikey={api_key}&{param}={title}&type={type}"
    response = requests.get(url)
    return response.json()

# función para mostrar la información y el poster de una película
def show_movie_info(movie):
    print(f"[bold]Title:[/bold] {movie['Title']}")
    print(f"[bold]Year:[/bold] {movie['Year']}")
    print(f"[bold]Type:[/bold] {movie['Type']}")
    print(f"[bold]Plot:[/bold] {movie['Plot']}")
    print(f"[bold]Director:[/bold] {movie['Director']}")

    # obtener la imagen del cartel de la película
    response = requests.get(movie['Poster'])
    img = Image.open(BytesIO(response.content))

    # mostrar la imagen del cartel de la película
    img.show()

# clave de API de OMDB
api_key = "ff6a6fc6"
param = 's'

# buscar películas por título
movie_title = input("Introduce el título de la película que deseas buscar: ")
movies_by_title = search_movies_by_title(movie_title, api_key, param, 'movie')

if movies_by_title['Response'] == 'False':
    print('[red]No se encontraron resultados[/red]')
else:
    movies = movies_by_title['Search']
    print('[bold]Resultados de la búsqueda:[/bold]')
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("No.")
    table.add_column("Título")
    table.add_column("Año")

    for i, movie in enumerate(movies):
        table.add_row(str(i+1), movie['Title'], movie['Year'])

    console = Console()
    console.print(table)
    print()

    # pedir al usuario que seleccione una película
    while True:
        param = 't'
        try:
            selection = int(input("Selecciona una película para ver más información (introduce el número correspondiente): "))

            if selection < 1 or selection > len(movies):
                raise ValueError
            break
        except ValueError:
            print("Introduce un número válido")

    # mostrar la información y el poster de la película seleccionada
    movie = movies[selection-1]
    movie_info = search_movies_by_title(movie['Title'], api_key, param, 'movie')
    show_movie_info(movie_info)
