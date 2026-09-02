# 10. Create a Temperature class with methods to convert Celsius to Fahrenheit and Fahrenheit to Celsius.

class Temperature:
    def c_to_f(self, c):
        return (c * 9 / 5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5 / 9

obj = Temperature()
print(obj.c_to_f(30))
print(obj.f_to_c(86))
