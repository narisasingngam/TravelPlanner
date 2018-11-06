def is_int(value):    
    try:
       int(value)
       return True
    except ValueError:
       return False

def int_time(time):
    h = []
    m = []
    t = []
    c = 0

    for i in time:
        t.append(i)
        c += 1

        if(is_int(i)):
            if( c <= 2): h.append(int(i))
            else: m.append(int(i))     

    if(t[2] == "m" or t[3] == "m"):
        if(is_int(t[0])): 
            m.append(int(t[0]))
        elif(is_int(t[1])): 
            m.append(int(t[1]))   

        h.clear()
 
    s = 0
    a = 0
    b = 0
    
    while a < len(h):
        if(len(h) == 2 and a == 0): s += h[a]*10
        else: s += h[a]  
        a += 1

    while b < len(m):
        if(b == 0): 
            s += m[b]*0.1

        else: s += m[b]*0.01
        b += 1    
    
    return float(f"{s:.2f}")  

print(int_time("30 mins"))        
