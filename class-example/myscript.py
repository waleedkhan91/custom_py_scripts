class vehicle:
    def __init__(self):
        self.waleed = "first class"
        print("Constructor called")
    
    def printMembers(self):
        print(self.waleed)
        print("Thats all!")

def main():
    print("Hello World!")
    obj = vehicle()
    obj.printMembers()
    print("End")

if __name__ == "__main__":
    main()
