# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class check_pair:
    def pair():
        value=int(input("Choisissez la taille du sapin"))
        if (value%2==0):
            return 0
        else:
            return value

def print_tree(n):
    space= " "
    symbol= "*"
    blank=(n-1)/2
    for i in range(1, n+1, 2):
        print(space*blank + symbol*i + space*blank)
        blank=blank-1

def print_leg(n):
    space = " "
    symbol = "*"
    print(space*((n-1) / 2) + symbol + space*((n-1) / 2))
    print(space*((n-1) / 2) + symbol + space*((n-1) / 2))

def main():
    length=check_pair()
    while(length==0):
        print("erreur")
        check_pair()
    print_tree(length)
    print_leg(length)

main()
