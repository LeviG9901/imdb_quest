from imdb import Cinemagoer


# Function for scraping the top 20 movie
def scrape():
    # Create an instance
    ia = Cinemagoer()

    # Get the top 250 movie from IMDB
    top250 = ia.get_top250_movies()

    # Creating the original top 250 movie list as empty list
    org_250 = []

    # Creating a movie dictionary
    # We will need the movie title, rating, votes, and number of how many oscar the movie won
    movie_dict = {'title': [], 'rating': [], 'votes': [], 'oscars': []}

    # For cycle for getting top20 movie
    # for index in range(len(top250)):
