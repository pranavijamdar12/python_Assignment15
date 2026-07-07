Square = lambda no:(no * no)

def main():
    Data = [10,20,30,40,50,60,70]
    print("Input Data is:",Data)

    MData = list(map(Square,Data))
    print("The Data after  MData",MData)

if __name__ == "__main__":
     main()
