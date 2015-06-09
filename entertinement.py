import fresh_tomatoes
import media
# Instantiate toy_story object of Movie class
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys than came to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://youtu.be/Bj4gS1JQzjk",
    "8.3/10",
    "Toy Story is a 1995 American computer-animated \
    buddy-comedy adventure film",
    "John Lasseter"
    )
# Instantiate avatar object of Movie class
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/EPTHpG7ovak",
    "7.9/10",
    "Avatar (marketed as James Cameron's Avatar) is a 2009 \
    American epic science fiction film",
    "James Cameron"
    )
# Instantiate spiderman object of Movie class
spiderman = media.Movie(
    "Spiderman",
    "Student gained the speed, strength and powers of a spider",
    "http://upload.wikimedia.org/wikipedia/en/0/02/\
    The_Amazing_Spiderman_2_poster.jpg",
    "https://youtu.be/1quRsv5QULc",
    "6.8/10",
    "Bitten by a radioactive spider, high school student Peter Parker gained \
    the speed, strength and powers of a spider",
    "Sam Raimi"
    )
# Instantiate jurassicpark object of Movie class
jurassicpark = media.Movie(
    "Jurassic Park",
    "An island full of living dinosaurs",
    "http://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
    "https://youtu.be/O-FuIzm68KE",
    "8.7/10",
    "Huge advancements in scientific technology have enabled a mogul \
    to create an island full of living dinosaurs",
    "Steven Spielberg"
    )
# Instantiate titanic object of Movie class
titanic = media.Movie(
    "Titanic",
    "Sinking of the RMS Titanic",
    "http://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://youtu.be/ZQ6klONCq4s",
    "7.7/10",
    "Titanic is a 1997 American epic romantic disaster film. \
    A fictionalized account of the sinking of the RMS Titanic",
    "James Cameron"
    )
# Instantiate terminator object of Movie class
terminator = media.Movie(
    "Terminator 2",
    "Science fiction",
    "http://upload.wikimedia.org/wikipedia/en/6/6b/\
    Terminator-2-shocking-dark-poster.jpg",
    "https://youtu.be/CAQ83W3DZS4",
    "8.5/10",
    "Terminator 2 is a 1991 American science fiction action film",
    "James Cameron"
    )
# Adding movie objects to the list
movies = [
    avatar,
    toy_story,
    titanic,
    terminator,
    spiderman,
    jurassicpark
    ]
# Passing movie list to movie page
fresh_tomatoes.open_movies_page(movies)

