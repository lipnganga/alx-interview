#!/usr/bin/python3
""" determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total)
    """ determine the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    if coins is None or len(coins) == 0:
        return -1
    coins.sort(reverse=True)
    i = 0
    num_coins = 0
    while total > 0 and i < len(coins):
        while total >= coins[i]:
            total -= coins[i]
            num_coins += 1
        i += 1
    if total != 0:
        return -1
    return num_coins

