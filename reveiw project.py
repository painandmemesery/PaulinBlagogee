#Paulin Blagogee 2/28/18

mediatype = input("Media Type: ")


media_type = ['movie', 'music', 'book', 'shows']
name_movie = []
name_music = []
name_book = []
name_shows = []
genre_movie = []
genre_music = []
genre_book = []
genre_shows = []
rating_movie = []
rating_music = []
rating_book = []
rating_shows = []

if mediatype == 'movie':
    name_movie.append(input("Name: "))
    genre_movie.append(input("Genre: "))
    rating_movie = (float(input("Rating: ")))
    print(name_movie[0])
    print(genre_movie[0])
    print (rating_movie)
elif mediatype == 'music':
    name_music.append(input("Name: "))
    genre_music.append(input("Genre: "))
    rating_music = (float(input("Rating: ")))
    print(name_music[0])
    print(genre_music[0])
    print(rating_music)
elif mediatype == 'book':
    name_book.append(input("Name: "))
    genre_book.append(input("Genre: "))
    rating_book = (float(input("Rating: ")))
    print(name_book[0])
    print(genre_book[0])
    print(rating_book)
elif mediatype == 'shows':
    name_shows.append(input("Name: "))
    genre_shows.append(input("Genre: "))
    rating_shows = (float(input("Rating: ")))
    print(name_shows[0])
    print(genre_shows[0])
    print(rating_shows)


