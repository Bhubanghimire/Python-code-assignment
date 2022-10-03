def double_until_all_digits(n, giveup=10):
    counter = 0
    while(giveup>0):
        data_list = [int(x) for x in str(n)]
        if 0 in data_list and 1 in data_list and 2 in data_list and 3 in data_list and 4 in data_list and 5 in data_list and 6  in data_list and 7 in data_list and 8 in data_list and 9 in data_list:
            return counter
        else:
            n=n*2
        counter +=1
        giveup -=1    

    return -1    

n = 555
result = double_until_all_digits(n)
print(result)
