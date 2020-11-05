people = [
    {"name": "harry", "house": "Gryfindor"},
    {"name": "cho", "house": "canal"},
    {"name": "raja", "house": "mangla"}
]
def f(person):
    return person["name"]
people.sort(key=f)
print(people)