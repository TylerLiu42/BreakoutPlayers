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

def findLowWobaPlayers():
    expectedHitting = statcast_batter_expectedHitting(2019, 100)
    row = math.ceil(cutOffWobaPercentile*len(expectedHitting.index))
    result = expectedHitting[['last_name','first_name','woba']].sort_values(by='woba')
    return result[:row]

def findHighExitVeloPlayers(launchInfo):
    row = math.ceil(cutOffExitVeloPercentile*len(launchInfo.index))
    result = launchInfo[['last_name', 'first_name', 'avg_hit_speed']].sort_values(by='avg_hit_speed')
    return result[row:]

def findHighBarrelPlayers(launchInfo):
    row = math.ceil(cutOffBarrelPercentile*len(launchInfo.index))
    result = launchInfo[['last_name', 'first_name', 'brl_percent']].sort_values(by='brl_percent')
    return result[row:]

def statcast_batter_exitVeloBarrels(year, minBBE="q"):
    url = f"https://baseballsavant.mlb.com/leaderboard/statcast?type=batter&year={year}&position=&team=&min={minBBE}&csv=true"
    res = requests.get(url, timeout=None).content
    data = pd.read_csv(io.StringIO(res.decode('utf-8')), skipinitialspace=True)
    return data

def statcast_batter_expectedHitting(year, minBBE="q"):
    url = f"https://baseballsavant.mlb.com/leaderboard/expected_statistics?type=batter&year={year}&position=&team=&min={minBBE}&csv=true"
    res = requests.get(url, timeout=None).content
    data = pd.read_csv(io.StringIO(res.decode('utf-8')), skipinitialspace=True)
    return data
        