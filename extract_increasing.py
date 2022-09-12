def extract_increasing(digits):
    final_list = []
    current = 0
    previous = -1

    for index, data in enumerate(digits):
        if len(final_list) == 0:
            final_list.append(data)
            previous = int(data)
        else:
            
            current = 10 * current + int(previous)
            print(current)
            print("ok")
            if previous < int(data):
                final_list.append(data)
                previous = int(data)
            else:
                final_list.append(current)
                previous = current
                current = 0
    return final_list


digits = "045349"
result = extract_increasing(digits)
print(result)
