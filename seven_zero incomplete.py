import math
while True:
    num =input(' Enetr your number: ')
    
   #checking the num is negative or not
    if not num.isnumeric():
        print('please enter an integer number')
    elif int(num)<0:
       print('please enter a posetive number')
    

    else: 
        break


result= []
result1= []
min_element = []
for i in range(1,int(num)):
    x =int(num)* i
    len_number=len(str(x))
    print(math.floor(x/(10**(len_number-1))))

    if math.floor(x/(10**(len_number-1)))== 7:
        print(x)
        if not '1' in(list(str(x))):
            if not '2' in(list(str(x))):
                if not '3' in(list(str(x))):
                    if not '4' in(list(str(x))):
                        if not '5' in(list(str(x))):        
                            if not '5' in(list(str(x))):
                                if not '6' in(list(str(x))):
                                    if not '8' in(list(str(x))):
                                        if not '9' in(list(str(x))):
                                            result1.append(x)

print(result1)
for element in range(0, len(result1)):
    for j in range(len(str(element))):
        element = str(element)
        if element[j] ==7  and element[j+1]==0:
            pass
        elif element[j]== 0  and element [j+1]==7:
            result1.remove(element)
                  
min_element = min(result1)
print (result1)