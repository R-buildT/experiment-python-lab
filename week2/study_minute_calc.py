
import random
while True:
    def hours(min):
        if(1 < min <= 60 ):
            print("study more",min)
        elif( min == 0):
            print("fuck off gay illitrerate")
        elif(60 < min <= 120):
            print("a lil more study period, ",min)
        elif(120 < min <= 180):
            print("perfect study period, ",min)
        elif(180 < min <= 240):
            print("more than perfect study period, ", min)
        elif(240 < min < 300):
            print("being the topper in the next exam, ",min)

    print("estimating your study hr... ")
    print("permission gransted??")
    a =input("> yes or no? >> ")

    if (a == "yes"):
        min = random.randint(1,300)
    else:
        min = 0

    hours(min)

