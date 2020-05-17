'''
Created on May 2, 2020

@author: Tyler Liu
'''
from percentileQueries import findLowWobaPlayers, findHighExitVeloPlayers, findHighBarrelPlayers,\
    statcast_batter_exitVeloBarrels, statcast_batter_expectedHitting

outputFile = open("output.txt", "w")

launchInfo = statcast_batter_exitVeloBarrels(2019, 100)

lowWobaPlayers = findLowWobaPlayers()
highExitVeloPlayers = findHighExitVeloPlayers(launchInfo)
highBarrelPlayers = findHighBarrelPlayers(launchInfo)
breakoutPlayers = list(set(highExitVeloPlayers) & set(highBarrelPlayers) & set(lowWobaPlayers))
for x in breakoutPlayers:
    print(x)
    outputFile.write(x[0] + "," + x[1] + "\n")

outputFile.close()
    
    
    