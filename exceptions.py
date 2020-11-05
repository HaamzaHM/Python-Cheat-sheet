import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Error: cant divided by 0.")
    sys.exit(1)

print(f"{x}/{y} = {result}")

"""
airports = [
    {
        "name": "Beijing Capital International Airport",
        "code": "PEK",
        "country": "China"
    },
    {
        "name": "Los Angeles International Airport",
        "code": "LAX",
        "country": "United States"
    },
    {
        "name": "London Heathrow Airport",
        "code": "LHR",
        "country": "United Kingdom"
    }
]

for airport in airports:
    print(f"{airport['name']} ({airport['code']}) is in {airport['country']}.")
"""