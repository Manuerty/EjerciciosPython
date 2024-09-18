def openAndCreateFile():
    name = input("Introduce el nombre del archivo que quieres abrir o crear: ")
    name = name + ".txt"
    open(name, "a")
    return name

def writeInFile(file):
    content = input("Escribe lo que desees: ")
    with open(file, "w") as fileToWrite:
        fileToWrite.write(content)

def countVocals(file):
    with open(file, "r") as fileToCount:
        hola = str(sum(fileToCount.read().lower().count(vocal) for vocal in "aeiou"))
        print(file + "\nHay " + str(sum(fileToCount.read().lower().count(vocal) for vocal in "aeiou")) + " vocales")

def writeNewLine(file):
    content = input("Escribe lo que desees: ")
    with open(file, "a") as fileToWrite:
        fileToWrite.write('\n')
        fileToWrite.write(content)

#writeInFile(openAndCreateFile())
countVocals(openAndCreateFile())
#writeNewLine(openAndCreateFile())

