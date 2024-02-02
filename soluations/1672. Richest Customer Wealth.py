


"""
map(sum, accounts): This applies the sum function to each sublist in accounts, resulting in an iterator of the sums of wealth for each customer.

max(...): This finds the maximum value in the iterator obtained from map. In other words, it finds the maximum wealth across all customers.

"""

def findRichAccounts( accounts):
    return max(map(sum , accounts))     