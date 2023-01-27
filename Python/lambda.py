people = [

    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"}

]

def f(person):
    return person["name"]
people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)

