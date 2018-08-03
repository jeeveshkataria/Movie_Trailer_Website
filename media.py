import webbrowser
" webbrowser is used to play the trailer of movie in browser"

class Movie():
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		#"constructor is used to initialize the value of an object"
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube

	def show_trailer(self): 
		#method is used to open the trailer of a movie
		webbrowser.open(self.trailer_youtube_url)
