import media                                                                                 #importing the python module media into this python file
import fresh_tomatoes                                                                        #importing the python module fresh_tomatoes into this python file
toy_story = media.Movie("Toy story",                                                         #Creating an instance toy_story using the python module media and its class Movie
                        "A story of a boy and his toys that have life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",                                                               #Creating an instance avatar using the python module media and its class Movie
                     "Some weird avatar story",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

eat_pray_love = media.Movie("Eat Pray Love",                                                #Creating an instance eat_pray_love using the python module media and its class Movie
                            "Story about love and travel",
                            "https://upload.wikimedia.org/wikipedia/en/7/7e/Eat_pray_love_ver2.jpg",
                            "https://www.youtube.com/watch?v=mjay5vgIwt4")

lion = media.Movie("Lion",                                                                  #Creating an instance lion using the python module media and its class Movie
                   "An adopted boy finding his biological parents in India",
                   "https://upload.wikimedia.org/wikipedia/en/d/d5/Lion_2016_Poster.jpg",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")

the_blind_side = media.Movie("The Blind Side",                                              #Creating an instance the_blind_side using the python module media and its class Movie
                            "Story about a big boy finding a new family",
                            "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                            "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

the_notebook = media.Movie("The Notebook",                                                  #Creating an instance the_notebook using the python module media and its class Movie
                           "Lovestory",
                           "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
                           "https://www.youtube.com/watch?v=4M7LIcH8C9U")
movies = [toy_story, avatar, eat_pray_love, lion, the_blind_side, the_notebook]             #listing out all the movies into a single list

fresh_tomatoes.open_movies_page(movies)                                                     #printing out the movies list

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
                           


