people=[
    {"name":"Tim", "country":"USA"},
    {"name":"Bob", "country":"RU"},
    {"name":"Drake", "country":"UK"}
]

def f(person):
    return person["name"]

#sorting by the name
people.sort(key=f)

print(people)

#LAMBDA
people.sort(key=lambda person: person["country"])

print(people)
