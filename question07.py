"""I cannot for the life of me get the numbers to go the other way counting down.
I tried to put 11 first and then 2 but it would not print anything. I also tried to
make numbers negative but it would not budge..."""
def count_down():
    number()
    print("Blastoff!")

def number():
    for i in range(2, 11):
        i -= 1
        print(i)

count_down()