def is_int(value):    
    try:
       int(value)
       return True
    except ValueError:
       return False
       
def int_time(time):
    hour = []
    mins = []
    t = []
    count = 0

    for i in time:
        t.append(i)
        count += 1

        if(is_int(i)):
            if( count <= 2): hour.append(int(i))
            else: mins.append(int(i))            

    if(len(t) < 2): return 0
    elif(t[2] == "m" or t[3] == "m"):
        if(is_int(t[0])): 
            mins.append(int(t[0]))
        if(is_int(t[1])): 
            mins.append(int(t[1]))   

        hour.clear()
    
    summ = 0
    a = 0
    b = 0
    
    while a < len(hour):
        if(len(hour) == 2 and a == 0): summ += hour[a]*10
        else: summ += hour[a]  
        a += 1
    
    while b < len(mins):
        if(b == 0 and len(mins) == 1): 
            summ += mins[b]*0.01
        elif(b == 0): 
            summ += mins[b]*0.1
        else: summ += mins[b]*0.01
        
        b += 1  
    
    return float(f"{summ:.2f}")

