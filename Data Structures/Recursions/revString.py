def revString(s):
    if s == "":
        return ""
    
    restrev = revString(s[1:])
    first = s[0:1]
    
    result =restrev + first
    
    return result
def main():
    print (revString("hello"))
    
if __name__ == '__main__':
    main()