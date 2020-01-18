class DJ:
    def __init__(self, name, age, gender, nationality, type):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.type = type

    # methods
    def play(arg):
        print("Now playing Cercle set")

    def describe(arg):
        print("{} is a {} years old {} {}".format(arg.name, arg.age, arg.nationality, arg.type))


# instance
DJ1 = DJ("BlackCoffee", 43, "male", "african", "club dj")

print(DJ1.name)
print(DJ1.type)
DJ1.play()
DJ1.describe()