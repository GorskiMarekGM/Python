names = ["Tim", "Bob", "Drake", "Ewa"]

print(names)
print(names[0])

names.append("Jim")

names.sort()

print(names)

#SET

s = set()

#add

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements")

#dict

country = {"Tim":"USA", "Bob":"UK"}

country["Drake"] = "RU"

print(country["Tim"])