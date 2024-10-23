dictiones = {"Name": "Juninho", "Age": 12}
print(dictiones["Name"])
dictiones["Loop"] = "Giros giros giros"
print(dictiones)

dictiones["Age"] = 15

for key in dictiones:
    print(key)
    print(dictiones[key])