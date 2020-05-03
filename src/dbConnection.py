'''
Created on May 2, 2020

@author: Tyler Liu
'''
import mysql.connector
import csv
from percentileQueries import findLowWobaPlayers, findHighExitVeloPlayers, findHighBarrelPlayers
import pandas as pd

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

csv_data = csv.reader(open('statcast2019.csv'))
next(csv_data)
for row in csv_data:
    cursor.execute('INSERT INTO statcastData(lastName, firstName, year, \
          xba, xslg, woba, xwoba, xobp, xiso, exitVelo, launchAngle, \
          sweetSpotPercentage, barrelRate )' \
          'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, \
          %s, %s, %s, %s)', 
          row)
cursor.execute("select count(*) from statcastData")
res = cursor.fetchone()
totalRows = res[0]

lowWobaPlayers = findLowWobaPlayers(mydb, totalRows)
highExitVeloPlayers = findHighExitVeloPlayers(mydb, totalRows)
highBarrelPlayers = findHighBarrelPlayers(mydb, totalRows)
breakoutPlayers = list(set(highExitVeloPlayers) & set(highBarrelPlayers) & set(lowWobaPlayers))
for x in breakoutPlayers:
    print(x)
    outputFile.write(x[0] + "," + x[1] + "\n")
    
pwFile.close()
outputFile.close()
    
    
    