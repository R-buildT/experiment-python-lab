marks = int(input("enter you marks = "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks <= 90):
    grade = "B"
elif(marks >= 70 and marks <= 80):
    grade = "c"
else:
    grade = "D"

print("grade of student ->  ", marks)
