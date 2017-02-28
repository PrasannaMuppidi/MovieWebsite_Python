import webbrowser                                                                       #importing webbrowser for the youtube trailer of the instances to play
class Movie():                                                                          #Creating a new class named Movie
    """ This is regarding a movie website. This website displays a                      
        list of my favorite movies and the trailer gets played when
        the user clicks on the movie poster """                                         #Doc for the class                           
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):    #initalizing the class. Whenever the class Movie is used, __init__ gets called
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):                                                             #Function to show the trailer when the user clicks on the movie
        trailer = webbrowser.open(self.trailer_youtube_url)
