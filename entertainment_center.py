import media
import fresh_tomatoes

#Creating an instance toy_story using the python module media and its class Movie
toy_story = media.Movie("Toy story",                                                         
                        "A story of a boy and his toys that have life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Creating an instance avatar using the python module media and its class Movie
avatar = media.Movie("Avatar",                                                               
                     "Some weird avatar story",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#Creating an instance eat_pray_love using the python module media and its class Movie
eat_pray_love = media.Movie("Eat Pray Love",                                                
                            "Story about love and travel",
                            "https://upload.wikimedia.org/wikipedia/en/7/7e/Eat_pray_love_ver2.jpg",
                            "https://www.youtube.com/watch?v=mjay5vgIwt4")

#Creating an instance lion using the python module media and its class Movie
lion = media.Movie("Lion",                                                                  
                   "An adopted boy finding his biological parents in India",
                   "https://upload.wikimedia.org/wikipedia/en/d/d5/Lion_2016_Poster.jpg",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")

#Creating an instance the_blind_side using the python module media and its class Movie
the_blind_side = media.Movie("The Blind Side",                                              
                            "Story about a big boy finding a new family",
                            "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                            "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

#Creating an instance the_notebook using the python module media and its class Movie
the_notebook = media.Movie("The Notebook",                                                  
                           "Lovestory",
                           "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
                           "https://www.youtube.com/watch?v=4M7LIcH8C9U")

#listing out all the movies into a single list
movies = [toy_story, avatar, eat_pray_love, lion, the_blind_side, the_notebook]

#printing out the movies list
fresh_tomatoes.open_movies_page(movies)                                                     

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.show_trailer.__doc__)
#print(media.Movie.__init__.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
                           


