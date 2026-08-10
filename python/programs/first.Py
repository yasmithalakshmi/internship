marks=int(input("Enter your marks: "))
if marks>=35 and marks<50:
    print("grade:D")
elif marks>=50 and marks<60:
    print("grade:C")
elif marks>=60 and marks<70:
    print("grade:B")
elif marks>=70 and marks<=100:
    print("grade:A")
else:
    print("Invalid marks. Please enter a value between 35 and 100.")