distances = {
    "Voyager 1": 163,
    "voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")

main()

distances = {
    "Voyager 1": 163,
    "voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values():
        print(f"{distance} AI is {convert(distance)} m")

def convert(au):
    return au * 149597870700

main()