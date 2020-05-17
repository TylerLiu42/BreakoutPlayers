'''
Created on May 2, 2020

@author: Tyler Liu
'''
from percentileQueries import findLowWobaPlayers, findHighExitVeloPlayers, findHighBarrelPlayers,\
    statcast_batter_exitVeloBarrels

launchInfo = statcast_batter_exitVeloBarrels(2019, 100)

lowWobaPlayers = findLowWobaPlayers()
highExitVeloPlayers = findHighExitVeloPlayers(launchInfo)
highBarrelPlayers = findHighBarrelPlayers(launchInfo)
breakoutPlayers = lowWobaPlayers.merge(highExitVeloPlayers,on=['last_name','first_name']).merge(highBarrelPlayers,on=['last_name','first_name'])
print(breakoutPlayers)

    
    
    