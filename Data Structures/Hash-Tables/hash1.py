def myHash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv = mult * ord(ch)
        mult += 1
        
    return hv
for item in ('hello world', 'world hello', 'gello xorld'):
    print("{}: {}".format(item, myHash(item)))
