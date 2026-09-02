# 8. Create a Movie class using __init__() and a method to display movie information.

class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

    def display(self):
        print("Movie:", self.movie_name)
        print("Hero:", self.hero)
        print("Heroine:", self.heroine)
        print("Rating:", self.rating)

m = Movie("3 Idiots", "Aamir Khan", "Kareena", 8.9)
m.display()
