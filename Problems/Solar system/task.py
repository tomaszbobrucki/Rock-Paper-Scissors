# create the planets.txt
file = open("planets.txt", "w", encoding='utf-8')
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for line in planets:
    file.write(line + "\n")

file.close()
