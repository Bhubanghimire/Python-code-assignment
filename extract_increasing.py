def extract_increasing(digits):
    final_list = []
    current = 0
    previous = -1
    index = 0
    lenght = 0

    for data in digits[index:]:
        # print(data, index)
        if index == 0:
            final_list.append(data)
            previous = int(data)
            lenght = 1

        else:    
            if previous < int(data):
                final_list.append(data)
                previous = int(data)
                lenght +=1
            

            else:
                current = 10*previous+int(data)
                print("o", data)
               
                final_list.append(current)
                previous = int(current)
               
        index += lenght
    return final_list


digits = "045349"
result = extract_increasing(digits)
print(result)
