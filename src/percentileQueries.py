'''
Created on May 2, 2020

@author: Tyler Liu
'''
import math

cutOffWobaPercentile = 0.5
cutOffExitVeloPercentile = 0.8
cutOffBarrelPercentile = 0.7

def findLowWobaPlayers(mydb, totalRows):
    cursor = mydb.cursor()
    row = cutOffWobaPercentile*totalRows
    cursor.execute("""select lastName, firstName from 
            statCastData order by woba asc limit %s""", [math.ceil(row)])
    resultSet = cursor.fetchall()
    return resultSet

def findHighExitVeloPlayers(mydb, totalRows):
    cursor = mydb.cursor()
    row = cutOffExitVeloPercentile*totalRows
    cursor.execute("""select lastName, firstName from statCastData 
            order by exitVelo desc limit %s""", [totalRows-math.ceil(row)])
    resultSet = cursor.fetchall()
    return resultSet

def findHighBarrelPlayers(mydb, totalRows):
    cursor = mydb.cursor()
    row = cutOffBarrelPercentile*totalRows
    cursor.execute("""select lastName, firstName from statCastData
            order by barrelRate desc limit %s""", [totalRows-math.ceil(row)])
    resultSet = cursor.fetchall()
    return resultSet