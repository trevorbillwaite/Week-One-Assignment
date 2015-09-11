__author__ = 'daniel.neumann'

# File: chaos.py
# A simple program illustrating chaotic behavior.
multiplier=2.0
loopCounter=10
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(loopCounter):
        x = (multiplier) * x * (1 - x)
        print(x)

main()

