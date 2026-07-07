Divisble = lambda no:(no % 3 == 0 and no % 5 == 0)

def main():
    Data = [10,20,30,40,50,60]
    print("Input Data is:",Data)
    FData = list(filter(Divisble,Data))
    print("The filter Data is:",FData)

if __name__ == "__main__":
    main()
