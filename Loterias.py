import random


def generatePrimitiva():
    yourNumber = random.sample(range(1, 49), 6)
    complementary = random.randint(1,9)
    print("Tu número es", yourNumber,"y tu complementario es", complementary)

def generateEuroMillon():
    yourNumber = random.sample(range(1, 50), 5)
    starNumbers = random.sample(range(1, 9), 2)
    print("Tu número es", yourNumber, "y tus números estrella es",starNumbers)

def generateFootballGueser():
    yourFootballGuess = []
    options = [1, "X", 2]
    for i in range(1, 16):
        yourFootballGuess.append( random.choice(options))
    print("Tu quiniela es", yourFootballGuess)

def generateFootballGueser2():
    options = [1, "X", 2]
    yourFootballGuess = [random.choice(options) for i in range(15)]
    print("Tu quiniela es", yourFootballGuess)


generatePrimitiva()
generateEuroMillon()
generateFootballGueser()
generateFootballGueser2()



