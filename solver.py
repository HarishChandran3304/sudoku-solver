from helpers import *

def main():
    grid = getgrid("./samples/hard.txt")
    print("Before solving: ")
    printgrid(grid)
    print()
    solved = solve(grid)
    if solved:
        print("After solving: ")
        printgrid(grid)
    else:
        print("No solution possible")

if __name__ == "__main__":
    main()