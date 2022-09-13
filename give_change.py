"""
Given the ​ amount of money (expressed as an integer as the total number of cents, one dollar being
equal to 100 cents) and the list of available denominations of ​ coins (similarly expressed as cents),
create and return a list of coins that add up to ​ amount using the ​ greedy approach where you use
as many of the highest denomination coins when possible before moving on to the next lower
denomination. The list of coin denominations is guaranteed to be given in descending sorted order,
as should your returned result also be.
"""

from re import I
from unittest import result


def give_change(amount, coins):
    coin_list = []
    sum = 0

    for coin in coins:
        while True:
            if amount >= (sum+coin):
                sum += coin 
                coin_list.append(coin)
            else:
                break
    return coin_list

coins = [100, 25, 10, 5, 1]
amounts = 223

result = give_change(amounts, coins)
print(result)
