class DJ:
    def __init__(self, name, age, gender, nationality, type):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.type = type

    # methods
    def play(self):
        print("Now playing Cercle set")

    def describe(self):
        print("{} is a {} years old {} {}".format(self.name, self.age, self.nationality, self.type))


# instance
DJ1 = DJ("BlackCoffee", 43, "male", "african", "club dj")

print(DJ1.name)
print(DJ1.type)
DJ1.play()
DJ1.describe()