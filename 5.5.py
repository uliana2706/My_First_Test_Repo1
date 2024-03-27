for n in range(1, 256):
    r = bin(n-1)[2:]
    r = '0'* (8 - len(r))+r
    r = r.replace('1','2')
    r = r.replace('0', '1')
    r = r.replace('2', '0')
    r = int(r,2)
    if n == 204:
        print(r)
        
    
    
    
