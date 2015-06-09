import webbrowser
class Movie():
    ''' This class provides a to store movie related information'''
    def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube,movie_rating,movie_desc,movie_director):
        '''This is a constructor of movie class and it gets called when memory for the object allocated
        The self parameter refers to the instance of the object
        title is an instance variable to store the title of the movie
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating=movie_rating
        self.movie_desc=movie_desc
        self.movie_director = movie_director
        
    def show_trailer(self):
        ''' show_trailer is an instance method to run the youutube movie trailer'''
        webbrowser.open(self.trailer_youtube_url)
# display docstring for help
help(Movie)
