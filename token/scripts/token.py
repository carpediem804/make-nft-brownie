#!/usr/bin/python3

from brownie import Token, accounts


def main():
    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0],'max_fee_per_gas': 100 * 10**9})
