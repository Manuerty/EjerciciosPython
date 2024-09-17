
def collatz(n):
    n = int(n)
    numberList = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        numberList.append(n)
    print(numberList)

n1 = input("introduce un número: ")

collatz(n1)