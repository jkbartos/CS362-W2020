# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:41:00 2020

@author: Jordan Bartos (ONID: bartosj)
This test case replaces all of the Gold cards in the supply with Silver cards
"""

import Dominion
import testUtility


supply_order = testUtility.get_supply_order()
supply = testUtility.get_supply()
players = testUtility.get_players()
trash = testUtility.get_trash()
supply["Gold"] = [Dominion.Silver() for x in range(20)]



# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)
            

# Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)