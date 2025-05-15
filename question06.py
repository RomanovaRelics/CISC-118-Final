"""Here I know what I am supposed to do but I cannot make it subtract the numbers.
It says that - is not valid on lines 9 and 12. I was trying to make it so it finds the bigger
number and then subtracts the smaller number from it. I think it is the subtraction bit
that is not working. I put all kinds of parentheses around trying to get it to work."""
def difference(number_one, number_two):
    number_one = input("number one")
    number_two = input("number two")
    if number_one > number_two:
        print(number_one - number_two)

    elif number_two > number_one:
        print(number_two - number_one)


difference(5,4)