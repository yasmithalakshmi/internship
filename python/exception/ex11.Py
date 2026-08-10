#custom exception with constructor example(eligible to vote)
class NotEligibleError(Exception):
    def __init__(self, age, message="Not eligible to vote"):
        self.age = age
        self.message = message
        super().__init__(self.message())
        
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise NotEligibleError(age)
    else:
        print("You are eligible to vote.")
except NotEligibleError as e:
    print("Error:", e.message, ". Your age is", e.age, ".")
else:
    print("Thank you for providing your age.")