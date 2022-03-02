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

    # For cycle for getting the movies
    for index in range(len(top250)):

        # Index only goes from 0 to 19 and that gives only TOP 20 movie
        if index <= 19:
            movie = top250[index]

            # Getting the movie title, rating, and vote
            title = movie.get('title')
            rating = movie.get('rating')
            votes = movie.get('votes')

            # This variable for counting the oscars won by the movie
            oscars = 0
