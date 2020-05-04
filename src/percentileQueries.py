'''
Created on May 2, 2020

@author: Tyler Liu
'''
import math
import requests
import pandas as pd
import io

cutOffWobaPercentile = 0.5
cutOffExitVeloPercentile = 0.8
cutOffBarrelPercentile = 0.7

def findLowWobaPlayers(mydb, totalRowsLaunchData):
    cursor = mydb.cursor()
    row = cutOffWobaPercentile*totalRowsLaunchData
    cursor.execute("""select lastName, firstName from 
            StatcastDataExpectedHitting 
            order by woba asc limit %s""", [math.ceil(row)])
    resultSet = cursor.fetchall()
    return resultSet

def findHighExitVeloPlayers(mydb, totalRowsLaunchData):
    cursor = mydb.cursor()
    row = cutOffExitVeloPercentile*totalRowsLaunchData
    cursor.execute("""select lastName, firstName from statCastData 
            order by avgHitSpeed desc limit %s""", [totalRowsLaunchData-math.ceil(row)])
    resultSet = cursor.fetchall()
    return resultSet

def findHighBarrelPlayers(mydb, totalRowsLaunchData):
    cursor = mydb.cursor()
    row = cutOffBarrelPercentile*totalRowsLaunchData
    cursor.execute("""select lastName, firstName from statCastData
            order by barrelPercentage desc limit %s""", [totalRowsLaunchData-math.ceil(row)])
    resultSet = cursor.fetchall()
    return resultSet

def statcast_batter_exitVeloBarrels(year, minBBE="q"):
    url = f"https://baseballsavant.mlb.com/leaderboard/statcast?type=batter&year={year}&position=&team=&min={minBBE}&csv=true"
    res = requests.get(url, timeout=None).content
    data = pd.read_csv(io.StringIO(res.decode('utf-8')))
    print(data)
    return res

def statcast_batter_expectedHitting(year, minBBE="q"):
    url = f"https://baseballsavant.mlb.com/leaderboard/expected_statistics?type=batter&year={year}&position=&team=&min={minBBE}&csv=true"
    res = requests.get(url, timeout=None).content
    return res;