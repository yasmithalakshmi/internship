# 9. Create a Teacher class with name, subject, and experience. Create multiple teacher objects.

class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

teachers = [
    Teacher("Mrs. Rao", "Math", 12),
    Teacher("Mr. Kumar", "Physics", 8),
    Teacher("Mrs. Devi", "English", 10)
]

for teacher in teachers:
    print(teacher.name, teacher.subject, teacher.experience)
