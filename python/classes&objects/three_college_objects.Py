# 7. Create a class called College with properties for college name, location, and course. Create three objects.

class College:
    def __init__(self, college_name, location, course):
        self.college_name = college_name
        self.location = location
        self.course = course

c1 = College("ABC College", "Hyderabad", "B.Tech")
c2 = College("XYZ College", "Chennai", "BCA")
c3 = College("PQR College", "Bangalore", "MBA")

print("College 1:", c1.college_name, c1.location, c1.course)
print("College 2:", c2.college_name, c2.location, c2.course)
print("College 3:", c3.college_name, c3.location, c3.course)
