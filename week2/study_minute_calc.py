import random

def hours(minutes):
    if 1 < minutes <= 60:
        print("study more", minutes)
    elif minutes == 0:
        print("study session cancelled")
    elif 60 < minutes <= 120:
        print("a lil more study period, ", minutes)
    elif 120 < minutes <= 180:
        print("perfect study period, ", minutes)
    elif 180 < minutes <= 240:
        print("more than perfect study period, ", minutes)
    elif 240 < minutes < 300:
        print("being the topper in the next exam, ", minutes)

while True:
    print("estimating your study hr... ")
    print("permission granted??")
    a = input("> yes or no? >> ")

    if a == "yes":
        minutes = random.randint(1, 300)
    else:
        minutes = 0

    hours(minutes)
