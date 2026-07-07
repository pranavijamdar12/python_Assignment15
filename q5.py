from functools import reduce
Max = lambda no1,no2 :(no1 if no1 > no2 else no2)

def main():
    Data = [10,20,30,40,50,60,70]
    print("Input Data is:",Data)

    RData = reduce(Max,Data)
    print("The reduce Data is :",RData)

if __name__ == "__main__":
    main()
    





