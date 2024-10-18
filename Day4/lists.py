batfamily = ["Nightwing", "Batgirl", "Robin", "Red Hood"]
supsfam = ["Supes", "Lois", "Jonathan"]
print(batfamily[-1])

batfamily[2] = "Red Robin"

print(batfamily)

batfamily.append("Huntress")

print(batfamily)

batfamily.extend(["James Gordon", "Azrael"])

print(batfamily)

allFam = [batfamily, supsfam]

print(allFam)
