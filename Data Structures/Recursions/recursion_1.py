def sumFirst(n):
    return n*(n+1)

def main():
    x = int(input("Enter a non-negative number: "))
    s = sumFirst(x)
    print(f"The sumof the first {x}, integers is {'str(s)'+'.'}")
    
if __name__ == '__main__':
    main()