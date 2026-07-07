from functools import reduce
Mul = lambda no1,no2:(no1 * no2)
def main():
    Data = [10,20,30,40,50,60]
    print("Input Data is:",Data)
    FData=reduce(Mul,Data)
    print("The filter Data is:",FData)

if __name__ == "__main__":
    main()
