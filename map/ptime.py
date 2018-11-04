def is_int(value):    
    try:
       int(value)
       return True
    except ValueError:
       return False

def int_time(time):
    x = []
    c = 0

    for i in time:
        if(is_int(i)):
            c += 1
            x.insert(c, i)      
 
    i = 0
    s = 0
    while i < len(x):
        if(i == 0):
            s += int(x[i])*60   
        elif(i == len(x)-2):
            s += int(x[i])*10
        else:
            s += int(x[i])    
        i += 1   

    return s  

