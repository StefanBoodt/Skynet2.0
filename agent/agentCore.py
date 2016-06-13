#! /usr/bin/env python

"""
This script will start the tribler exit node.

It will then occasionally check it's wallet.
and if it's wallet has enough money it will procure, install and start exactly 1 child.
"""

from ExitNode import ExitNode
from market.market import Market
from Birthchamber import Birthchamber
from ZappiehostBuyer import ZappiehostBuyer
from Wallet import Wallet
from time import sleep

en = ExitNode()
market = Market(en.market_community)

wallet = Wallet()

print("successful instantiation")

#this should actually compare with the current necessary bitcoins plus a small margin
while(wallet.balance()<0.01):
    print("Not enough bitcoins, waiting for money to arrive")
	sleep(600)

bc = Birthchamber()
bc.getChild(ZappiehostBuyer())
