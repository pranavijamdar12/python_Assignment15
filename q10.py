CheckEven = lambda no: no % 2 == 0

def main():
    Data = [10, 15, 20, 25, 30, 35, 40]
    print("Input Data is:", Data)

    FData = list(filter(CheckEven, Data))

    print("Even numbers are:", FData)
    print("Count of even numbers is:", len(FData))

if __name__ == "__main__":
    main()
