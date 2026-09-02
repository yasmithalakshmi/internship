# 10. Create a class called Movie with movie name, hero, heroine, and rating. Create two objects and display their details.

class Movie:
    def __init__(self, movie_name, hero, heroine, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

m1 = Movie("Bahubali", "Prabhas", "Anushka", 9.0)
m2 = Movie("KGF", "Yash", "Srinidhi", 8.8)

print("Movie 1:", m1.movie_name, m1.hero, m1.heroine, m1.rating)
print("Movie 2:", m2.movie_name, m2.hero, m2.heroine, m2.rating)
