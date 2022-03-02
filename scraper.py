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

            # Awards for getting a list of the movie awards
            awards = ia.get_movie(movie.getID(), info=['awards']).get('awards', [])

            # For cycle to get the number of oscars won for every movie
            for index2 in range(len(awards)):
                if awards[index2]['award'] == 'Oscar' and awards[index2]['result'] == 'Winner':
                    oscars += 1

            # Print out the movie with it's details
            print("\n", movie.get('title'), "\nRating: ", movie.get('rating'), "\tVotes: ", movie.get('votes'),
                  "\tOscars: ", oscars)
