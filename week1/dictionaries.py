#A dictionary (dict) in Python is a data structure that stores data as key-value pairs.

# (key : value)

a = input("enter your name:")
info = {
    "name" : "RTBUILDS",
    "work" : "school",
    "age" : 15,
    "hobbies" : "coding",
    "hello" : "welcome sir"
}

print(info)

print(info["name"])

if (a == info["name"]):
    print(info["hello"])
else:
    print("you are not allowed to enter this page")

info["name"] = "RT"
print(info["name"])

#a dictionary inside another dictionary.
# Used to group related information together.

student = {
    "name" : "RTBUILDS",
    "subjects" : {
        "maths" : 67,
        "science" : 12,
        "hindi" : 35,
        "sst" : 56,
    }
}

print(student["subjects"])
