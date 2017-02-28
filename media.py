import webbrowser

#Creating a new class
class Movie():
    #Doc for the class
    """ This is regarding a movie website. This website displays a                      
        list of my favorite movies and the trailer gets played when
        the user clicks on the movie poster """                                                                    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #initalizing the class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #Doc for the function __init__
        """ This function __init__ takes as input the title of the movie,
            the storyline, the poster image and the youtube trailer url
            and initalizes the variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #Function to show the trailer when the user clicks on the movie
    def show_trailer(self):
        #Doc for the function show_trailer
        """ This function show_trailer takes as input the youtube trailer url
            and shows the trailer when the user clicks the poster of a movie"""
        trailer = webbrowser.open(self.trailer_youtube_url)
