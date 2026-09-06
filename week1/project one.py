maths= int(input("input your marks "))
science = int(input("input your marks "))
hindi = int(input("input your marks "))
assamese = int(input("input your marks "))
sst = int(input("input your marks "))

if( maths > science and maths > hindi and maths > assamese and maths > sst):
    print("highest marks obtained in maths")
elif(science > hindi and science > assamese and science > sst):
    print("highest marks obtained in science")
elif(hindi > assamese and hindi > sst):
    print("highest marks obtained in hindi")
elif(assamese > sst):
    print("highest marks obtained in assamese")
else:
    print("highest marks obtained in sst")

print("marks obstained in maths = ", maths , " out of 100" )
print("marks obstained in maths = ", science , " out of 100" )
print("marks obstained in maths = ", hindi , " out of 100" )
print("marks obstained in maths = ", assamese , " out of 100" )
print("marks obstained in maths = ", sst , " out of 100" )

average = (maths + science + sst + hindi + assamese)/ 5

print("Average = ", average)

