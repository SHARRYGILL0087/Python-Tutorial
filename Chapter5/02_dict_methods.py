marks = {
    "sharry" : 100,
    "sher" : 50,
    "rohan" : 30,
    0 : "SSG"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"sharry" : 99 , "shamsher" : 110}) # update and add new key and val
print(marks)

print(marks.get("sharry")) # give none if sharry not exist
print(marks["sharry"]) # give error if sharry not exist