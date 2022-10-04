    
def count_and_say(digits):
    final_ans = ""
    tested_data = []
    for index, item in enumerate(digits):
        
        if item not in tested_data:
            print(item)
            count = digits.count(item)
            text = f"{count}{item}"
            final_ans += text
            tested_data.append(item)

    return final_ans

digits = '777777777777777'
result = count_and_say(digits)
print(result)