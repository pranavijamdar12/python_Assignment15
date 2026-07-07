List = lambda string:(len(string) > 5)
def main():
    Data =["Anisha","Vars","Pallvi","Pranavi","Saki"]
    print("Input Data is:",Data)
    FData = list(filter(List,Data))
    print("The filter Data is:",FData)
if __name__ == "__main__":
    main()

