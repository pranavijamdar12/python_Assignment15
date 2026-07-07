from functools import reduce
Addition = lambda no1,no2:(no1 + no2)
def main():
    Data = [10,20,30,40,50,60]
    print("Input Data is:",Data)
    FData=reduce(Addition,Data)
    print("The filter Data is:",FData)

if __name__ == "__main__":
    main()
