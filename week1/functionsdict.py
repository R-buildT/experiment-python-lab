student = {
    "name" : "RTBUILDS",
    "subjects" : {
        "maths" : 67,
        "science" : 12,
        "hindi" : 35,
        "sst" : 56,
    }
}

print(student["subjects"]) #returns value of key but may give error if key is not present

print(student.keys()) #returns keys 

print(len(student)) # you know what len is duh

print(student.values()) #returns values

print(student.items()) #both value and key

print(student.get("name")) #returns value of key but may give none as a ans

print(len("subject")) #len of the nested dictionary

student.update({"age": "15"}) #updates the value of key

print(student)