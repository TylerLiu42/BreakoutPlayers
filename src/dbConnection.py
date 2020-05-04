'''
Created on May 2, 2020

@author: Tyler Liu
'''
import mysql.connector
import csv
from percentileQueries import findLowWobaPlayers, findHighExitVeloPlayers, findHighBarrelPlayers,\
    statcast_batter_exitVeloBarrels, statcast_batter_expectedHitting

pwFile = open("pw.txt", "r")
password = pwFile.readline()

outputFile = open("output.txt", "w")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=password,
  db="statcast",
  autocommit=True
)

cursor = mydb.cursor(prepared=True)

res = statcast_batter_exitVeloBarrels(2019, 100)
with open("statcast2019.csv", "wb") as fp:
    fp.write(res)
    
res = statcast_batter_expectedHitting(2019, 100)
with open("statcastExpectedHitting.csv", "wb") as fp:
    fp.write(res)

csv_data = csv.reader(open('statcast2019.csv'))
next(csv_data)
totalRowsLaunchData = 0;
totalRowsExpectedHitting = 0;
for row in csv_data:
    totalRowsLaunchData += 1 
    if (row[12] == ''): row[12] = 0
    cursor.execute('INSERT INTO statcastData(lastName, firstName, playerID, \
          attempts, avgHitAngle, sweetSpotPercentage, maxHitSpeed, avgHitSpeed, fbld, gb, maxDistance, \
          avgDistance, avgHRDistance, ev95plus, ev95percent, barrels, barrelPercentage, barrelPerPA)' \
          'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, \
          %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
          row)

csv_data = csv.reader(open('statcastExpectedHitting.csv'))
next(csv_data)
for row in csv_data:
    totalRowsExpectedHitting += 1
    cursor.execute("""
        INSERT INTO StatcastDataExpectedHitting(lastName, firstName, playerID,
        year, pa, bip, ba, xba, xbaDiff, slg, xslg, xslgDiff, woba, xwoba, xwobaDiff)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, row)

lowWobaPlayers = findLowWobaPlayers(mydb, totalRowsExpectedHitting)
highExitVeloPlayers = findHighExitVeloPlayers(mydb, totalRowsLaunchData)
highBarrelPlayers = findHighBarrelPlayers(mydb, totalRowsLaunchData)
breakoutPlayers = list(set(highExitVeloPlayers) & set(highBarrelPlayers) & set(lowWobaPlayers))
for x in breakoutPlayers:
    print(x)
    outputFile.write(x[0] + "," + x[1] + "\n")

pwFile.close()
outputFile.close()
    
    
    