CheckEven = lambda no:(no % 2 == 0)

def main():
    Data = [10,20,35,40,50,69,75]
    print("Input Data is:",Data)
    FData = list(filter(CheckEven,Data))
    print("The filter Data is:",FData)
    
if __name__ == "__main__":
    main()

