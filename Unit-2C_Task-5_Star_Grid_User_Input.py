def print_grid():
    size = int(input("Enter the grid size: "))
    for _ in range(size):
        print("* " * size)
if __name__ == "__main__":
    print_grid()
