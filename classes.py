class DJ:
    def __init__(self, name, age, gender, nationality, type):
    #instance variables
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.type = type

    # methods
    def play(self):
        return ("Now playing Cercle set")

    def describe(self):
        return ("{} is a {} years old {} {} nominated for {}".format(self.name, self.age, self.nationality, self.type, self.award))

    # adding instance varialble
    def setAward(self, award):
        self.award = award

    # retrieve instance variable
    def getAward(self):
        return self.award

# instance
DJ1 = DJ("BlackCoffee", 43, "male", "african", "club dj")

DJ1.setAward("International DJ 2019")
print(DJ1.getAward())


print(DJ1.play())
print(DJ1.describe())